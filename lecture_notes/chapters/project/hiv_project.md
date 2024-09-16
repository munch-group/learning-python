# Identifying the subtype of an HIV sequence

*This chapter is a programming project where you will put your new programming skills to use analyzing an HIV DNA sequences.*

You have now been introduced to all the programming rules you will see in this course. You now know all the building blocks required to write *any* program -- literally *any*. The reason why computer geeks are good at what they do is not that they know some incomprehensible secrets. It is because they practiced, a lot. With practice, the simple rules you know now will let you write anything from first-person shooter games over jumbo jet autopilots to scripts for simple problems in bioinformatics. In the last three chapters, we will train your ability to solve bioinformatics problems by putting together all the things you have learned. 

The programming project in this chapter deals with DNA sequences from HIV viruses. There are two types of HIV: HIV-1, which is by far the most common, and HIV-2, which is mostly found in West Africa. HIV-1 vira are divided into groups M, N, O, and P. The most important group M (for major) is one primarily responsible for the global epidemic. Group M is further divided into subtypes A, B, C, D, F, G, J, K, and CRFs. In this project we will look at sequences from the subtypes A, B, C, and D. You have multiple database sequences for each of these four subtypes and you have one *unknown* sequence from a patient that you need to assign to either subtype A, B, C or D. To do this you will have to write a program that *predicts* the subtype of the unknown sequence. How cool is that?

On the course page you can download the files you need for this project:

- `unknown_type.txt` contains an HIV sequence of unknown subtype
- `subtypeA.txt` contains a database of HIV sequences of subtype A
- `subtypeB.txt` contains a database of HIV sequences of subtype B
- `subtypeC.txt` contains a database of HIV sequences of subtype C
- `subtypeD.txt` contains a database of HIV sequences of subtype D

You also need to download the two project files:

- `hivproject.py` is an empty file where you must write your code.
- `test_hivproject.py` is the test program that lets you test the code you write in `hivproject.py`.

Put the files in a folder dedicated to this project. On most computers you can right-click on the link and choose "Save file as..." or "Download linked file".

Now open each file in *VScode* and have a look at what is in the data files. (Do *not* change them in any way and do not save them after viewing. If VScode asks you if you want to save it before closing, say *no*.) How many sequences are there in each file?

The project is divided into the following parts:

- Compute the similarity of two sequences
- Read the HIV sequences into your program.
- Assess the similarity of your unknown HIV sequence to each of the HIV sequences with known subtype.
- Find the maximum similarity of your unknown sequence to sequences from each subtype.
- Identify the HIV subtype of your sequence as the subtype of that sequence that your sequence is most similar to.

Make sure you read the entire exercise and understand what you are supposed to do before you begin!

## Compute the similarity of two sequences {-}

We need to compare our unknown HIV sequence to all the HIV sequences of known subtypes. That way we can identify the sequence of a known subtype that is most similar to your unknown sequence. We will then assume that our unknown sequence has the same subtype as this sequence. To accomplish this we first need to write some code that compares two sequences so we can compare our HIV sequence to each of the other HIV sequences. 

### Compare two sequences {-}

*Write a function* `sequence_similarity` that takes two arguments:

1. A string which is a DNA sequence.
2. A string of the same length as argument one, which is also a DNA sequence.

The function must return:

* A float, which is the proportion of bases that are the same in two DNA sequences.

Example usage:

```python
sequence_similarity('AGTC' 'AGTT')
```

should return `0.75`.

Start out defining your function like this:

```python
def sequence_similarity(seq1, seq2):
    # your code here...
```

Remember that `range(len(seq1))` generates the numbers you can use to index the string `seq1`. You can use those numbers as indexes to look up positions in both strings. You will need a for-loop in your function and a variable that keeps track of how many similarities you have seen as you iterate through the sequences. 

### Compare aligned sequences {-}

All sequences, including the unknown sequence, are from the same multiple alignment. This ensures that sequence positions match up across all sequences but also means that a lot of gap characters (`'-'`) are inserted. To compute similarities between such sequences you need to make function much like `seqeuence_similarity` that does not consider sequence positions where both bases are a gap (`'-'`) characters. In other words, you must not only count the number of characters that are the same, you also need to count how many alignment columns that are `"-"` for both sequences. E.g. the following mini alignment has five such columns and four columns where the bases are the same. So in the following alignment, the similarity is 0.8 (4/5):

    A-CT-A
    A-CTTA

*Write a function* `alignment_similarity` that takes two arguments:

1. A string which is a DNA sequence with gap characters.
2. A string of the same length as argument one, which is also a DNA sequence with gap characters.

The function must return:

* A float, which is the proportion of bases that are the same in two DNA sequences.

```python
alignment_similarity('A-CT-A', 'A-CTTA')
```

should return `0.8`.

**Hint:** Use an if-statement to test if the two characters at some index are equal to `'-'` in both sequences. You can use an expression like this:

```python
seq1[i] == '-' and seq2[i] == '-'
```

Once your function has computed both the number of identical bases and the number of alignment columns that are not both `'-'`, you can have it return the similarity as the ratio of the two.

## Read the HIV sequences into your program {-}

To use your `alignment_similarity` function to assess similarity between your unknown sequence and the sequences of known subtype, you need to read the sequences into your program. Here is a function that will read the sequences from one of the files you downloaded into a list:

```python
def read_data(file_name):
    f = open(file_name)
    sequence_list = list()
    for line in f:
        seq = line.strip()
        sequence_list.append(seq)
    f.close()
    return sequence_list
```

You can use that function to read the unknown sequence into your program:

```python
unknown_list = read_data('unknown_type.txt')
```

In this case, the list only contains the one unknown HIV sequence in unknown_type.txt.

You also need to load the typed HIV sequences into your program. Here is a function that returns a dictionary in which the keys are subtypes (`'A'`, `'B'`, `'C'` and `'D'`) and each value is a lists of sequences with that subtype:

```python
def load_typed_sequences():
    return {'A': read_data('subtypeA.txt'),
            'B': read_data('subtypeB.txt'),
            'C': read_data('subtypeC.txt'),
            'D': read_data('subtypeD.txt') }
```

If you use the function like this:

```python
typed_data = load_typed_sequences()
```

then you can access the list of sequences of subtype A like this: `typed_data['A']`.

## Compare your HIV sequence to HIV sequences of known subtype {-}

To type you HIV sequence you must compare your sequence to all the database sequences to see which group has the best matching sequence.

*Write a function* `get_similarities` that takes two arguments:

1. A string, which is your unknown HIV sequence.
2. A list of strings, each of which is an HIV sequence of known type.

The function must return:

* A list of floats, which should be the similarities between the unknown sequence given as the first argument and the list of sequences given as the second argument.

Example usage:

```python
get_similarities(unknown_list[0], typed_data['A'])
```

should return:

```python
[0.8553288474061211, 0.8721742704480066,
 0.854924397221087, 0.8481709291032696,
 0.8498330281159108] 
```

The function should use the function `alignment_similarity` to compare your unknown sequence (`unknown_list[0]`) to each of the sequences of some subtype. Start out like this:

```python
def get_similarities(unknown, typed_sequences):
    # Your code here...
    
```

In your function you need to define a list that you can *append* the similarities you compute to:

```python
similarities = []
```

This is the list of results that your function must return. To compute the similarity between you unknown sequence and each of the sequences of known subtype, you can use your `alignment_similarity` function inside a for-loop.

## Compute maximum similarity to each subtype {-}

To predict the subtype of the unknown HIV sequence you need to compare the unknown sequence to all the sequences of each of the different subtypes. The subtype of the sequence with the highest similarity to your unknown sequence is then our predicted subtype (or our best guess). 

*Write a function* `get_max_similarities` that takes two arguments:

1. A string, which is your unknown HIV sequence.
2. A dictionary, like the one returned by `load_typed_sequences`.

The function must return:

* A dictionary, in which keys are strings representing each subtype (`'A'`, `'B'`, `'C'`, and `'D'`) and values are floats representing the maximum similarity between the unknown sequence and the sequences of a subtype. The dictionary *could* look like this (it does not, you need to compute the similarities yourself.):

```python
{'A': 0.89, 'B': 0.95, 'C': 0.82, 'D': 0.99}
```

To get the highest number in a list of numbers, you can use the `max` function in Python. It works like this:

```python
numbers = [3, 8, 53, 12, 7]
print(max(numbers))  # prints 53
```

For example, to get the highest similarity between the unknown sequence and sequences in `typed_data['A']`:

```python
subtypeA_similarities = get_similarities(unknown_list[0], typed_data['A'])
subtypeA_max = max(subtypeA_similarities)
```

<!-- TODO: Have them also compute mean similarity to each group -->


## Identify the HIV subtype {-}

Now for the grand finale! You ultimately want to be able to write code like this:

```python
unknown_list = read_data('unknown_type.txt')
typed_data = load_typed_sequences()
subtype = predict_subtype(unknown_list[0], typed_data)
print("Patient HIV is subtype {}".format(subtype))
```

So all you need now is the `predict_subtype` function.

*Write a function* `predict_subtype` that takes two arguments:

1. A string, which is your unknown HIV sequence.
2. A dictionary, like the one returned by `load_typed_sequences`.

The function must return:

* A string of length one (either `'A'`, `'B'`, `'C'`, or `'D'`) representing the predicted subtype of your unknown HIV sequence.

The function should use `get_max_similarities` to compute the dictionary of max similarities and then extract from that dictionary the key with the highest value (similarity). So the function must return `'A'` if the unknown sequence is most similar to a sequence of subtype A, `'B'` if the unknown sequence is most similar to a sequence of subtype B and so on.


