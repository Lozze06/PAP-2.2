import numpy as np
from scipy.optimize import curve_fit
from scipy.special import gamma

# --- Modellsammlungen ---

def linear(x, m, c):
    """Lineare Ausgleichsgerade (z.B. Induktion, Kalibrierung)"""
    return m * x + c

def linear_origin(x, m):
    """Ursprungsgerade (z.B. Rauschspannung vs. Widerstand)"""
    return m * x

def exponential(x, A, lam, y0):
    """Einfacher exponentieller Zerfall mit Untergrund (z.B. Indium, RLC-Dämpfung)"""
    return A * np.exp(-lam * x) + y0

def double_exponential(x, A1, lam1, A2, lam2, y0):
    """Doppelter exponentieller Zerfall (z.B. Silber-Aktivierung)"""
    return A1 * np.exp(-lam1 * x) + A2 * np.exp(-lam2 * x) + y0

def gaussian(x, A, mu, sigma):
    """Gauß-Verteilung (z.B. Histogramme, Spektren-Peaks)"""
    return A * np.exp(-0.5 * ((x - mu) / sigma)**2)

def poisson_dist(k, A, mu):
    """Poisson-Verteilung (für k als kontinuierliche Variable approximiert über Gamma)"""
    return A * (mu**k) * np.exp(-mu) / gamma(k + 1)

def moseley(z, A, sigma):
    """Moseley-Gesetz für Röntgenfluoreszenz (sqrt(E) vs Z)"""
    return A * (z - sigma)

# --- Fit-Wrapper ---

def perform_fit(model, x, y, y_err=None, p0=None, bounds=(-np.inf, np.inf)):
    """
    Führt curve_fit durch und extrahiert automatisch die Parameter-Fehler.
    """
    if y_err is not None:
        popt, pcov = curve_fit(model, x, y, sigma=y_err, absolute_sigma=True, p0=p0, bounds=bounds)
    else:
        popt, pcov = curve_fit(model, x, y, p0=p0, bounds=bounds)
        
    perr = np.sqrt(np.diag(pcov)) # 1-Sigma Standardfehler
    return popt, perr, pcov