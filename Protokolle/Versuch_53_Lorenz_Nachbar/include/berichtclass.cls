\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{include/berichtclass}
\LoadClass[a4paper,11pt,titlepage,openany,twoside=semi]{scrbook}

%% ------------------
%% |    Packages    |
%% ------------------

\usepackage[utf8]{inputenc}                     % for using utf8 chars (äöüß)
\usepackage[T1]{fontenc}                        % for correct font encoding (you 
                                                % can't search for non-ascii 
                                                % chars in pdf otherwise)
\usepackage{lmodern}                            % the font used by T1 font enc
\usepackage[protrusion=true,                    % microtype package for better 
            expansion,                          % line breaks, kerning, etc.
            tracking,
            kerning,
            spacing]{microtype}
\microtypecontext{spacing=nonfrench}            % option for scrbook to allow 
                                                % microtype->nonfrenchspacing
                                                % for info on nonfrenchspacing:
                                                % en.wikipedia.org/wiki/       \
                                                % History_of_sentence_spacing# \
                                                % French_and_English_spacing

\usepackage[english,ngerman]{babel}             % babel language styles. you may 
                                                % add languages, if need to be.
\usepackage[fixlanguage]{babelbib}              % use babel bibtex. fixlanguage 
                                                % = don't switch language
                                                % between bib items
%\usepackage{cite}                              % for bibtex without babel

\usepackage{amsmath}                            % lots of math packages
\usepackage{amssymb}                            % ... even more math packages
                                                
\usepackage{upgreek}                            % use $\uppi$ etc.
\usepackage{nicefrac}                           % use \nicefrac{1}{2} 
                                                % for inline text, if you want
\usepackage[load-configurations=abbreviations]{siunitx} % package for units. Use 
                                                % \si{\ampere} or 
                                                % \SI{0.3}{\angstrom}.
\sisetup{per-mode=fraction}                     % style of writing units
\sisetup{separate-uncertainty=true}             % to allow for $\pm...$ as un-
                                                % certainty instead of 0.34(12)
\usepackage[version=3]{mhchem}                  % to nicely write chemcial 
                                                % elements (e.g.
                                                % \ce{^{227}_{90}Th+})

\usepackage{vmargin}                            % Adjust margins in a simple way 
                                                % (is used below).
\usepackage{fancyhdr}                           % Define simple page headings 
                                                % (is used below).
\usepackage{placeins}                           % To use \FloatBarrier

\usepackage{setspace}                           % As per requirement by jufo
\onehalfspacing

\usepackage[nottoc,                             % So that the Bibliography will 
            notlot,                             % be added to the ToC
            notlof]{tocbibind}

\usepackage{varioref}                           % Intelligent page 
                                                % references. Provides \vref 
                                                % and \vpageref

\usepackage{booktabs}
\usepackage[table]{xcolor}                      % used for some coloring 
                                                % commands. table option for 
                                                % beautiful colored tables.
\definecolor{expcolor}{rgb}{142 27 71}        % color is defined here and 
                                                % later used for several 
                                                % definitions

\usepackage[pdftex]{graphicx}                   % including images
\usepackage[normal,
                font={small,color=black},
                labelfont=bf,
                margin=2em]{caption}            % create graphics/

\usepackage{subfig}

\usepackage{etoolbox}                           % necessary to update page 
                                                % numbering for chapters
% \usepackage{xstring}                            % used for creating substring 
%                                                 % out of \appendixname
% \usepackage{multicol}                           % used for titlepage. Usefull 
%                                                 % for other stuff, too.

\DeclareGraphicsRule{*}{mps}{*}{}               % enables compiling 
                                                % images with pdf-latex
\DeclareGraphicsExtensions{.eps,                % different image exts used
                           .pdf,
                           .png,
                           .jpg,
                           .jpeg,
                           .mps}
\usepackage{epstopdf}                           % may be necessary for miktex to 
                                                % convert eps to pdf figures

\usepackage[raiselinks=true,                    % package enables hyperlinks in
            bookmarks=true,                     % document. hyperref also incl.
            bookmarksopenlevel=1,               % url package for \url{...}
            bookmarksopen=true,
            bookmarksnumbered=true,
            hyperindex=true,
            plainpages=false,
            pdfpagelabels=true,
            pdfborder={0 0 0.5},
            colorlinks=false,
            linkbordercolor=expcolor,
            citebordercolor=expcolor]{hyperref}


\expandafter\def\csname ver@subfig.sty\endcsname{}
                                                % stop package svg from loading 
                                                % package subfig
                                                % http://tex.stackexchange.com/\
                                                % questions/213273/undefined-  \
                                                % control-sequence-            \
                                                % at-begindocument
\usepackage{svg}                                % include svg graphics







%% --------------------------
%% |    Globale Settings    |
%% --------------------------
\setcounter{secnumdepth}{3}           % Numbering also for \subsubsections
\setcounter{tocdepth}{3}              % Register \subsubsections in content dir

\setpapersize{A4}
\setmarginsrb{2.5cm}{1.2cm}{2.5cm}{1.6cm}     % {leftmargin}{topmargin}{rightmargin}...
             {6mm}{7mm}{5mm}{10mm}    % {bottommargin}{headheight}{headsep}...
                                      % {footheight}{footskip}

\setlength{\marginparwidth}{1.5cm}    % for todos to be positioned correctly

\parindent 0cm                        % do not indent beginning of paragraph
\parskip 0.5ex plus0.5ex minus0.5ex   % Margin between paragraphs

\newcommand{\blankpage}{\clearpage{\pagestyle{empty}\clearpage}}

\addto\captionsngerman{\renewcommand{\bibname}{Quellen- und Literaturverzeichnis}}



%% ------------------------
%% |    Language Setup    |
%% ------------------------
\newcommand{\SelectLanguage}[1]
{
    \AtBeginDocument
    {
        \selectlanguage{#1}           % babel command

        \iflanguage{ngerman}
        {
            \sisetup{output-decimal-marker={,}}
            % sets , for German and . otherwise
            \sisetup{list-final-separator={ und }}
            % "3, 4 and 5" in English or "3, 4 und 5" in German
            \sisetup{range-phrase={ bis }}
            % "1.5 to 1.8" in English or "1,5 bis 1,8" in German
            \sisetup{locale=DE}
            % e.g. using \cdot instead of \times for floating points
        }
        {
            \sisetup{output-decimal-marker=.}
            \sisetup{list-final-separator={ and }}
            \sisetup{range-phrase={ to }}
        }
    }
}





%% ---------------------------
%% |    Style of captions    |
%% ---------------------------
\newcommand{\changefont}[3]{\fontfamily{#1} \fontseries{#2}%
                            \fontshape{#3} \selectfont}
\newcommand{\chapterheadfont}{}

\renewcommand{\chaptername}{}

\renewcommand{\section}{%
\@startsection{section}%
{1}                                    % Structure level
{0mm}                                  % Indention
{2ex plus 1ex minus 1ex}               % Pre-Margin
{0.5ex plus 0.5ex minus 0.5ex}         % Post-Margin
{\chapterheadfont\large\bfseries}      % Style
}
\renewcommand{\subsection}{%
\@startsection{subsection}%
{2}                                    % Structure level
{0mm}                                  % Indention
{1.5ex plus 1ex minus 0.5ex}           % Pre-Margin
{0.3ex plus 0.3ex minus 0.3ex}         % Post-Margin
{\chapterheadfont\large\bfseries}      % Style
}
\renewcommand{\subsubsection}{%
\@startsection{subsubsection}%
{3}                                    % Structure level
{0mm}                                  % Indention
{1.5ex plus 1ex minus 0.5ex}           % Pre-Margin
{0.2ex plus 0.2ex minus 0.2ex}         % Post-Margin
{\chapterheadfont\normalsize\bfseries} % Style
}
\renewcommand{\paragraph}{%
\@startsection{paragraph}%
{4}                                    % Structure level
{0mm}                                  % Indention
{0.5ex plus 1ex minus 0.3ex}           % Pre-Margin
{0.2ex plus 0.2ex minus 0.2ex}         % Post-Margin
{\chapterheadfont\normalsize\bfseries} % Style
}
\renewcommand{\subparagraph}{%
\@startsection{subparagraph}%
{5}                                    % Structure level
{0mm}                                  % Indention
{1ex plus 1ex minus 0.2ex}             % Pre-Margin
{0.1ex plus 0.1ex minus 0.1ex}         % Post-Margin
{\chapterheadfont\normalsize\bfseries} % Style
}





%% -----------------------------------
%% |    Style of chapter captions    |
%% -----------------------------------
\newlength{\chapnolen}
\newlength{\chapparlen}
\newsavebox{\chapno}
\renewcommand{\@makechapterhead}[1]{
    % \vspace*{2mm}
    \vskip 18\p@
    {\parindent \z@ \raggedright \normalfont
        \ifnum \c@secnumdepth >\m@ne
            \if@mainmatter
                \savebox{\chapno}{\chapterheadfont\huge\bfseries \thechapter.}
                \settowidth{\chapnolen}{\usebox{\chapno}}
                \parbox[t]{\chapnolen}{\usebox{\chapno}}\nobreak\leavevmode
            \fi
        \fi
        \interlinepenalty\@MM
        \setlength{\chapparlen}{\textwidth}
        \addtolength{\chapparlen}{-1.0\chapnolen}
        \addtolength{\chapparlen}{-2ex}
        \leavevmode\nobreak
        \parbox[t]{\chapparlen}%
        {\raggedright\chapterheadfont\huge \bfseries #1\par\nobreak}
        \vskip 8\p@
    }}

\renewcommand{\@makeschapterhead}[1]{
    \vspace*{2mm}
    {\parindent \z@ \raggedright
        \normalfont
        \interlinepenalty\@M
        \chapterheadfont \huge \bfseries  #1\par\nobreak
        \vskip 8\p@
    }
}





%% ------------------------------------
%% |    Style of content directory    |
%% ------------------------------------
\let\oldtableofcontents\tableofcontents
\renewcommand{\tableofcontents}{{\pdfbookmark{\contentsname}{\contentsname}%
\chapterheadfont\oldtableofcontents}}
\let\@olddottedtocline\@dottedtocline
\renewcommand{\@dottedtocline}[5]{\@olddottedtocline{#1}{#2}{#3}{#4}%
{\chapterheadfont #5}}





%% ------------------------------------------
%% |    Style of appendix and mainmatter    |
%% ------------------------------------------
\newboolean{chapWiseNumb}
\setboolean{chapWiseNumb}{false}

\newboolean{chapResetPageNumb}
\setboolean{chapResetPageNumb}{false}

\fancyhf{}
\renewcommand{\footrulewidth}{0pt}
\cfoot{\thepage}

% pages and right on odd pages

\newcommand{\FrontMatter}
{
    \frontmatter

    \pagestyle{empty}

    \fancypagestyle{plain}{}
    \fancyhead[RE,LO]{}    % Page number (boldface) in left on even
    \fancyhead[LE]{\scshape \versuch }
    \fancyhead[RO]{\scshape \name}

}

\newcommand{\MainMatter}
{
    \clearpage

    \begingroup                        % make sure that there is no involuntary 
                                       % blankpage added after toc.
    \let\cleardoubleoddstandardpage\relax
    \mainmatter
    \endgroup

    \mainmatter
    \pagestyle{fancy}
    
    \fancyhead[LE,RO]{}    % Page number (boldface) in left on even
    \fancyhead[RE]{\scshape \name}      % Chapter in the right on even pages
    \fancyhead[LO]{\scshape \versuch}     % Section in the left on odd pages
}

\newcommand{\TheBibliography}
{
    \clearpage
    \thispagestyle{plain}
    \ifthenelse{\boolean{chapWiseNumb}}
    {
        \StrMid{\bibname}{1}{3}[\bibnameshort]
        \renewcommand{\thepage}{\bibnameshort.-\arabic{page}}
    }{}
}

\newcommand{\emptychapter}[2][]
{
    \addtocounter{chapter}{1}
    \addtocontents{toc}{\protect\contentsline
        {chapter}{\protect\numberline {\thechapter}#2}{#1}{}}
}

\newcounter{tmppage}

\newcommand{\pseudochapter}[2][0]
{
    \clearpage
    \ifthenelse{\boolean{chapResetPageNumb}}
    {
        \setcounter{tmppage}{1}
    }
    {
        \setcounter{tmppage}{\arabic{page}}
    }
    \addtocounter{chapter}{1}
    
    \ifthenelse{\boolean{chapWiseNumb}}
    {
        \addtocontents{toc}{\protect\contentsline
            {chapter}{\protect\numberline {\thechapter}#2}
            {\thechapter-\thetmppage}{}}
        \clearpage
    }
    {
        \addtocontents{toc}{\protect\contentsline
            {chapter}{\protect\numberline {\thechapter}#2}{\thetmppage}{}}
        \clearpage
    }
    \addtocounter{page}{#1}
}

%% **** END OF CLASS ****
\endinput
