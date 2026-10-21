import pandas as pd
import os

def load_messdaten(filepath, sep=',', decimal='.', skiprows=0, encoding='utf-8-sig'):
    """
    Lädt CSV/TXT-Messdaten robust ein, entfernt UTF-8-BOM sowie Leerzeichen
    in den Spaltennamen.
    """
    if not os.path.exists(filepath):
        if os.path.exists(os.path.join('Code', filepath)):
            filepath = os.path.join('Code', filepath)
        else:
            raise FileNotFoundError(f"Die Datei wurde nicht gefunden: {filepath}")
    
    df = pd.read_csv(
        filepath, 
        sep=sep, 
        decimal=decimal, 
        skiprows=skiprows, 
        encoding=encoding,
        engine='python'
    )
    
    # Spaltennamen von BOM-Zeichen und Leerzeichen bereinigen
    df.columns = [str(col).strip() for col in df.columns]
    return df