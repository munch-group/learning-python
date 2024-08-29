# Project: Codon usage in *Streptococcus* bacteria

Codon usage bias refers to differences in the frequency of occurrence of synonymous codons in coding DNA. There are 64 different codons (61 codons encoding for amino acids plus 3 stop codons) but only 20 different translated amino acids. The overabundance in the number of codons allows many amino acids to be encoded by more than one codon. Because of such redundancy, it is said that the genetic code is degenerate. Different organisms often show particular preferences for one of the several codons that encode the same amino acid, that is, a greater frequency of one will be found than expected by chance. How such preferences arise is a much-debated area of molecular evolution.

Given an open reading frame (ORF), you must compute the codon usage. Your goal is to create a data structure where you can look up an amino acid and the frequencies of codons in that encode that amino acid the ORF. Here is a made-up example:

```python
{'A': {'GCA': 0.0, 'GCC': 0.0, 'GCT': 1.0, 'GCG': 0.0}, 
 'C': {'TGC': 0.0, 'TGT': 1.0}, 
 'E': {'GAG': 0.2, 'GAA': 0.8}, 
 'D': {'GAT': 1.0, 'GAC': 0.0}, 
 'G': {'GGT': 0.3, 'GGG': 0.0, 'GGA': 0.7, 'GGC': 0.0}, 
 'F': {'TTC': 0.0, 'TTT': 1.0}, 
 'I': {'ATT': 1.0, 'ATC': 0.0, 'ATA': 0.0}, 
 'H': {'CAC': 0.0, 'CAT': 1.0}, 
 'K': {'AAG': 0.2, 'AAA': 0.8}, 
 '*': {'TAG': 0.0, 'TGA': 1.0, 'TAA': 0.0}, 'M': {'ATG': 1.0}, 
 'L': {'CTT': 0.0, 'CTG': 0.6, 'CTA': 0.0, 'CTC':0.0, 'TTA': 0.4, 'TTG': 0.0}, 
 'N': {'AAT': 0.5, 'AAC': 0.5}, 
 'Q': {'CAA': 0.6, 'CAG': 0.4}, 
 'P': {'CCT': 0.5, 'CCG': 0.0, 'CCA': 0.5, 'CCC': 0.0}, 
 'S': {'TCT': 0.0, 'AGC': 0.0, 'TCG': 0.0, 'AGT': 0.5, 'TCC': 0.0, 'TCA': 0.5}, 
 'R': {'CGA': 0.5, 'CGC': 0.0, 'AGA': 0.5, 'AGG': 0.0, 'CGG': 0.0, 'CGT': 0.0}, 
 'T': {'ACC': 0.0, 'ACA': 0.0, 'ACG': 0.0, 'ACT': 1.0}, 
 'W': {'TGG': 1.0}, 
 'V': {'GTA': 0.6, 'GTC': 0.0, 'GTT': 0.2, 'GTG': 0.2}, 
 'Y': {'TAT': 1.0, 'TAC': 0.0}}
```

That data structure is a dictionary with keys corresponding to amino acids (i.e. single letter strings designating an amino acid such as `'R'` for arginine). The value associated with *each* amino acid key is also a dictionary, and the keys of *this* dictionary should be the different codons that encode the amino acid. The value associated with each codon key should be a number, representing the frequency with which that codon is used to encode that amino acid. The final data structure should only include amino acids that are found in the ORF.

On the course page you can download the files you need for this project:

- `sample_orfs.txt` contains open reading frame sequences you can work on.

You also need to download the two project files:

- `codonbiasproject.py` is an empty file where you must write your code.
- `test_codonbiasproject.py` is the test program that lets you test the code you write in `codonbiasproject.py`.

Put the files in a folder dedicated to this project. On most computers you can right-click on the link and choose "Save file as..." or "Download linked file".

Now open each file in *VScode* and have a look at what is in `sample_orfs.txt`. (Do *not* change it in any way and do not save it after viewing. If VScode asks you if you want to save it before closing, say *no*.) How many sequences are there in each file?

As in the translation project, you will need a data structure that pairs each codon to the amino acid it encodes. This is an obvious use of a dictionary and at the top of `codonbiasproject.py` I have defined such a dictionary you can use. Defining it outside the functions means that it is visible inside all your functions (unless you define *another* variable called `codon_map` inside a function). Defining variables globally like this sometimes make sense if some value can be considered a *constant* in your program and is *never* changed.

> It is normally very bad programming style to access variables outside functions in this way because it may have all kinds of unexpected side effects across function calls. So make it a rule for yourself that code *inside* a function should never to access variables *outside* the function. The reason we define `codon_map` globally in this project is to help you understand that when Python cannot find a variable inside a function, it looks outside the function to find it. In this project, functions will find `codon_map` in this way. However, as I already said, you should *never* do this yourself. The chance that you make an unexpected mistake is overwhelming. 

The project is split into four parts: 

1. Read an open reading frame (ORF) into your script and count the codons.
2. Group the codon counts by the amino acids the codons encode.
3. Convert counts to frequencies.
4. Build the data structure representing the codon bias information.

## Read an open reading frame and count its codons {-}

### Read ORFs from a file {-}

You can use this code to read the ORFs into your script:

```python
f = open('sample_orfs.txt', 'r')
orf_list = list()
for line in f:
    seq = line.strip()
    orf_list.append(seq)
f.close()
```

Try to print the list to see it. Then pick out the first ORF in the list so you can use that to test your code:

```python
test_orf = orf_list[0]
```

### Split the ORF into codons {-}

You need a function that splits the ORF into codons. This one you have already implemented in the exercise about translating DNA -- and if, not here it is in my version to get you started.

```python
def split_codons(orf):
    codon_list = []
    for i in range(0, len(orf)-2, 3):
        codon_list.append(orf[i:i+3])
    return codon_list
```

Before you go on, make sure you understand/remember how this function works and what it returns.

### Count codons in an ORF {-}
Now you need to count the number of times each codon occurs in the ORF.

*Write a function*, `count_codons`, that take one argument:

1. A string, which represents the open reading frame.

The function must return:

* A dictionary where keys are strings representing codons and associated values are integers representing the number of times each codon occurs in the ORF given as argument.

Example usage:

```python
count_codons("ATGTCATCATGA")
```

should return:

```python
{'CTT': 0, 'ATG': 1, 'ACA': 0, 'ACG': 0, 'ATC': 0, 'AAC': 0, 
 'ATA': 0, 'AGG': 0, 'CCT': 0, 'ACT': 0, 'AGC': 0, 'AAG': 0, 
 'AGA': 0, 'CAT': 0, 'AAT': 0, 'ATT': 0, 'CTG': 0, 'CTA': 0, 
 'CTC': 0, 'CAC': 0, 'AAA': 0, 'CCG': 0, 'AGT': 0, 'CCA': 0, 
 'CAA': 0, 'CCC': 0, 'TAT': 0, 'GGT': 0, 'TGT': 0, 'CGA': 0, 
 'CAG': 0, 'TCT': 0, 'GAT': 0, 'CGG': 0, 'TTT': 0, 'TGC': 0, 
 'GGG': 0, 'TAG': 0, 'GGA': 0, 'TGG': 0, 'GGC': 0, 'TAC': 0, 
 'TTC': 0, 'TCG': 0, 'TTA': 0, 'TTG': 0, 'TCC': 0, 'ACC': 0, 
 'TAA': 0, 'GCA': 0, 'GTA': 0, 'GCC': 0, 'GTC': 0, 'GCG': 0, 
 'GTG': 0, 'GAG': 0, 'GTT': 0, 'GCT': 0, 'TGA': 1, 'GAC': 0, 
 'CGT': 0, 'GAA': 0, 'TCA': 2, 'CGC': 0}
```

   -- though not necessarily with key-value pairs in that order.

In the function, you should use the `split_codons` function to split the ORF into a list of codons. Then create an empty dictionary that you can populate with counts. You want *all* the possible codons to be in your dictionary. That way, the codons you do *not* find in your ORF will have a count of `0`. In this case, such absence is also valuable information. To achieve this you must start by filling the dictionary with a key for each codon and give each a count of `0`. You can do that by iterating over the keys in the dictionary that maps codons to amino acids. Then you must iterate over all the codons in the list of codons produced by the `split_codons` function and add counts to the dictionary as you go.

## Group codon counts by amino acid {-}

Having counted how many times each codon appears in the ORF, you need to group the counted codons by the amino acid they encode. 

*Write a function*, `group_counts_by_amino_acid`, which takes one argument:

1. A dictionary, as that returned by `count_codons`.

The function must return:

* A dictionary of dictionaries, which pairs each amino acid with a dictionary with counts of how many times each codon is used to encode that amino acid in the ORF. 

Example usage: Assuming `counts` is the dictionary returned by `count_codons` as in the previous example.

```python
grouped_counts = group_counts_by_amino_acid(counts)
```

then `group_counts_by_amino_acid` should return:

```python
{'A': {'GCA': 0, 'GCC': 0, 'GCT': 0, 'GCG': 0}, 
 'C': {'TGC': 0, 'TGT': 0}, 
 'E': {'GAG': 0, 'GAA': 0}, 
 'D': {'GAT': 0, 'GAC': 0}, 
 'G': {'GGT': 0, 'GGG': 0, 'GGA': 0, 'GGC': 0}, 
 'F': {'TTC': 0, 'TTT': 0}, 
 'I': {'ATT': 0, 'ATC': 0, 'ATA': 0}, 
 'H': {'CAC': 0, 'CAT': 0}, 
 'K': {'AAG': 0, 'AAA': 0}, 
 '*': {'TAG': 0, 'TGA': 1, 'TAA': 0}, 
 'M': {'ATG': 1}, 
 'L': {'CTT': 0, 'CTG': 0, 'CTA': 0, 'CTC': 0, 'TTA': 0, 'TTG': 0}, 
 'N': {'AAT': 0, 'AAC': 0}, 
 'Q': {'CAA': 0, 'CAG': 0},
 'P': {'CCT': 0, 'CCG': 0, 'CCA': 0, 'CCC': 0}, 
 'S': {'TCT': 0, 'AGC': 0, 'TCG': 0, 'AGT': 0, 'TCC': 0, 'TCA': 2}, 
 'R': {'AGG': 0, 'CGC': 0, 'CGG': 0, 'CGA': 0, 'AGA': 0, 'CGT': 0}, 
 'T': {'ACC': 0, 'ACA': 0, 'ACG': 0, 'ACT': 0}, 
 'W': {'TGG': 0}, 
 'V': {'GTA': 0, 'GTC': 0, 'GTT': 0, 'GTG': 0}, 
 'Y': {'TAT': 0, 'TAC': 0}}
```

   -- though not necessarily with key-value pairs in that order.

So if we pretend the resulting dictionary of dictionaries is called `d`, then `d['S']` will be a dictionary where keys are codons encoding the 'S' amino acid and the values are the counts of those codons. That means that you can access a particular count like this:

```python
d['S']['TCA'] 
```

In the above example, this count is `2`. So the task is really just to distribute counts given as the first argument into groups for each amino acid. Depending on what you call your variables it could look something like this:

```python
grouped_counts[acid][codon] = codon_counts[codon]
```

Your function should begin by defining an empty dictionary to add to. Then use a for-loop to run through all codon/amino-acid pairs and populate your dictionary of dictionaries.

## Turn counts into frequencies {-}

Now you know how many times each codon represents a certain amino acid, but we would like to know with which *frequency* a certain codon represents an amino acid. So you need to normalize the counts so they become frequencies. You do that by dividing each codon count by the total number of codons encoding the same amino acid. We split the solution to this problem in two. We first write a helper function that turns codon counts for *one* amino acid into frequencies.

*Write a function*, `normalize_counts`, which takes one argument:

1. A dictionary, where keys are strings representing codons and values are integers representing the counts of these codons.

The function must return:

* A dictionary, where keys are strings representing codons and values are floats representing the frequency at which each codon appear. That is, the count of that codon divided by the total of all codon counts in the dictionary. The frequencies for codons that encode the same amino acid must of sum to one. That means that in cases where the total count is zero, the function must return `None`.

Example usage:

```python
normalize_counts({'ATT': 8, 'ATC': 10, 'ATA': 2})
```

should return:

```python
{'ATC': 0.5, 'ATA': 0.1, 'ATT': 0.4}
```

   -- though not necessarily with key-value pairs in that order.

Now you have solved part of the task, what remains is to now use that function to normalise the codon counts of *each* amino acid in your grouped counts:

*Write a function*, `normalize_grouped_counts`, which takes one argument:

1. A dictionary of dictionaries, as that returned by `group_counts_by_amino_acid`.

The function must return:

* A new dictionary of dictionaries where the values of the inner dictionaries are frequencies instead of counts as in the example in the introduction. You should not include amino acids for which there are no counted codons.

Example usage: Assuming `gr_counts` is the dictionary of dictionaries returned by `grouped_group_counts_by_amino_acid` in the example above.

```python
normalize_grouped_counts(gr_counts)
```

should return:

```python
{'*': {'TAA': 0.0, 'TGA': 1.0, 'TAG': 0.0}, 
'M': {'ATG': 1.0}, 
'S': {'AGC': 0.0, 'TCG': 0.0, 'TCC': 0.0, 'TCT': 0.0, 'AGT': 0.0, 'TCA': 1.0}}
```

   -- though not necessarily with key-value pairs in that order.

Here is some help to get you started:

```python
def normalize_grouped_counts(grouped_counts):
    grouped_freqs = {}
    for aa in grouped_counts:
        counts = grouped_counts[aa]

```

Amino acids with no codon counts should *not* be part of the data structure. Remember that in this case `normalize_counts` returns `None`, so you can simply test if the return value from `normalize_counts` is `None`

## Compute the codon usage {-}

Now all that remains is to tie together the functions you have written in a final function that generates your big data structure from an ORF:

Write a function, `codon_usage`, which takes one argument:

1. A string, which is an ORF.

The function must return:

* A dictionary of dictionaries, same as that returned by `normalize_grouped_counts`.

 
 