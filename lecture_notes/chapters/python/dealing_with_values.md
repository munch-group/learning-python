# Dealing with values

*This chapter is about values and variables, the two most central concepts in programming.*

## Math {-}

Much programming is done to compute stuff. In Python the usual math operations are done using these arithmetic operators:

| Operator | Operation          |
|----------|--------------------|
| `+`      | plus               |
| `-`      | minus              |
| `/`      | division           |
| `//`     | integer division   |
| `*`      | multiplication     |
| `**`     | exponentiation     |
| `%`      | modulo (remainder) |

You are probably quite familiar with these - except perhaps for integer division, exponentiation and modulo. Let us take some of the operators for a spin. Remember to carefully write the whole thing in an empty file in *VScode*. Do *not* copy-paste. Then save the file as `mathandlogic.py` and run it from the terminal.Do not call your file `math.py`. It may bite you later. Just trust me on that one. 

```python
print("Four times two is",  4 * 2)
```

Notice how you can print more than one thing at a time if you put commas between the values you want to print? We can group computations using parentheses, just like in normal math. Try this:

```python
print("10 / (2 + 3) is", 10 / (2 + 3))
print("(10 / 2) + 3 is", (10 / 2) + 3)
```

In addition to the regular math operators, there are a few extra operators that we call *comparison operators* because they are used to compare two values, e.g. two numbers.

| Operator | Operation             |
|----------|-----------------------|
| `<`      | less-than             |
| `>`      | greater-than          |
| `<=`     | less-than-or-equal    |
| `>=`     | greater-than-or-equal |
| `==`     | equal                 |
| `!=`     | not equal             |

Try this:

```python
print("Is 5 greater than -2?", 5 > -2)
print("Is 5 greater or equal to -2?", 5 >= -2)
print("Is 5 less or equal to -2?", 5 <= -2)
print("Is 5 less than 7 - 2?", 5 < 7 - 2)
print("Is 5 equal to 7 - 2?", 5 == 7 - 2)
```

As you may have noticed running this code, comparing things using these operators we always produce either `True` or `False`. E.g. the following

```python
print(5 < 7)
```

prints the value `True`, because 5 *is* actually smaller than 7. `True` and `False` are special values in Python that we can use (and print if we like) just like any other Python value:

```python
print(True)
print(False)
```

#### Exercise
Try to write and run the code below. Compare each line to what is printed when you run the code. Make sure you understand why.

```python
print("I have", 25 + 30 / 6, "of someting")
print("I have", 100 - 25 * 3 % 4, "of something else")

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2.1 < 5.4 - 7)

print("3 + 2.1 is", 3 + 2.1)
print("5.4 - 7 is", 5.4 - 7)

print("Oh, that's why it's False.")
```

#### Exercise {#sec:in_operator}
There is even an additional comparison operator that tests if something is a part of something else. That operator is called `in`. One use of it is to to test if one string is part of another string. Try this to figure out how it works:

```python
print("Hell" in "Hello world")
print("Hello world" in "Hello world")
print("Hello world" in "Hell")
print("lo wo" in "Hello world")
print("Artichoke" in "Hello world")
```

#### Exercise {#sec:chocolatebars}
Say the supermarket has chocolate bars for 7 kr. Write a small Python program (in a file called chocolate.py) that prints how many chocolate bars you can get for your 30 kr. You should run it like this;

For example, it could output something like this:

```zsh
$ python chocolate.py
```

to have it print something like this:

```
I can buy 4.285714285714286 chocolate bars!
```

#### Exercise
We mentioned a special operator called *modulo*. Google it you do not remember what it does. How about *integer division*. Explain both to a fellow student (or to yourself out loud).

#### Exercise
You obviously cannot go buy 4.3 chocolate bars in a store. You will have to settle for 4. Can you change the program you made in @sec:chocolatebars to print the number of bars you can actually buy, and the change you then have left? Use the modulo and integer division operators. Somthing like:

```
I can buy 4 chocolate bars leaving me with 2 kr in change
```

#### Exercise
What happens if you try to run the following program?

```python
print( 1 / 0 )
```

If you get an error? What kind of error? Why do you think you get that error? Does it make sense?

#### Exercise {#sec:pythagoras}
You have probably know the Pythagorean theorem for computing the hypotenuse (the longest side) of a right-angled triangle. The Pythagorean theorem looks like this: $a^2 + b^2 = c^2$. Here $c$ is the length of the hypotenuse and $a$ and $b$ are the lengths of the two legs of the triangle. So if we have a triangle where $a = 5$ and $b = 2$ and we want to find $c^2$ we can do this in Python:

```python
print("The squared length of the hypotenuse is:", 5**2 + 2**2)
```

#### Exercise
However, we are rarely interested in the *squared* length of the hypotenuse. Can you modify the code you wrote in @sec:pythagoras so you compute $c$ instead of $c^2$? Taking the square root of a number is the same as taking that number and exponentiating it to 0.5, so the square root of $x$ is $x^{0.5}$. Do you know of a Python operator that does exponentiation?


## Logic {-}

Now you know how to use the comparison operstors to produce a `True` or `False` value. There are three additional operators that lets you express more elaborate “True/False” statements than with the comparison operators alone. These are the *logical* operators: `and`, `or` and `not`.

#### Exercise
Go through the code below and see if you can figure out what each line does. Then write the code into your editor and run it to see what actually happens. 

```python
print(2 < 3)
print(10 < 12)
print(8 > 100)
print(2 < 3 and 10 < 12)
print(8 > 100 and 2 < 3)
print(8 > 100 or 2 < 3)
print(not 8 > 100 and 2 < 3)
print(not 8 > 100 and not 2 > 3)
```

Did it do what you expected? Can you explain each line?

#### Exercise {#sec:trueish_falseish}
When exposed to the operators `and`, `or` and `not`, some values are considered true and others are considered false. What happens when you put `not` in front of someting that is considered true or false? Decide what you think and why before you write the code and try it out.

```python
print(not True)
print(not False)
print(not 0)
print(not -4)
print(not 0.0000000)
print(not 3.14159265359)
print(not "apple")
print(not "")
```

From the code above, try to find out which values Python considers true and which it considers false. Can you come up with a rule?

#### Exercise {#sec:and_rules}
The logical operator `and` takes two values (the one to the left of the operator and the one to the right) and figures out whether *both* the left and the right expression is true. It actually boils down to this:

| Left expression | Right expression | Result  |
|------------|-------------|---------|
| `True`     | `True`      | `True`  |
| `True`     | `False`     | `False` |
| `False`    | `True`      | `False` |
| `False`    | `False`     | `False` |

Write some code to confirm that the table above is correct using Python. For example, to test the first case, do this:

```python
print(True and True)
```

#### Exercise
Python will not do any more work than absolutely necessary to find out if a logical expression is true or not. That means that, if the value left of `and` is considered false by Python, then there is no reason look at the right value, since it is already established that they are not *both* considered true. In this case the expression reduces to the *left* value. I.e. `False and True` reduces to `False`.

If the value left of `and` is considered *true* by Python, then Python needs to look at the right value too to establish if they are *both* considered true. In this case the expression reduces to the value on the *right*. I.e. `True and False` reduces to `False`. 

A rule-of-thumb is that the whole expression reduces to the last value that Python needs to consider to decide if the whole expression is true or flase. Use that rationale to explain to yourself how the two last combinations in @sec:and_rules are evaluated.


#### Exercise {#sec:or_rules}
Like the `and` operator, the `or` operator also takes two values. However, the `or` operator tries to figure out whether *one* of the two values are true. Thus, the `or` operator boils down to this:

| Left expression | Right expression | Result  |
|------------|-------------|---------|
| `True`     | `True`      | `True`  |
| `True`     | `False`     | `True`  |
| `False`    | `True`      | `True`  |
| `False`    | `False`     | `False` |

Write some code to confirm that the table above is correct using Python. For example, to test the first case, do this:

```python
print(True or True)
```

#### Exercise {#sec:logic_rule_of_thumb}
As with the `and` operator, Python will not do any more work than absolutely necessary when evaluating an expression with 'or'. So if the value left of `or` is considered true by Python, then there is no reason look at the right value, since it is already established that at least *one* of them are considered true. In this case the expression reduces to the *left* value. I.e. `True or False` reduces to `True`.

If the value left of `or` is considered *false* by Python, then Python stil needs to look at the right value to establish if at least one of them are considered true. In this case the expression reduces to the *right* value. I.e. `False or True` reduces to `True`.

Again, the whole expression reduces to the last value that Python needs to consider to decide if the whole expression is true or flase. Use that same rationale to explain to yourself how the two last combinations in @sec:or_rules are evaluated.

#### Exercise
Remember what you learned in @sec:trueish_falseish about which values are considered true and which are considered false. Combine that with what you learned in @sec:and_rules and @sec:or_rules about what logical expressions reduce to and see if you can figure out what is printed below and why. Use the rule-of-thumb from @sec:logic_rule_of_thumb. Decide what you think before you write the code and try it out. 

```python
print(True and 4)
print(0 and 7)
print(-27 and 0.5)
print(42 and 0)
print("apple" and "orange")
print("apple" and "")
print(42 or 0)
print("apple" and "")
print("apple" or "")
```

If you where surprised what was printed, maybe go back and have a look at @sec:and_rules and @sec:or_rules again.

#### Exercise
Recall the `in` operator from @sec:in_operator? There is also an operator called `not in`. I guess you can imagine what that tests. Try it out.


## Variables {-}

> By now you probably feel the first signs of brain-overload. If you do not take breaks, your brain may overheat and explode - we have seen that happen. One of the nice things about the brain is that it works when you rest. Archiving and understanding a lot of new information takes time, and force-feeding your brain will not help. The last part of this chapter is very important so now might be a good time for a good long break.

This section is about *variables* and this is where the fun begins. A variable is basically a way of assigning a name to a value. `8700000` is just a value, but if we assign a name to it then it gets a special meaning:

```python
number_of_species = 8700000
print(number_of_species)
```

In this case, the variable `number_of_species` represents the [estimated number of eukaryotic species on the planet](http://www.nature.com/news/2011/110823/full/news.2011.498.html), which is 8700000. So `8700000` is the *value* and "number_of_species" is the variable name. Write the code above into a file and run it. Notice how this lets us refer to the *value* using the *variable name*. What appears in the terminal when you do that? do you see `number_of_species` or `8700000`? 

As you can see in the small program above, one of two different things happens when a variable name appears in Python code:

- **Assignment:** When a variable name appears to the left of an equals sign, then a value is assigned to the variable. This is what happens in the first line where `number_of_species` is *assigned* the value `8700000`.
- **Substitution:** In all other contexts, the variable is substituted for its value. This is what happens in the second line where Python *substitutes* the variable name `number_of_species` for its value `8700000` and then prints that.

That is basically it, but let us take the example a bit further and create another variable that we assign the value `1200000` to. That is the number of species discovered so far. Now, lets add this to the program and use it to compute the number of species we have yet to identify. Start by reading the code below super carefully. Remember that a variable is *either* assigned a value or substituted for the value it represents. For each occurrence of the variables below, determine if they are being assigned a value or if they are substituted for their value.

```python
number_of_species = 8700000
number_discovered = 1200000
number_unidentified = number_of_species - number_discovered
print(number_unidentified)
```

Now write the code into a file and run it. Take some time to let it sink in that variables are extremely useful for two reasons:

1. Variables give meaning to a value. Without the variable name, the value 1200000 could just as well be the number of people that lives in Copenhagen. However, by giving the value a meaningful name, it becomes clear what the value is meant to represent.
2. We can assign new values to variables (that is why they are called *variables*). That way we can change the value of `number_discovered` as new species are discovered.

Your variable names can be pretty much anything, but they have to start with a letter or an underscore (`_`) and the rest of the name has to be either letters, numbers or underscores. Just to be clear: a space is *not* any of those things, so do not use spaces in variable names. Above all, be careful in your choice of variable names. Variable names are case sensitive, meaning that `count` and `Count` are two different variables. Stick to lower case variable names. That makes your code easier to read.

#### Exercise
For each occurrence of the variables below, determine if they are being assigned a value or if they are substituted for their value.

```python
breeding_birds = 4
print(breeding_birds)
breeding_birds = 5
print(breeding_birds)
```

#### Exercise
For each occurrence of the variables below, determine if they are being assigned a value or if they are substituted for their value.

```python
breeding_birds = 4
print(breeding_birds)
breeding_birds = breeding_birds + 1
print(breeding_birds)
```

#### Exercise
What happens if you take the first example in this section swap the two lines? So going from this:

```python
number_of_species = 8700000
print(number_of_species)
```

to this:

```python
print(number_of_species)
number_of_species = 8700000
```

Explain to yourself what happens in each line of each version of the program. What kind of error do you get with version two and why? Remember Oath 2!

#### Exercise
Write the following code in a file, save it and run it.

```python
income = 45000
taxpercentage = 0.43
tax_amount = tax_percentage * income
income_after_tax = income - tax_amount
print('Income after tax is', income_after_tax)
```

You should get an error that looks at lot like this one:

```plain
Traceback (most recent call last):
  File "tax.py", line 3, in <module>
    tax_amount = tax_percentage * income
NameError: name 'tax_percentage' is not defined
```

It says that the error is on line 3. Can you figure out what is wrong? Hopefully, you will now appreciate how much attention to detail is required when programming. Every tiny, little symbol or character in your code is *essential*.

## Different types of values {-}

By now you probably have a pretty good idea about what a value in Python is. So far you have seen text like `'Banana'`, integers like `7` and numbers with a fractional part like `4.25`.

In Python, a text value is a *type* of value called a *string* which Python denotes `str` (abbreviation for "string"). So `'Banana'` is a string, and so is `'Banana split'`.  There are two types of numbers in Python. Integers (like 7, 42, and 3) are called `int`. Numbers with a fractional part (like 3.1254 and 4.0) are that are called `float` (abbreviation for "floating-point number").

As I mentioned earlier, `True` and `False` are Python values too. They are called booleans or `bool`, named after an English mathematician called [George Boole](https://en.wikipedia.org/wiki/George_Boole) famous for his work on logic.

So the different *types* of values we know so far are:

| Name           | Type in Python | Examples           |
|----------------|----------------|--------------------|
| String         | `str`          | `"hello"`, `'9'` |             
| Integer        | `int`          | `0`, `2721`, `9`   |             
| Floating-point | `float`        | `1.0`, `4.4322`    |             
| Boolean        | `bool`         | `True`, `False`    |             
| None           | `NoneType`     | `None`             |         

In case you did not notice, I added a special type at the end that can only have the value `None`. I may sound a little weird, but in programming, we sometimes need a value that represents nothing, or `None`. For now, just make a mental note that `None` is also a Python value.

When you do computations in Python it is no problem to mix integers and floating-point numbers. Try this:

```python
print("What is 0.5 * 2?", 0.5 * 2)
print("What is 3 / 2?", 3 / 2)
```

As you can see we can also make computations using only integers that result in floating-point numbers. 

Some of the math operators not only work on numbers, they also work on strings. That way you can add two strings together. It is no longer math of course - but quite handy.

```python
fruit = 'Ba' + 'na' + 'na'
print(fruit)
```

#### Exercise
If you try to combine different types of values in ways that are not allowed in Python, you will get an error. Try each of the following weird calculations in turn, and read the each error message carefully.

```python
x = 3 - '1.5'
print(x)
```

```python
x = None - 4
print(x)
```

#### Exercise
Write these two examples and compare the resulting values of `x`

```python
x = '9' + '4'
print(x)
```

```python
x = 9 + 4
print(x)
```

#### Exercise
Try these two examples. What happens in each case? Does it make sense?

```python
x = '72' * 3
```

```python
x = '72' * '3'
```

#### Exercise
Will this work? Use what you have learned from the other exercises and try to predict what will happen here. Then write the code and try it out.

```python
x = 'Ba' + 'na' * 2
print(x)
```

#### Exercise {#sec:type_conversion}
Sometimes you may need to change a string to a number. You can do that like this:

```python
some_value = "42"
other_value = int(some_value)
```

Write some code that converts strings to numbers and numbers to strings. Remember that numeric values are either integers or floats. Use `int`, `float` as in the example above. You will notice that only meaningful conversions work. E.g. this will not work: `number = int('four')`. To convert a number to a string you can use `str`


Having completed the above exercises you should take note of the following four important points:
 
1. All Python values have a type. So far you know about strings, integers, floating-points, and booleans.
2. Math operators let you do cool things like concatenating two strings by adding them together.
3. The flip side of that cool coin is that Python will assume you know what you are doing if you add two strings (`'4' + '4'` is `'44'` *not* `8`) or multiply a string with an integer (`'4' * 4` is `'4444'` *not* `16`).
4. You can change the type of a value. E.g `'4'` to `4` or `1` to `1.0`.
4. Python will throw a `TypeError` if you try to combine types values of values in ways that are not allowed.

> **Escape characters:** An escape character is a backslash `\` followed by a single character. In Python, the most commonly used ones are `\n` and `\t`.

#### Exercise
What do you think is printed here?

```python
main_course = 'Duck a la Banana\n'
dessert = 'Banana split\n'
menu = main_course + dessert
print(menu)
```

Can you figure out what the special character `\n` represents?

#### Exercise
What do you think is printed here?

```python

dish_one = 'Banana\t\tsplit'
dish_two = 'Chocolate\tcake'
print(dish_one)
print(dish_two)
```

Can you figure out what the special character `\t` represents?

## Mixed exercises {-}

Each chapter in the book ends with a set of mixed exercises that are ment to give you an opportunity to combine what you have learned so far. In this case, they are meant to train your familiarity with the following topics:

- Strings
- Math
- Logic
- Types of values
- Variables

#### Exercise
What happens if you try to run the following program?

```python
print("What happens now?", 1 / )
```

If you get an error, why do you think you get that error?

#### Exercise
What happens if you try to run the following program?

```python
print("What happens now?", 1 / 3
```

If you get an error, why do you think you get that error? Can you fix it? (Hint: EOF is short for End Of File)

#### Exercise
Determine, for each or the eight occurrences of the variable `x` below, where it is being assigned a value and when it is substituted for its value:

```python
x = 1
x = x + 1
x = x + 1
x = x + 1
print(x)
```

Then figure out what is printed and why (remember oath 2). What value does `x` represent at each occurrence in the code?

#### Exercise
Some comparison operators also work with strings. Consider this code:

```python
print("apples" == "pears")
```

What is printed here? Write the code and see for yourself once you think you know. If you were wrong, make sure you understand why.

#### Exercise
Consider this code:

```python
print('aaaaaa' < 'b')
print('a' < 'b')
print('aa' < 'ab')
print('99' > '100')
print('four bananas' > 'one banana')
```

What is printed here? Write the code and see for yourself once you think you know. By what rule does Python decide if one string is smaller than an other? If you have looked something up in an encyclopedia recently, you may have a clue. Also try to google "ASCII table".

#### Exercise
Consider this code:

```python
print('banana' < 'Banana')
```

What is printed here? Write the code and see for yourself once you think you know.

#### Exercise
Do you think it is allowed to use relational operators on values of different types?  Try these out and see for yourself:

```python
print('Banana' > 4)
```

```python
print('42' == 43) # this one is dangerous...
```

```python
print(4 in '1234')
```

Practice reading this kind of error (`TypeError`).

#### Exercise
Can you use the `in` operator to test if this mini gene is part of the DNA string?

```python
mini_gene = 'ATGTAG'
dna_string = 'GCTATGTAGGTA'
```

#### Exercise
Say you have two strings `"4"` and `"2"`. What happens if you add them like this: ``"4" + "2"``. Can you convert each one to integers so you get `6` when you add them? (have a look at 
@sec:type_conversion if you do not remember).

#### Exercise
What happens if you run this code? Do you get an error? Do you remember why?

```python
1value = 42
```

#### Exercise
What happens if you run this code?

```python
print('Hi')
print('Hi')
print('Hi')
```

Compare to what happens when you run this code:

```python
print('Hi\nHi\nHi')
```

Do you remember what `\n` represents? What does it tell about what is added at the end every time you print something?

#### Exercise
Make three exerices for your fellow students. See if you can make them so they test the understanding of (almost) all you have learned so far.

