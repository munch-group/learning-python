# Project: Pairwise global alignment

*This chapter is about global pairwise alignment and you will implement your own Needleman-Wunch algorithm.*

Your task is to find an optimal alignment of two sequences. If two such sequences are both roughly 140 bases long, there are as many different ways to align them as there are atoms in the visible universe, literally. Finding an optimal alignment among those $10^{80}$ possibilities is obviously a hard problem, but implementing the Needleman-Wunch algorithm will let you do it.

This project is meant to train your coding abilities and consolidate your understanding of the Needleman-Wunch algorithm. The better you understand the algorithm before you begin, the easier and more rewarding the project will be. So re-read the book chapter about pairwise alignment and browse through the lecture slides.

Under "Assignments" on the Blackboard course page, you will find an assignment with the same name as this chapter. There you can download the files you need for this project.

- `alignmentproject.py` is the file where you must write your code. It already contains a function I wrote for you.
- `test_alignmentproject.py` is the test program that lets you test the code you write in `alignmentproject.py`.

Put the files in a folder dedicated to this project. On most computers you can right-click on the link and choose "Save file as..." or "Download linked file".

The project is split into two parts: 

1. Filling in a dynamic programming matrix.
2. Reconstructing the optimal alignment by doing traceback through the dynamic programming matrix.

To help you along, the `alignmentproject.py` file already contains a function I wrote for you so you can print your dynamic programming (DP) matrix as you gradually fill it in. You are not expected to understand how this function works. I tried to make it as condensed as possible so it does not take up so much space in your file. 

The function is named `print_dp_matrix` and takes two arguments:

1. A string, which represents a DNA sequence of some length `m`.
2. A string, which represents a DNA sequence of some length `n`.
3. A lists of lists of integers, representing a dynamic programming matrix.

The function returns:

* None, but it *prints* a nice representation of the matrix lined with the bases of the two sequences.

## Filling in the dynamic programming matrix {-}

### Make a matrix {-}
We start out by making a list of lists (a matrix) that has the right shape but only holds `None` values. We use the `None` values as place-holders, which you can later replace with scores. You can think of it as an empty matrix that you can fill scores into, just as we did at the lectures. If you want to align two sequences like `AT` and `GAT` you want a matrix that has 3 rows and 4 columns. Note that the matrix must have one more row than the number of bases in sequence one, and one more column than the number of bases in sequence two.

*Write a function*, `empty_matrix`, that takes two arguments

1. An integer (which represents the length of sequence one + 1).
2. An integer (which represents the length of sequence two + 1).

The function must return:

* A list of lists. The number of sub-lists be must equal to the first integer argument. Each sublist must contain a number of `None` values equal to the second integer argument.

Example usage:

```python
empty_matrix(3, 4)
```

returns a list with *three* lists each of length *four*:

```python
[[None, None, None, None], [None, None, None, None], [None, None, None, None]]
```

Even though this is a list of lists we can *think of it* as a three by four matrix:

    [[None, None, None, None], 
     [None, None, None, None], 
     [None, None, None, None]]

If you want to print the matrix in a way that looks like the slides I showed you at the lecture, you can use the `print_dp_matrix` function (again `None` represents empty cells):

              G    A    T
      None None None None
    A None None None None
    T None None None None

**Important:** You can implement `empty_matrix` in a way superficially looks ok but will cause you all kinds of grief when you start filling it in. When you create the list of lists (e.g. three lists as above) you need to generate and add three *separate* lists. If you add the *same* list three times you do not have three separate  rows in your matrix. Instead you have *three* references to the *same* row. You can test if you did it right this way -- by changing the value of one cell to see what happens: 

```python
empty = empty_matrix(3, 4)
empty[0][0] = 'Mogens'
print(empty)
```

If this only changed *one* value like below, you are ok:

```python
[['Mogens', None, None, None], [None, None, None, None], [None, None, None, None]]
```

If it changed the first value in *all* the lists, it means that all your lists are the same (which is not what you want).

```python
[['Mogens', None, None, None], ['Mogens', None, None, None], ['Mogens', None, None, None]]
```






### Fill top row and left column {-}
Now that you can make a matrix with the correct dimensions, you need to write a function that fills in the top row and the left column in accordance with what the gap score is. E.g. if the gap score is `-2` you want the matrix to look something like this when you print it with `print_dp_matrix`:

              G    A    T
         0   -2   -4   -6
    A   -2 None None None
    T   -4 None None None

*Write a function*, `prepare_matrix`, which takes three arguments:

1. An integer (which represents the length of sequence one plus one)
2. An integer (which represents the length of sequence two plus one)
3. An integer, which represents the gap_score used for alignment.

The function must return:

* A list of lists. The number of sub-lists be must equal to the first integer argument. The values in the first sub-list must be multiples of the gap score given as the third argument. The first elements of remaining sub-lists must be multiples of the gap score. All remaining elements of sub-lists must be `None`.

Example usage:

```python
prepare_matrix(3, 4, -2)
```

must return:

```python
[[0, -2, -4, -6], [-2, None, None, None], [-4, None, None, None]]
```

**Hint:** You should call `empty_matrix` inside `prepare_matrix` to get a matrix filled with `None`. 

Now all you need to do is replace the right `None` values with *multiples* of the gap score. E.g. the third element in the first sub-list is `matrix[2][0]`, which you would need to assign the value: `2` times the gap score. In the same way `matrix[3][0]` should be `3` times the gap score. So you need to figure out which elements you should replace and which pairs of indexes you need to access those elements. Then use `range` to generate those indexes and for-loops to loop over them. 

### Fill the entire matrix {-}
Now that we are able to fill the top row and left column we can start thinking about how to fill the whole matrix. 

For that we need a score matrix of match scores. In Python that is most easily represented as a dictionary of dictionaries like this:

```python
match_scores = {'A': {'A': 2, 'T': 0, 'G': 0, 'C': 0},
                'T': {'A': 0, 'T': 2, 'G': 0, 'C': 0},
                'G': {'A': 0, 'T': 0, 'G': 2, 'C': 0},
                'C': {'A': 0, 'T': 0, 'G': 0, 'C': 2}}
```

That lets you get the score for matching an `A` with a `T` like this: `match_scores['A']['T']`. Note that the match scores are only for uppercase letters (`A`, `T`, `G`, `C`).

*Write a function*, `fill_matrix`, which takes four arguments:

1. A string, which represents the first sequence.
2. A string, which represents the second sequence.
3. A dictionary of dictionaries like the one shown above, which represents match scores.
4. An integer, which represents the gap score.

The function must return:

* A list of lists of integers, which represents a correctly filled dynamic programming matrix given the two sequences, the match scores, and the gap score.

Example usage: If `match_scores` is defined as above then

```python
fill_matrix('AT', 'GAT', match_scores, -2)
```

must return:

```python
[[0, -2, -4, -6], [-2, 0, 0, -2], [-4, -2, 0, 2]]
```

If you print that matrix using `print_dp_matrix` it should look like this:

	      G  A  T
	   0 -2 -4 -6
	A -2  0  0 -2
	T -4 -2  0  2

**Hint:** You should call `prepare_matrix` inside `fill_matrix` to get a matrix with the top row and left column filled. Assuming `seq1` is sequence one and `seq2` is sequence two then you can do it like this:

```python
matrix = prepare_matrix(len(seq1)+1, len(seq2)+1, gap_score)
```

Now you only need to fill out the rest. To produce the indexes of the elements in the list of lists that you need to assign values to, you need two nested for-loops.

```python
for i in range(1, len(seq1)+1):
    for j in range(1, len(seq2)+1):
        print(i, j) # just to see what i and j are

```

Examine this code and make sure you understand why we give those arguments to `range`. Each combination of `i` and `j` let you access an element `matrix[i][j]` in `matrix` (list of lists) that you can to assign a value to. The value to assign to `matrix[i][j]` (green cell on the slides) is the maximum of three values (the yellow cells on the slide):

1. The value of the cell to the left (`matrix[i][j-1]`) plus the gap score.
2. The cell above (`matrix[i-1][j]`) plus the gap score.
3. The diagonal cell (`matrix[i-1][j-1]`) plus the match score for base number `i` (index `i-1`) of sequence one and base number `j` (index `j-1`) of sequence two.

## Reconstructing the optimal alignment {-}

This is the most difficult part, so I will hold your hand here. Below is first a function that identifies which of three cells (the yellow cells on the slides) some cell (green cell on the slides) is derived from. On the slides, this is the cell pointed to by the red arrow.

```python
def get_traceback_arrow(matrix, row, col, match_score, gap_score):

    # yellow cells:
    score_diagonal = matrix[row-1][col-1]
    score_left = matrix[row][col-1]
    score_up = matrix[row-1][col]

    # gree cell:
    score_current = matrix[row][col]

    if score_current == score_diagonal + match_score:
        return 'diagonal'
    elif score_current == score_left + gap_score:
        return 'left'
    elif score_current == score_up + gap_score:
        return 'up'
```

Write (no copy paste) this into your file and make sure that it works and that you understand exactly how it works before you go on. 

Here is a function that uses `get_traceback_arrow` to do the traceback. It reconstructs the alignment starting from the last column adding columns in front as the traceback proceeds. It is big, so it breaks across three pages.

```python
def trace_back(seq1, seq2, matrix, score_matrix, gap_score):

    # Strings to store the growing alignment strings:
    aligned1 = ''
    aligned2 = ''
# continues...
```

```python
    # The row and col index of the bottom right cell:
    row = len(seq1)
    col = len(seq2)

    # Keep stepping backwards through the matrix untill
    # we get to the top row or the left col:
    while row > 0 and col > 0:

        # The two bases we available to match:
        base1 = seq1[row-1]
        base2 = seq2[col-1]

        # The score for mathing those two bases:
        match_score = score_matrix[base1][base2]

        # Find out which cell the score in the current cell was derived from:
        traceback_arrow = get_traceback_arrow(matrix, row, col, match_score, gap_score)

        if traceback_arrow == 'diagonal':
                # last column of the sub alignment is base1 over base2:
            aligned1 = base1 + aligned1
            aligned2 = base2 + aligned2
            # next cell is the diagonal cell:
            row -= 1
            col -= 1
        elif traceback_arrow == 'up':
                # last column in the sub alignment is base1 over a gap:
            aligned1 = base1 + aligned1
            aligned2 = '-' + aligned2
            # next cell is the cell above:
            row -= 1
        elif traceback_arrow == 'left':
                # last column in the sub alignment is a gap over base2:
            aligned1 = '-' + aligned1
            aligned2 = base2 + aligned2
            # next cell is the cell to the left:
            col -= 1
# continues...
```

```python
    # If row is not zero, step along the top row to the top left cell:
    while row > 0:
        base1 = seq1[row-1]
        aligned1 = base1 + aligned1
        aligned2 = '-' + aligned2
        row -= 1

    # If col is not zero, step upwards in the left col to the top left cell:
    while col > 0:
        base2 = seq2[col-1]
        aligned1 = '-' + aligned1
        aligned2 = base2 + aligned2
        col -= 1

    return [aligned1, aligned2]
```

Once you have *written* it into your file, make sure you understand the correspondence to the sequences of events on the lecture slides. 

Now you can write a function you can call to do perform the alignment. You get to do that yourself. It just calls `fill_matrix` and then `trace_back` to get the optimal alignment

*Write a function*, `align`, that takes four arguments:

1. A string, which represents sequence one.
2. A string, which represents sequence two.
3. A dictionary of dictionaries, which represents the match scores (as described above).
4. An integer, which represents the gap score.

The function must return:

* A list of length two. The first element of that list must be a string, representing the aligned sequence one. The second element must be a string, representing the aligned sequence two.

Example usage:

```python
align('ATAT', 'GATGAT', score_matrix, -2)
```

must return:

```python
['-AT-AT', 'GATGAT']
```

Once you have written that function you can print your alignment like this:

```python
alignment = align('ATAT', 'GATGAT', score_matrix, -2)
for s in alignment:
    print(s)
```