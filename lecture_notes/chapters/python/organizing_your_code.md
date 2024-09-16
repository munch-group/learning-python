# Organising your code {.unnumbered}

*This chapter is about how you can organize your code into chunks that you can call upon to perform a well defined tasks in your program.*

## Functions  {.unnumbered}

Buckle down for the most powerful and useful thing in programming. Functions! Functions serve as mini-programs that perform small well-defined tasks in your program. 

I have started to write a song about functions:

```python
print("Functions are super, Functions are cool")
print("When writing a program they are a great tool")
print("La la dim du da da di")
print("Skubi dubi dumdi di")
print("Bing di dubi dum da di")

print("Functions are used to package some code")
print("They are not so strange that your head will explode")
print("La la dim du da da di")
print("Skubi dubi dumdi di")
print("Bing di dubi dum da di")
```

I am going to add a lot more verses and I do not want to have to write the entire chorus every time. So what would be more natural than to make a function named `chorus` that takes care of that for us? That way we can write our song the way lyrics with a chorus are usually written:

```python
def chorus():
    line1 = "La la dim du da da di"
    line2 = "Skubi dubi dumdi di"
    line3 = "Bing di dubi dum da di"
    return line1 + '\n' + line2 + '\n' + line3

print("Functions are super, Functions are cool")
print("When writing a program they are a great tool")
print( chorus() )

print("Functions are useful to wrap up some code")
print("They are not so strange that your head will explode")
print( chorus() )
```

First, let us break down the function definition in the top part of this code:

1. We *define* a function with the `def` keyword (which is short for “define” in case you wonder).
2. After `def` we write the name of the function. We call the function `chorus`. We could name it something else, but like good variable names, good function names can help you remember what your code does.
3. After the name you put two parentheses, `()`.
4. Then a colon, `:`.
5. The statements that are part of the function are nested under the `def` statement and are indented with four spaces exactly like we do under if-statements.
4. The return-statement ends the function. The expression after the `return` keyword reduces to a *value* that the function then returns.

When Python runs this code, each line is executed one by one starting from the first line (remember oath two?). So in this case python first executes the *definition* of the `chorus` function. The only thing that has happened after Python has executed the first five lines of code is that it has assigned the name `chorus` to the four indented statements. So Python now "knows" about the `chorus` function (like it "knows" about a variable `x` after we do `x = 4`).

To *use* the function, we "call" it by writing its name followed by parentheses: `chorus()`. When it comes to functions, "use", "call" and "run" means the same thing. As you can see, we call the function twice in the rest of the code. Each time we do, the following happens:

1. When a function is *called*, each statement in the definition is executed one after the other. If you look at the function definition, you can see that our `chorus` function has four statements.
2. The first statement assigns a string value to the variable `line1`.
3. The second statement assigns a string value to the variable `line2`.
4. The third statement assigns a string value to the variable `line3`.
5. The fourth statement is a return-statement. The expression after the `return` keyword in the final statement reduces to a *value* and this value is what the function call is substituted for. In this case, that value is the following string:

```python
"La la dim du da da di\nSkubi dubi dumdi di\nBing di dubi dum da di"
```

So the key properties of functions are:

- A function names a piece of code (some statements) just like variables name values like strings and numbers.
- We call a function by writing the function name followed by parentheses: `chorus()`. Just writing the function name will not call the function.
- When a function is *called* it is substituted by the *value* that the function *returns* -- exactly like a variable in an expression is substituted by its value. It is absolutely crucial that you remember this.

#### Exercise
Now that we have a `chorus` function, that part is out of the way and we can concentrate on our song without having to worry about remembering how many "la la"s it has and so on. Try to change the "lyrics" in the chorus a little bit. Notice how you only need to make the change in one place to change all the choruses in the song -- cool right? Without the function, you would have to rely on correctly changing the code in many different places.

#### Exercise
Try to delete the return-statement in the `chorus` function (the last line in the function) and run the code again. You should see something like this:

```
Functions are super, Functions are cool
When writing a program they are a great tool
None
Functions are used to wrap up some code
They are not so strange that your head will explode
None
```

It seems that the function call (`chorus()`) is now substituted with `None`. How can that be when we did not return anything? The reason is that when you do not specify a `return` statement the function returns `None` by default. This is to honour the rule that variables and a function calls are substituted by a value, and `None` is simply the value that Python uses to represent "nothing". `None` is basically a value denoting the lack of value. As you just saw it is used to represent that no value is returned from a function. It can also be assigned to a variable as a placeholder value until another value is assigned:

```python
x = None
x = 4
```
Also, `None` is considered false in a logical context:

```python
print(not None)
```
 

#### Exercise
Try this variant to the chorus function. Go through the code *slowly* and repeat all the steps in the breakdown of what happens when a function is called. Remember to also do each substitution and reduction carefully.

```python
def chorus():
    line1 = 'La la'
    line2 = 'Du bi du'
    return line1 + '\n' + line2
```    

Do the same for this variant:

```python
def chorus():
    line1 = 'La la'
    line2 = 'Du bi du'
    chrous_text = line1 + '\n' + line2
    return chrorus_text
```

and for this variant:

```python
def chorus():
    return "La la\nDu bi du"
```

#### Exercise
What do you think happens if you move the definition of `chorus` to the bottom of your file? Decide what you think will happen and why (maybe you remember what happens when you try to use a variable in an expression before you have defined it?). Then try it out.

```python
print("Functions are super, Functions are cool")
print("When writing a program they are a great tool")
print( chorus() )

print("Functions are useful to wrap up some code")
print("They are not so strange that your head will explode")
print( chorus() )

def chorus():
    line1 = "La la dim du da da di"
    line2 = "Skubi dubi dumdi di"
    line3 = "Bing di dubi dum da di"
    return line1 + '\n' + line2 + '\n' + line3
```

Make sure you understand how the error you get relates to the way Python runs your script (remember oath two?). If you still do not understand, do the next exercise and then return to this one.

#### Exercise
Which error do you get here and why? How is that similar to the the error in the previous exericse?

```python
print(x)
x = 7
```

#### Exercise
Consider the code below. Do all the substitution and reduction steps in your head. Remember that each function call is substituted by the value that the function returns. Then run it.

```python
def lucky_number():
    return 7

x = lucky_number()
y = lucky_number()
twice_as_lucky = x + y
print(twice_as_lucky)
```

Now change the code to that below. The code makes the same computation but in fewer steps. Do all the substitution and reduction steps again.

```python
def lucky_number():
    return 7

twice_as_lucky = lucky_number() + lucky_number()
print(twice_as_lucky)
```

Now change the code to that below. The code makes the same computation but in fewer steps. Do all the substitution and reduction steps again.

```python
def lucky_number():
    return 7

print(lucky_number() + lucky_number())
```        


## Functions can take arguments  {.unnumbered}

The functions we have written so far are not very flexible because they return the same thing every time they are called. Now write and run this beauty:

```python
def square(number):
    squared_number = number**2
    return squared_number 

result = square(3)
print(result)
```

Notice how we put a variable (`number`) between parentheses in the function *definition*. This variable is assigned the value that we put between the parentheses (`3`) when we *call* the function. So when we call the function like this: `square(3)` -- then this implicitly happens inside the function: `number = 3`.

Here is another example:

```python
def divide(numerator, denominator):
    result = numerator / denominator 
    return result

division_result = divide(44, 77)
print(division_result)
```

When the function call `divide(44, 77)`, these two things implicitly happen: `numerator = 44` and `denominator = 77`.

Take note of the following three important points:
1. The *values* that we pass to the function in the function call (like `3`, `44` and `77`) are called *arguments*. It is crucial to remember that it is *values* and not variables that are passed to functions.
2. The *variables* in the definition line of a function, like `number`, `numerator` and `denominator`, are called *parameters*. They hold the *values* passed to the function when it is called (the arguments).
3. You can define functions with any number of *parameters* as long as you use the same number of *arguments* when you call the function.

#### Exercise
Try to call your `divide` function like this `divide(77, 44)`. What does it return and what do you learn from that? Does the order of arguments and parameters correspond?

#### Exercise
Try to call your `divide` function like this `divide(44)`. Do you get an error, and what do you learn from that?

#### Exercise
Try to call your `divide` function like this `divide(44, 77, 33)`. Do you get a different error message, and what do you learn from that?

#### Exercise
Read this code and do all substitution and reduction steps from beginning to end.

```python
def square(x):
    return x ** 2

result = square(9) + square(5)
print("The result is:", result)
```

Now replace the line `return x ** 2` with `print(x ** 2)`. What is printed now? and why?

#### Exercise
As described above, a `return` statement ends the function by producing the value that replaces the function call. If a function has more than one `return` statement, then the function ends when the first one is executed.

```python
def assess_number(x):
    if x < 3:
        return 'quite a few'
    if x < 100:
        return 'a lot'
    return 'a whole lot'

nr_apples = 2
print(nr_apples, "apples is", assess_number(nr_apples))
```

What happens when x is 2, 3, 50, 200? Think about it first.


## Functions and variables  {.unnumbered}

A function call is temporary little world only exists from the function is *called* and until it *returns* its value. It did not exist *before* the function was called and it does not exist *after* the function returns its value. By necessity, the variables defined in your function are also temporary. 

This means that variables defined inside a function are private to each function call. It also means that variables defined inside functions are not available to code *outside* the function. Running the following example in should help you understand this:

```python
def make_greeting():
    greeting = 'Guten tag'
    name = 'Heinz' 
    message = greeting + " " + name
    return message

greeting = 'Buongiorno'
name = 'Giovanni'
print( make_greeting() )
print(greeting + " " + name)
```

Notice how Heinz and Giovanni are greated in their native languages. This means that the variable definitions inside the function does not overwrite the Italian versions already defined outside the function. This is because the variables defined in the function are temporary and private to the function, even if they have the same names as variables outside the function. This is why the function call `make_greeting()` in the `print` statement does not change the values of the variables that are printed in the last line.

Now try to "comment out" the line `greeting = 'Guten tag'` and run the example again. All of a sudden Heinz is greeted in Italian! The reason is that now Python cannot find a definition of `greeting` inside the function. It then looks outside the function for a definition and finds the Italian version. 

Now try to "comment out" the line `greeting = 'Buongiorno'` and run the example again. You get an error, but which one? Python complains that it cannot find a definition of `greeting`. The reason is that once the last print statement is executed the small world of the function call in the previous line no longer exists.

You should learn two rules from the above example:

1. All variables that you define inside a function are *private* to the function. If a variable in a function has the same name as a variable in the main script (like `greeting` above) then these are two *separate* variables that just happen to have the same name.
2. When you use a variable like `greeting` in the function (E.g. `message = greeting + " " + name`), then Python checks if the variables have been defined in the function. If that is not the case, then it will look for it outside the function. In the above example, it finds `name` in the function and `greeting` outside the function. It is good practice to make your functions "self-contained", in the sense that Python should not have to look outside the function for variables.


#### Exercise

Try this version of the example above. Now `name` is defined as a function parameter, but is it still a function variable just like `greeting`.

```python
def make_greeting(name):
    greeting = "Guten tag"
    message = greeting + " " + name
    return message

greeting = 'Buongiorno'
name = 'Giovanni'
print( make_greeting("Heinz") )
print(greeting + " " + name)
```

#### Exercise
Consider the following example:

```python
def double(z):
    return z * 2
   
x = 7
result = double(x)
print(result)
```

When the function is called (`double(x)`) the x is substituted by its value `7`. That *value* is passed as the argument and assigned to the function parameter `z` (`z = 7`). `z` is a private function variable and does not exist before or after the function call. Does this change in any way if we use the variable name `x` instead of `z` like below?

```python
def double(x):
    return x * 2
   
x = 7
result = double(x)
print(result)
```

Do *all* substations and reductions for each line of code from top to bottom. Keep the sequence of events in mind and remember that a function definition is merely a template describing a mini-world that is created anew everytime the function is called.


## Builtin functions  {.unnumbered}

So far we have only talked about functions you write yourself, but Python also has built-in functions that are already available to you. They work just like a function you would write yourself. You already know the `print` function quite well, and that is an example of a function that prints something but returns `None`. There are many other useful builtin function, but for now, I will just tell you about another two: Those are `len` and `type`. 

#### Exercise {#sec:type_and_len}
Try these examples:

```python
x = 'Banana'
print("The value of variable x is of type", type(x))
print("The value of variable x has length", len(x))
```

As you can see, `type` returns the type of the value passed as the argument, and `len` returns the length of the value passed as the argument. The `type` function is handy in case you wonder what type a value has, but it is not a function we will use in this course. The `len` function, however, is your new best friend. You will see why soon enough.

#### Exercise
Try to change the value of the `x` in @sec:type_and_len to an integer or a float and see what happens when you run it. Do you get an error? Does it make sense that not all types of values can meaningfully be said to have a length?

#### Exercise
What happens if you pass an empty string (`""`) as the argument to the `len` function?

#### Exercise

What is printed here? Think about it first and then try it out. Remember to do the substitution and reduction steps.

```python
return_value = print("Hello world")
print(return_value)
```

#### Exercise

What is printed here? Think about it first and then try it out. Remember to do the substitution and reduction steps.

```python
print(print("Hello world"))
```


## General exercises  {.unnumbered}

The following exercises treat the areas we have worked on in this and previous chapters. They are meant to train your familiarity with if-statements and functions. Remember that the purpose of the exercises is not to answer the questions but to train the chain of thought that *allows* you to answer them. Play around with the code for each example and see what happens if you change it a bit.

#### Exercise
Consider this function definition that takes a single number as the argument:

```python
def square(n):
    return n**2
```

What does it do? What does it return? What number does `square(2)` then represent?

Below I have used it in some expressions that are printed. Make sure you understand what each expression evaluates to. Do the explicit substitutions and reductions on paper before you run it. Remember that we substitute a function call (like `square(2)`) for the value it returns, just like we substitute a variable `x` for the value it points to.

```python
print(square(3))
print(square(2 + 1))
print(square(2) * 2 + square(3))
print(square(square(2)))
print(square(2 * square(1) + 2))
```

#### Exercise
What does this function do? How many parameters does it have? How many statements does the function have? What does the function print? Which value does it return? 

```python
def power(a, b):
    print("This function computes {}**{}".format(a, b))
    return a**b

print(power(4, 2))
```

Try (possibly strange) variations of the code like the ones below to better understand the contribution of each line of code. What is the difference between return and print?
What happens when the Python gets to a `return` statement in a function? What happens when the function does not have a `return` statement?

Variation 1:

```python
def power(a, b):
    print("This computes", a, "to the power of", b)
    print(a**b)

result = power(4, 2)
print(result)
```

Variation 2:

```python
def power(a, b):
    print("This computes", a, "to the power of", b)
    return a**b

result = power(4, 2)
print(result)
```

Variation 3:

```python
def power(a, b):
    print("This computes", a, "to the power of", b)
    a**b

print(power(4, 2))
```

Variation 4:

```python
def power(a, b):
    return a**b
    print("This computes", a, "to the power of", b)

print(power(4, 2))
```

#### Exercise
Define a function called `diff`, with two parameters, `x` and `y`. The function must return the difference between the values of `x` and `y`.

```python
Example:
def diff(x, y):
    ...

diff(8, 2) # should return 6
diff(-1, 2) # should return -3
```

Save the value returned from the function in a variable. Then test if the function works correctly by comparing the result to what you know is the true difference (using `==`).

#### Exercise
Define a function called `all_equal` that takes five arguments and returns `True` if all five arguments have the same value and `False` otherwise. The function should work with any input, for example:

```python
all_equal("Can", "Can", "Can", "Can", "Can")
all_equal(0, 0, 0, 0, 0)
all_equal(0.5, 0.5, 0.5, 0.5, 0.5)
all_equal(True, True, True, True, True)
```

Hint: You test equality with `a == b`. Now think back to what you learned about logic. Which operator can you use to test if `a == b` *and* `b == c`?

#### Exercise {#sec:is_even}
Define a function called `is_even` which takes one argument and returns `True` if (and only if) this is an even number and `False` otherwise (remember the modulo operator?).

```python
is_even(8) # should return True
is_even(3) # should return False
```

#### Exercise
Define a function called `is_odd` which takes one argument and returns `True` if (and only if) the argument is an odd number and `False` otherwise.

```python
is_odd(8) # should return False
is_odd(3) # should return True
```

Can you use the `is_even` you defined in @sec:is_even to complete this exercise? How? Why is that a good idea?

#### Exercise {#sec:none_eval_false}
Here is a function that should return `True` if given an uppercase (English) vowel, and `False` otherwise:

```python
def is_uppercase_vowel(c):
    c == 'A' or c == 'E' or c == I or c == 'O' or c == 'U'
    
char = 'A' 
if is_uppercase_vowel(char):
    print(char, "is an uppercase vowel")
else:
    print(char, "is NOT an uppercase vowel")
```

Now type the code exactly as shown and run it. Do you get what you expect? Does the code work? If not, try to figure out why. Try print the value that the function returns. Does that give you any hints about the cause of the problem?

#### Exercise {#sec:is_nucleotide_symbol}
Define a function called `is_nucleotide_symbol` which takes one argument and returns `True` if this is either A, C, G, T, a, c, g or t, and `False` in any other case.

Name your parameter something sensible like `symbol`.

```python
is_nucleotide_symbol("A") # should return True
is_nucleotide_symbol("B") # should return False
is_nucleotide_symbol("Mogens") # should return False
is_nucleotide_symbol("") # should return False
```

#### Exercise
Define a function called `is_base_pair` which takes two parameters, `base1`, `base2`, and returns `True` if `base2` is the complementary of `base1`, and `False` otherwise.

```python
is_base_pair("A", "G") # should return False
is_base_pair("A", "T") # should return True
is_base_pair("T", "A") # should return True
is_base_pair("Preben", "A") # should return False
```

#### Exercise
Did you find the bug in @sec:none_eval_false? You were supposed to find that the function did not have a return value. This makes the function return `None` by default. Do you think the `None` value is considered true or false in an if-statement?

#### Exercise
Define a function called `celcius2fahrenheit` that converts from celsius to Fahrenheit. You can do this because you know the linear relationship between the two. On @fig:figureX you can see that the slope is `9 / 5` and the intercept is `32`. The function should have one parameter `celsius`. Inside the function, you should define the variables `slope` and `intercept` and give them the appropriate values. Then you can calculate the conversion to Celcius using these variables and return the result.

![Temperature conversion](./images/temperature.png){#fig:figureX width=75%}

#### Exercise
Try to change your conversion function so it takes three arguments, corresponding to celsius, slope and intercept so you can call it like this to convert 27 degrees celsius: `conversion(37, 9 / 5, 32)`. Now you have a function that can do any linear conversion that you can put inside another function like this:

```python
def celcius2fahrenheit(celsius):
    return conversion(celsius, 9 / 5, 32)
```

#### Exercise
Now try to extend this to a different problem: It has been found that the height and weight of a person are related by a linear equation with slope = 0.55 and intercept = -25. Define a function called `predict_weight` which takes just one argument, the height of a person, and returns the estimated weight of the person.

#### Exercise
By now you know that some of the words in your code have specific purposes. `def` defines functions, `return` returns value from a function, `and` is a logical operator etc. Here is a list of the ones you will see in this course: `and`, `assert`, `break`, `continue` `def`, `del`, `elif`, `else`, `False`,    `for`, `from`, `if`, `import`, `in`, `is`, `not`, `or`, `pass`, `return`, `while`, `True`, `None` (you can see a full list [here](https://docs.python.org/3.0/reference/lexical_analysis.html#id8))

These words are reserved for their special purposes in Python and you will not be allowed to assign values to them. Try this to see for yourself:

```python
None = 4
```

or this:

```python
and = 2
```


### FAQ - Frequently Asked Questions  {.unnumbered}

| **Q:** Can function names be anything?
| **A:** Just about. The rules that apply to variable names also apply to function names. Good function names are lower case with  underscores (`_`) to separate words, like in the examples above.









