# Controlling behavior

*This chapter is about how you make your program do different things under different circumstances. Making functionality dependent on data is what makes programs useful.*

## If-statement {-}

The small programs you have written so far all run the exact same sequence of statements (lines). Imagine if you could control which statements were run depending on the circumstances. Then you would be able to write more flexible and useful programs. Cue the music - and let me introduce: the "if-statement".

Write the following carefully into a file. It is a small program to monitor bus passenger status. Notice the colon ending the if-statements. Also, note that the lines below each if-statement are indented with exactly four spaces. While you write the program, try to figure out what the if-statement does. Then run the code and see what happens.

```python
bus_seats = 32
passengers = 20
bags = 20

print(passengers, "people ride the bus")

if bus_seats >= passengers + bags:
    print("Smiles, everyone has room for bags")

if bus_seats >= passengers:
    print('Everyone gets to sit down, no complaints')

if bus_seats < passengers:
    print('Some passengers standing, annoyed')
    
if bus_seats < passengers / 3:
    print("General dissatisfaction, some swearing too")
```

Try to change the values of `bus_seats`, `passengers` and `bags` and see how execution of the program changes.

You have probably realized that the if-statements control which print-statements that are evaluated. A statement nested under an if-statement is only evaluated if the expression between the `if` keyword and the `:` reduces to a value Python considers as *true*. This does not happen if the expression between the `if` and `:` reduces to a value Python considers *false*. 

Remind yourself that when asked to evaluate something as true or false, Python will interpret zero and empty values (like `0` and `''`) as `False` and all other non-zero and non-empty values as `True`.

#### Exercise
Which of the following letters are printed: A, B, C, D, E, F, G. Make up your mind before you write and run the code.

```python
if 0:
    print('A')

if "Banana":
    print('B')

if 3.14159265359:
    print('C')

if False:
    print('D')

if 9 > 5 and 4 < 7:
    print('E')

if '':
    print('F')

if False or "banana":
    print('G')
```

#### Exercise
What happens if you forget to write the `:` in the if-statement?

```python
if 4 > 2
    print('Hi!')
```

#### Exercise
What happens if you do not indent the code under the if-statement?

```python
if 4 > 2:
print('Hi!')
```

> By now you have probably know that your text editor is intelligent when it comes to indentation. If you hit Enter after a statement ending with `:`, it will indent the next line with four spaces. Also, if you use the tab in python code, it will produce four spaces for you.

### FAQ {-}

| **Q:** Isn't "If" a poem by Rudyard Kipling?
| **A:** [Yes.](https://www.poetryfoundation.org/poems-and-poets/poems/detail/46473)

## Else-statement {-}

Sometimes you not only want your program to do something if an expression reduces to `True`, you also want it to do something *else* if it is `False`. It is as simple as it looks:

```python
cookies = 3

if cookies > 0:
    print("Uh, I wonder if we have some milk too...")
else:
    print("Sigh!")
```

Remember to put a `:` after the `else` keyword. Write the code and change the value of `cookies` to `0`.

#### Exercise
Test your understanding about which expressions that reduce to a `True` or `False` value. Write the code below and then see how it responds to different values of `x`. Try to come up with other variations yourself.

```python
x = 0.0
# x = '0'
# x = '   '
# x = ''
# x = not 0
# x = 'zero'

if x:
    print('x is substituted with True in the if-statement')
else:
    print('x is substituted with False in the if-statement')
```

### FAQ {-}

| **Q:** Isn't "Else" a poem by Rudyard Kipling?
| **A:** No.

#### Exercise {#sec:nested_if_else}
What do you think this code prints? Notice how you can nest if and else-statements under other if and else-statements. This way you can make your program only include some statements when certain combinations of conditions are met. Just remember that the code below each `if` or `else` is indented by four spaces. Try to change the True/False values of `milk` and `cookies`.

```python
milk = False
cookies = True
if milk:
    if cookies:
        status = 'Good times!'
    else:
        status = 'Not thirsty, thanks or asking'
else:
    if cookies:
        status = 'How does something like this happen?'
    else:
        status = 'Whatever...'
        
print(status)
```


## Blocks of code {-}

In the examples above, some lines are indented more than others, and you probably already have some idea of how this is interpreted by Python. Indentation defines blocks of code. Whether each block of code is evaluated when your code runs, is controlled by the `if` and `else` statements. The following three rules define individual blocks of code:

1. All statements in a block of code have the *same indentation*. That is, they line up vertically. 
2. A block of code *begins* at the first line of code at a line that is indented more than the one before it.
3. A block *ends* when it is followed by a line that is less indented, or at the last line of code.

This way, a block can be nested inside another block by indenting it further to the right as shown in [@fig:blocks]. Compare the example in [@fig:blocks] to the code example above. Note how a colon at the end of a statement means "this applies the block of code below". Make sure you understand which print statements that are controlled by which `if` and `else` statements.

![The amount of indentation defines blocks of code](./images/blocks.png){#fig:blocks}

## Elif-statement {-}

Say you need to test a number of mutually exclusive scenarios. E.g. if a base is equal to A, T, C or G. You can do that like in the example below, but it is very verbose and shifts your code further and further to the right. 

```python
base = 'G'

if base == 'A':
    print('This is adenine')
else:
    if base == 'T':
        print('This is thymine')
    else:
        if base == 'C':
            print('This is cytosine')
        else:
            print('This is guanine')
```

This is where an `elif` statement can be helpful. It is basically short for "else if". If you compare to the example below the correspondence is hopefully obvious.

```python
base = 'G'

if base == 'A':
    print('This is adenine')
elif base == 'T':
    print('This is thymine')
elif base == 'C':
    print('This is cytosine')
else:
    print('This is guanine')
```

Here we put an else-statement at the end to capture all cases not covered by the if-statement and the two elif-statements.

#### Exercise
You can use logical operators (`and`, `or`, `not`) in the expressions tested in an if-statement. Can you change the program from @sec:nested_if_else so that there are no nested if-statements - in a way so the program still does exactly the same? You can use `if`, `elif` and `else` and test if e.g. both `milk` and `cookies` are true using `and`.

#### Exercise
In the snippet of code below there are three blocks with three statements in each. Which statements belong to which block? Which statements are executed?

```python
x = 5
if x > 4:
    y = 3
    if x < 1:
        x = 2
        y = 7
        z = 1
    x = 1
z = 4
```

#### Exercise
Can you see four blocks of code? If not, read the three rules above again. Which statements are executed?

```python
x = 5
if x > 4:
    y = 3
    if x < 1:
        x = 2
        y = 7
    else:
        x = 1
        y = 9
z = 4
```


## General exercises {-}

#### Exercise
Will this print `You are a super star!`?

```python
if -4 and 0 or 'banana' and not False:
    print("You are a super star!")
```

#### Exercise
Will this print `You are a super star!`?

```python
if -1 + 16 % 5 == 0 :
    print("You are a super star!")
```

#### Exercise
Assign values to two variables `x` and `y`. Then write some code that prints `OK` if and only if `x` is smaller than five *and* `y` is larger than five. Do it using *two* `if` statements:

```python
x = 3 # or someting else
y = 7 # or someting else

# rest of code here...
```

Now solve the same problem using only *one* `if` statement.

#### Exercise
Assign values to two variables `x` and `y`. Then write some code that prints `OK` if and only if `x` is smaller than five *or* `y` is larger than five. Do it using *two* `if` statements:

```python
x = 3 # or someting else
7 = 7 # or someting else

# rest of code here...
```

Now solve the same problem using only *one* `if` statement and *one* `elif` statement.

#### Exercise
Assign values to two variables `x` and `y`. Then write some code that prints `OK` if either `x` or `y` is zero, but not if both are zero (this is tricky one).

```python
x = 3 # or someting else
y = 7 # or someting else

# rest of code here...
```

#### Exercise
Which value of `x` makes the code below print Banana?

```python
x = 
s = ''
if x**2 == 16:
    s = s + 'Ba'
if x + 6 == 2:
    s = s + 'na'
if 7 == x - 3:
    s = 'na' * 2
else:
    s = s + 'na'
print(s)
```

<!-- #### Exercise
Say you have two values represented by the variables `x` and `y`. Now you want to assign the largest of those two values to a third value `z`. Can you see that the two pieces of code below are essentially two ways of expressing the same thing? (You will need to define `x` and `y` yourself, and print `z` to see its value.) This is a tricky one, but it trains both variables, assignment, operators, precedence, substitution, reduction, logic, control flow. Make sure you are aware of how.

```python
if x > y:
    z = x
else:
    z = y
```

```python
z = x > y and x or y
``` -->

#### Exercise
Make three exercises that requires the knowledge of programming so far. Have your fellow students solve them.
