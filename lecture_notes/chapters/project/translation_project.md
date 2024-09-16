# Translating open reading frames

*This chapter is about translating DNA into protein. If bacteria can do it, so can you.*

In this project you will write the code needed to translate an open reading frame (ORF) on a DNA sequence into into the corresponding sequence of amino acids.

You need two project files for the project, which you can download from the course page:

- **translationproject.py** is an empty file where you must write your code.
- **test_translationproject.py** is the test program that lets you test the code you write in translationproject.py.

The file `translationproject.py` is for your code. The file `test_translationproject.py` is the script you use to test the functions you write for this project (see @sec:testing_your_code).

In this project you will need a data structure that pairs each codon to the amino acid it encodes. This is an obvious use of a dictionary and at the top of `translationproject.py` I have defined such a dictionary you can use. Defining it outside the functions means that it is visible inside all your functions (unless you define *another* variable called `codon_map` inside a function). Defining variables globally to your program sometimes make sense if some value can be considered a *constant* in your program and is *never* changed.

> It is normally very bad programming style to access variables outside functions in this way because it may have all kinds of unexpected side effects across function calls. So make it a rule for yourself that code *inside* a function should never to access variables *outside* the function. The reason we define `codon_map` globally in this project is to help you understand that when Python cannot find a variable inside a function, it looks outside the function to find it. In this project functions will find `codon_map` in this way. However, as I already said, you should *never* do this yourself. The chance that you make an unexpected mistake is overwhelming. 

## Translating a single codon  {.unnumbered}

Write a function, `translate_codon` that takes one argument:

1. A string, which is a codon.

The function should return:

* A string of length one (one character). If the string argument is a valid codon then this letter should the be an amino acid letter specified by the `codon_map` dictionary. Note that stop codons are represented by a star (`'*'`). If the string argument is *not* a valid codon, the function must return `'?'`.

Example usage:

```python
translate_codon('ACG')
```

should return

```python
'T'
```

Before you start coding you should always outline for yourself intuitively what you need to do to complete the task at hand. In this case want to translate, or map, between a three letter string, codon, and the corresponding one letter string for the amino acid that the codon corresponds to. Notice that the keys in the `codon_map` dictionary are in upper case, so you must make sure that the keys *you* use are also in upper case. You can translate codon into an upper case version of itself using the upper() method.

Try this out first:

```python
codon = 'TTG'
amino_acid = codon_map[codon]
print(amino_acid)
```

Now write the function so it uses the string parameter as a key to look up the corresponding amino acid letter and returns this letter. Before you go on, make a function that does only that.

Before you are completely done you need to make your function handle the situation when the argument to the function is not a key in the `codon_map` dictionary. Use an if-else construct to handle the two cases. The boolean expression must test if the function argument is a key in `codon_map`. Remember that you can use the `in` operator to do this.

## Splitting an open reading frame into codons  {.unnumbered}

To translate an entire open reading frame into the corresponding amino acid sequence, you need to split the ORF sequence into codons. When we have done that we can translate each codon using the function `translate_codon` you just wrote.

*Write a function*, `split_codons`, that takes one argument:

1. A string, which is an ORF sequence

The function must return:

* A list of strings. Each string must have length 3 and must represent the-non overlapping triplets in the same sequence as they appear in the string given as argument.

Example usage:

```python
split_codons('ATGTATGCCTGA')
```

should return

```python
['ATG', 'TAT', 'GCC', 'TGA']
```

Divide the problem into simpler tasks like above. You need to loop over the sequence to perform operations on it. Start by writing a function that prints each character:

```python
def split_codons(orf):
    for i in range(len(orf)):
        print(orf[i])
```

Now try to figure out how you can modify the function to make it move over the sequence in jumps of three. Look at the [documentation](https://docs.python.org/3/library/stdtypes.html#range) for the `range` function to see how you can make it iterate over numbers with increments of three like this: 0, 3, 6, 9, 12, ... . Modify your function so that it now prints every third character.

What you want is obviously not every third character. You want three characters. I.e. every third character *and* the two characters that come right after. You can use the index in the for loop to get the corresponding codon using slicing. Modify your function so that it prints each codon.

Now all that remains is to put each codon on a list that you can return from the function. You can define a list before your for-loop so you have a list to add codons to.

## Translating an open reading frame  {.unnumbered}

Now you can use the two functions `split_codons` and `translate_codon` to write a function that translates an ORF into a protein sequence.

*Write a function*, `translate_orf`, that takes one argument:

1. A string, which is a DNA sequence.

The function must return

* A string, which is the protein sequence translated from the ORF sequence argument.

Example usage:

```python
translate_orf('ATGGAGCTTANCAAATAG')
```

should return

```python
'MEL?K*'
```

