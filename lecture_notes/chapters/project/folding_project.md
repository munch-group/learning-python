

# Project: Primer analysis

Say you have a short sequence that you want to use as a PCR primer. To evaluate if it a suitable primer, you need to know the melting temperature of the sequence. You also need to make sure that it will not fold up on itself so that it cannot bind to the DNA sequence you want to amplify.

On the course page you can download the files you need for this project:

- `foldingproject.py` is an empty file where you must write your code.
- `test_foldingproject.py` is the test program that lets you test the code you write in translationproject.py.

Put the files in a folder dedicated to this project. On most computers you can right-click on the link and choose "Save file as..." or "Download linked file".

## Count the number of bases in your candidate primer {-}

Before you can compute the melting temperature, you need to determine how many times each base occurs in the sequence. You can assume that the only characters in the string are A, T, G, and C.

*Write a function*, `count_bases`, which takes one argument:

1. A string, which is a DNA sequence.

The function must return:

* A dictionary, which in which keys are strings that represent bases and values are integers that represent the number of occurrences of each base. If a base is not found in the sequence, its count must be zero.

Example usage: If the function is called like this:

```python
count_bases("ATGG")
```

then it should return (not necessarily with key-value pairs in the same order):

```python
{"A": 1, "C": 0, "G": 2, "T": 1}
```

## Compute the melting temperature {-}

Knowing the base composition in your sequence, you can now calculate the melting temperature the double-stranded DNA that forms when your primer pairs up with the sequence to amplify. If the primer has less than 14 bases the formula for calculating melting temperature is:

$$ Temp = (A + T) * 2 + (G + C) * 4 $$ 

and if the primer has 14 bases or more it is calculated like this:

$$ Temp = 64.9 + 41 * (G + C - 16.4) / (A + T + G + C) $$ 

 The A, T, C, and G in the formulas represent the numbers of A, T, C and G in the DNA primer.

You must write a function that applies these two formulas appropriately by taking the length of the primer into account.

*Write a function*, `melting_temp`, which takes one argument:

1. A string, which is a DNA sequence (your primer).

The function must return:

* A number, which represents the melting temperature of the double-stranded DNA corresponding to the DNA string given as argument.

Example usage: If the function is called like this:

```python
melting_temp("ATG")
```

then it should return:

```python
8
```


## Reverse complement the sequence {-}

It is possible that one part of the primer forms base pairs with another part of the primer to form a hairpin structure. To figure out if this can happen to your primer, you need to be able to find the reverse complement of DNA sequence. The reverse complement of a DNA sequence is one where the sequence of bases is first reversed, and then each base is replaced with its Watson-Crick complementary base.

*Write a function*, `reverse_complement`, which takes one argument:

1. A string, which is a DNA sequence.

The function must return:

* A string, which represents the reverse complement of the DNA string given as argument.

Example usage: If the function is called like this:

```python
reverse_complement("AATTC")
```

then it should return:

```python
"GAATT"
```

<!-- TODO: Add function to test if the primer can form a dimer (interacting with another sequence) -->


## Check for hairpins {-}

You would like to be able to determine if your primer can fold to form a hairpin with some specified minimum number of consequtive base pairs. We assume that hairpin loops are always at least four bases long and that base pairs in the hairpin can only be Watson-Crick basepairs. Here is an example of a hairpin with five basepairs and a loop of four bases (four Cs):

```
        C C
      C     C
       A - T
       T - A
       A - T
       T - A
       A - T
```

To test if a sequence can form a hairpin with at least four consequtive base pairs, you need to test if the sequence contains any subsequence of length four whose reverse complement is identical to another nonoverlapping subsequence. To take into account that the hairpin loop is at least four bases long, any such two subsequences must be separated by at least four bases.

*Write a function*, `has_hairpin`, which takes two arguments:

1. A string, which is a DNA sequence.
2. An integer, which represents the minimum number of consequtive base pairs in the hairpins to search for.

The function must return:

* `True` if the sequence contains a hairpin of at least the specified length and `False` otherwise.

Example usage: If the function is called like this:

```python
print(has_hairpin("ATATACCCCTATAT", 4))
```

then it should return:

```python
True
```

This is a hard one, so I will give you a bit of help. Here is the function with some parts missing. 

```python
def has_hairpin(s, k):
	looplen = 4
	for i in range(len(s)-k+1):
		subs = # Hint A
		right = # Hint B
		revcl = reverse_complement(subs)
		if revcl in right[looplen:]:
			return True
	return False
```


Hint A: Here you need to extract a substring of length k starting at i. Hint B: Here you need to extract all the sequence to the right of `substr`.
