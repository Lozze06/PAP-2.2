import numpy as np
import math
import pandas as pd
import sympy as sp
from uncertainties import ufloat

def round_error_and_value(val, err):
    """
    Rundet Fehler auf 1 oder 2 signifikante Stellen auf und passt den 
    Messwert auf die entsprechende Nachkommastelle an.
    """
    if err == 0 or np.isnan(err):
        return f"{val}", f"{err}"
    
    first_sig_exp = math.floor(math.log10(abs(err)))
    first_digit = math.floor(abs(err) / (10**first_sig_exp))
    
    if first_digit <= 2:
        num_sig_digits = 2
    else:
        num_sig_digits = 1
        
    target_exp = first_sig_exp - (num_sig_digits - 1)
    scale = 10**target_exp
    
    err_rounded = math.ceil(err / scale) * scale
    decimals = max(0, -target_exp)
    val_rounded = round(val, decimals)
    
    val_str = f"{val_rounded:.{decimals}f}"
    err_str = f"{err_rounded:.{decimals}f}"
    
    return val_str, err_str


def auswerten_messreihe(daten, name="Messgröße", einheit=""):
    """
    Berechnet Mittelwert, Standardabweichung und Standardfehler aus CSV-Spalten 
    (Pandas Series), NumPy-Arrays oder Listen.
    
    Gibt ein `uncertainties.ufloat`-Objekt zurück, mit dem exakt weitergerechnet 
    werden kann, und druckt die gerundeten Ergebnisse aus.
    """
    if isinstance(daten, pd.Series):
        y = daten.dropna().to_numpy(dtype=float)
    else:
        y = np.array(daten, dtype=float)
        y = y[~np.isnan(y)]
        
    n = len(y)
    if n == 0:
        raise ValueError(f"Die Messreihe '{name}' enthält keine gültigen Datenpunkte.")
    
    mittelwert = np.mean(y)
    std_abw = np.std(y, ddof=1) if n > 1 else 0.0          # s_y (Stichprobe)
    std_fehler = std_abw / np.sqrt(n) if n > 1 else 0.0    # s_y_bar (Standardfehler)    
    val_str, err_str = round_error_and_value(mittelwert, std_fehler)
    
    print("=" * 45)
    print(f"STATISTISCHE AUSWERTUNG: {name}")
    print("=" * 45)
    print(f"Anzahl Messungen (n):       {n}")
    print(f"Mittelwert (y_bar):         {mittelwert:.4f} {einheit}")
    print(f"Standardabweichung (s_y):   {std_abw:.4f} {einheit}")
    print(f"Standardfehler (s_y_bar):   {std_fehler:.4f} {einheit}")
    print(f"\nEndergebnis gerundet:       ({val_str} ± {err_str}) {einheit}")
    print("=" * 45)
    
    # Rückgabe als ufloat zur direkten Weiterverarbeitung
    return ufloat(mittelwert, std_fehler)


def gauss_fehlerfortpflanzung(funktion_expr, messwerte_dict, fehler_dict):
    """
    Führt eine allgemeine analytische Gauß'sche Fehlerfortpflanzung durch.
    
    Parameters:
    -----------
    funktion_expr : sympy.Expr
        SymPy-Formel der Zielgröße (z. B. sp.sympify("a * b / c"))
    messwerte_dict : dict
        Dictionary mit SymPy-Symbolen als Key und Messwerten als Value {var: wert}
    fehler_dict : dict
        Dictionary mit SymPy-Symbolen als Key und Fehlern als Value {var: fehler}
        
    Returns:
    --------
    ergebnis_ufloat : ufloat
        Berechneter Wert samt fortgepflanztem Fehler
    latex_formula : str
        Formel der Fehlerfortpflanzung in LaTeX-Syntax für das Protokoll
    """
    variablen = list(messwerte_dict.keys())
    
    # 1. Symbolische partielle Ableitungen bilden: sum((df/dxi * sigma_i)^2)
    quadrat_summe = 0
    sigma_symbole = {}
    
    for var in variablen:
        sigma_var = sp.Symbol(rf"\sigma_{{{var.name}}}")
        sigma_symbole[var] = sigma_var
        ableitung = sp.diff(funktion_expr, var)
        quadrat_summe += (ableitung * sigma_var)**2
        
    fehler_formel_sym = sp.sqrt(quadrat_summe)
    latex_formula = sp.latex(sp.Eq(sp.Symbol(rf"\sigma_{{{funktion_expr.name if hasattr(funktion_expr, 'name') else 'f'}}}") , fehler_formel_sym))
    
    # 2. Numerische Auswertung
    subs_values = {**messwerte_dict}
    val_num = float(funktion_expr.subs(subs_values))
    
    subs_errors = {**messwerte_dict, **{sigma_symbole[v]: fehler_dict[v] for v in variablen}}
    err_num = float(fehler_formel_sym.subs(subs_errors))
    
    return ufloat(val_num, err_num), latex_formula
