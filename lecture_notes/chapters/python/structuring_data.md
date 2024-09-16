# Structuring data

*This chapter is about lists and dictionaries that are Python values that can contain other Python values. Lists and dictionaries lets you build relationships between values, which is what data structures represent.*

## Lists  {.unnumbered}

For many kinds of data, the order of things is important. Just like the order of characters is important for the meaning of text in a string, we sometimes we want to specify the order of other things because the relative order of items in the list has some meaning. It could be a grocery list where you have listed the things to buy in the order you get to them in the supermarket. This is where Python lists are useful. When you print a list it nicely shows all the values it contains.

```python
grocery_list = ["salad", "canned beans", "milk", 'beer', 'candy']
print(grocery_list)
```

Unlike strings that can only store the order of characters, lists can contain *any* kind of values and you can mix different types of values any way you like. Here is a list that contains an integer, a boolean, a string and a list:

```python
mixed_list = [42, True, 'programming', [1, 2, 3] ]
```

By now you have probably guessed that you make a list with two square brackets. Between them you can put values with commas in-between. A list is a *container* of other values and the value of the list itself does not depend on the values it contains. This makes sense. Otherwise, an empty list would not have a value:

```python
my_list = []
```

You can add single values to the end of a list using the `append` method of lists. Try it out:

```python
desserts = []
print(desserts)
desserts.append('Crepe suzette')
print(desserts)
desserts.append('Tiramisu')
print(desserts)
desserts.append('Creme brulee')
print(desserts)
```

If you have a list you want to add to the end of another list you use the `extend` method:

```python
cheeses = ['Gorgonzola', 'Emmentaler', 'Camembert']
desserts.extend(cheeses)
print(desserts)
```

Notice how `append` and `extend` *modifies* the existing list instead of producing a new list with the added element.

#### Exercise
Do you think this will work?

```python
cheeses = ['Gorgonzola', 
           'Emmentaler', 
           'Camembert']
print(cheeses)
```

Surprised? Code inside parentheses, brackets and braces can span several lines, which can sometimes make your code easier to read.

#### Exercise
If you want to test if a value is in a list you use the `in` operator. Try this:

```python
print('Tiramisu' in desserts)
print('Meatloaf' in desserts)
```

#### Exercise
You can concatenate two lists to produce a new joined list. Make sure you figure out how this works before you try it out. Then experiment with changing the lists. Can you concatenate two empty lists?

```python
some_list = [1, 2, 3]
another_list = [7, 8, 9]
merged_list = some_list + another_list
print(merged_list)
```

This is yet another example of how the functionality of Python objects lets them "know" how to behave under different circumstances, such as when adding two objects (see @sec:add_method).

#### Exercise
What do you think is printed here? Make sure you figure out how you think this works before you try it out. What does the `append` method return?

```python
my_list = []
x = my_list.append(7)
print(x)
print(my_list)
```

## Indexing and slicing lists  {.unnumbered}

Now you know how to make lists, but to work with the values in lists you must also know how to access the individual values that a list contains. Fortunately, indexing lists works just like indexing strings: Each value in a list is identified by an *index* exactly like each character in a string:

```python
numbers = [7, 4, 6, 2, 8, 1]
print("first value is", numbers[0])
print("second value is", numbers[1])
print("third value is", numbers[2])
```

Notice that the function `len` can also compute the length of a list. So you also get the last value in list like this:

```python
numbers = [7, 4, 6, 2, 8, 1]
last_index = len(numbers)-1
print("Last element is", numbers[last_index])
```

If you want a sub-list of values from a list (we also call that a *slice*) you specify a start index and an end index separated by a colon, just like with strings:

```python
print(numbers[1:4])
```

When you run that you can see that `numbers[1:4]` is substituted for `[4, 6, 2]`, so the slicing operation produces a new list of the specified values.

#### Exercise
What do these two expressions reduce to?

```python
[11, 12, 13, 14, 15, 16, 17][2]
```

#### Exercise
What is printed here? Do all the substitution and reduction steps and compare to the exercise above.

```python
l = [11, 12, 13, 14, 15, 16, 17] 
print(l[2])
```

#### Exercise
What is printed here? Do *all* the substitution and reduction steps -- and do it *twice*. Next week you will be happy you did.

```python
numbers = [1,2,3]
i = 0
print(number[i])
i = 1
print(number[i])
i = 2
print(number[i])
```

#### Exercise
What do you think happens here? Make up your mind and try out the code below:

```python
l = [11, 12, 13, 14, 15, 16, 17] 
l[4] = "Donald"
print(l)
```

Were you surprised what happened? Compare to @sec:immutable_strings. Lists are not immutable like strings and you can replace values by assigning a new value to an index in the list.

#### Exercise
With your knowledge of slicing, what do you think is printed below:

```python
l = [11, 12, 13, 14, 15, 16, 17]
print(l[:3])
print(l[3:])
print(l[:])
```

#### Exercise
What do you think happens when you specify an index that does not correspond to a value in the list:

```python
l = [11, 12, 13, 14, 15, 16, 17] 
print(l[7])
```

Read and understand the error message. Does it ring a bell?

#### Exercise
Do you think you also get an error when you specify a slice where the end is too high? Try it out:

```python
l = [11, 12, 13, 14, 15, 16, 17]
print(l[4:99])
```

I guess that is also worth remembering.

#### Exercise
Which value in a list named `l` does this expression reduce to?

```python
l[len(l)-1]
```

#### Exercise
If you do not like Emmentaler you can just delete it. What do you think the `del` keyword does?

```python
cheeses = ['Gorgonzola', 'Emmentaler', 'Camembert']
print(cheeses)
del cheeses[1]
print(cheeses)
```

#### Exercise
Because intervals are "ends exclusive" we can compute the length of a slice as `end - start`:

```python
l = [7, 4, 6, 2, 8, 1]
start = 1
end = 4
print("{} has length {}".format(l[start:end], end-start))
```

Think about what this code would look like if ends were included in intervals.

#### Exercise
Another advantage of "ends exclusive" intervals is that you only need one index to split a list in two:

```python
l[:idx] + l[idx:] == l
```

If ends were included in intervals this would not be as simple.

#### Exercise
Do *all* the substitution and reduction steps in your head (or on paper) before you write any of the following code. Think carefully and make up your mind what you think will be printed below. Remember that the *value* of a list is a container that holds other *values* in it. Then write the code and see if you were right. If you were not, make sure you figure out what led you to the wrong conclusion. 

```python
x = 'A'
y = 'B'
z = 'C'
lst = [x, y, z]
print(lst)

x = 'Preben'
print(lst) # what is printed here? 

lst[0] = 'Mogens'
print(lst) # what is printed here?
```

#### Exercise
Do you remember this trick from string slicing?

```python
l = [1, 2, 3, 4, 5]
print(l[::-1])
```

#### Exercise
You can produce a list by splitting a long string into smaller parts. Think: "*Hey string, split yourself on this smaller string*". Try these variations to figure out how it works

```python
"Homo sapiens neanderthalensis".split(" ")
"Homo sapiens neanderthalensis".split('en')
'ATGCTCGTAACGACACTGCACTACTACAATAG'.split('')
"1, 2, 3, 5, 3, 2, 5, 3".split(', ')
"1,2,3,5,3,2,5,3".split(',')
'ATGCTCGTAACGACACTGCACTACTACAATAG'.split()
"Homo sapiens neanderthalensis".split()
```

Notice that the method has a default behavior when no argument is passed to it.

#### Exercise
You can produce a string by joining the elements of a list (if all the elements are strings of course). Think: "*Hey string, put yourself in between all the strings in this list*".

```python
"-".join(['Homo', 'sapiens', 'neanderthalensis'])
"...".join(['Homo', 'sapiens', 'neanderthalensis'])
"".join(['A', 'T', 'G'])
```

Notice how you can join something on an empty string. This is a very useful technique; for example if you want to turn a list of characters into a string.

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

