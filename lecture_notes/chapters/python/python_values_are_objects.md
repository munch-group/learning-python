# Python values are objects

*This chapter introduces the notion of an object, one of the most central aspects of Python. Once you get catch your breath, you will love that all Python values are objects.*

## Methods  {.unnumbered}

In Python, a value like an integer or string, not only holds data. It is also packaged with a lot of useful functionality relevant to the particular *type* of value. When a value is packaged with such relevant functionality and meta information, programmers call it an *object* - and in Python *all* values are objects.

The associated functionality comes in the form of *methods*. You can think of methods as functions that are packaged together with the value. For example, string values have a method called `capitalize`.  Try it out:

```python
x = "banana".capitalize()
print(x)
```

To call the method on the string value, you connect the string value and the method call with a dot. So to call a method on a value you do the following:

1. Write the value (or a variable name that substitutes for a value).
2. Then write a `.`.
3. Then write the name of the method (like `capitalize`).
4. Then write two parentheses to call the method. If the method takes any arguments other than the value it belongs to, then you write those additional values between the parentheses with commas in between, just as when you call a function.

You can see that the method call looks just like a function call and in many ways calling a method works much like calling a function. The difference is that when we call a function we say: "*Hey function, capitalize this string!*". When we call a method we say: "*Hey string, capitalize yourself!*"

So why do we need methods? Why do we need them when we have functions? It turns out that it is very handy to have some relevant and ready-to-use functionality packaged together with the data it works on. You will start to appreciate that sooner than you think.

Methods are almost always used with variables. So remember to do any substitutions and reductions requried. When we put a method call after a *variable* like below, the variable is first substituted for its value and *then* the method is called on the value. Consider the second line of this example:

```python
x = "banana"
print(x.capitalize())
```

Here `x` is first substituted by `"banana"` and *then* the method is called on that value, like this: `"banana".capitalize()`.

Now write and run these examples:

```python
message = "Methods Are Cool"
print(message)

shout = message.upper()
print(shout)

whisper = message.lower()
print(whisper)

new_message = message.replace("Cool", "Fantastic")
print(new_message)
```

You can see what these methods do. For example: `upper` returns an uppercased copy of the string. 

#### Exercise {#sec:first_format_exe}
Write and run the following code. What do you think it does?

```python
line = '\n\tSome text\n'
print(">{}<".format(line))

line = line.strip()
print(">{}<".format(line))

```

Make sure you do the substitution and reduction steps in your head. Be especially careful about the third line of code. Also, what do you think the special `\t` character is?

#### Exercise
The string methods you have tried so far have all returned a new string. Try this example:

```python
'ATGACGCGGA'.startswith('ATG')
```

and this

```python
'ATGACGCGGA'.endswith('ATG')
```

What do the methods do and what do they return?

## Using the Python documentation  {.unnumbered}

Now that you are well underway to becoming a programmer, you should know your way around the [Python documentation](https://docs.python.org/3). Especially the part called the [Python standard library](https://docs.python.org/3/library). There is a *lot* of details in there that we do not cover in this course. These are mainly are tools and techniques that for writing more efficient, extensible, robust and flexible code. The parts we cover in this course are is the minimal set that will allow you to write a program that can do *anything*.

#### Exercise
There is a string method that returns a secret agent:

```python
print('7'.zfill(3))
```

You can look it up in the [Python documentation](https://docs.python.org/3/library/stdtypes.html#str.zfill).

#### Exercise

Browse through all the [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) to get am impression of all the functionality that is packaged with string objects. 


## String formatting  {.unnumbered}

You have already tried string formatting in @sec:first_format_exe. String formatting is a simple but powerful technique that lets you generate pretty strings from pre-computed values. You may have noticed that every time we print a floating-point number, a lot of decimals are shown. Not very pretty if you are only interested in two decimals anyway. To format a string, you use the `format` method (surprise). In its simplest use, `format` replaces occurrences of `{}` with the arguments that is passed to it - like this:

```python
taxon = "genus:{}, species:{}".format('Homo', 'sapiens')
```

#### Exercise
What happens if you try this?

```python
question = "Was {} {} Swedish?".format('Carl', 'Linneaus')
```

and this?

```python
question = "Was {} Swedish?".format('Carl', 'Linneaus')
```

and this?

```python
question = "Was {} {} Swedish?".format('Carl Linneaus')
```

In the two last examples the number of `{}` did not match the number of arguments to `format`. What happens when there are too few and what happens when there are too many?


#### Exercise
Consider this code:

```python
s = "{} is larger than {}".format(4, 3)
print(s)
```

What will happen if you run this code? Write the code and see for yourself once you think you know. If you were wrong, make sure you understand why.

#### Exercise
Consider this code:

```python
language = 'Python'
invention = 'sliced bread'
s = '{} is the best thing since {}'.format(language, invention)
print(s)
```

What will happen if you run this code? Write the code and see for yourself once you think you know. If you were wrong, make sure you understand why.

#### Exercise
Consider this code:

```python
my_template = '{} is the best thing since {}'
language = 'Python'
print(my_template.format(language, 'sliced bread'))
print(my_template.format(language, 1900 + 89))
```

What will happen if you run this code? Do the substitution and reduction steps in your head.

#### Exercise
Think back to @sec:chocolatebars where you calculated how many cookies you could buy for 30 kr. The bars are 7 kr. So your program looked something like this:

```python
nr_bars = 30 / 7
print('I can buy', nr_bars, 'chocolate bars!')
```

and it ran like this: `python chocolate.py`

```
I can buy 4.285714285714286 chocolate bars!
```

String formatting lets you rewrite the program like this:

```python
nr_bars = 30 / 7
message = "I can buy {} chocolate bars!".format(nr_bars)
print(message)
```

Try to replace `{}` with `{:.2f}`. `format` reads the stuff after the colon in each set of curly brackets and uses it as directions for how to format the value it inserts. Try it out and see what happens if you change the number `2` to `3`, `4`, `5` or `10`.

#### Exercise
See if you can find the documentation for the `format` function in the [Python documentation](https://docs.python.org/3). It can do wondrous things, for this course we will only try to control the number of digits and padding with spaces. Look at the examples below. Maybe you can figure out how it works

```python
pi = 3.14159265359
print("*{}*".format(pi))
print("*{:.3f}*".format(pi))
print("*{:.6f}*".format(pi))
print("*{:>5.3f}*".format(pi))
print("*{:>10.3f}*".format(pi))
```

#### Exercise {#sec:add_method}
This is bonus info, rather than an actual exericse. How do you think python can figure out that adding strings with is supposed to work differently than adding numbers? Remember that `'1' + '2'` is `'12'` not `3`. The answer is that all values you can add with the `+` operator has a secret method called `__add__` that defines how adding works for that type of value:

```python
s1 = "11"
s2 = "22"
n1 = 11
n2 = 22
print(s1 + s2)
print(s1.__add__(s2))
print(n1 + n2)
print(n1.__add__(n2))
```

This is one of many examples of how objects allow Python to implement functionality that fits each particular type of value. This was just to show how Python does this. Just like yellow and black stripes in nature means "don't touch me!" -- double underscores (`__`) is Python's way of saying "do not use this!". You are supposed to use the `+` operator not the `__add__` method.


## Indexing and slicing strings  {.unnumbered}

Another feature of string objects is that they allow you to extract individual parts of the string.

Each character in a string is identified by its *index* in the string. To access a character in a list you write brackets after the string. Between those brackets, you specify the index of the character you want. The first character has index 0, the second has index 1 and so on.

```python
codon = 'ATG'
print("first base is", codon[0])
print("second base is", codon[1])
print("third base is", codon[2])
```

You may wonder why the index of the first character is zero and not one. That is simply the convention in programming and is so for good reason. Over time you will begin to find this useful rather than annoying. You should think of the index as the offset from the start of the string.

That also means that the index is not the length of the string, but the length minus one:

```python
amino_acids = 'ARNDCQEGHILKMFPSTWYV'
last_index = len(amino_acids)-1
print("Last amino acid is", amino_acids[last_index])
```

If you want a sub-string from a larger string (we call that a *slice*), you specify a start index and an end index separated by a colon:

```python
print(amino_acids[1:4])
```

When you run that you can see that `amino_acids[1:4]` is substituted for `'RND'`, so the slicing operation produces a sub-string of `amino_acids`. You may wonder why the value at index 4 is not in the resulting sub-string. That is another programming convention: intervals are *ends exclusive*. So when you specify an interval with a start index of 1 and an end index of 4 it represents all the characters starting from 1 and up to, *but not including*, 4. So the slice `1:4` corresponds to the characters at indexes 1, 2 and 3. The reason programmers handle intervals in this way is that it makes it easier to write clear and simple code as you will see in the exercises.

#### Exercise
What do this expression reduces to?

```python
"Futterwacken"[7]
```

#### Exercise
What is printed here? Do all the substitution and reduction steps and compare to the exercise above.

```python
s = "Futterwacken"
print(s[7])
```

#### Exercise
What is printed here? Do all the substitution and reduction steps -- and do it *twice*. Next week you will be happy you did.

```python
dna = 'TGAC'
i = 0
print(dna[i])
i = 1
print(dna[i])
i = 2
print(dna[i])
```


#### Exercise {#sec:immutable_strings}
What do you think happens here? Make up your mind and try out the code below:

```python
s = "Futterwacken"
s[6] = 'W'
```

Did you see that coming? Strings are *immutable*, which means that you cannot change them once you have made them. If you want `"FutterWacken"` you need to produce a new string with that value. Try to figure out how to do that with the [`replace`](https://docs.python.org/3/library/stdtypes.html#string-methods) method of strings.

#### Exercise
When you do not specify the start and/or the end of a slice, Python will assume sensible defaults for the start and end indexes. What do you think they are? Make up your mind and try out the code below:

```python
s = 'abcdefghijklmnopqrstuvxyz'
print(s[:11])
print(s[11:])
print(s[:])
```

#### Exercise  {#sec:slicing_docs}
Find the documentation for how slicing of strings work.

#### Exercise
What do you think happens when you specify an index that does not correspond to a value in the list:

```python
alphabet = 'abcdefghijklmnopqrstuvxyz'
print(alphabet[99])
```

Read and makek sure you understand the error message. You can try to Google the error message.

#### Exercise
Do you think you also get an error when you specify a slice where the end is too high? Try it out:

```python
alphabet = 'abcdefghijklmnopqrstuvxyz'
print(alphabet[13:99])
```

and this:

```python
alphabet = 'abcdefghijklmnopqrstuvxyz'
print(alphabet[10000:10007])
```

I guess that is worth remembering, right?

#### Exercise
Which character in a string named `alphabet` does this expression reduce to?

```python
alphabet[len(alphabet)-1]
```

#### Exercise
Because intervals are "ends exclusive" we can compute the length of a slice as `end - start`:

```python
dna = "ATGAGGTCAAG"
start = 1
end = 4
print("{} has length {}".format(dna[start:end], end-start))
```

Figure out what this code would look like if ends were included in intervals.

#### Exercise
Another advantage of "ends exclusive" intervals is that you only need one index to split a string in two:

```python
s = 'Banana'
idx = 3
beginning = s[:idx]
end = s[idx:]
print(beginning + end)
```

Figure out what indexes you would need to use to split a sequence in two if ends were included in intervals.

#### Exercise
Did you look up the details of how slicing works in @sec:slicing_docs? Then you should be able to explain what happens here:

```python
s = 'zyxvutsrqponmlkjihgfedcba'
print(s[::-1])
```


## General exercises  {.unnumbered}

#### Exercise
Will this print `Bananas rule!`? Do all the substitutions and reductions. 

```python
if 'na' * 2 == "Banana"[2:]:
    print("Bananas rule!")
```

#### Exercise
Will this print `Bananas rule!`? Do all the substitutions and reductions. 

```python
if "{}s".format('Banana'[1:].capitalize()) == 'Ananas':
    print("Bananas rule!")
```

#### Exercise
Write a function called `even_string` that takes a string argument and returns `True` if the length of the string is an even number and `False` otherwise. E.g. `even_string('Pear')` should return `True` and `even_string('Apple')` should return `False` (remember the `modulo` operator?).

#### Exercise
Look at the code below and decide what is printed at the end. Then write the code and test your prediction. If you are wrong, make sure you figure out why ny revisiting the chapter about functions.

```python
def enigma(x):
    if x == 4:
        return x

result = enigma(5)
print(result)
```

#### Exercise
Inspect the code below and figure out why it does not print that you are a super star. Test the function using various input and figure out the mistake.

```python
def even_number(x):
    if x % 2:
        return False

if even_number(4):
    print('You are a super star!')
```



<!-- TODO: More general exercises 
-->


