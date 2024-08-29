# Bioinformatics and Programming

This repository contains the teaching material required to teach a practical 14-week undergraduate course in bioinformatics and programming. It is put here to be available to anyone setting up such a course. For information about how to run this course see [this page](teachers).

## Course description and qualifications
After the course, the participants will have basic knowledge of computer methods and applications for analyzing biological sequence data and insight into principles and techniques for constructing simple programs. Participants will acquire practical experience with analyzing problems in bioinformatics and related fields and implementing programs to solve such problems using the Python programming language.

The participants must, at the end of the course, be able to:

* Apply fundamental constructs of a programming language.
* Analyse data and construct data structures for the representation of data.
* Analyse simple computational problems and construct programs for their solution.
* Describe and relate essential methods in bioinformatics analysis.
* Apply bioinformatics software to biological data.
* Judge the reliability of results obtained using Bioinformatics software.

## Course contents
The course introduces programming and its practical applications in bioinformatics. The course also outlines and discusses bioinformatics algorithms, and the most common tools for bioinformatics analysis of sequence data are presented and demonstrated. The participant will acquire and train basic programming skills during the first seven weeks. The last seven weeks introduce key topics in bioinformatics, focusing on applying bioinformatical software and developing programming skills. Subjects for lectures and exercises include bioinformatics databases, sequence alignment, genome annotation, sequence evolution, and phylogenetic analysis.

## 14 Week outline

<!-- 
Week    | Double lecture                                        | Exercises                                         | Single lecture
---     | ---                                                   | ---                                               | ---                       
1, 35   | Introduction, Python, values, operators, variables, logic, types  | Up and running, basic Python exercises            | substitution, reduction, course helper tools
2, 36   | If, else, logic, functions, scope                     | Values, operators, math, variables                | functions, builtin functions
3, 37   | Objects, methods, strings, lists                      | Functions                                         | dictionaries, tuples
4, 38   | iteration                                             | objects, strings, lists, dictionaries (MO/B only) | Files, tests
5, 39   | **Databases, sequencing, chipSeq, mapping, GWAS**     | Reprise of last week's exercise (MM only)         | Recursion
6, 40   | **Global pairwise alignment**, data struct/project    | Iteration, files + translation project            | **Local pairwise alignment**
7, 41   | **Substitution matrices**, classes/project            | **GWAS and databases** + Folding project          | **Multiple alignment**
8, 43   | **Blast, alignment significance**, k-mers/project     | **HIV and alignment** + alignment project         | **Evolutionary distance**
9, 44   | **Clustering**, python/project                        | **MRSA, blast and mult. aln.** + Codon usage project | BioPython, Master in bioinformatics
10, 45  | **Phylogenetics**, python/project                     | **Aardwarks and DNA evolution** + HIV project     | TBA
11, 46  | **Hidden Markov models**, python/project              | **Evolution of the whale** +  Clustering project  | **Hidden Markov models**
12, 47  | **Assembly**, modules, python/project                 | **Archaea in the tree of life** +  ORF project    | **Neural networks**
13, 48  | **Genome and protein annotation**                     | **Gene finding** + Assembly project               | **RNA structure**
14, 49  | modules, biopython, **guest talk**                    | **RNA folding** + biopython                       | Evaluation, exam information
 -->


Week    | Double lecture                                        | Exercises                                         | Single lecture
---     | ---                                                   | ---                                               | ---                       
1, 35   | Introduction, Python, values, operators, variables, logic, types  | Up and running, basic Python exercises            | substitution, reduction, course helper tools
2, 36   | If, else, logic, functions, scope                     | Values, operators, math, variables                | functions, builtin functions
3, 37   | Objects, methods, strings, lists                      | Functions                                         | dictionaries, tuples
4, 38   | iteration                                             | objects, strings, lists, dictionaries (MO/B only) | Files, tests
5, 39   | **Databases, sequencing, chipSeq, mapping, GWAS**     | Reprise of last week's exercise (MM only)         | Recursion
6, 40   | **Global pairwise alignment**, data struct/project    | Iteration, files + translation project            | **Local pairwise alignment**
7, 41   | **Substitution matrices**, classes/project            | **GWAS and databases** + Folding project          | **Multiple alignment**
8, 43   | **Blast, alignment significance**, k-mers/project     | **HIV and alignment** + alignment project         | **Evolutionary distance**
9, 44   | **Clustering**, python/project                        | **MRSA, blast and mult. aln.** + Codon usage project | BioPython, Master in bioinformatics
10, 45  | **Phylogenetics**, python/project                     | **Aardwarks and DNA evolution** + HIV project     | TBA
11, 46  | **Hidden Markov models**, python/project              | **TBA** +  Clustering project                     | **Hidden Markov models**
12, 47  | **Assembly**, modules, python/project                 | **TBA** +  ORF project                            | **Neural networks**
13, 48  | **Genome and protein annotation**                     | **TBA** + Assembly project                        | **RNA structure**
14, 49  | modules, biopython, **guest talk**                    | **TBA** + Biopython                               | Evaluation, exam information



<!-- 

## Lecture notes

The [Lecture notes](book)

## Bioinformatics exercises

The [bioinformatics exercises](bioinf_exercises)

## Programming projects

The [programming projects](programming_projects)

## Lectures

The [lectures](lectures) 

## Weekly notes

The [weekly notes](weekly_notes)

-->


## Weekly notes


### Week 1 (35)

#### Reading Material
I will cover chapters 1-7 in the lecture notes.

Make sure you have installed Python and VScode for the first lecture.

#### Lectures
In the first lecture, I will outline how the course is organized and how you will get the most out of your efforts in learning programming. I will also try to give you an intuitive understanding of what programming is and what the world looks like to a computer.

In the first lecture, I will also talk about how a Python program works and about values, math, and logic.

In the second lecture, I will talk about variables, substitution, and reduction.

#### Exercises
If you have yet to do so at home, you will install Python and the text editor. To do this, follow the instructions "Before you begin". Then, start doing the exercises in the other three chapters. You will also have time to do these exercises in the TA session of week two, so go slow. It is important to properly absorb the basic concepts at the beginning of the course; otherwise, it will become too difficult later on.

---

### Week 2 (36)

#### Reading Material
I will cover chapters 8-9 in the lecture notes.

#### Lectures
In the first lecture, I will talk about how to use logic to control which statements in your program that get executed.

In the first lecture, I will also talk about how you can efficiently organize your code using functions.

In the second lecture, I will talk more about functions.

#### Exercises
The topics for this week's exercises are statements, variables, operators, expressions, substitution, reduction, and logic. You will work on the rest of the exercises in last week's curriculum for the TA session. Do what you can at home and do the rest at the TA session.

---

### Week 3 (37)

#### Reading Material
I will cover chapters 10-13 in the lecture notes.

#### Lectures
- In the first lecture, I will talk about objects and methods.
- In the first lecture, I will also talk about lists.
- In the second lecture, I will talk about dictionaries and a bit about tuples.

#### Exercises
The topics for this week's exercises are if, else, logic, and functions. You are meant to complete all the exercises in the curriculum from last week. Do what you can at home and do the rest at the TA session.

---

### Week 4  (38)

#### Reading Material
I will cover chapters 14-15 in the lecture notes.

#### Lectures
- In the first lecture, I will talk about iteration and lists.
- In the second lecture, I will talk about how your code can interact with files on your computer.

#### Exercises
The topics for this week are objects, methods, strings, lists, tuples, and dictionaries. You are meant to complete all the exercises in the curriculum from last week. Do what you can at home and do the rest at the TA session.

*Only MO and Bio classes attend the exercises this week. MM classes do not. The exercise is repeated next week for the MM classes to attend*


### Week 5  (39)

#### Reading Material

- Chapters 16-18 in the lecture notes
- [Chapter 11: Genomewide Association Studies](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002822)
- [Benefits and limitations of genomewide association studies](https://www.nature.com/articles/s41576-019-0127-1)

#### Lectures
- In the first lecture, I will talk about databases, genotyping arrays, and genomewide association studies (GWAS).
- In the second lecture, I will talk about how to use recursion in Python.

#### Exercises
The topics for this week are iteration and data structures. You are meant to complete all the exercises in the curriculum from last week. 

*Only MM classes attend the exercises this week. MO and Bio classes do not. The exercise is repeated from last week*.

---

### Week 6 (40)

#### Reading Material

- Chapter 19 in the lecture notes
- Understanding Bioinformatics 127-141

#### Lectures
- In the first lecture, I will talk about global pairwise alignment
- In the first lecture, I will also talk about Python data structures and the weekly programming project. 
- In the second lecture, I will talk about local pairwise alignment and more realistic gap scoring.

#### Exercises

You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.

**NB: This programming project "Translating open reading frames" is a mandatory exercise. The deadline for handing it in is the night before your exercise class in week 41.**

---

### Week 7 (41)

#### Reading Material

- Chapter 20 in the lecture notes
- Understanding Bioinformatics: 117-127
- Alignment methods: strategies, challenges, benchmarking, and comparative overview (don't do the exercises).

#### Lectures

- In the first lecture, I will talk about protein substitution matrices and how to score protein alignments.
- In the first lecture, I will also talk about Python topics and the weekly programming project.
- In the second lecture, I will talk about multiple alignment.

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.


---

### Week 8 (43)

#### Reading Material

- Chapter 21 in the lecture notes
- Bioinformatics Explained: BLAST
- Biological Sequence Analysis pp. 192-197

#### Lectures

- In the first lecture, I will talk about how to search for matches in a sequence database and how to asses alignment significance. 
- In the first lecture, I will also talk about Python topics and the weekly programming project.
- In the second lecture, I will talk about models of DNA evolution and how to measure evolutionary distance between sequences.

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.


---

### Week 9 (44)

#### Reading Material

- Chapter 22 in the lecture notes
- Biological Sequence Analysis pp. 165-179

#### Lectures

- In the first lecture, I will talk about methods for sequence clustering
- In the first lecture, I will also talk about Python topics and the weekly programming project.
- In the second lecture, I will talk about bioinformatics code libraries for Python, such as BioPython, and the Master in Bioinformatics that we offer at the Bioinformatics Centre.

---

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.


---

### Week 10 (45)

#### Reading Material

- Chapter 23 in the lecture notes
- Biological Sequence Analysis pp. 192-202

#### Lectures

- In the first lecture, I will talk about phylogenetic trees.
- In the first lecture, I will also talk about Python topics and the weekly programming project.
- In the second lecture, I will talk about ... (TBA) 

<!-- TODO: Add topic for second lecture -->

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.

**NB: This programming project "Identifying the subtype of an HIV sequence" is a mandatory exercise. The deadline for handing it in is the night before your exercise class in week 46.**

---

### Week 11 (46)

#### Reading Material

- Chapter 24 in the lecture notes
- Biological Sequence Analysis pp. 46-66
- Understanding Bioinformatics pp. 494-496

### Lectures
- In the first lecture, I will talk about hidden Markov models (HMMs).
- In the first lecture, I will also talk about python topics and the weekly programming project.
- In the second lecture, I will talk about more about HMMs

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.


---

### Week 12 (47)

#### Reading Material

- Chapter 25 in the lecture notes
- [The Theory and Practice of Genome Sequence Assembly](https://www.annualreviews.org/doi/10.1146/annurev-genom-090314-050032)

### Lectures

- In the first lecture, I will talk about genome assembly.
- In the first lecture, I will also talk about Python topics and the weekly programming project.
- In the second lecture, I will talk about neural networks.

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.

---

### Week 13 (48)

#### Reading Material

- Chapter 26 in the lecture notes
- [Automatic generation of gene finders for Eukaryotic species](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-7-263)
- Understanding Bioinformatics pp. 438-448
- Exploring Bioinformatics pp. 242-248

### Lectures
- In the first lecture, I will talk about gene finding and protein annotation
- In the second lecture, I will talk about RNA secondary structure prediction.

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.

---

### Week 14 (49)

#### Reading Material

- TBA

#### Lectures

- First lecture, TBA + Guest lecture
- In the last lecture, we will evaluate the course and review the exam's practicalities.

#### Exercises
You will do the weekly bioinformatics web exercise. You can find the description of the exercise and any relevant files below. You will also do the weekly programming project described in the chapter listed under Reading Material. You can download the files needed for the programming project under the "Programming project files" tab. There will be lots of work, so do what you can at home and do the rest at the TA session.



