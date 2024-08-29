# Gluing values in sequence

## Tuples {-}

A tuple is a sequence of values just like a list. However, unlike a list, the elements of a tuple can not be changed. You cannot append to a tuple either. Once a tuple is made it is immutable (or unchangeable). To make a tuple you just use round brackets instead of square brackets:

```python
fruits = ("apple", "banana", "cherry")
```

It may seem strange that Python has both tuples and lists. One reason is that whereas lists are more flexible, tuples are more efficient. We will not use tuples a lot, but you need to know what they are.

You can do most of the operations on a tuple that you can also do on a list. The following exercises should be easy if you remember how to do the same thing on lists:

#### Exercise
Find the number of elements in the `fruits` tuple using the `len` function.

#### Exercise
Extract the second element of the `fruits` tuple (`"banana"`) using indexing.

#### Exercise
Try to change the second element of the `fruits` tuple to `"apple"` and see what happens. It should be someting like this:

```
Traceback (most recent call last):
  File "script.py", line 2, in <module>
    fruits[3] = "apple"
TypeError: 'tuple' object does not support item assignment
```

You cannot change elements of a tuple because they are immutable (once made, they stay that way).

## Tuple assignment {-}

Python lets you assign a tuple of values to a tuple of variables like this:

```python
father, mother, son = ("Donald", "Ivana", "Eric")
```

It does the same as the following three assignments:

```python
father = "Donald"
mother = "Ivana"
son = "Eric"
```

When a tuple is made, the values are "packed" in sequence:

```python
family = ("Donald", "Ivana", "Eric")
```

Using the same analogy, values can be "unpacked" using tuple assignment:

```python
father, mother, son = family
```

The only requirement is that the number of variables equals the number of values in the tuple.

Once in a while, it is useful to swap the values of two variables. With conventional assignment statements, we have to use a temporary variable. For example, to swap a and b:

```python
tmp = a
a = b
b = tmp
```


#### Exercise

Try this and read the error message:

```python
family = ("Donald", "Ivana", "Eric")
father, mother = family
```

#### Exercise

Try this and read the err or message:

```python
family = ("Donald", "Ivana", "Eric")
father, mother, son, daughter = family
```

Compare to the error message in the previous exercise.

#### Exercise

Say want to swap the values of two variable `a` and `b`. To do that you would need to keep one of the values in an extra variable like this:

```python
temp = a
a = b
b = temp
```

Can you come up with a simple and pretty way of swapping `a` and `b` in one statement, using what you have learned in this chapter? Maybe it occurs to you before you realize how it works, so make sure you can connect your solution to the rules of tuples and tuple assignment.


<!-- TODO: Find annother example than Donald Trump -->
