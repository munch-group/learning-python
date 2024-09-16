
# General exercises  {.unnumbered}

#### Exercise

Remind yourself of the different types of Python values you know. E.g. one of them is integer (`int`). Make a list.

#### Exercise {#sec:coercion_of_type}

You already know about several types of data values in Python. Two of them are integers called `int`, and decimal numbers (or floating points) called `float`. When you use an operator like `+` or `>` it produces a value. No matter what you put on either side of `>` in it produces a boolean value (`bool`), `True` or `False`. For other operators what type of value that is produced depends on which values the operator work on. Try this and see if you print an integer or a float (`8` or `8.0`):

```python
x = 4
y = 2
result = x * y
print(result)
```

Now try to replace `4` with `4.0`. What type is result now?. Try to also replace `2` with `2.0`. What type is result now? Can you extract a rule for what the `*` operator produces depending on the what types the two values have?

#### Exercise

In @sec:coercion_of_type you investigated what types of values the `*` operator produce. Redo that exercise with the operators: `+`, `-`, `/`, `**`, `//`, and `%`. What are the rules for what is returned if both values are integers, one values is a float, or both values are floats?

#### Exercise 

Make a list of all the operators you know so far in order of precedence (without looking in the notes). Then check yourself. 

#### Exercise

What does his expression reduce to?

```python
3 > 2
```

#### Exercise

What does his expression reduce to? Do all the reduction steps in your head. 

```python
2 - 4 * 5 - 2 * 9
```

#### Exercise

What does his expression reduce to? Do all the reduction steps in your head. 

```python
3 > 2 and 2 - 4 * 5 - 2 * 9
```

#### Exercise

What does his expression reduce to? Do all the reduction steps in your head. 

```python
0 and 1 or 2
```

#### Exercise

What does his expression reduce to? Do all the reduction steps in your head. 

```python
4 and 1 or 2
```

#### Exercise 

What is the value of `results` once the code below has run?

```python
x = 7
y = 13
z = x + y
x = 0
result = x + y + z
```

#### Exercise 

What is the value of `results` once the code below has run?

```python
x = 5
y = x + 1
x = y + 1
y = x + 1
result = x + y
```

#### Exercise

In the code below I have shuffled the statements. Put them in the right order to make the code print `9`. To do that you must think about which values each variable will in each statement depending on the how you order the statements.

```python
x = x + 1
y = 5
y = y - 1
print(y)
x = 1
y = y * x
```

#### Exercise

In the code below I have shuffled the statements. Put them in the right order to make the code print ``

```python
c = b
print(c)
a = b + a
b = 'og'
b = c + a
c = 'M'
a = 'ens'
```

#### Exercise

Make three exercises that requires the knowledge of programming so far. Have your fellow students solve them.
