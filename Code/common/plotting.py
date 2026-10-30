from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd



def setup_plot_style():
    einstellungen = {
        "font.size": 11,  # Allgemeine Schriftgröße
        "axes.labelsize": 12,  # Schriftgröße der Achsenbeschriftung
        "axes.titlesize": 12,  # Schriftgröße des Diagrammtitels
        "legend.fontsize": 10,  # Schriftgröße der Legende
        "figure.figsize": (7.5, 5.2),  # Diagrammgröße in Zoll (Breite, Höhe)
        "figure.dpi": 150,  # Bildauflösung auf dem Bildschirm
        "savefig.dpi": 300,  # Bildauflösung beim Speichern
    }
    plt.rcParams.update(einstellungen)


def plot_with_fit(x, y, connect_points = False, y_err=None, x_fit=None, y_fit=None, y_fit_upper=None, y_fit_lower=None,
    vlines=None, xlabel="x", ylabel="y", title="",filename=None, log_y=False, log_x=False, fit_label="Fit",
    error_label=r"Fehlerkurven $\pm 1\sigma$", output_dir="figures", annotation=None,):

    fmt_data = "k.-" if connect_points else "k."

    #Plot-Stil anwenden und Diagramm erstellen
    setup_plot_style()
    fig, ax = plt.subplots()

    #Messdaten mit Fehlerbalken
    ax.errorbar(x, y, yerr=y_err,fmt="o", capsize=3,  label="Messdaten", color="black", markersize=2,)

    # Fit-Kurve einzeichnen
    hat_fit_daten = x_fit is not None and y_fit is not None
    if hat_fit_daten:
        ax.plot(x_fit, y_fit, "-", label=fit_label, linewidth=1.8, color="C0")

    # Fehlerkurven / Band einzeichnen (falls übergeben)
    hat_fehler_grenzen = (x_fit is not None  and y_fit_upper is not None and y_fit_lower is not None)
    if hat_fehler_grenzen:
        ax.plot( x_fit,y_fit_upper,"--", color="red", linewidth=1.0,label=error_label,)
        ax.plot(x_fit, y_fit_lower, "--", color="red", linewidth=1.0)  

    # vertikale Hilfslinien einzeichnen (falls vorhanden)
    if vlines is not None:
        for linie in vlines: 
            x_position = linie["x"]
            farbe = linie.get("color", "black")
            linien_stil = linie.get("linestyle", "--")
            breite = linie.get("linewidth", 1.0)
            beschriftung = linie.get("label", None)

            ax.axvline( x=x_position,color=farbe,linestyle=linien_stil, linewidth=breite, label=beschriftung,)
# Achsenskalierung
    if log_x:
        ax.set_xscale("log")
    if log_y:
        ax.set_yscale("log")

    # Beschriftungen und Gitter 
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, which="both", linestyle="--", alpha=0.35)

    #  Text-Box 
    if annotation:
        ax.text(0.03, 0.97, annotation, transform=ax.transAxes, va="top",ha="left",fontsize=9,bbox={"boxstyle": "round,pad=0.35","facecolor": "white","alpha": 0.85,},)

    # Legende anzeigen, Ränder anpassen
    ax.legend(loc="upper right")
    fig.tight_layout()

    # Diagramm als PDF speichern
    gespeicherter_pfad = None

    if filename:
        # Ordner erstellen, falls er noch nicht existiert
        ziel_ordner = Path(output_dir)
        ziel_ordner.mkdir(parents=True, exist_ok=True)

        # Endung .pdf automatisch ergänzen, falls vergessen
        dateiname_text = str(filename)
        if not dateiname_text.lower().endswith(".pdf"):
            dateiname_text = dateiname_text + ".pdf"

        gespeicherter_pfad = ziel_ordner / dateiname_text

    
        fig.savefig(gespeicherter_pfad, format="pdf", bbox_inches="tight")
        print(f"Plot gespeichert unter: {gespeicherter_pfad}")
    plt.show()
    plt.close(fig)

    return gespeicherter_pfad


def export_table_to_latex(
    df: pd.DataFrame,
    filename: str,
    caption: str,
    label: str,
    float_format="%.4f",
    formatters=None,
    output_dir="tables",
):
    """Wandelt eine Pandas-Tabelle in LaTeX-Code um und speichert sie als .tex-Datei."""

  
    ziel_ordner = Path(output_dir)
    ziel_ordner.mkdir(parents=True, exist_ok=True)


    latex_code = df.to_latex(
        index=False,
        escape=False,
        caption=caption,
        label=f"tab:{label}",
        float_format=float_format,
        formatters=formatters,
    )

   
    dateiname_text = str(filename)
    if not dateiname_text.lower().endswith(".tex"):
        dateiname_text = dateiname_text + ".tex"

    dateipfad = ziel_ordner / dateiname_text

 
    dateipfad.write_text(latex_code, encoding="utf-8")
    print(f"LaTeX-Tabelle gespeichert unter: {dateipfad}")

    return dateipfad