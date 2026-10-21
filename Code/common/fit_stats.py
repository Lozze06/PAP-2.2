import numpy as np
import scipy.stats as stats

def calculate_chi2(y_obs, y_fit, y_err, num_params):
    """
    Berechnet chi^2, red. chi^2 und die Fitwahrscheinlichkeit (p-Wert).
    """
    residuen = y_obs - y_fit
    chi2 = np.sum((residuen / y_err)**2)
    dof = len(y_obs) - num_params # Freiheitsgrade
    
    if dof > 0:
        chi2_red = chi2 / dof
        # Fitwahrscheinlichkeit (Survival Function)
        p_value = stats.chi2.sf(chi2, dof) * 100 
    else:
        chi2_red = np.nan
        p_value = np.nan
        
    return chi2, chi2_red, dof, p_value

def print_fit_results(params, param_errors, names, chi2_data=None):
    """Gibt die Fit-Ergebnisse übersichtlich aus."""
    print("--- Fit-Ergebnisse ---")
    for name, p, err in zip(names, params, param_errors):
        print(f"{name}: {p:.4e} ± {err:.4e}")
        
    if chi2_data:
        chi2, chi2_red, dof, p_val = chi2_data
        print(f"\nChi^2: {chi2:.2f}")
        print(f"Red. Chi^2: {chi2_red:.2f}")
        print(f"Freiheitsgrade: {dof}")
        print(f"Fitwahrscheinlichkeit: {p_val:.2f} %")