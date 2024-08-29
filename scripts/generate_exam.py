
import yaml
import subprocess
import sys
import os
from contextlib import redirect_stdout
import argparse
import subprocess
import random
random.seed(999)


###########################################################
## Latex header ###########################################

latex_header = r"""
\documentclass[12pt]{article}
\usepackage{graphicx}

\usepackage[a4paper, text={6in,10in}, centering]{geometry}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{inconsolata}


\usepackage[sfdefault,lf]{carlito}
\renewcommand*\oldstylenums[1]{\carlitoOsF #1}

% for correct quotes in verbatim
\usepackage{upquote}

% remove indentation of header
\usepackage{titlesec}
\titleformat{\subsection}
{\large\bfseries}
{\makebox[1in][l]{\thesubsection}}{0in}{}

\titlespacing{\subsection}{0pt}{1em}{0pt}

\usepackage{color}
\usepackage{xcolor}
\usepackage{fancyvrb}
\usepackage{mdframed}
\DefineShortVerb[commandchars=\\\{\}]{\|}
\DefineVerbatimEnvironment{Highlighting}{Verbatim}{commandchars=\\\{\}}
% Add ',fontsize=\small' for more characters per line
\definecolor{codegray}{rgb}{0.97,0.97,0.97}
\newenvironment{Shaded}{\begin{mdframed}[skipabove = 0.2cm, 
                                          skipbelow=0.2cm, 
                                          innerleftmargin=6pt,
                                          linecolor=codegray,
                                          backgroundcolor=codegray]}{\end{mdframed}}
\newcommand{\KeywordTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{\textbf{{#1}}}}
\newcommand{\DataTypeTok}[1]{\textcolor[rgb]{0.56,0.13,0.00}{{#1}}}
\newcommand{\DecValTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
\newcommand{\BaseNTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
\newcommand{\FloatTok}[1]{\textcolor[rgb]{0.25,0.63,0.44}{{#1}}}
\newcommand{\CharTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
\newcommand{\StringTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}
%\newcommand{\CommentTok}[1]{\textcolor[rgb]{0.38,0.63,0.69}{\textit{{#1}}}}
\newcommand{\OtherTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{{#1}}}
\newcommand{\AlertTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{{#1}}}}
\newcommand{\FunctionTok}[1]{\textcolor[rgb]{0.02,0.16,0.49}{{#1}}}
\newcommand{\RegionMarkerTok}[1]{{#1}}
\newcommand{\ErrorTok}[1]{\textcolor[rgb]{1.00,0.00,0.00}{\textbf{{#1}}}}
\newcommand{\NormalTok}[1]{{#1}}

\newcommand{\BuiltInTok}[1]{\textcolor[rgb]{0.00,0.00,0.50}{\textbf{{#1}}}}
\newcommand{\ControlFlowTok}[1]{\textcolor[rgb]{0.00,0.44,0.13}{\textbf{{#1}}}}
\newcommand{\OperatorTok}[1]{{#1}}
\newcommand{\VariableTok}[1]{{#1}}
\newcommand{\CommentTok}[1]{\textcolor[rgb]{0.25,0.44,0.63}{{#1}}}


\setlength{\parindent}{0cm}
% \setlength{\parskip}{0.3cm plus2mm minus1mm}

% used by pandoc
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

\usepackage{enumitem}


\usepackage{parskip}

\newlength{\currentparskip}
\newenvironment{myminipage}
  {\setlength{\currentparskip}{\parskip}% save the value
   \begin{minipage}{\textwidth}% open the minipage
   \setlength{\parskip}{\currentparskip}% restore the value
  }
  {\end{minipage}}

\usepackage{hyperref}

% Scale images if necessary, so that they will not overflow the page
% margins by default, and it is still possible to overwrite the defaults
% using explicit options in \includegraphics[width, height, ...]{}
\setkeys{Gin}{width=\maxwidth,height=\maxheight,keepaspectratio}
    
\begin{document}

"""

###########################################################
## Latex tail #############################################

latex_end = r"""
\end{document}
"""

###########################################################
## Bioinformatics question latex template #################



question_tmpl = r"""

\noindent
    \begin{{myminipage}} % []{{\textwidth}}

    \noindent
    \subsection*{{ {label}: {question_header} }}

    {question_intro}

    Udsagn og/eller spørgsmål:

    \begin{{enumerate}}[itemsep=0mm]
    {questions_latex}
    \end{{enumerate}}

    \end{{myminipage}}

"""

###########################################################
## Programming problem latex template #####################

problem_tmpl = r"""

\noindent
    \begin{{myminipage}} % []{{\textwidth}}

    {content}

    \end{{myminipage}}

"""

MAXCHARS = 200

def markdown2latex(s):
    """
    Turn a snippet of markdown into pandoc style latex
    """
    cmd = 'pandoc --to latex'
    p = subprocess.Popen(cmd.split(), 
        stdin=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE)
    stdout, stderr = p.communicate(s.encode())
    assert not p.returncode
    latex = stdout.decode()
    latex = latex.replace('section{', 'section*{')
    return latex


def format_question(question, nr):
    """
    Format a true/false bioinformatics question as latex
    """
    question_header = markdown2latex(question['header'])
    question_intro = markdown2latex(question['intro'])

    questions_latex = ''
    for n in sorted(question['statements']):
        if 'S' in question['statements'][n]:
            assert question['statements'][n]['S'].endswith('.'), ('wrong punctuation:', question['statements'][n]['S'])
            questions_latex += "\item {} (True/False)\n".format(question['statements'][n]['S'])
        elif 'Q' in question['statements'][n]:
            assert question['statements'][n]['Q'].endswith('?'), ('wrong punctuation:', question['statements'][n]['Q'])
            questions_latex += "\item {} (talværdi)\n".format(question['statements'][n]['Q'])
        elif 'F' in question['statements'][n]:
            # assert question['statements'][n]['F'].endswith('.'), ('wrong punctuation:', question['statements'][n]['F'])
            questions_latex += "\item {} (tekst, max {} karakterer incl. mellemrum)\n".format(question['statements'][n]['F'], MAXCHARS)

    latex = question_tmpl.format(label="Emne {}".format(nr),
        question_header=question_header,
        question_intro=question_intro,
        questions_latex=questions_latex,
        )
    return latex


def format_answer_form(question, nr):
    answer_form = "# Emne {}: {}\n".format(nr, question[key]['header'])

    # make sure sub questions are numbered consequtively from 1 (1, 2, 3, 4, ..)
    expected_numbers = list(range(1, len(question[key]['statements'])+1))
    subquestion_numbers = sorted(question[key]['statements'])
    assert subquestion_numbers == expected_numbers, (subquestion_numbers, expected_numbers) 

    for n in subquestion_numbers:
        if 'S' in question[key]['statements'][n]:
            answer_form += "emne_{}_del_{} = None    # True/False \n".format(nr, n)
            assert question[key]['statements'][n]['A'] != 'str', 'question label not F'
        elif 'Q' in question[key]['statements'][n]:
            answer_form += "emne_{}_del_{} = None    # Talværdi\n".format(nr, n)
            assert question[key]['statements'][n]['A'] != 'str', 'question label not F'
        elif 'F' in question[key]['statements'][n]:
            assert question[key]['statements'][n]['A'] == 'str', 'answer for free text not "str"'
            answer_form += 'emne_{}_del_{} = \' \'     # Tekst streng (max {} karakterer incl. mellemrum)\n'.format(nr, n,  MAXCHARS)
        else:
            assert 0
    answer_form += "##########################################################"
    return answer_form


def format_facit_form(question, nr):
    facit_form = "# Emne {}: {}\n".format(nr, question[key]['header'])
    for n in sorted(question[key]['statements']):
        if 'F' in question[key]['statements'][n]:
            # add question as the facit (for comparison to the students answer):
            facit_form += "emne_{}_del_{} = \"\"\"{}\"\"\"\n".format(nr, n, question[key]['statements'][n]['F'])            
        else:
            facit_form += "emne_{}_del_{} = {}\n".format(nr, n, question[key]['statements'][n]['A'])
    facit_form += "##########################################################"
    return facit_form


if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument("-y", "--year", 
                        type=float, # so you can call re-exams 2017.1
                        default='None',
                        help="Year for course")
    parser.add_argument("-f", "--front-page", 
                        type=str,
                        dest='front_page',
                        default='None',
                        help="Markdown file with explanatory text for front page")
    parser.add_argument("-p", "--programming-assignments", 
                        type=str,
                        dest='programming_assingments',
                        default='None',
                        help="Markdown file with programming assignments")
    parser.add_argument("-r", "--shuffle-bioinf", 
                        action="store_true",
                        help="Shuffle order of bioinf topics")
    parser.add_argument("-m", "--mult-choice-questions", 
                        type=str,
                        dest='mult_choice_questions',
                        default='None',
                        help="yaml file with multiple choice questions")    
    parser.add_argument("-o", "--output-pdf-file", 
                        type=str,
                        dest='output_pdf_file',
                        default='exam_assignment',
                        help="Base name of output pdf file")

    args = parser.parse_args()

    latex_file_name = args.output_pdf_file + '.tex' #'exam_assignment.tex'
    student_file_dir = '.'

    if not os.path.exists(student_file_dir):
        sys.makedirs(student_file_dir)

    multiple_choice_student_file = open(student_file_dir + '/bioinfexam.py', 'w')

    multiple_choice_facit_file = open(student_file_dir + '/bioinformatics_facit.py', 'w')

    bioinf_answer_intro = """
# Dette er en Python fil. Hver variabel nedenfor representerer et 
# udsagn eller spørgsmål i bioinformatik-delen af eksamensopgaven. 
# 
# Der er to typer delopgaver i eksamenssættet:
#  - Udsagn der enten er sande eller falske.
#  - Spørgsmål hvis svar er en talværdi.
#  - Spørgsmål hvis svar er tekst.
# 
# Du svarer på en delopgave ved at ændre None til en talværdi eller
# til True eller False, alt efter hvilken type opgave det er. Hvis 
# delopgaven skal besvares med tekst skal du skrive din tekst i den
# tomme tekst streng.
# Jeg har anført for hver variabel om værdien skal være et tal, 
# True/False eller tekst. 
"""

    with open(latex_file_name, 'w') as tex_file:
        with redirect_stdout(tex_file):

            print(bioinf_answer_intro, file=multiple_choice_student_file)

            # latex header
            print(latex_header)

            # Print explanation of assignment
            with open(args.front_page) as f:
                print(markdown2latex(f.read()))

            print('\\newpage')

            print(markdown2latex("# Programming assignments"))

            with open(args.programming_assingments) as f:
                content = f.read()
                delim = '## Problem'
                for i, text in enumerate(content.split(delim)):
                    if not i:
                        # introduction preceeding actual problems
                        print(markdown2latex(text))         
                    else:
                        print(markdown2latex("{} {}".format(delim, i)))
                        print(problem_tmpl.format(content=markdown2latex(text)))

            print('\\newpage')

            print(markdown2latex("# Bioinformatikopgaver"))

            question_keys = set()
            nr = 1
            with open(args.mult_choice_questions) as f:
                all_yaml = yaml.load(f, Loader=yaml.FullLoader)

                if args.shuffle_bioinf:
                    random.shuffle(all_yaml)

                for question in all_yaml: # get a list of dictionaries
                    for key in question: # there is only one key
                        assert key not in question_keys, ("Duplicate key", key)
                        question_keys.add(key)
                        if args.year in question[key]['used']:

                            print(format_question(question[key], nr))

                            answer_form = format_answer_form(question, nr)
                            print(answer_form, file=multiple_choice_student_file)

                            facit_form = format_facit_form(question, nr)
                            print(facit_form, file=multiple_choice_facit_file)

                            nr += 1

            # latex footer 
            print(latex_end)


    subprocess.run('pdflatex -output-directory {} {}'.format(student_file_dir, latex_file_name).split())

