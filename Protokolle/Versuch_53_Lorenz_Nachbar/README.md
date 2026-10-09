# PAP-1-Messprotokollvorlage für VS Code und MiKTeX

Diese Vorlage orientiert sich an der bereitgestellten PAP-1-Vorlage. Die Berichtklasse und das grundlegende Layout bleiben erhalten; die Projekt- und VS-Code-Konfiguration ist für wiederverwendbare Protokolle ergänzt.

## Ordnerstruktur

```text
.vscode/                 VS-Code-Einstellungen und Extension-Empfehlung
a_content/               Einzelne Kapitel des Protokolls
include/                 Berichtklasse, Titelseite, Hilfsbefehle und Logo
fig/                     Abbildungen
tab/                     Ausgelagerte Tabellen-Dateien
data/                    Messdaten und sonstige Rohdaten
main.tex                 Zentrale Hauptdatei des kompletten Dokuments
lit.bib                  Literaturdatenbank
```

## Einrichtung und Verwendung

1. ZIP-Datei entpacken und in VS Code **den gesamten Ordner** öffnen, nicht nur eine einzelne `.tex`-Datei.
2. Die VS-Code-Erweiterung **LaTeX Workshop** installieren.
3. MiKTeX und `latexmk` installieren bzw. aktualisieren. `latexmk` benötigt Perl; Perl muss installiert und über `PATH` erreichbar sein. Nach einer neuen Installation von Perl oder MiKTeX VS Code gegebenenfalls neu starten.
4. In `main.tex` die Angaben `\versuch`, `\datum`, `\name`, `\gruppe` und `\Kurs` ändern.
5. Die Kapitel in `a_content/1_einleitung.tex`, `2_durchfuehrung.tex`, `3_auswertung.tex` und `4_diskussion.tex` bearbeiten. Abbildungen in `fig/` ablegen; Quellen in `lit.bib` ergänzen.
6. Das Projekt mit **Strg+Alt+B** bauen oder eine `.tex`-Datei speichern. Die PDF-Datei heißt `main.pdf` und wird im Projektordner abgelegt.

## Immer das gesamte Dokument kompilieren

`main.tex` ist die einzige Hauptdatei. Sie bindet alle Kapitel mit `\input{...}` ein. Die Kapitel- und Include-Dateien enthalten am Anfang den Root-Hinweis

```tex
% !TeX root = ../main.tex
```

Dadurch erkennt LaTeX Workshop beim Bearbeiten einer solchen Datei `main.tex` als Root-Datei. Beim Build wird somit das vollständige Protokoll mit Titelseite, Inhaltsverzeichnis, allen Kapiteln und Literaturverzeichnis erstellt – nicht nur das einzelne Kapitel. Die Einstellung `latex-workshop.latex.rootFile.doNotPrompt` verhindert unnötige Rückfragen zur Root-Datei.

Als Build-Werkzeug wird `latexmk` mit `-pdf` verwendet. Es ruft pdfLaTeX und bei Bedarf BibTeX auf und wiederholt die notwendigen Läufe, bis Literaturverzeichnis und Querverweise aktualisiert sind. Voraussetzung ist, dass `latexmk`, Perl und die MiKTeX-Programme über die Umgebungsvariable `PATH` gefunden werden.

## Literatur und Zitate

Quellen als BibTeX-Einträge in `lit.bib` eintragen und im Text beispielsweise mit `\cite{Skript}` zitieren. Der Literaturstil `natdin` aus der Ausgangsvorlage bleibt erhalten. Die Bibliografie wird in `main.tex` mit `\bibliography{lit}` eingebunden; der Dateiname wird dort **ohne** `.bib` angegeben.

## Hinweise

- `include/berichtclass.cls` definiert das vorhandene Layout. Nur ändern, wenn eine Formatänderung beabsichtigt ist.
- `include/cmds.tex` enthält Hilfsbefehle und wird bereits in `main.tex` eingebunden.
- In `main.tex` werden die Titelangaben und die Reihenfolge der Kapitel verwaltet.
- `data/` ist für Rohdaten vorgesehen und wird nicht automatisch in das Dokument eingebunden.
- Die Ordner `fig/`, `tab/` und `data/` enthalten `.gitkeep`, damit sie in der Vorlage erhalten bleiben, auch wenn sie noch leer sind.
