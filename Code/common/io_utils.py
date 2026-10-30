import os
import numpy as np
import pandas as pd

def load_messdaten(
    filepath, sep="\t", decimal=",", skiprows=0, encoding="utf-8-sig"): #txt oder csv laden

    # Prüfen, ob die Datei am angegebenen Ort existiert
    datei_existiert = os.path.exists(filepath)

    if datei_existiert == False:
        print("Fehler: Die Datei konnte nicht gefunden werden!")
        print("Gesuchter Pfad:", filepath)
        return None
                            
    # Datei mit Pandas einlesen
    daten_tabelle = pd.read_csv(filepath, sep=sep, decimal=decimal, skiprows=skiprows, encoding=encoding, engine="python",)

    # Tabelle in ein NumPy-Array umwandeln
    daten_array = daten_tabelle.to_numpy()

    return daten_array