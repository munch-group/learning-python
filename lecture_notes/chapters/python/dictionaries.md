# Pairs of things {.unnumbered}

<!-- \includegraphics[height=\fontcharht\font`\B]{picture.png} -->

*This chapter is about dictionaries that, like lists, is another Python value that can contain other Python values. Dictionaries dictionaries lets you build relationships between values, which is what data structures represent.*

## Dictionaries  {.unnumbered}

Lists are useful for storing values when the order of the values is important but lists have one drawback: you can only access a value in a list using the index of the value.

A dictionary, called `dict` in Python, is a much more flexible data type. Like a list, a dictionary is a container for other values, but dictionaries do not store values in sequence. They work more like a database that lets you store individual *values*. When you store a value you assign it to a *key* that you can then use to access the stored value. Now create your first dictionary:

```python
person = {'name': 'Robert Redford', 'height': 179, 'job': 'Actor'}
```

This dictionary has three values (`'Actor'`, `'Robert Redford'` and `179`) and each value is associated with a key. Here `'height'` is the key for the value `179`. So when defining a dictionary you should note the following:

1. You make a dictionary using braces.
2. Between you braces you put key-value pairs separated by a colon.
3. The key-value pairs are separated by commas.
4. To make an empty dictionary you just write the braces with nothing between them: `{}`.

To access a value in the dictionary you its key in square brackets after the dictionary:

```python
"{} is a {} cm {}".format(person['name'], person['height'], person['job'])
```

Here we used strings as keys, but you can also use many types of values as keys (Python will give you an error if you try to use a type that is not allowed):

```python
misc_dict = {42: "Meaning of life", "pi": 3.14159, True: 7}
```

A dictionary stores key-value pairs but do not keep track of their order. So when you print a dictionary the order of the key-values pairs is arbitrary.

If you have a dictionary you can add key-value pairs in this way:

```python
person['job'] = 'Retired'
person['hair'] = 'uniquely combed'
print(person)
```

Notice that if you assign a value (`71`) to a key that is already in the dictionary (`'age'`), then the old value (`70`) is replaced.

#### Exercise
What does this expression evaluate to?

```python
{'name': 'Robert Redford', 'height': 179, 'job': 'Actor'}['name']
```

#### Exercise
Assuming the definition of the `person` dictionary above, what does this expression evaluate to? Compare to the expression in the previous exercise.

```python
person['name']
```

#### Exercise
The *in* operator also works with dictionaries. Look at what these expressions reduce to and then try to figure out what *in* does when applied to a dictionary:

```python
'name' in person
'height' in person
'job' in person
84 in person
'Actor' in person
'Robert Redford' in person
```

#### Exercise
Write and run this code with different values of `key` and read any error messages.

```python
key = 3
# key = 'banana'
# key = 3.14159
# key = True
# key = {}
# key = []
d = {}
d[key] = 7
```

Are any of the values not allowed as keys?

#### Exercise
Do you think this will work?

```python
person = {'name': 'Robert Redford', 
                'height': 179,
                'job': 'Actor'}
print(person)
```

## General exercises  {.unnumbered}

<!-- TODO: Find annother example than Donald Trump -->

Start by makeing dictionaries for (some of) the Trump family:

```python
donald = {'name': 'Donald Trump', 'age': 70, 'job': 'President' }
melania = {'name': 'Melania Trump', 'age': 70, 'job': 'First lady' }
tiffany = {'name': 'Tiffany Trump', 'age': 23, 'job': 'Internet personality' }
ivanka = {'name': 'Ivanka Trump', 'age': 35, 'job': 'Top aide' }
```

#### Exercise
What do you think the following code produces? Do *all* of the substitution and reduction steps in your head, and only then try out the code.

```python
donald['child'] = tiffany
melania['husband'] = donald

print(melania)
print(melania['husband']['child'])
```

#### Exercise
A dictionary can contain *any* kind of Python values, even lists or dictionaries. Consider the code below where we add a list of ex-wives to the Trump persona. Can you see why we need to check if the `'ex-wives'` key before we add to the list of ex-wives?

```python
donald = {'name': 'Donald Trump', 'age': 70, 'job': 'President' }

if 'ex-wives' not in donald:
    donald['ex-wives'] = []
donald['ex-wives'].append('Marla Maples')
donald['ex-wives'].append('Ivana Trump')

print(donald)
```

#### Exercise
I case you wonder what the *type* of value a list is, or a dictionary, try this:

```python
print("A list has type:", type([]))
print("A dictionary has type:", type({}))
```

Now the types `list` and `dict` are your friends too.

#### Exercise
Lists can also contain any kind of value. Consider this example. What do you think the following code produces? Do *all* the substitution and reduction steps in your head, and only then try out the code.

```python
trump_family = [donald, melania, ivanka, tiffany]
print(trump_family)
print(trump_family[1]['job'])
```

#### Exercise
Write and run this code

```python
amino_acids = {}
amino_acids['ATG'] = 'met'
amino_acids['TCT'] = 'ser'
amino_acids['TAC'] = 'tyr'

codon = 'TCT'
print("{} encodes {}".format(codon, amino_acids[codon]))
```


> You have probably noticed that, for each type of value, the interpretation of length is different. In a string it is the number of characters, in a list is the number of values in the list and in a dictionary, it is the number of key-value pairs. How do you think Python knows which interpretation of length to use when the `len` function is called? This is where objects shine. `len(x)` just returns the value that `x.__len__()` returns. So the `len` function is defined roughly like this:
> ```
> def len(x):
>     return x.__len__()
> ```
>
> Similarly, the `in` operator call a secret `__contains__` method. 

