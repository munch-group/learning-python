# Sequence Curation


**TURN EXAM ASSIGNMENT INTO PROJECT**


## Download the exam package

This assignment proceeds like the programming projects you completed during the course. You start by downloading the exam assignment from the Blackboard course home page. Once you have downloaded the package you must turn off internet on your computer. Internet is ***not*** allowed during the exam.

At the bottom of the course front page you can see the exam assignment just below project1, projct2 and project3. Download the file `exam.zip` and unpack it on your computer. The package contains two files: `exam.py` and `test_exam.py`. These two files are the equivalent to `project3.py` and `test_project3.py` from programming project 3. You write your code in `exam.py` and you can test your code using `test_exam.py`.

As always you run your code like this:

```
python exam.py
```

and test your code like this:

```python
python test_exam.py
```

Note that functions, which do not pass *ALL* tests, are considered failed. 

## How to hand in your assingment

At the end of the exam you will be allowed to go online and upload your solution under “Exam Assignment” on Blackboard (The same place you donwloaded `exam.zip` from). If you are done before the end of the exam you can raise your hand and you will be allowed to go online and upload your solution under supervision.

## How to solve this assignment

In each problem below you are asked to write one function with a given name. You must name this function **exactly** as specified. Functions that are not correctly named are considered completely failed. Functions that do not work **exactly** as specified are considered completely failed. You can use the `test_exam.py` script to test your functions and to make sure they are named correctly, but the correct implementation of each function is entirely your own responsibility.

The final file with code, which you hand in, should only contain definitions of these functions. No code for testing the functions should be included in the final file. You should also know that comments are not considered in the evaluation. 

In the assignment, Python code will look like this:

```python
print("hello world")
```
and whenever we refer to Python code inside a sentence it will be styled like `this`.

## Introduction

In this exam assignment you will work with DNA sequences. For the purpose of this exam assignment we will assume that DNA sequences are always upper case. In some of the problems you will also work with strings of quality scores associated with the DNA sequences. In these cases, each DNA sequence has a string of quality scores of the same length as the DNA sequence. Each digit in the string of quality scores corresponds to a base in the DNA sequence and represents how certain we are that this base has been corrrectly called by the sequencing machine. Quality scores can take the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. E.g. if a DNA sequence is `'ATG'` and the associated string of quality scores is `'735'`, then the quality score of the first base, `'A'`, is `7`.

Note that your functions should work as specified in each problem no matter what these DNA sequences and quality scores are. However, to provide examples of input data I will give you two DNA sequences and a string of qualities for bases in each of these DNA strings.

The two example DNA sequences are:

```python
ex_s1 = 'AGTCGACGGATGAACCTCCACTTACACTATCTT'
ex_s2 = 'TGTCTACGGTTGATCCTGCACGTACAGTATCAT'
```

The two example strings of quality scores for sequences `ex_s1` and `ex_s2` are:

```python
ex_q1 = '707915609164612603160290247832979'
ex_q2 = '059565606246285080270942561713910'
```

In some of the problems below I will provide an example of what each function should return when the example sequences (`ex_s1` and `ex_s2`) and/or quality strings (`ex_q1`, `ex_q2`) are used as arguments. To use the examples provided you must of course define these variables (exactly) as shown above.

The actual assignment starts on the next page. Happy coding.

<div style="page-break-after: always;"></div>

## Problem 1

We want to compute how long a DNA sequence is.

*Write a function*, `find_length`, which takes one argument:

1. A string, which is a DNA sequence.

The function must return:

* An integer, which is the length of the string provided as argument to the function.

Example usage: If the function is called like this `find_length("AGTC")` it should return `4`.


## Problem 2

We want to compare the length of two sequenes to test if they have the same length. 

*Write a function*, `compare_length`, which takes two arguments:

1. A string, which is a DNA sequence.
2. A string, which is a DNA sequence.

The function must return:

* `True` if the two sequences have equal length, and `False` otherwise.

Example usage: If the function is called like this `compare_length("TGA", "TGAC")` it should return `False`.

<div style="page-break-after: always;"></div>

## Problem 3

We want to be able to count how many of each base that a DNA sequence contains.

*Write a function*, `count_bases`, which takes one argument:

1. A string, which is a DNA sequence.

The function must return:

* A dictionary, in which keys are strings representing bases and values are the integers representing the number of times bases occur in the sequence. Bases that are *not* in the DNA string must *not* be represented as keys in the dictionary.

Example usage: If the function is called like this 

```python
count_bases(ex_s1)
```

it should return (not necessarily with key-value pairs in the same order):

```python
{'A': 9, 'C': 10, 'T': 9, 'G': 5}`.
```

(assuming, of course, that `ex_s1` is defined as above).

## Problem 4

We want to be able to count the number of differences between two DNA sequences.

*Write a function*, `count_differences`, which takes two arguments:

1. A string, which is a DNA sequence.
2. A string, which is a DNA sequence.

The function must return:

* An integer, which is the number of differences between the two DNA strings.

Example usage: If the function is called like this 

```python 
count_differences("AATT", "TTTT")
```

it should return `2`.

<div style="page-break-after: always;"></div>

## Problem 5

We want to write a function that reverses a DNA sequence.

*Write a function*, `reverse_seq`, which takes one argument:

1. A string, which is a DNA sequence. 

The function must return:

* An string, which is the reverse of the DNA sequence provided as argument.

Example usage: If the function is called like this `reverse_seq("ACTG)` it should return `'GTCA'`.

## Problem 6

We want to obtain the reverse complement of a DNA sequence. I.e. the resulting DNA sequence should not only be in the reverse order, but each base must also be translated into its complementary base (A to T, T to A, C to G and G to C).

*Write a function*, `reverse_complement_seq`, which takes one argument:

1. A string, which is a  DNA sequence.

The function must return:

* An string, which is the reverse complement of the DNA sequence provided as argument.

Example usage: If the function is called like this `reverse_complement_seq("ACTG")` it should return `CAGT`.

<div style="page-break-after: always;"></div>

## Problem 7

In DNA a "CpG" site is a C followed by a G: I.e. the string "CG". We want to find the location of all such CpG sites in a DNA sequence.

*Write a function*, `find_cpg_sites`, which takes one argument:

1. A string, which is a DNA sequence.

The function must return:

* A list of integers, which represent the positions of all CpG sites in the the DNA sequence. Each integer in the list must represent the string index of the 'C' base of the 'CG' pair.

Example usage: If the function is called like this 

```python
find_cpg_sites('CGAGCGAACG')
``` 

it should return `[0, 4, 8]`.

## Problem 8

We want to be able to find the CpG sites that appear at the *same* positions in *two* sequences of same length. 

*Write a function*, `find_orthologous_cpg_sites`, which takes two arguments:

1. A string, which is a DNA sequence.
2. A string, which is a DNA sequence.

The function must return:

* A list of integers, which represent the positions where both DNA sequences have a CpG site. Each integer in the list must represent the string index of the 'C' base of the 'CG' pair.

Example usage: If the function is called like this

```python
find_orthologous_cpg_sites('CGAGCGAACG', 'CGAGAGAACG')
```

it should return `[0, 8]`.

<div style="page-break-after: always;"></div>

## Problem 9

In several of the problems below you will work with strings of quality scores like this: `'4892743'`. To turn such strings of digits into a list of integers we need a function. You get this one for free, so to solve this problem all you need to do is define this function *exactly* as stated below:

```python
def string_to_list_of_integers(qualities):
    return list(map(int, qualities))
```

Example usage: If the function is called like this 

```python
string_to_list_of_integers("473")
```

it should return:

```python
[4, 7, 3]
```

## Problem 10

We want to find the average sequencing quality of bases in a sequence.

*Write a function*, `average_quality`, which takes one argument:

1. A string, which is a string of quality scores.

The function must return:

* A float, which is the average of all digits in the string provided as argument to the function.

Example usage: If the function is called like this `average_quality('12')` it should return `1.5`.

<div style="page-break-after: always;"></div>

## Problem 11

We suspect that the quality of adjacent bases may not be independent. To address this we want to compute the average difference between adjacent quality scores in a string of qualities. E.g. in the string `'125'` there are two adjacent pairs: `'12'` and `'25'`. The difference is `1` in the first case and `3` in the other, so the average difference is `2.0` in this case.

*Write a function*, `average_quality_difference`, which takes one argument:

1. A string, which is a string of quality scores of for a DNA sequence.

The function must return:

* An float, which is the average difference between adjacent qualities in the string. If the string is shorter than 2 the function must return `None`.

Example usage: If the function is called like this:

```python
average_quality_difference('125')
```

it should return `2.0`.

<div style="page-break-after: always;"></div>

## Problem 12

We want to find the average sequencing quality of each type of base (A, T, C and G) in the sequence.

*Write a function*, `average_quality_by_base`, which takes two arguments:

1. A string, which is a DNA sequence
2. A string, which is a string of quality scores of same length as the DNA sequence.

The function must return:

* A dictionary, in which keys are strings representing bases and values are the floats representing the average quality score for each base. The dictionary must only include bases which occur in the DNA sequence.

Example usage: If the function is called like this:

```pyhton
average_quality_by_base(ex_s1, ex_q1)
```

it should return (not necessarily with key-value pairs in the same order):

```python
{'A': 3.6666666666666665, 'C': 4.5, 'T': 5.555555555555555, 'G': 2.8}
```

<div style="page-break-after: always;"></div>


## Problem 13

We want to compute the average sequencing quality of bases that are part of CpG sites. I.e. all bases that are part of a "CG" pair.

*Write a function*, `average_quality_for_cpg_sites`, which takes two arguments:

1. A string, which is a DNA sequence.
2. A string, which is a string of quality scores of same length as the DNA sequence.

The function must return:

* A float, representing is the average quality of bases that are part of a "CG" pair.

Example usage: If the function is called like this

```python
average_quality_for_cpg_sites(ex_s1, ex_q1)
```

it should return `4.0`.

## Problem 14

We want to mask a DNA sequence so the bases with a sequencing quality below some cutoff are replaced by `'N'` characters.

*Write a function*, `mask_low_quality_bases`, which takes three arguments:

1. A string, which is a DNA sequence.
2. A string, which is a string of quality scores of same length as the DNA sequence.
3. An integer, which is the lowest acceptable quality score for a base.

The function must return:

* A string that is the DNA string provided as argument, in which all bases with quality score lower than that specified by the third argument are replaced by `'N'`.

Example usage: If the function is called like this 

```python
mask_low_quality_bases('AGCT', '2134', 2)
```

it should return `'ANCT'`.

<div style="page-break-after: always;"></div>

## Problem 15

Given two strings of qualities of equal length, we want to find the lowest quality at each position.

*Write a function*, `lowest_qualities_at_position`, which takes two arguments:

1. A string, which is a string of quality scores.
2. A string, which is a string of quality scores of same length as the other string of quality scores.

The function must return:

* An list of integers representing the lowest quality at each position along the two quality strings provided as function arguments.

Example usage: If the function is called like this 

```python
lowest_qualities_at_position('1234', '4321')
```

it should return `[1, 2, 2, 1]`.

<div style="page-break-after: always;"></div>

## Problem 16

When comparing two homologous DNA sequences of equal length we suspect that differences could be due to sequencing errors rather than mutations. To address this problem we want to find out if the lowest quality base at positions where the DNA sequences differ (heterozygous positions) is lower than where the DNA sequences are the same (homozygous positions). 

*Write a function*, `average_lowest_quality_at_homo_and_hetero`, which takes four arguments:

1. A string, which is the DNA sequence of sequence one
2. A string, which is the DNA sequence of sequence two
3. A string, which is a string of quality scores for sequence one
4. A string, which is a string of quality scores for sequence two

The function must return:

* A list with two floats. The first float must be the average of minimum qualities at *homozygous* sites. The second float must be the average of minimum qualities at *heterozygous* sites.

Example usage: If the function is called like this 

```python
average_lowest_quality_at_homo_and_hetero('AAAA', 'TAAT', '1234', '4321')
```

it should return `[2.0, 1.0]`.

<div style="page-break-after: always;"></div>

## Problem 17

We want to count the number of occcurences of each base in a DNA sequence at the sequence positions associated with a specified quality score. 

*Write a function*, `count_bases_with_a_quality`, which takes three arguments:

1. A string, which is a DNA sequence.
2. A string, which is a string of quality scores of same length as the DNA sequence.
3. An integer, which is the quality score for sites we want to count.

The function must return:

* A dictionary, in which keys are strings representing each base, and values are the integers representing the number of occurences of the base. When some base is not observed its count must be 0.

Example usage: If the function is called like this 

```python
count_bases_with_a_quality(ex_s1, ex_q1, 9)
```

is should return (not necessarily with key-value pairs in the same order):

```python
{'T': 2, 'C': 2, 'A': 0, 'G': 1}
```

<div style="page-break-after: always;"></div>

## Problem 18

We suspect there is a relation between quality at a site and which base that is called at that site. To address this we need to count the number of occcurences of different bases at sites with each quality score.

*Write a function*, `count_bases_by_quality`, which takes two arguments:

1. A string, which is a DNA sequence.
2. A string, which is a string of quality scores of same length as the DNA sequence.

The function must return:

* A dictionary of dictionaries, specifying the counts of each base for each quality score observed. The keys in the dictionary should be integers representing quality scores. The values should be dictionaries pairing bases with their counts (as produced in problem 17). 

Example usage: If the function is called like this 

```python
count_bases_by_quality(ex_s1, ex_q1)
```

and if the dictionary to be returned is called `d` then `d[9]` should be `{'T': 2, 'C': 2, 'A': 0, 'G': 1}` (though not necessarily with key-value pairs in the same order).

<div style="page-break-after: always;"></div>

## Problem 19

Replacing low-quality bases with `'N'` produces a DNA sequence with lots of Ns in it. We want to extract all the sub-sequences that do not have N characters in them.

*Write a function*, `get_unmasked_sequence`, which takes one argument:

1. A string, which is a DNA sequence that may contain `'N'` characters.

The function must return:

* A list of strings, which are the sub-sequences without `'N'` characters that are found in the DNA sequence. If there are no sub-sequences without `'N'` characters the function must return an empty list. If the function argument does not contain `'N'` characters the function must return the function argument. 

Example usage: If the function is called like this 

```python
get_unmasked_sequence("AAANNTTNGGG")
```

it should return:

```python
['AAA', 'TT', 'GGG']
```

<div style="page-break-after: always;"></div>

## Problem 20

If we want to compare two sequences in an analysis we want sequence positions with low quality in *either* sequence to be replaced with `'N'` in *both* sequences. This way the two resulting sequences will have `'N'` characters in the same positions.

*Write a function*, `mask_sequence_pair`, which takes five arguments:

1. A string, which is the DNA sequence of sequence one
2. A string, which is the DNA sequence of sequence two
3. A string, which is a string of quality scores for sequence one
4. A string, which is a string of quality scores for sequence two
5. An integer, which is the lowest acceptable quality score for a base.

The function must return:

* A list of two strings. The first string must be a masked version of the first sequence argument. The second string must be a masked version of the second sequence argument.

Example usage: If the function is called like this:

```python
mask_sequence_pair(ex_s1, ex_s2, ex_q1, ex_q2, 2)
```

it should return:

```python
['NNTCNACNGNTGANCNNNNANTTNCANTNTCNN', 'NNTCNACNGNTGANCNNNNANGTNCANTNTCNN']
```
