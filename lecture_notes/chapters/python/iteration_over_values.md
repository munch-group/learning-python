# Iteration over values {.unnumbered}

*This chapter is about how you repeat the same code for many different values -- and the many reasons why this is useful.*

## The for-loop  {.unnumbered}

Programs often need to do repetitive things. Consider this example below where `x` is assigned a value that is then printed:

```python
x = 1
print(x)
x = 5
print(x)
x = 3
print(x)
x = 7
print(x)
```

You can see that we do the same thing four times with the only difference that the variable `x` takes a new value each time. Now carefully write the alternative version below and compare what is printed to what was printed in the above example.

```python
for x in [1, 5, 3, 7]:
    print(x)    
```

It should be exactly the same. What you just wrote is called a *for-loop*. It is called a for-loop because it does something *for* each of many values -- in this case for each value in our list.

The statements nested under the for-loop are run as many times as there are values in our list, and every time they are run `x` is assigned a new value. The first time the statements are run, `x` is assigned the *first* value in the list. The second time they are run `x` is assigned the *second* value in the list. This continues until `x` has been assigned all the values in the list.

The semantics of a for-loop is as follows:

1. First, you write `for`.
2. Then you write the name of the variable that will be assigned a new value for each iteration of the loop (`x` in the above case).
3. Then you write `in`.
4.  Then you write the name of an *iterable* or an expression that reduces to one. In the above case, it was the list `[1, 5, 3, 7]`.
5. The statements nested under the for loop are indented with four spaces just like with if-statements. These statements are executed once for every value in the *iterable*. 

What is an *iterable*, you may ask? Actually, it is any kind of value that knows how to serve one value at a time until there are none left. Only objects that have an `__iter__` method can do this. If you try to iterate over a value that does not have an `__iter__` method you will get an error. Try the code below and see how Python complains that "'int' object is not iterable":

```python
for x in 4:
    print(x)
```

Try these variations of the for-loop above and notice how the rules 1-5 apply in each case:

```python
for x in [1, 5, 3, 7]:
    print(x)    

list_of_numbers = [1, 5, 3, 7]
for x in list_of_numbers:
    print(x)    

for x in [1, 5] + [3, 7]:
    print(x)    
```

In each case, the expression after `in` reduces to the *value* `[1, 5, 3, 7]`, which then serves as the *iterable*.

Not only lists are iterable. Strings are too. Their '__iter__' method of a string tell it that it should serve once character at a time. Try this:

```python
for character in 'banana':
    print(character)
```

Neat, right?.

In programming, you very often need to iterate over integer values, and sometimes quite a few (like the 250 million bases of the human chromosome one). It would be quite annoying if you had to manually make long lists of integers, so Python provides a builtin function called `range` that helps you out. It returns a special *iterator* value that lets you iterate over a specified range of numbers. Try the two examples below and compare what is printed:

```python
total = 0
for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    total += number
print(total)

total = 0
for number in range(10):
    total += number
print(total)
```

You can see that using `range` works just like using a list of numbers, but the cool thing about range is that it does not return a list. It just serves one number at a time until it is done. This is also why you will not see a list if you try to print what `range` returns:

```python
number_iterator = range(10)
print(number_iterator)
```

The `range` function needs three values to know which values to iterate over: "start", "end" and "step". If you do not give it all three arguments it will assume sensible defaults. Try this:

```python
for i in range(0, 10, 1):
    print(i)

for i in range(0, 10):
    print(i)

for i in range(10):
    print(i)
```

You can see that the first and the last arguments default to 0 and 1. If you give it two arguments it will assume that they are "start" and "end". If you only give it one argument it will assume that it is the "end". 

#### Exercise
What do you think the third argument to `range` specifies? Try these variations and see if you can figure it out:

```python
for i in range(0, 10, 1):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(0, 10, 3):
    print(i)
```

[Check the documentation](https://docs.python.org/3/library/stdtypes.html#range) once you have made up your mind.

#### Exercise
What will happen here:

```python
for x in []:
    print(x)  
```

and here:

```python
for x in range(0):
    print(x)  
```

and here:

```python
for x in range(10, 10):
    print(x)  
```

#### Exercise
The two examples below print the same. Make sure you understand why. Write and experiment with the code on your own.

```python
list_of_words = ['one', 'two', 'three']

# example 1
for word in list_of_words:
    print(word)

# example 2
list_length = len(list_of_words)
for index in range(list_length):
    print(list_of_words[index])
```

#### Exercise
Finish the code below so all the even numbers go into one list and all the odd numbers go into the other (hint: remember the modulo operator?)

```python
numbers = [4, 9, 6, 7, 4, 5, 3, 2, 6]
even = []
odd = []
for n in numbers:
    # your code here ...
    
    
```

#### Exercise
You can put any statements under the for-loop. Here it includes an if-statement that lets you generate a list of all the `a` characters in banana (in case you need that).

```python
result = []
fruit = 'banana'
for character in fruit:
    if character == 'a':
        result.append(character)
print(result)
```

Now change the code so you instead get the *indexes* of the 'a' characters: `[1, 3, 5]`. Here are some hints:

1. You need a for-loop over a list of numbers.
2. `range(len(fruit))` may be relevant numbers :-).
3. `fruit[1]` substitutes for `'a'`.

#### Exercise
Imagine you want to throw a big party and that you have a rented a place with room for 100 people. Now you want to start inviting people. What kind of error do you get here and why?

```python
friends = ["Mogens", "Preben", "Berit"]
invited = []
for index in range(100):
    invited.append(friends[index])
```

#### Exercise {#sec:ij_pairs}
You can also put a for-loop under another for loop, and the rules for *each* for loop are still those explained above: The statements nested under the for loop are indented with four spaces just like with if-statements. These statements are executed once for every value in the iterable. Think carefully about what you think is printed in the example below before you try it out.

```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

Make sure you understand i, j pairs are printed in the order they are.


