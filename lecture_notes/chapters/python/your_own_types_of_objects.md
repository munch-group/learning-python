# Your type of object

*Do you know that type you are? Python objects do, and this chapter is about how they know.*

## What defines the type of an object? {-}

By now, you know that Python values are objects and that there are different *types* of objects. Strings have type `str`, integers have type `int` and lists have type `list`, just to mention a few of the ones we know. Remember that you can use the built-in `type` function to find out what type an object is. Try this:

```python
print( type('banana') )
print( type(4) )
print( type([]) )
```

And as you already know, objects are "data with associated functionality". Some of this functionality is available in the form of *methods*: For example, the `upper` and `split` methods of string objects, or the `append` and `extend` methods of lists. 

Objects also behave sensibly in different contexts: When if you sum two integers (`4 + 6`) you get their sum `6`, but if you sum two strings (`'ban' + 'ana'`) you get concatenation of the two strings `'banana'`. The two different types of objects each know how to act with the `+` operator. Another example is iteration: If you iterate over a string, you get one character at time in order, but if you iterate over a dictionary, you get the keys in the dictionary (in random order). This super convenient context-aware behaviour, is, in fact, also defined as methods, but more about that below.

Each object carries its own data: different numbers, different stings etc., but their *functionality* is shared by all objects of the same type. So all string objects refer to the same definition of the `upper` and `split` methods in the string *type* as graphically illustrated in figure @fig:objects_and_type.

![Objects and type. Each object carries its own data, but refers to the type for a definition of its methods.](./images/objects_and_type.png){#fig:objects_and_type width=50%}


## Making your own objects {-}

Imagine if you could create your own types of objects, carrying a particular kind of data and functionality. "Data" can litterally represent anything. It bioinformatics it could be an open reading frame, a patient profile, or a tree. Fortunately Python lets us do this using something called *classes*. New kinds of objects and the functionality they provide are defined by classes. So by defining a new class you define a new type of object, and the methods you define in that class are available to objects of the type that particular kind (type). 

Lets define a new class, `Point`, that represents a point in a two-dimentional coordinate system. Each such point has an x-value and a y-value as shown in @fig:points, so we need our new point object to hold two numbers representing those two values.

![Points](./images/points.png){#fig:points width=60%}

Here is how we define the `Point` class:

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Let us beak it down: We use the keyword `class` followed by the name of class we define. Nested under that statemet we can put a  -->

<!-- $$f(x) = f(x-1)$$ {#eq:some_other_label} -->


<!-- TODO: Finish chapter about classes -->
