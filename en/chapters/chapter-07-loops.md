\pagebreak

# Loops and Iteration

Let's talk a bit about loops in Python, and say a few words about iteration as well. What it is, why it exists, and who needs it. We'll discuss different types of loops: `for` (the step loop), `while` (the regular loop), iteration, and iterable objects.

But what does all of this actually mean?

Loops are a programming concept used to execute a piece of code a specified number of times. Imagine you need to process 10 elements from an array. You need to perform some operations on each of them. Let's say these operations aren't just one line but complex processing. Actually, let's just take multiplication for our example. Now what?

A naive solution would look like this:

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> elements[0] *= 2
>>> elements[1] *= 2
>>> elements[2] *= 2
(...)
>>> elements[9] *= 2
```

Nightmare. Now imagine there are more elements. For example, a million, because that's how many users you have. You can't edit that manually unless you hire a finite number of interns. Still, it would take an incredibly long time. And this is exactly where loops come to the rescue.

## The For Loop

### Brief Overview

Let's start with something called a for loop (or step loop). This is a loop that allows you to "walk through" the elements of a given object and enables you to process each element step by step. The `for` keyword allows you to iterate over elements of an iterable object.

### Iterable Objects

What is an iterable object? It's an object that, when passed to the `iter()` function, returns an iterator. And an iterator is something you call `next()` on. You've already seen several examples of iterable objects: Lists, Dicts, Tuples.

These are objects that have the `__iter__` method implemented, followed by `__next__`. In short, the programmer told Python how to get successive elements from a given object/structure and it returns an iterator object.

In lists, dicts, and tuples, this is provided by default as part of the language. If you create specialized classes yourself, you can also make them iterable by implementing this method. Simply put, it's something you can iterate over.

To iterate means to go through the elements of a given structure step by step. Clear? Hopefully. If not, google it or look at the code below.

How does this look in practice? Let's modify our example from above.

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for index, element in enumerate(elements):
...     elements[index] *= 2
...
>>> elements
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

Instead of a million lines, we have two. Pretty cool, right? But wait, what's this magical `enumerate` function? It's a built-in Python function that allows you to number the elements of a given object. Simply put, it's a wrapper around your object, like a list, that returns each element along with its index.

The whole thing, translated into plain instructions, looks like this:

1. Take the object elements. Elements is a list.
2. Pass the elements object as an argument to the enumerate function.
3. The enumerate function returns a new object. This object returns successive elements of the original object with an index attached to them.

Then when we have this newly returned object, the for loop kicks in and gets to work:

1. Take the newly returned object.
2. Under the hood, call `__iter__()`, which returns an iterator for this list, unless we already have an iterator passed.
3. Call `next()` with the obtained iterator as an argument.
4. Next returns the next element that the iterator has to give.
5. When there are no more elements, the iterator raises a StopIteration exception, which is the correct behavior for iterators that have no more elements to return.

```python
>>> l = elements.__iter__()
>>> next(l)
2
>>> next(l)
4
>>> next(l)
6
>>> next(l)
8
>>> next(l)
10
>>> next(l)
12
>>> next(l)
14
>>>
>>> next(l)
16
>>> next(l)
18
>>>
>>> next(l)
20
>>> next(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

This is what it looks like in practice, and this is more or less what happens under the hood when we use a for loop and iterate over a given object. In short, as I mentioned, we simply go through all elements step by step, getting each individual element at our disposal and being able to process it in some way.

This has many applications, and the for loop is everyday bread in Python. You'll see it many more times. Get comfortable with it because it will probably become your friend.

## The While Loop

### Brief Overview

The regular loop, as I call it, is simply the `while` loop. While the for loop executes by going through elements of a given iterable object, the `while` loop executes as long as a given condition is true. A concept somewhat similar to the for loop, but slightly different.

### Examples of Loop Usage

```python
counter = 0
while True:
    counter += 1
    if counter >= 10:
        break
```

And that's about it. The rest is for independent analysis.

## Comprehensions

Comprehensions are nothing more than a kind of syntactic sugar that makes it possible to describe certain common behaviors in Python more concisely. These behaviors relate to for loops and using them to create new objects, lists, tuples, etc.

Example of how to use comprehensions:

```python
list_comprehension = [x for x in range(10)]
dict_comprehension = {x: x**2 for x in range(10)}
set_comprehension = {x for x in range(10)}
set_comprehension_variation = set(x for x in range(10))
tuple_comprehension = tuple(x for x in range(10) if x % 2)
```

Read a bit more and experiment on your own. Remember that comprehensions can be nested, meaning you can have a list comprehension made from a list comprehension. Inception.

I'll just add that I personally like to format longer list comprehensions in the following way:

```python
list_comprehension = [
    value
    for value in range(10)
    if value % 2
]
```

Three lines, with each element on its own line. If the comprehension is short, I don't do this, but for more complex ones, I do. In my opinion, it improves readability.

## Generators

Since we're talking about loops and iteration, let me mention generators. What are they?

Generally, these are functions that `yield` something instead of returning it. What does this mean in practice and why would you need it?

In simple terms, sometimes we have datasets that are too large to load into RAM all at once, because RAM is finite - large, but finite and limited. What do you do then? A generator is one strategy for dealing with such a situation. Generators allow us to process large datasets step by step.

Under the hood, generators are basically ordinary loops wrapped in functions that `yield` a value. What does this mean? Instead of returning a given element and ending execution, the generator yields the value, "saves" or "remembers" its current state, and waits for a signal to return the next element. In the meantime, we can process and do something with those values.

Generators can work on finite sets or can be infinite. Many variations.

```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
for i in infinite_sequence():
    print(i, end=" ")
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39 40 41 42
[...]
6157818 6157819 6157820 6157821 6157822 6157823 6157824 6157825 6157826 6157827
6157828 6157829 6157830 6157831 6157832 6157833 6157834 6157835 6157836 6157837
6157838 6157839 6157840 6157841 6157842
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

Generators also have the characteristic of being single-use. This means that once initialized, a generator can only be traversed once. This, plus the fact that we don't load data into memory all at once, is the main difference between generators and traditional lists or tuples.

## Walrus Operator

Since Python 3.8, we have access to something called the Walrus operator or the assignment expression operator. It allows us to assign variables not only in statements but also in expressions, using the operator `NAME := expr`.

Okay, but what does this mean in practice? Let's look at some code.

```python
data = None
if our_function_getting_json(some_arg) is not None:
    data = our_function_getting_json(some_arg)
    data.do_stuff()
```

Pretty simple to understand, reasonable, right? An example taken from some code. An ugly example. The above code sucks in this context. How could it be improved?

```python
data = our_function_getting_json(some_arg)
if data is not None:
    data.do_stuff()
```

We can do something like this, but is this the shortest it can be, the best it can be? Currently, probably yes, but...

It would be nice if you could declare that variable right there in the if statement - simply save the function result where it's originally used. This is important when you want to later perform some operations on the result of an expression that you executed, for example in a condition, but because you currently can't save variables in expressions, you have to save it yourself, earlier. Whether in loops, list comprehensions, lambda functions, or others.

Unless you use the walrus operator.

```python
if (data := our_function_gettin_json(some_arg)) is not None:
    data.do_stuff()
```

Other examples of usage:

```python
if (match := pattern.search(data)) is not None:
    match.do_stuff()

while (value := read_next_item()) is not None:
    ...

filtered_data = [y for x in data if (y := f(x)) is not None]
results = [(x, y, x/y) for x in input_data if (y := f(x)) > 0]
# or also something like below
stuff = [[y := f(x), x/y] for x in range(5)]
y = y1 := f(x) # ERROR
bar(x = y := f(x)) # ERROR
bar(x = (y := f(x))) # OK
something := 'lalala' # ERROR
something2 = 'hey' # OK
```



## Summary

Loops, generators, list comprehensions, etc. are useful tools for every programmer and the basic building blocks of any code. It's good to be very familiar with them.

## Questions and Exercises

1. Write examples of for and while loops. 3 different ones each.
2. Write an article comparing the for loop with the while loop.
3. Add a comparative analysis of the for loop and comprehensions.
4. Write code that finds the largest and smallest number in a list.
5. Write code that counts words in a given string.
6. Then letters.
7. And the frequency of their occurrence.
8. Check whether there are two numbers on a given list - a and b - whose sum equals a given number.
9. Write code that displays only those numbers from any list (numbers only) that are less than 5.
10. Ask the user for a number and then print all divisors of that number.
11. Get two numbers from the user and then return the square of their sum.
12. Write code that takes a string from the user and then displays the first three letters of that string, one after another, without new lines. E.g., "MelonTusk" -> "MelMelMel"
13. Get a string from the user and then display it in reverse order of letters.
14. Based on the benchmarking code for f-strings from the previous chapter, analyze which is faster: list(), [], or list comprehensions. Each should contain natural numbers from 1 to 10.

\pagebreak
