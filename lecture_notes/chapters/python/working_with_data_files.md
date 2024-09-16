# Working with data files

*This chapter covers the bare necessities of how to make your program read data from a file on your computer and how to make it create a file that it can write results to.*

## Writing files  {.unnumbered}

To interact with a file on your harddisk you need to know the name of the file and whether you want to write to it or read from it. Then you can use the builtin function `open` to create a file object that lets you read or write to that file. The `open` function takes two arguments: The first is a string, which gives the name of the file. The second argument is also a string and should be `'w'` for "write" if you want to write to the file or `'r'` for "read" if you want to read from the file. To keep things simple we will assume that the file you want to open is always in the same folder (directory) as the Python script that calls the `open` function.

#### Exercise {#sec:write_to_file}
Try to write the code below and run it:

```python
f = open('workfile.txt', 'w')
f.write("First line\n")
f.write("Second line\n")
f.close()
```

Now open the `workfile.txt` in *VScode* and see what is in it now. It should contain:

```zsh
First line
Second line
```

Lets break down what happened:

1. You used the `open` builtin function to open a file called "workfile.txt" in *writing* mode using the `'w'` as the second argument.
2. You then wrote the string `"First line\n"`  to the file using the `write` method of the file object.
3. You wrote another string `"Second line\n"`  to the file using the `write` method of the file object.
4. You closed the file using the `close` method of the file object.

Note that if you open a file for writing, a file with that name is created. If a file of that name already exist, it is overwritten.

#### Exercise
Close workfile.txt in *VScode* again and change your program above to this (removing the `\n` characters):

```python
f = open('workfile.txt', 'w')
f.write("First line")
f.write("Second line")
f.close()
```

What do you think the content of workfile.txt is now? Decide before you open workfile.txt in *VScode* again and have a look. What do you think the `\n` character represents?

#### Exercise
Close workfile.txt in *VScode* and change your program above to this:

```python
f = open('workfile.txt', 'w')
f.write("First line\nSecond line\n")
f.close()
```

Can you see how that is equivalent to what you did before? Open workfile.txt in *VScode* again and have a look.

#### Exercise {#sec:write_to_file_with_print}
You can also make `print` write to a file instead of the terminal. That way your output ends up in the file instead of the terminal. To make print write to a file, you need to use the `file` keyword argument to give print the file object that represents the file you want to write to (`file=f` below). Try to write the code below and run it:

```python
f = open('workfile.txt', 'w')
print("First line", file=f)
print("Second line, file=f")
f.close()
```

Compare the the code to that in @sec:write_to_file. Notice how  the strings we print do end with a newline. This is because the default behaviour for `print` is to add a newline to the end of what it prints - just like when you print to the terminal.

## Reading files  {.unnumbered}

When you want to read a from an existing file you give the `open` function the name of that file and specify `'r'` for reading as second argument. If the file you name does not exist, Python will tell you that it does not exist (it is nice like that). Before you head into the next rest of this section make sure you redo @sec:write_to_file so the content of workfile.txt is:

```zsh
First line
Second line
```

#### Exercise {#sec:read_from_file}

```python
f = open('workfile.txt', 'r')
file_content = f.read()
print(file_content)
f.close()
```

Lets break down what happened:

1. You used the `open` builtin function to open a file called workfile.txt in *reading* mode using the `'r'` as the second argument.
2. You then read the content of the file using the `read` method, which return the contents as a string.
3. You printed the string. 
4. You closed the file using the `close` method of the file object.

#### Exercise 
Try to read from the file after you close it:

```python    
f = open('workfile', 'r')
f.close()
file_content = f.read()
```

Do you get an error? Which one? Do you understand why?

#### Exercise 
You can use the `readline` method to read one line at a time. What do you think happens if you run this code:

```python
f = open('workfile.txt', 'r')
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)
```

Once you decide, try it out. What is printed in the last print statement? The thing is, the file object keeps track of how much of the file it has read. Once it is at the end you can read as much as you like -- there is nothing left. If you want to start reading from the top of the file you can close and open the file again. Try to insert the following two statements at various places in the code above and see what happens?

```python
f.close()
f = open('workfile.txt', 'r')
```

#### Exercise
Look at the code below and figure out for yourself what it does:

```python
input_file = open('workfile.txt', 'r')
output_file = open('results.txt', 'w')

for line in input_file:
    line = line.upper()
    output_file.write(line)
```

Then run it and open results.txt in *VScode* and see what it produced.

Were you surprised that the file object can be an iterator in a for-loop? Just like stings can iterate over characters, lists can iterate over values and dictionaries can iterate over keys, file objects can iterate over the lines in the file.

Try to modify your code to use the `print` function instead of the `write` method (see @sec:write_to_file_with_print).


## General exercises  {.unnumbered}

#### Exercise
Write a function `read_file` that takes the name of a file as argument. The file should read the content of the file and return it. Like:

```python
content_of_file = read_file('some_file.txt')
```

#### Exercise
Write a function that takes the name of two files as arguments. The file should read the content of the first file and write it to the second file.

```python
copy_file('some_file.txt', 'other_file.txt')
```



