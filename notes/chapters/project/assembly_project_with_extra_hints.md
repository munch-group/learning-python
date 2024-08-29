# Chapter 6

## Genome assembly

In genome assembly many short sequences (reads) from a sequencing machine are assembled into long sequences - ultimately chromosomes. This is done by ordering overlapping reads so that they together represent genomic sequences. For example given these three reads: AGGTCGTAG, CGTAGAGCTGGGAG, GGGAGGTTGAAA ordering them based on their overlap like this

	AGGTCGTAG
	    CGTAGAGCTGGGAG
	             GGGAGGTTGAAA

produces the following genomic sequence:

	AGGTCGTAGAGCTGGGAGGTTGAAA

We split the problem into four parts: 

1. Get the sequencing data.
2. Compute the overlaps between reads.
3. Find the right order of reads.
4. Reconstruct the genomic sequence.

Real genome assembly is of course more sophisticated than what we do here, but the idea is the same. To limit the complexity of the problem we make two simplifying assumptions:

1. There are no sequencing errors implying that true overlaps between reads can be identified as perfectly matching overlaps.
2. No reads are nested in other reads. I.e. They are never a smaller part of another read.

The second assumption implies that overlaps are always of this type:

```
    CGTAGAGCTGGGAG
             GGGAGGTTGAAA
```

and never of this type:

```
    CGTAGAGCTGGGAG
       AGAGCTG
```

In this project you will be asked to write functions that together solve the problem of assembling a genomic sequence. Some of the functions each solve a small problem, and you will call these functions inside other functions, to put together solutions to larger subproblems.

The sequence reads for the mini-assembly are in the file sequencing_reads.txt in the project folder. The format of this file is like this:

	Read1 ATGCG...
	Read2 AGGCG...
	Read3 TGAAG...

Each line represents a read. The first field on each line is the name of the read and the second field is the read sequence itself. So for the first line "Read1" is the name and "ATGCG..." is the sequence.

This is a tricky project. Make sure you read the entire exercise and understand what you are supposed to do before you begin!

## Part 1: Get the sequencing data

### Read the sequence reads into a dictionary

The first task is to read and parse the input data. 

*Write a function*, `read_data`, that takes one argument:

1. A string, which is the name of the data file.

The function must return

* A dictionary, where the keys are read *names* and the values are the associated read *sequences*. Both keys and values must be strings.

Example usage:

```python
read_data('sequencing_reads.txt')
```

should return a dictionary with the following content (maybe not with key-value pairs in that order)

```python
{'Read1': 'GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGC',
 'Read3': 'GTCTTCAGTAGAAAATTGTTTTTTTCTTCCAAGAGGTCGGAGTCGTGAACACATCAGT',
 'Read2': 'CTTTACCCGGAAGAGCGGGACGCTGCCCTGCGCGATTCCAGGCTCCCCACGGG',
 'Read5': 'CGATTCCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC',
 'Read4': 'TGCGAGGGAAGTGAAGTATTTGACCCTTTACCCGGAAGAGCG',
 'Read6': 'TGACAGTAGATCTCGTCCAGACCCCTAGCTGGTACGTCTTCAGTAGAAAATTGTTTTTTTCTTCCAAGAGGTCGGAGT'}
```

Here is some scaffold code to get you started:

```python
def read_data(file_name):
    input_file = open(file_name)
    # ...
    for line in input_file:
	     # ...    
    # ...
    
    input_file.close()        
```

### Compute mean length of sequence reads

Often there are too many reads to look at them manually. To know what we are working with we want to know what the mean length of the reads is.

*Write a function*, `mean_length`, that takes one argument:

1. A dictionary, which contains read names as keys and reads sequences as values (this is a dictionary like that returned by `read_data`).

The function must return

* A float, which is the average length of the sequence reads.


## Part 2: Compute the overlaps between reads.

### Compute the overlap between two reads

Next thing is to figure out which reads overlap each other. To do that we need a function that takes two read sequences and computes their overlap. Remember that in the input data none of the reads are completely nested in another read.

We know that there are no sequencing errors, so in the overlap the sequence match will be perfect. To compute the overlap betwee the 3' end of the left read with the 5' end of the right read, you need to loop over all possible overlaps honouring that one sequence is the left one and the other is the right one. In the for loop, start with the largest possible overlap ( `min(len(left), len(right))`) and evaluate smaller and smaller overlaps until you find an exact match.

Hint: In each iteration of the for-loop you want to to compare the last `i` bases of the left sequence with the first `i` bases of the right sequence. You can slice out the latter using `right[:i]`.

*Write a function*, `get_overlap`, that takes two arguments

1. A string, which is the left read sequence.
2. A string, which is the right read sequence.

The function must return

* A string, which is the overlapping sequence. If there is no overlap it should return an empty string. 

Example usage:

```python
s1 = "CGATTCCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC"
s2 = "GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGC"
get_overlap(s1, s2)
```

should return the string

```python
'GGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTC'
```

and `get_overlap(s2, s1)`

should return the string

```python
'C'
```

From these two examples it seems that `s1` and `s2` overlap and that `s1` is the left one and `s2` is the right one. Treating `s2` as the left one and `s1` as the right one only gives an overlap of one base (we expect a few bases of overlap even for unrelated sequences).

### Compute all overlaps

Now that we can evaluate the overlap between two reads in some orientation we can compute overlaps between all pairs of reads in both left-right and right-left orientations.

*Write a function*, `get_all_overlaps`, that takes one argument:

1. a dictionary with read data as returned by `read_data`.

The function must return

* A dictionary of dictionaries, specifying the number of overlapping bases for a pair of reads in a specific left-right orientation. 

Computing the overlap of a read to itself is meaningless and must not be included. If the overlap between read 2 in left position and `5` in right position is `21` then `d['Read2']['Read5']` must be `21` (if the dictionary was called `d`). Make sure you understand how this data structure represents the overlaps before you go on.

Assuming the resulting dictionary of dictionaries is called `d`, then `d['Read2']` will be a dictionary where keys are the names of reads that have an overlap with read `'Read2'` when `'Read2'` is put in the left position, and the values for these keys are the number of overlapping bases for those reads.

Example usage: assuming that `reads` is a dictionary returned by `read_data` then:

```python
get_all_overlaps(reads)
```

should return a the following dictionary of dictionaries (but not necessarily with the same ordering of the key-value pairs):

```python
{'Read1': {'Read3': 0, 'Read2': 1, 'Read5': 1, 'Read4': 0, 'Read6': 29},
 'Read3': {'Read1': 0, 'Read2': 0, 'Read5': 0, 'Read4': 1, 'Read6': 1},
 'Read2': {'Read1': 13, 'Read3': 1, 'Read5': 21, 'Read4': 0, 'Read6': 0},
 'Read5': {'Read1': 39, 'Read3': 0, 'Read2': 1, 'Read4': 0, 'Read6': 14},
 'Read4': {'Read1': 1, 'Read3': 1, 'Read2': 17, 'Read5': 2, 'Read6': 0},
 'Read6': {'Read1': 0, 'Read3': 43, 'Read2': 0, 'Read5': 0, 'Read4': 1}}
```

Hint: To generate all combinations of reads you need two for-loops. One looping over reads in left positions and another (inside the first one) looping over reads in right position. Remember that we do *not* want the overlap of a read to itself.

### Print all overlaps nicely

The dictionary returned by `get_all_overlaps` is a little messy to look at. We want to print it in a nice matrix-like format so we can better see which pairs overlap in what orientations.

*Write a function*, `pretty_print`, that takes one argument:

1. A dictionary of dictionaries as returned by `get_all_overlaps`.

The function should not return anything but must *print* a matrix exactly as shown in the example below with nicely aligned and right-justified columns. The first column must hold names of reads in left orientation. The top row holds names of reads in right orientation. Remaining cells must each hold the number of overlapping bases for a left-right read pair. The diagonal corresponds to overlaps to the read itself. You must put dashes in these cells.

Example usage: assuming that `overlaps` is a dictionary of dictionaries returned by `get_all_overlaps` then:

```python
pretty_print(overlaps)
```

should print exactly

	       Read1  Read2  Read3  Read4  Read5  Read6 
	Read1      -      1      0      0      1     29 
	Read2     13      -      1      0     21      0
	Read3      0      0      -      1      0      1
	Read4      1     17      1      -      2      0 
	Read5     39      1      0      0      -     14 
	Read6      0      0     43      1      0      -

Hint: To make a string that is padded with space characters to give it a total length of 6 you can do this:

```python
s = '{:>6}'.format('Read1')
```

To print this string without adding a `\n` at the end, use the end keyword argument to `print`:

```python
print(s, end='')
```

Notice that the overlaps are not either zero or a large number. A lot of the overlaps are `1` or `2`. This is because you often find a few bases of overlap just by chance between any two reads. So in the following we must distinguish true (significant) overlaps from random ones. For this purpose we simply decide that true overlaps are the ones with an overlap larger than two (>2).

## Part 3: Find the right order of reads

Now that we know how the reads overlap we can chain them together pair by pair from left to right to get the order in which they represent the genomic sequence. To do this we take the first (left-most) read and identify which read has the largest overlap to its right end. Then we take that read and find the read with the largest overlap to the right end of that - and so on until we reach the rightmost (last) read.

### Find the first read

The first thing you need to do is to identify the first (leftmost) read so we know where to start. This read is identified as the one that only has a significant (>2) overlap to its right end (it only has a good overlap when positioned to the left of other reads). In the example output from `pretty_print` above the first read would be read `'Read4'` because the `'Read4'` column has no significant overlaps (no one larger than two).

*Write a function*, `find_first_read`, that takes one argument:

1. A dictionary of dictionaries as returned from `get_all_overlaps`.

The function must return

* A string containing the name of the first read.

Example usage:

```python
find_first_read(reads)
```

should return

```python
'Read4'
```

### Find the order of reads

Now that we have the first read we can find the correct ordering of reads. We want a list with the read names in the right order.

The read that should come after some read is the one which has the largest overlap to the right end of that read. To figure out which read that is, we use our dictionary of overlaps. If the first read is `'Read4'` then `overlaps['Read4']` is a dictionary of reads with overlap to the right end of read `'Read4'`. So to find the name of the read with the largest overlap you must write a function that finds the key associated with the largest value in a dictionary. We do that first:

*Write a function*, `find_key_for_largest_value`, that takes one argument:

1. A dictionary.

The function must return the key associated with the largest value in the dictionary argument.

You need this function as a tool in the next function:

*Write a function*, `find_order`, that takes two arguments:

1. A string, which is the name of the first (left-most) read (that returned by `find_first_read`).
2. A dictionary of dictionaries, of all overlaps (that returned by `get_all_overlaps`).

The function must return

* A list of strings, which are read names in the order in which they represent the genomic sequence. 

Hints: You know the first read is given by the first argument to the function, you also know that you can find the next read in the chain of overlapping reads by using the `find_key_for_largest_value` function, and you know that you should keep adding on reads to the chain as long as the overlap is larger than two (you can use a for-loop with an if-statement inside to check that the overlap is larger than 2).

Example usage: assuming that `overlaps` is a dictionary of dictionaries returned by `get_all_overlaps` then:

```python
find_order('Read4', overlaps)
```

should return:

```python
['Read4', 'Read2', 'Read5', 'Read1', 'Read6', 'Read3']
```

Make sure you understand why this is the right list of read names before you try to implement the function.

## Part 4: Reconstruct the genomic sequence

### Reconstruct the genomic sequence from the reads

Now that you have the number of overlapping bases between reads and the correct order of the reads you can reconstruct the genomic sequence.

*Write a function*, `reconstruct_sequence`, that takes three arguments:

1. A list of strings, which are the names of reads in the order identified by `find_order`.
2. A dictionary, with read data as returned from `read_data`.
3. A dictionary of dictionaries with overlaps as returned from `get_all_overlaps`. 

The function must return

* A string, which is the genomic sequence.

Example usage: assuming that `order` is the list of strings returned by `find_order`, that `reads` is the dictionary returned by `read_data` and that `overlaps` is a dictionary of dictionaries returned by `get_all_overlaps` then:	

```python
reconstruct_sequence(order, reads, overlaps)	
```

should return one long string with these letters (had to break it in three to make it fit on hte page):

```python	
TGCGAGGGAAGTGAAGTATTTGACCCTTTACCCGGAAGAGCGGGACGCTGCCCTGCGCGATT
CCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGCTGGTA
CGTCTTCAGTAGAAAATTGTTTTTTTCTTCCAAGAGGTCGGAGTCGTGAACACATCAGT
```

Hint: iterate over the reads in order and use the overlap information to extract and join the appropriate parts of the reads.

### Putting the whole thing together

Now that you have written functions to take care of each step you can write one last function that uses them to do the entire assembly.

*Write a function*, `assemble_genome`, that takes one argument:

1. A string, which is the name of a file with sequencing reads in the format described in the beginning of this project description.

The function must return

* A string, which is the genome assembled from the sequencing reads

Example usage:

```python
assemble_genome('sequencing_reads.txt')
```

should return the assembled genome:

```python	
TGCGAGGGAAGTGAAGTATTTGACCCTTTACCCGGAAGAGCGGGACGCTGCCCTGCGCGATT
CCAGGCTCCCCACGGGGTACCCATAACTTGACAGTAGATCTCGTCCAGACCCCTAGCTGGTA
CGTCTTCAGTAGAAAATTGTTTTTTTCTTCCAAGAGGTCGGAGTCGTGAACACATCAGT
```
