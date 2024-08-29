# Writing a program

*Lets get you started...*

## Hello World {-}

Dive in and make your first program. Begin by creating a new file in your editor (*VScode*) and save it as `hello.py`. The `.py` suffix tells your editor that this file contains Python code. As you will see, this makes your life a whole lot easier. Such a file with Python code is usually called a *script*, but we can also call it a program.

Now write *exactly* this in the file (`hello.py`):

```python
print("Hello world")
```

Your editor will color your code a little differently, but that is not important. Save your file with the added code, and you have your first program! Of course, there is not much point in having a program if it just sits there on your computer. To run your program, do the following:

1. Open the terminal and navigate to the folder (directory) where you saved `hello.py`. Use the `cd` command to do so. If you do not remember how, go back and read the previous chapter again.
2. Type `python hello.py` in the terminal and hit Enter.

You should see something like [@fig:hello_world].

![Hello world](./images/helloworld.png){#fig:hello_world}

This is where you shout "it's alive!", toss your head back and do the insane scientist laugh.

Okay, what just happened? You wrote a program by creating a file in which you wrote one line of code. You then ran the program using Python and it wrote (printed) `Hello world` in the terminal. Do not worry about the parentheses and quotes for now and just enjoy your new life as a programmer.

Maybe you wonder why we write `print` and not `write` or something else? That actually goes all the way back to the days when computers were big clunky things with no screens attached. They could only interact with the user by *printing* out things on a real physical paper printer. Back then, the output you now see on the screen was printed onto a piece of paper that the programmer could then look at. These days print shows up in the terminal, but the story should help you remember that `print` spits text *out of your program* just like a printer.

Now try to add another line of code like this:

```python
print("Hello world")
print("I am your first program")
```

Save the file and run it again by typing `python hello.py` in your terminal and hit Enter.

You should see this:

```
Hello world
I am your first program
```

Now your program first prints `Hello world` and *then* it prints `I am your first program`. The *then*-part is important. That is how a Python program works. Python (the `python` you write in front of `hello.py`) reads your `hello.py` file and then executes the code, one line after another until it reaches the end of the file.

This is essential, so read that paragraph again. Now read it once more. It may seem trivial, but it is absolutely fundamental always to remember that this is how Python runs your code. So here is oath 2:

> **Oath 2:** I swear always to remember that each line of code in my script is executed one after another, starting from the first line in the script and ending at the last line.

When you write Python code, you always follow this workflow:

1. Change the code in the file.
2. Save the file.
3. Execute the code in the file using the terminal.
4. Start over.

Make sure you get the hang of this in the following exercises.

**Important:** The examples and exercises in this course are designed to work if you execute your scripts from the folder they are stored in. So you must navigate into the relevant folder before you execute your script. If your script is called `hello.py`, you must *always* execute it exactly like this: `python hello.py`. On some computers it is possible to just type `hello.py` without `python` in front of it. Do *not* do that. Also, do *not* "drag" the script file into the Terminal either.

#### Exercise
Try to swap the two lines of code in the file and run the program again. What does it print now?

#### Exercise
Try to make the program print a greeting to yourself. Something like this:

```
Hello Sarah!
```

&ndash; if your name is Sarah, of course.

#### Exercise
Add more lines of code to your program to make it print something else. Can you make your program print the same thing ten times?

## Error Messages {-}

Did you get everything just right with your first program or did you get error messages when you executed your code with `python`? Maybe you wrote the following code (adding an extra closing parenthesis):

```python
print("Hello world"))
```

&ndash; and then got an error like this:

```
  File "hello.py", line 1
    print('Hello world'))
                        ^
SyntaxError: invalid syntax
```

This is Python's way of telling you that the `hello.py` script has an error in line 1. If you write something that does not conform to the proper syntax for Python code then you will get a `SyntaxError`. Python will do its best to figure out where the problem is and point to it with a `^` character.

You will see many such error messages in your new life as a programmer. So it is important that you practice reading them. At first, they will be hard to decipher, but once you get used to them, they will help you quickly identify where the problem is. If there is an error message that you do not understand the internet is your friend. Just paste the error message into Google's search field, and you will see that you are not the only one out there getting started on Python programming. It is okay if you do not know how to fix the problem right now, but it is essential to remember that these error messages are Pythons way of helping you understand what you did wrong. 

#### Exercise
Try to break your new shiny program and make it produce an error message when you run it. An easy way of doing this is to remove or change random characters from the program. If you run this (with a missing end-parenthesis:

```python
print("Hello world"
print("I am your first program")
```

You will get this error

```
  File "hello.py", line 2
    print("I am your first program")
        ^
SyntaxError: invalid syntax
````

The `^` character tells you when your code stopped making sense to Python. Some times that is a bit after where you made your mistake. 

Try to make other kinds of errors. Which error messages do you see? Do you see the same error message every time, or are they different? Try googling the error messages you get. Can you figure out why the change you made broke the program? How many different error messages can you produce?


## Strings {-}

In programs, text values are called *strings*, and you have already used strings a lot in your first program. A string is simply a piece of text, but we call it a string because it is a "string of characters". In Python, we represent a string like this:

```python
"this is a string"
```

or like this:

```python
'Hello world'
```

That is, we take the text we wish to use as our value, and we put quotes around it. We are allowed to use either double quotes (the first example) or single quotes (the second example). We can mix them like this:

```python
print('this is "some text" with a quotes')
```

   -- but not like this:

```python
print("this is a broken string')
```

Can you see why, and how it is handy to have both single and double quotes? Well, if we did not have both, we could not have text with quotes in it. You just need to remember to use the same kind of quotes at each end of the string. Running the latter example gives an error message telling you that Python cannot find the quote that was supposed to end the string:

```
  File "broken.py", line 1
    print("this is a broken string')
                                   ^
SyntaxError: EOL while scanning string literal
```

It is Python's way of saying: "I got to the end of the line (EOL) without finding an matching end quote".

## Comments {-}
You have already learnt that Python reads and executes one line of code at a time until your program has no more lines of code.

However, we can make a line invisible to Python by putting a `#` symbol in front of it, like this:

```python
# print("Hello world")
print("Greetings from your first program")
```

When you do that, Python simply does not read that line. It is not part of the program. Run the program again. You will notice that now only the second line is part of your program:

```
$ python hello.py
Greetings from your first program
```

This is useful in two ways:

1. It lets you disable certain lines of your code, by keeping Python from reading them. For example, you may want to see what happens if that line of code was not executed to understand how your program works.
2. It allows you to write notes in your code Python to help you remember how your code works.

Lines with a `#` in front are called "comments" because we normally use them to write comments about the code we write. If you ask for help about some problem, you will often hear your instructor say: try to "comment out" line two. When your instructor says that, it simply means that you should add a `#` in front of line two to see what then happens.

#### Exercise
What happens if I put a `#` in the middle of a line of code?
Try it out!

#### Exercise
Try this:

```python
# Note to self: the lines below print stuff
print("Hello world")
print("Greetings from your first program")
```
#### Exercise
Try this:

```python
print("Hello world") # actually, everything after a # is ignored
print("Greetings from your first program")
```

What did yo learn? Which parts of each line are considered part of the program?

#### Exercise
Now try this:

```python
print("Hello # world")
print("Greetings from your first program")
```

What did you learn about `#` characters in strings?
#### Exercise
Try this:

```python
print("Hello world"#)
print("Greetings from your first program")
```

Did you expect this to work? Why? Why not? What error message did you get?


