
# Course tools

## Wax on, wax off {-}

> Mr. Miyagi: First, wash all car. Then wax. Wax on...
> 
> Daniel: Hey, why do I have to...?
> 
> Mr. Miyagi: Ah ah! Remember deal! No questions!
> 
> Daniel:
> Yeah, but...
> 
> Mr. Miyagi: Hai! Wax on, right hand. Wax off, left hand. Wax on, wax off. Breathe in through nose, out of mouth. Wax on, wax off. Don't forget to breathe, very important. [walks away, still making circular motions with hands] Wax on... wax off. Wax on... wax off.

Seeing the sequence of substitutions and reductions in a Python expression will become natural over time. Until it does, you are in troubled waters, and if you do not practice in time, you may only realize this too late. Considering how simple this is to practice and how crucial it is to your progress, I have written a small companion program called `myiagi` where you can train this particular skill daily. The program is installed in the conda environment you created for this source, so make sure it is activated as described. To run the program, you execute this command in the terminal:

```
myiagi
```
 
![Visual Studio Code (VScode)](./images/myiagi.png){#fig:myiagi width=80%}

It should look like [@fig:myiagi], and the simple game is as follows. The program generates a Python expression. From that expression, it then performs all the substitution and reduction steps. Each substitution or reduction results in an intermediate expression until only a single Python value remains. Here is an example where the expression is `4 * y + x` and the value it reduces to is `37`:

```python
1.   4 * y + x
2.   4 * 8 + x
3.   24 + x
4.   24 + 13
5.   37
```

You do not know what values the `y` and `x` variables point to, but you can deduce it from the sequence of expressions that they are `24` and `13`. In the game, you are given a series of numbered expressions in the wrong order like this:

```python
1.   4 * y + x
2.   37
3.   4 * 8 + x
4.   24 + x
5.   24 + 13
```
 
Your task is to put them in the right order so that the original expression is at the top and the single Python value it reduces to is at the bottom. Now, you might grab line 2 by tabbing `2` on your keyboard (the number turns red so you can see it is active). Then, you move the line using the up/down arrow keys. If you move it to the bottom, the list then looks like this:

```python
1.   4 * y + x
2.   4 * 8 + x
3.   24 + x
4.   24 + 13
5.   37
```

Now, you repeat this process until the order is correct (the program will let you know when it is). The fewer lines you grab to produce the right order, the more points you earn. Problems with longer lists of expressions also earn you more points. As problems become harder and include more aspects of Python, solving them also awards more points. Each week has a score goal to guide your effort. Reaching this goal ensures that you practice as much as you should. Practicing a bit every day daily is more effective than practicing a lot a few days a week. To provide an incentive, the points you earn slowly expire, so the easiest way to maintain your score is to practice a bit every day.


## A helping hand {-}

Using the `myiagi`, you train your ability to read and understand Python expressions. Seeing a similar breakdown of a Python expression in your code may also be helpful. For that purpose, I have written another tool called `print-steps`. Say you have some code like the one below and need clarification on how the single value assigned to z is produced (here, you are probably not).

```python
x = 7
y = 5
z = x * y + 4
```

All you need to do is then to add `# PRINT STEPS` comment to the end of the line like this:

```python
x = 7
y = 5
z = x * y + 4 # PRINT STEPS
```

Say your file is called `myfile.py`, you would normally run the code like this:


```python
python myfile.py
```

But to see the breakdown of expressions marked by `# PRINT STEPS`, you need to run your code with the `print-steps` program instead:

```python
print-steps myfile.py
```

The command prints the following in the terminal:

```txt
Line 4 in test_studentfile.py:
As written:      z = x * y + 4
Substitution:    z = 7 * y + 4
Substitution:    z = 7 * 5 + 4
Reduction:       z = 35 + 4
Reduction:       z = 39
```

You can even mark more than one line like this and have `print-steps` break down all of them for you:

```python
x = 7
y = 5
z = x * y + 4 # PRINT STEPS
k = z * 42 # PRINT STEPS
```

like this:

```txt
Line 3 in myfile.py:
As written:      z = x * y + 4
Substitution:    z = 7 * y + 4
Substitution:    z = 7 * 5 + 4
Reduction:       z = 35 + 4
Reduction:       z = 39

Line 4 in myfile.py:
As written:      k = z * 42
Substitution:    k = 39 * 42
Reduction:       k = 1638
```

However, it would be best if you used this helping hand sparingly. It is much better to train your ability to do this in your head with the help of Mr. Myagi. Trust me, it works.

