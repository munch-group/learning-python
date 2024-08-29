# Project: Clustering sequences based on distance ⁕

*This chapter is about clustering sequence based on the evolutionary distance between them.*

On the course page you can download the files you need for this project:

- `seqdistproject.py` is an empty file where you must write your code.
- `test_seqdistproject.py` is the test program that lets you test the code you write in translationproject.py.

Put the files in a folder dedicated to this project. On most computers you can right-click on the link and choose "Save file as..." or "Download linked file".

## Measuring sequence distance {-}

Clustering is based on the distances between all pairs of sequences. So before you can build your tree you must compute those distances and fill them into a table like that in the book. Here we break that task into three parts:

1. Compare two sequences
2. Make the Jukes-Cantor correction
3. Generate a (lower triangular) distance matrix

### Compare two sequences {-}

The first function you must write is one that finds the proportion of different bases between two sequences:

*Write a function*, `sequence_difference`, which takes two arguments:

1. A string, which represents a DNA sequence.
2. A string, which represents a DNA sequence of the same length as argument one.

The function must return:

* A float, which represents the proportion of different bases between the two sequences.

Example usage:

```python
sequence_difference('AAATTAAA', 'AAAAAAAA')
```

should return

```python
0.25
```

### Make the Jukes-Cantor correction {-}

To take into account that some substitutions may fall on top of others you must do the Jukes-Cantor correction you read about in the book. The formula is like this:

$$ K = -\frac{3}{4} \ln(1 - \frac{4}{3}*D) $$

Where $D$ is the proportion of differences as returned by `seqeunce_diff` and $K$ is the Jukes-Cantor corrected distance. In the top of `seqdistproject.py` it already says: 

```python
from math import log
```

That line makes the `log` (logarithm) builtin function from the `math` python library available to your programme. Try to find its Python documentation to see how you use it.

*Write a function*, `jukes_cantor`, which takes one argument:

1. A float, which represents a proportion of different bases between two sequences.

The function must return:

* A float, which represents the Jukes-Cantor corrected distance corresponding the proportion of differences given as argument.

Example usage:

```python
jukes_cantor(0.1)
```

should return

```python
0.10732563273050497
```

## Lower triangular distance matrices {-}

This project is all about distances between pairs (of sequences), and what would be more natural than to put all the distances in a matrix so you can look up the distance between the sequences with indexes `i` and `j` as the matrix element in row `i` and column `j`. You already know how matrices can be represented by lists of lists. E.g. a matrix like this:

<pre>
0.0  0.1  0.3  0.3  0.1  0.2
<b>0.1</b>  0.0  0.2  0.4  0.1  0.1
<b>0.3</b>  <b>0.2</b>  0.0  0.4  0.2  0.3
<b>0.3</b>  <b>0.4</b>  <b>0.4</b>  0.0  0.2  0.1
<b>0.1</b>  <b>0.1</b>  <b>0.2</b>  <b>0.2</b>  0.0  0.1
<b>0.2</b>  <b>0.1</b>   <b>0.3</b>  <b>0.1</b>  <b>0.1</b> 0.0
</pre>

can be expressed as a list of lists like this:

```python
[[0.0, 0.1, 0.3, 0.3, 0.1, 0.2],
 [0.1, 0.0, 0.2, 0.4, 0.1, 0.1],
 [0.3, 0.2, 0.0, 0.4, 0.2, 0.3],
 [0.3, 0.4, 0.4, 0.0, 0.2, 0.1],
 [0.1, 0.1, 0.2, 0.2, 0.0, 0.1],
 [0.2, 0.1, 0.3, 0.1, 0.1, 0.0]]
```

Notice how the diagonal is all zeros because these distances represent the distance of a sequence to itself. Also, notice that the part above the diagonal is a mirror the part below the diagonal (in bold). This is all a bit redundant, especially in this project where you will have to reduce the matrix as you group (or cluster) sequences together. We want something nice and lean where we only have the numbers we need -- and that is the *lower triangular matrix*:

    
    0.1
    0.3 0.2
    0.3 0.4 0.4
    0.1 0.1 0.2 0.2
    0.2 0.1 0.3 0.1 0.1

In Python this is still just a list of lists, only, each sublist now has the same length as its index in the big list (E.g. `[0.3, 0.2]` has index `2` in the list and has length `2`):

```python
matrix = [[],
		      [0.1],
		      [0.3, 0.2],
		      [0.3, 0.4, 0.4],
		      [0.1, 0.1, 0.2, 0.2],
		      [0.2, 0.1, 0.3, 0.1, 0.1]]
```

Here I am just writing it nicely. If you where to print that list of lists it would look like this:

	[[], [0.1], [0.3, 0.2], [0.3, 0.4, 0.4], [0.1, 0.1, 0.2, 0.2], [0.2, 0.1, 0.3, 0.1, 0.1]]

Say your sequences had names: A, B, C, D, E, and F, then the above data structure represents distances between each pair like this:

	
	A 
	B 0.1
	C 0.3 0.2
	D 0.3 0.4 0.4
	E 0.1 0.1 0.2 0.2
	F 0.2 0.1 0.3 0.1 0.1
	   A   B   C   D   E   F

There is only one drawback with this reduced representation of the full square matrix: In the full matrix you can get the distance between the sequences with indexes `i` and `j` as *both* `matrix[i][j]` and `matrix[j][i]` because the part above and below the diagonal are the same. Using the lower triangular matrix, you must always use the *largest* index first. Using the smaller one first will give you an `IndexError`. So if you want the distance between sequences with index `2` and `4`, you must use the bigger index first (as the row index): `matrix[4][2]`.

## Generate a distance matrix {-}

*Write a function*, `lower_trian_matrix`, which takes one argument:

1. A list of strings. All strings have equal length and represent DNA sequences.

The function must return:

* A list of lists of floats, which represent the lower triangular matrix of Jukes-Cantor distances between DNA sequences given as argument.  

Example usage:

```python
sequences = ['TAAAAAAAAAAA', 
             'TTAAAAAAAAAA', 
             'AAAAAAAAAAGG', 
             'AAAAAAAAGGGG']
lower_trian_matrix(sequences)
```

here `lower_trian_matrix` should return:

```python
[[], 
 [0.08833727674228764], 
 [0.30409883108112323, 0.4408399986765892], 
 [0.6081976621622466, 0.8239592165010822, 0.18848582121067953]]
```

You should use `sequence_difference` to compute the proportion of differences between each pair of sequences and `jukes_cantor` to produce the corrected distance to fill into the matrix.

Start by figuring out what pairs of indexes you need and then figure out how you can make two nested for-loops generate them. Remember that the length of each sublist is equal to its index in the big list.

## Clustering {-}

Now that you have the distance matrix you are ready for the actual clustering. There are three steps to that:

1. Find the pair you want to join
2. Compute the distances between the joined pair and all other elements (linkage)
3. Keep going until you only have one left

Depending on how you choose which pair to join and how you compute the new distances for the joined pair determines what kind of clustering you do. Here we will try a centroid-like linkage called WPGMA. It does not work as well as UPGMA but is a bit easier to implement (you can look up WPGMA on wikipedia).

### Find the pair to join {-}

Here you want to be able to find the pair with the smallest distance. To do that we identify the cell in the matrix with the smallest value:

*Write a function*, `find_lowest_cell`, which takes one argument:

1. A list of lists, which represents a lower triangular distance matrix as returned by `lower_trian_matrix`.

The function must return:

* A list of two integers, which represent the row and column index of the cell with the smallest value in the matrix.

Remember that the row index is always smaller than the column index. The two indexes tell you which two elements to join next.

Example usage: Assuming that `matrix` is the lower triangular matrix returned by `lower_trian_matrix` in the previous example, then

```python
find_lowest_cell(matrix)
```

Should return

```python
[1, 0]
```

### Decide on a linkage method {-}

You also need a function that computes a new distance from two original ones using the the centroid-like linkage we have decided to use.

*Write a function*, `link`, that takes two arguments:

1. A float, which represents a matrix element.
2. A float, which represents another matrix element.

The function must return:

* A float, which is the average of the two arguments

Example usage:

```python
link(0.4, 0.2)
```

Should return:

```python
0.3
```

## Perform the clustering {-}

The three functions that do the actual clustering are complicated but you should be able to follow what they do. The first one updates the table to reflect that you join a pair. The second updates the list of sequence names (labels) to reflect that you joined a pair. The last one uses the two other functions to cluster pair until there is only one cluster left.

Your task is to carefully type the code for each function and to understand what every line of code does.

### Updating labels {-}

The function `update_labels` takes three arguments:

1. A list of strings representing sequence names.
2. An integer representing the index of a sequence name.
3. An integer representing the index of another sequence name.

The function does not return anything, but it updates the list of names to reflect that you joined a pair. If your  list looks like this *before* you call the function:

```python
labels = ['A', 'B', 'C', 'D']
```

Then *after* you call the function like this `update_labels(labels, 1, 0)`, the list will look like this:

```python
['(A,B)', 'C', 'D']
```

Here is the function:

```python
def update_labels(labels, i, j):

    # turn the label at first index into a combination of both labels
    labels[j] = "({},{})".format(labels[j], labels[i])

    # Remove the (now redundant) label in the first index
    del labels[i]
```


### Updating the matrix {-}

The function `update_table` takes three arguments:

1. A list of lists, which represents a lower triangular distance matrix.
2. An integer representing the index of one of the elements to join.
3. An integer representing the index of the other element to join.

The way this function is implemented, it is assumed that the second argument is always larger than the third argument. I.e. the second argument is a row index and the third argument is a column index.

The function does not return anything, but it updates the matrix to reflect that a pair has been joined. If your  matrix looks like this *before* you call the function:

```python
m = [[], [0.1], [0.3, 0.4], [0.6, 0.8, 0.2]]
```

Then *after* you call the function like this `update_table(m, 1, 0)`, the matrix will look like this:

```python
[[], [0.35], [0.7, 0.2]]
```

Here is the function:

```python
def update_table(table, a, b):

    # For the lower index, reconstruct the entire row (ORANGE)
    for i in range(0, b):
        table[b][i] = link(table[b][i], table[a][i])

    # Link cells to update the column above the min cell (BLUE)
    for i in range(b+1, a):
        table[i][b] = link(table[i][b], table[a][i])
        
    # Link cells to update the column below the min cell (RED)
    for i in range(a+1, len(table)):
        table[i][b] = link(table[i][b], table[i][a])

    # Delete cells we no longer need (lighter colors)
    for i in range(a+1, len(table)):
        # Remove the (now redundant) first index column entry
        del table[i][a]
    # Remove the (now redundant) first index row
    del table[a] 
```

The colors refer to cell colors on the slide you I showed you at the lecture.


### Do the clustering {-}

Now onto the real task, the actual clustering. The function `cluster` takes two arguments:

1. A list of strings representing DNA sequences of equal length. 
2. A list of strings representing sequence names.

The function returns:

* A string representing the generated clustering.

Here is the function:

```python
def cluster(sequences, names):

    table = lower_trian_matrix(sequences)
    labels = names[:]

    # Until all labels have been joined...
    while len(labels) > 1:
        # Locate lowest cell in the table
        i, j = find_lowest_cell(table)

        # Join the table on the cell co-ordinates
        update_table(table, i, j)

        # Update the labels accordingly
        update_labels(labels, i, j)

    # Return the final label
    return labels[0]
```

Here is a simple example of how you can use your new clustering code:

```python
names = ['A', 'B', 'C', 'D']
sequences = ['TAAAAAAAAAAA', 
             'TTAAAAAAAAAA', 
             'AAAAAAAAAAGG', 
             'AAAAAAAAGGGG']

tree = cluster(sequences, names)
print(tree)
```

### On your own {-}

From here on you are on your own. If you find a FASTA file with aligned (ungapped) homologous sequences, you can use the function below to read it into your program and try your code out on real-world sequences. I will leave it to you to figure out how it works. 

```python
def read_fasta(filename):
    f = open(filename, 'r')
    record_list = []
    header = ""
    sequence = ""
    for line in f:
        line = line.strip() ## get rid of whitespace and newline
        if line.startswith(">"):
            if header != "": ## if it is the first header
                record_list.append([header, sequence])
                sequence = ""
            header = line[1:]
        else:
            sequence += line
    record_list.append([header, sequence])
    return record_list
```