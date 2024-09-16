# Structuring data

This section will further train your ability to create such data structures using iteration. Data structures in Python are fundamental tools that allow you to organize, store, and manipulate data effectively. They provide a way to represent and manage data in a structured and organized manner, making it easier to perform various operations on the data. Python offers a variety of built-in data structures, such as lists and dictionaries, with different properties and useful for different needs. Sometimes, a single list or dictionary is all you need. Still, sometimes you need to combine many lists and dictionaries to make elaborate data structure. As your programming skills progress, you will find that mastering the use of different data structures is crucial for becoming a proficient Python programmer.

#### Exercise {#sec:dict_count_fixed}
Imagine you want to count how many times each nucleotide appears in a DNA string like this one: `'ATGCCGATTAA'`. One way to proceed an account of this is in the form of a dictionary where the keys represent the different values we want to count (in this case `'A'`, `'T'`, `'C'` and `'G'`). The values associated with each key is the number of times we have seen that key (nucleotide). So we want to end up with a dictionary like this one (not necessarily with key-value pairs in this order): 

```python
{'G': 2, 'C': 2, 'T': 3, 'A': 4}
```

Remind yourself how you assign a value to an existing key in a dictionary. Here is some code to get you going:

```python
dna = 'ATGCCGATTAA'
counts = {'G': 0, 'C': 0, 'T': 0, 'A': 0}
for base in dna:
    # Your code here...
    
```


#### Exercise {#sec:dict_count}
In @sec:dict_count_fixed we started by initializing a dictionary with a key for each nucleotide and the number zero for each key to show that we had not seen any of those nucleotides yet. *Then* we iterated over the values we wanted to count using the for-loop. This approach of cause only works if know which values we will encounter in the iteration. When counting nucleotides, this works because we know there are only four different nucleotides. 

Often, however, we are faced with one or both of the following problems:

- The number of different values to count is very large. If we were to count English words, we would have to initialize a dictionary with more than 170.000 key value pairs (which would be somewhat impractical). If we were to count numbers this would be impossible (as there are infinitely many of those).
- We do not know what values we are going to count. It goes without saying that we cannot initialize a dictionary with keys if we do not know what they are.

We can solve this problem by only adding keys for the values we actually see in the iteration. To do this we need to change our approach from before in two ways:

1. We start with an *empty* dictionary.
2. For every value we iterate over, we check if that value is a key in our dictionary. If it is not, then we need to add it and pair it with the value `0`. You can test if a key is not in a dictionary using the `not in` operator:

```python
if number not in counts:
    counts[number] = 0
```

Now use these hints to complete the code below so that it counts how many times each number appears in `number_list`.

```python
counts = {}
number_list = [13, 51, 3, 51, 6, 42, 3]
for number in number_list:
    # Your code here...
    
```

When you are done you should have a dictionary like this (possibly with key-value pairs in a different order):

```python
{3: 2, 42: 1, 51: 2, 13: 1, 6: 1}
```

#### Exercise
The counting technique you developed in @sec:dict_count lets you count pretty much anything that can be a key in a dictionary. Try using the same approach to count the number of each thing in this list:

```python
stuff = ['sofa', 42, 42, 3.14159, 'sofa', 'Dragon']
```


#### Exercise {#sec:build_lists_fixed}

Instead of counting values, we sometimes need to split the values we iterate over into categories. Here we build a dictionary where the keys are the first letter of each word we iterate over, and the value associated with each key is a list of all the words that start with that letter. So if we iterate over the words in this list:

```python
names = ['apricot', 'banana', 'ananas', 'apple', 'cherry']
```

we should end up with this dictionary (not necessarily with key-value pairs in that order):

```python
{'c': ['cherry'], 'a': ['apricot', 'ananas', 'apple'], 'b': ['banana']}
```

Now figure out how to reorder and indent the statements below to  produce code that performs this task:

```python
names = ['apricot', 'banana', 'ananas', 'apple', 'cherry']
words[first_letter].append(fruit)
first_letter = fruit[0]
for fruit in names:
words = {'a': [], 'b': [], 'c': []}
```

#### Exercise
Produce the same dictionary as in @sec:build_lists_fixed by reordering and indenting the following statements:

```python
first_letter = fruit[0]
words = {}
words[first_letter].append(fruit)
if first_letter not in words:
names = ['apricot', 'banana', 'ananas', 'apple', 'cherry']
words[first_letter] = []
for fruit in names:
```

Compare the solution to that in @sec:build_lists_fixed. How is it different? Is it more generic? How does the difference relate to the difference between @sec:dict_count_fixed and @sec:dict_count?

#### Exercise {#sec:mult_greetings}
Look at this code and figure make up your mind about what will be printed. Do we first greet one person in three languages or do we first greet all people in one language? Then try it out to see if you were right.

```python
greetings = ['Hi', 'Hola', 'Ciao']
names = ['Mogens', 'Preben', 'Henning']
for greeting in greetings:
    for name in names:
        print(greeting, name)
```

#### Exercise
Now consider the code below. How is it different from the code in @sec:mult_greetings? How does that alter the order of what is printed?

```python
greetings = ['Hi', 'Hola', 'Ciao']
names = ['Mogens', 'Preben', 'Henning']
for name in names:
    for greeting in greetings:
        print(greeting, name)
```

#### Exercise {#sec:pairs}
Decide what you think the code below does and why you think so. Do *every* step in your head including all the substitutions and reductions. Then write the code carefully and run it. 

```python
nr_list = [10, 20, 30]
combinations = []
for a in nr_list:
    for b in nr_list:
        pair = [a, b]
        combinations.append(pair)
```

The `combinations` list becomes:

```python
[[10, 10], [10, 20], [10, 30],
 [20, 10], [20, 20], [20, 30], 
 [30, 10], [30, 20], [30, 30]]
```

Here I broke over three lines to make it fit on the page. You should print your own `combinations` list to make sure you got the code right.

#### Exercise {#sec:pairs_no_doubles}
The code in @sec:pairs printed all combinations of numbers in the list -- including those where the two numbers are the same. Change the code above so these pairs are *not* printed. You should end up with this list:

```python
[[10, 20], [10, 30], [20, 10], [20, 30], [30, 10], [30, 20]]
```

#### Exercise {#sec:pairs_unique}
Can you solve the same task as in @sec:pairs_no_doubles, by modifying the code below? Begin by making sure you understand why it produces the same list as that in @sec:pairs. If you have trouble with that, then have another look at @sec:ij_pairs.

```python
nr_list = [10, 20, 30]
combinations = []
for i in range(len(nr_list)):
    for j in range(len(nr_list)):
        pair = [nr_list[i], nr_list[j]]
        combinations.append(pair)
```

#### Exercise
The code in the exercise above printed all combinations of *different* numbers in the list. But you can see that each pair of numbers still appear twice if you do not take their order into account (e.g. `[10, 30]` are the same two numbers as `[30, 10]`). Change the code you wrote for the previous exercise so these pairs are not printed. You should end up with a list like this:

```python
[[10, 20], [10, 30], [20, 30]]
```

Hint: the easiest way to do it is to use the value of `i` to change the range of numbers you iterate over in the second for-loop.

#### Exercise {#sec:matrix}
Sometimes programmers (like you) work with matrices of numbers like the one below:

```python
[[0, 1, 2, 3, 4], 
 [0, 1, 2, 3, 4], 
 [0, 1, 2, 3, 4], 
 [0, 1, 2, 3, 4],
 [0, 1, 2, 3, 4]]
```

Here I wrote the list in a nice way so you can see that a matrix is really just *a list of lists*. When you print it looks like this:

```python
[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
```

Do you think you can write some code that produces this matrix? If you let out a sigh just now, then reread the sections on lists and for-loops. You may think absorbed all the information you could when you read it the first time, but with your practice since then, you may be able to understand it at a deeper level the second or third time you read it.

The code below produces the matrix above. There are several tricky parts that you need to make sure you understand. In line three we add an empty list to the list of lists. In line five we add the value of `j` to the list at index `i` in the list of lists. Go over this many times in your head and with pen and paper.

```python
matrix = []
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
```

#### Exercise
If you understand how you created the matrix in @sec:matrix, you should be able to produce the matrix below using a small modification to the code from @sec:matrix.

```python
[[1, 1, 1, 1, 1],
 [2, 2, 2, 2, 2],
 [3, 3, 3, 3, 3],
 [4, 4, 4, 4, 4],
 [5, 5, 5, 5, 5]]
```

#### Exercise
Now produce this matrix:

```python
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
```

#### Exercise
Can you write some code that produces this matrix?:

```python
[[ 0, -1, -2, -3, -4],
 [-1,  0,  0,  0,  0],
 [-2,  0,  0,  0,  0],
 [-3,  0,  0,  0,  0],
 [-4,  0,  0,  0,  0]]
```

## General exercises  {.unnumbered}

> By now you have learned a lot and the general exercises, which serve to keep it all current, get more complicated. But remember: even though the code may mix lists, for-loops, and functions, the *rules* for lists, for-loops and functions are *not* mixed. The separate simple rules for a list, a for-loop and a function are *still* the same. If you get confused, it is time revisit the sections about each separate topic. You will probably have to do that many times during the course.

#### Exercise
Write a function, `square_numbers`, that takes a list of numbers as argument and returns a new list with the numbers squared.

```python
# write your function definition here ...

numbers = [1, 5, 3, 7]

# then you can call it like this:
squared = squared_numbers(numbers)
```


#### Exercise
Write a function `count_characters`, which takes a string argument and returns a dictionary with the counts of each character in the string. When you call the function like this: 

```python
count_characters('banana')
```

it must return (not necessarily with key-value pairs in that order):

```python
{'n': 2, 'b': 1, 'a': 3}
```

The technique you should use is the one you learned in @sec:dict_count. Here we just iterate over a string of characters instead of over a list of numbers. Here is a bit of code to help you along...

```python
def count_characters(text):
    counts = {}
    # fill in the missing code ...

    return counts
```

#### Exercise
Use the function you made in the previous exercise to construct the following data structure:

```python
{ 'banana': {'b': 1, 'a': 3, 'n': 2},
  'apple': {'a': 1, 'e': 1, 'p': 2, 'l': 1}, 
  'ananas': {'a': 3, 's': 1, 'n': 2} }
```

from this list:

```python
['banana', 'ananas', 'apple']
```

Here is some code to help you along:

```python
my_database = {}
for word in ['banana', 'ananas', 'apple']:
    my_database[word] =  # you figure this out...
```

Once you are done, what value do you think `my_database['banana']` represents? I.e. what will it reduce to if used in an expression? And what value does `my_database['banana']['a']` represent?

#### Exercise
Read the code below and make sure you understand each single step before you write any of it. Revisit previous sections if you must, go look in the Python documentation. *Then* write and run the code - and enjoy that it was exactly what you expected.

```python
def get_words(text, search_string):
    hits = []
    for word in text.split():
         if search_string in word:
            hits.append(word)
    return hits
    
s = 'eenie meenie minie moe'
nie_words = get_words(s, 'nie')
m_words = get_words(s, 'm')

print(' '.join(nie_words))
print(' '.join(m_words))
```


#### Exercise 
This larger will take you through some of the most common string manipulations. A palindrome is a string that is spelled the same way backward and forwards. 

*Write a function*, `is_palindrome`, which takes one argument:

* A string.

The function must return:

* `True` if the string argument is a palindrome and `False`
otherwise.

Example usage:

```python
is_palindrome('abcba')
```

should return `True` and

```python
is_palindrome('foo')
```

should return `False`

One approach to this is to run through s from the first to the middle character and for each character check if the character is equal to the character at the same index from the right rather than the left. Remember that the first character of a string is at index `0` and the last at index `-1`, the second character is at index `1` and the second last at index
`-2` and so forth.

Since you need to run through the string from the first to the middle character you first need to figure out how many characters that corresponds to. Say your palindrome is `"ACTGTCA"`, then the number of indexes you need to loop over with a for loop is:
 
```python
s = "ACTGTCA"
nr_indexes = len(s)//2 
```

Figure out how to make `range()` return indexes you can use to access the characters in the first half of the sequence. Then make a for loop where you iterate over the indexes you get from `range()`. Try to make the for-loop print out the first half of the characters, just to make sure you are using the right indexes.

Once you get this far you need to compare each character from the first half of the corresponding ones starting from the other end of the palindrome. Figure out how to change each index used for the first half to the corresponding index for the other half so you can compare the relevant pairs. (You need to compare index `0` with `-1`, `1` with `-2` and so on...)

Now try to make the for-loop print both the character from the first half and the corresponding character from the other end. If you got the indexes right you will see that the A print with the A from the other end, the C with the C and so on.

Write an if-statement in the for-loop that tests if the two corresponding characters are the same. If the string is a palindrome, then each pair is identical. So as soon as you see a pair which is not identical, you know it is not a palindrome and you can let your function return `False` like this:

```python
if left_character != right_character:
    return False
````

Remember that the function ends as soon as it encounters a `return` statement.

If all pairs pass the test, it means that the string is a palindrome, and the function should return `True` when exiting the for-loop.
