# Testing your code {#sec:testing_your_code}

*This chapter is about how you figure out if the code you wrote actually solves the problem in the way you intended. You will be surprised how often that is not the case -- even for seasoned programmers.*

## Why test your code?  {.unnumbered}

There are tons of reasons why you should test your code. Here are what I think are the two most important ones:

1. **Makes you think:** Testing forces you to slow down and think about exactly what the code is supposed to do. By deciding what tests to do before you start coding, you try to anticipate errors and cases that are not covered by the way you want to solve the problem at hand. The notion of falsification is important in science and in coding too. The idea is that you should try to prove that your idea is wrong and only consider it valid only if this process fails. So testing motivates you to think about ways to break their code, thereby helping you solve your programming problem in a way that is general and robust so that it does exactly what you expect it to do.
2. **Gives you peace of mind:** Testing increases your confidence that a function you have written actually works as it is supposed to so that you can now stop thinking about how it is implemented and focus on using it as a component in solving a larger problem. Having set up a series of tests also allows you to change and improve the implementation of your function without having to worry that it stops working they way it is supposed to. As long as it passes all the tests is should be ok.

Testing of code is a *big* thing in programming. Professional consistently test their code. In time you will too, but in this course, you will only do the very basic testing yourself. Instead, you will have access to readymade testing suites made especially for each of your programming projects.

## Basic testing  {.unnumbered}

Say that you are asked to make a function that takes a string argument and returns `True` if that string is a palindrome and `False` otherwise (hypothetical example). Then you start thinking about which strings should make the function should return `True` and which should return `False`. Once you have defined you `is_palindrome` function you can set up some fairly obvious tests like this:

```python
print(is_palindome('123321') == True)
print(is_palindome('ATGGTA') == True)
print(is_palindome('ATGATG') == False)
print(is_palindome('XY') == False)
```

But if you keep thinking, maybe you come up with more tests to cover all the different types of cases you may encounter:

```python
print(is_palindome('12321') == True) # uneven length
print(is_palindome('121') == True) # uneven length
print(is_palindome('AA') == True)
print(is_palindome('A') == True) # single char
```

## The project testing utility  {.unnumbered}

To keep you focused on the programming part, each of the programming projects that you will do in this course comes with a ready-made suite of tests of the functions you are asked to implement. So for each function, you can run tests to make sure it implements the behaviour it is supposed to.

Each project comes with two files that you download from the course page. They have their names for a good reason, so do not change them. In the first project about translating DNA, they are called `translationproject.py` and `test_translationproject.py`.  

To be able to test your functions, you *must* write your code in the file called `translationproject.py`. To run your code you type this in the Terminal as usual:

```zsh
python translationproject.py
```

To test the functions as you complete each one, you can run the test script `test_translationproject.py` like this:

```zsh
python test_translationproject.py
```

The code in `test_translationproject.py` reads your code in `translationproject.py` and performs a series of tests of each function. When you run the test script four things may happen depending on the state of your code:

**Case 1:** If you did not yet implement all the functions, the test script will remind you (once for each test) that you did not implement the functions with the names required.

```
*********************************************************
ATTENTION! The following functions are not defined:

	translate_codon
	split_codons
	translate_orf

These functions are either not correctly named (spelled)
or not defined at all. They will be marked as FAILED.
Check your spelling if this is not what you intend.
*********************************************************

Ran 16 tests in 0.000s

OK (skipped=14)
```

If you have implemented a function but misspelled its name, you will also get this type of reminder. The reminders are meant as a safeguard to ensure that you do not hand in the assignment with missing or misspelled function definitions.

**Case 2:** If a test for one the functions you have written fails, the testing is aborted and the script prints some information to help you understand what the problem could be. Say you wrote the function `translate_codon` wrongly so that it always returns `M` for some reason:

```python
def translate_codon(codon):
    return 'M' # crazy
```

then you would get this message:

```
FAILED TEST CASE: test_translate_codon_2

MESSAGE:
    The call:

        translate_codon('TAA')

    returned:

        'M'

    However, it should return:

        '*'

======================================================================
Ran 4 tests in 0.001s

FAILED (failures=1)
```

It is now left to you to figure out why your function returns the wrong value when called with these arguments.

**Case 3:** If you defined all functions correctly and they all work the way they are supposed to, then the test script just prints:

```
Ran 14 tests in 0.140s

OK
```

