from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def setup_plot_style():
    plt.rcParams.update({
        "font.size": 11,
        "axes.labelsize": 12,
        "axes.titlesize": 12,
        "legend.fontsize": 10,
        "figure.figsize": (7.5, 5.2),
        "figure.dpi": 150,
        "savefig.dpi": 300,
    })


def plot_with_fit(x, y, y_err=None, x_fit=None, y_fit=None, 
                  y_fit_upper=None, y_fit_lower=None, vlines=None,
                  xlabel="x", ylabel="y", title="", filename=None, 
                  log_y=False, log_x=False, fit_label="Fit", 
                  error_label=r"Fehlerkurven $\pm 1\sigma$",
                  output_dir="figures", annotation=None):
    setup_plot_style()
    fig, ax = plt.subplots()
    
    ax.errorbar(x, y, yerr=y_err, fmt="o", capsize=3, label="Messdaten",
                color="black", markersize=2)

    if x_fit is not None and y_fit is not None:
        ax.plot(x_fit, y_fit, "-", label=fit_label, linewidth=1.8, color="C0")

    if x_fit is not None and y_fit_upper is not None and y_fit_lower is not None:
        ax.plot(x_fit, y_fit_upper, "--", color="red", linewidth=1.0, label=error_label)
        ax.plot(x_fit, y_fit_lower, "--", color="red", linewidth=1.0)

    # Vertikale Linien einzeichnen
    if vlines:
        for vline in vlines:
            ax.axvline(x=vline['x'], color=vline.get('color', 'black'), 
                       linestyle=vline.get('linestyle', '--'), 
                       linewidth=vline.get('linewidth', 1.0),
                       label=vline.get('label', None))

    if log_x:
        ax.set_xscale("log")
    if log_y:
        ax.set_yscale("log")
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, which="both", linestyle="--", alpha=0.35)
    
    if annotation:
        ax.text(0.03, 0.97, annotation, transform=ax.transAxes,
                va="top", ha="left", fontsize=9,
                bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "alpha": 0.85})
        
    ax.legend(loc="upper right")
    fig.tight_layout()

    saved_path = None
    if filename:
        out_dir = Path(output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        saved_path = out_dir / (filename if str(filename).lower().endswith(".pdf")
                                else f"{filename}.pdf")
        fig.savefig(saved_path, format="pdf", bbox_inches="tight")
        print(f"Plot gespeichert unter: {saved_path}")
    plt.show()
    plt.close(fig)
    return saved_path


def export_table_to_latex(df: pd.DataFrame, filename: str, caption: str, label: str,
                          float_format="%.4f", formatters=None, output_dir="tables"):
    """Exportiert DataFrame als LaTeX; formatters ermöglicht Spalten-spezifische Formate."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    latex_str = df.to_latex(
        index=False, escape=False, caption=caption, label=f"tab:{label}",
        float_format=float_format, formatters=formatters
    )
    path = out_dir / (filename if str(filename).lower().endswith(".tex")
                      else f"{filename}.tex")
    path.write_text(latex_str, encoding="utf-8")
    print(f"Tabelle gespeichert unter: {path}")
    return path
