# The order of events

*This chapter is about how Python interprets (or evaluates) the code you write. It has a few fancy long words that may seem foreign to you. Do not let that throw you off. They are all just fancy names for something very simple.*

## Precedence of Operators  {.unnumbered}

Fear not. Precedence is just a nasty word for something we have already talked about. Precedence simply specifies that some things are done before other things -- or more correctly, that some operations are performed before others. You already know that multiplication is done before addition. Another way of saying that is that multiplication *takes precedence* over addition. The expression below obviously reduces to 7 in two steps: 

$$ 1 + 3 * 2 $$

First, $3 * 2$ reduces to 6 and then $1 + 6$ reduces to 7. If we wanted to add 1 and 3 first we would need to enforce this by adding parentheses:

$$ (1 + 3) * 2 $$

This is because the multiplication operator (`*`) has higher precedence than the addition operator (`+`). Here is the list of the most common operators and their precedence in Python:

| Level   | Category            | Operators                        |
| ------- | ------------------- | -------------------------------- |
| Highest | exponent            | `**`                             |
|         | positive / negative | `+x`, `-x`                       |
|         | multiplication      | `*`, `/`, `//`, `%`              |
|         | addition            | `+`, `-`                         |
|         | relational          | `!=`, `==`, `<=`, `>=`, `<`, `>`, `in`, `not in` |
|         | logical             | `not`                            |
|         | logical             | `and`                            |
| Lowest  | logical             | `or`                             |

Sometimes a statement contains adjacent operators with the same precedence. In this case Python evaluates the expression left to right. I.e. This following expression first reduces to $0.5 * 2$ and then to $1$

```python
2 / 4 * 2
```

The following one first reduces to $1 * 4$ and then to $4$:

```python
2 / 2 * 4
```

If you want Python order the oprations in any other way, you need to use perentheses (E.g. `2 / (2 * 4)`).

#### Exercise
Look at each expression in the exercises below and use the table above to decide if it evaluates to `True` or `False`. Then write the code and test if you were right. If not figure out why.

```python
2 + 4 * 7 == 2 + (4 * 7) 
```

#### Exercise
Does this reduce to `True` or `False`?

```python
4 > 3 and 2 < 1 or 7 > 2
```

#### Exercise
Does this reduce to `True` or `False`?

```python
4 > 3 and (2 < 1 or 7 > 2)
```

#### Exercise
Does this reduce to `True` or `False`?

```python
2 * 4 ** 4 + 1 == (2 * 4) ** (4 + 1)
```


## Statements and Expressions  {.unnumbered}

To be able to talk concisely about programming (and to receive more useful help from your instructors) you need a bit of vocabulary. *Statements* and *expressions* are two such words that you need to know. Distinguishing between statements and expressions will help us talk about the code we write.

- A **statement** is a line of code that performs an action. Python evaluates each statement in turn until it reaches the end of the file (remember oath 2?). `print(y * 7)` is a statement and so is `x = 14`. They each represent a full line of code and they each perform an action.
 
- An **expression** is any piece of code that reduces to one value. `y * 7` is an expression and so is `y * 7 + 14 - x` and `4 > 5`.

We will talk more about how expressions are handled by Python in the next section, but right now it is important that you understand that statements *do something* while expressions are things that reduces to a value. Hopefully, this distinction will be clearer when you have completed the following exercises.

#### Exercise
Did you notice in the above examples that `print(y * 7)` is a statement and `y * 7` is an expression? Yes, expressions can be part of statements. In fact they most often are. Similarly, expressions are often made up of other smaller expressions. E.g. `y * 7` is part of the larger expression `y * 7 + 14 - x`.


Take a look at this code:

```python
x = 5
y = 20
z = (x + y) / 2 + 20
print(z * 2 + 1)
h = 2 * x - 9 * 48
print(h)
```

Write down the code on a piece of paper. Now mark all statements and all expressions. Remember that expression are often made up of smaller expressions, so you can find a *lot* of them. E.g. `(x + y)`, `2 + 20`, and `(x + y) / 2 + 20` are all expressions. In fact, a single variable (like `x`) is also a small expression. Discuss with a fellow student. Do you agree on what find?

#### Exercise
Consider the following code:

```python
greeting = 'Hello' + ' my '
print(greeting + 'friend')
```

How many statements are there in this piece of code? How many expressions?


## Substitution and Reduction  {.unnumbered}

Although *substitution* and *reduction* may not sound like your new best friends, they truly are! If you remember to think about your Python code in terms of substitution and reduction, then programming will make a lot of sense. Understanding and using these simple rules you will allow to read and understand any code. If you do not, you may get by for a while - only to find yourself in big big trouble later when things start to become more complicated. 

You should remember, from the section on variables in the previous chapter, that variables in Python in are *either* assigned a value *or* substituted for the value they represent.

In the first two lines of code below, the variables `x` and `y` are each assigned a value. Now consider the last line in the example:

```python
x = 4
y = 3
z = x * y + 8
```

Here `x` is *substituted* by the value `4` and `y` is *substituted* by the value `3`. So now the expression after the equals sign reads `4 * 3 + 8`. Because we multiply before we add, `4 * 3` *reduces* to `12` so that the expression now reads `12 + 8`. Finally, this *reduces* to the value `20`. The very *last* thing that happens is that the variable `z` is assigned the value `20`.

You should do these steps every time you see an expression. You may think that this is overdoing things a bit, but it is *not*. This kind of explicit thinking is what programming is all about and it will become increasingly important as the course progresses. So make sure you make it a habit while it still seems trivial. Then, over time, it will become second nature.

Now raise your right hand and read the third and last oath out loud: 

> **Oath 3:** I hereby solemnly swear to consciously consider every single substitution and reduction in every Python expression that I read or write from this moment on.

This was the last of the three oaths but it is *by far* the most important one. You can take your hand down now.

**NB:** You may not realize at this point, but the last two subsections are the most important ones in the book. Go back and read them many times as you proceed through the course. If you explicitly think in terms of substitution and reduction you will have no trouble. If you do not, you are entering a mine field with snowshoes on.

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by inserting a `print` statement at the end.

```python
x = 7
y = 4 + x
2 + x * x**2 + y - x
```

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
a = 4
b = a
c = 2
c = a + b + c
```

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
x = 1
x = x
```

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
microsatellite = "GTC" * 41
```

Surprised?

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
mini_gene = "ATG" + "GCG" + "TAA"
```

What did you do first here? Does the order of additions matter? What operations do Python perform first when operators have same precedence? (left to right, or right to left)

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
number = 1 / 1 * 4
```

In what order are reductions made? Does the order of operations matter, and in what order does Python do the reductions?

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
x = 4
y = x + x
```

#### Exercise {#sec:adding_one}
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
x = 4
x = x + 1
```

#### Exercise
Do the substitution and reduction steps with pen and paper, then run it to check yourself by iserting a `print` statement at the end.

```python
x = 4
x += 1
```

Compare the final value of `x` to that in @sec:adding_one. Can you see what `+=` is a short hand for? Nifty, right?


## General exercises  {.unnumbered}

The following exercises are meant to train your familiarity with the topics we have treated so far -- in this case especially:

- Substitution
- Reduction
- Assignment
- Simple precedence rules
- Comparison operators
- Logical operators
- Distinction between text and numbers

Read each exercise and think hard about the questions before you code anything. *Then* write the code and try it out. Remember that it is crucial that you type it in -- as super boring as it may be (remember oath one). This trains your accuracy and attention to detail and it builds programming into your brain. Play around with each bit of code. Make small changes and see how it behaves.

There is a reason why there are lots of questions in this exercise but no answers. You are supposed to find them yourself -- also if it takes you quite a while. That is the way you build understanding. Some of the questions may seem trivial but do them anyway. If you only understand these concepts superficially they will come back and bite you in the ass when things get more complicated.

#### Exercise
Consider this code:

```python
1.2 * 3 + 4 / 5.2
```

What does that expression evaluate to? Try to explicitly make all the reductions on a piece of paper before you write and run the code.

#### Exercise
Consider this code:

```python
1.2 * (3 + 4) / 5.2
```

What does that expression evaluate to? Try to explicitly make all the reductions on a piece of paper before you write and run the code.

#### Exercise
Consider this code:

```python
10 % 3 - 2
```

What does that expression evaluate to? Try to explicitly make all the reductions on a piece of paper before you write and run the code.

#### Exercise
Consider this code:

```python
11 % (7 - 5)**2
```

What does that expression evaluate to? Try to explicitly make all the reductions on a piece of paper before you write and run the code.

#### Exercise
Consider this code:

```python
a = 5
x = 9
banana = 7
x + 4 * a > banana
```

What does the last expression evaluate to? Try to explicitly make all the substitutions and reductions on a piece of paper before you write the code. What happens if you write and run the code? Why?

#### Exercise
Consider this code:

```python
dance = 'can'
dance = dance + dance
print("Do the", dance)
```

What is printed? Try to explicitly make all the substitutions and reductions on a piece of paper before you write the code. What happens if you write and run the code? Why?

#### Exercise
Consider this code:

```python
foo = 30
bar = 50
baz = bar + foo
print(baz)
bar = 10
print(baz)
```

There are two print statements. The first print statement prints `80`. But what about the second print statement? Does that print `80` or `40`? Find out and make sure you understand why it prints what it prints. If not, reread the section on subsitution.

#### Exercise
Consider this code:

```python
1 == '1'
```

and this:

```python
1 == 1.0
```

What does this reduce to? Try to print it and see once you think you know. If you were wrong, make sure you figure out why.

#### Exercise {#sec:string_gotcha1}
Consider this code:

```python
a = '1'
b = '2'
c  = a + b
print(a, b, c)
print(a + b == 3)
```

What is printed here? Write the code and see for yourself once you think you know. If you were wrong, make sure you understand why.

#### Exercise
Consider this code:

```python
a = 1
b = 2
c  = a + b
print(a, b, c)
print(a + b == 3)
```

What is printed here? Compare to @sec:string_gotcha1. Write the code and see for yourself once you think you know. If you were wrong, make sure you understand why.

#### Exercise
Consider this code:

```python
x = 4
print(x + 2 and 7)
print(x + 2 or 7)
x = -2
print(x + 2 and 7)
print(x + 2 or 7)
```

What is printed here? Write the code and see for yourself once you think you know. If you were wrong, make sure you understand why.

#### Exercise {#sec:puzzle)
In the code below I have shuffled the statements. Put them in the right order to make the code print `100`.

```python 
x = x + 4
print(x)
x = x * 5
x = x * x
x = 4
```

#### Exercise
In the code below I have shuffled the statements. Put them in the right order to make the code print the string `"Banana"`.

```python
y = 'n'
x = 'B' + y + x
print(x)
x = 'a'
y = (x + y) * 2
```

#### Exercise
Make a puzzle exericise, like the two previous ones, for a fellow student.

#### Exercise
Remind yourself of the different types of Python values you know. E.g. one of them is integer (`int`). Make a list.

#### Exercise {#sec:type_coercion}

You already know about several types of data values in Python. Two of them are integers called `int`, and decimal numbers (or floating points) called `float`. When you use an operator like `+` or `>` it produces a value. No matter what you put on either side of `>` in it produces a boolean value (`bool`), `True` or `False`. For other operators the type of value produced depends on which values the operator works on. Try this and see if you print an integer or a float (`8` or `8.0`):

```python
x = 4
y = 2
result = x * y
print(result)
```

Now try to replace `4` with `4.0`. What type is result now?. Try to also replace `2` with `2.0`. What type is result now? Can you extract a rule for what the `*` operator produces depending on the what types the two values have?

#### Exercise

In @sec:type_coercion you investigated what types of values the `*` operator produce. Redo that exercise with the operators: `+`, `-`, `/`, `**`, `//`, and `%`. What are the rules for what is returned if both values are integers, one value is a float, or both values are floats?

#### Exercise 

Make a list of all the operators you know so far in order of precedence (without looking in the notes). Then check yourself. 

#### Exercise

What does his expression reduce to and what type of value is it?

```python
3 > 2
```

#### Exercise

What does his expression reduce to and what type of value is it? Do all the reduction steps in your head. 

```python
2 - 4 * 5 - 2 * 1/3
```

#### Exercise

What does his expression reduce to and what type of value is it? Do all the reduction steps in your head. 

```python
3 > 2 and 2 - 4 * 5 - 2 * 9
```

#### Exercise {#sec:oneline_ifelse}
What is printed here and why?:

```python
print(True and "banana" or "orange")
```

Try to change the `True` value to `False` and see what happens. Can you explain it? If not look at @sec:logic_rule_of_thumb again.

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
If you understood @sec:oneline_ifelse, then you should also understand this one:

```python
weather = 'rain'
what_to_do = weather == 'rain' and 'watch movies' or 'go swimming'
print(what_to_do)
```

What happens if you change `'rain'` in the first line to something else (like `'sun'`)?

#### Exercise 

What is the value of `results` once the code below has run? Do the substitutions, reductions, and assignments in your head before you run the code.

```python
x = 7
y = 13
z = x + y
x = 0
result = x + y + z
```

#### Exercise 

What is the value of `results` once the code below has run? Do the substitutions, reductions, and assignments in your head before you run the code.

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

In the code below I have shuffled the statements. Put them in the right order to make the code print `'Mogens'`

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

