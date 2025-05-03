# Loops and Iteration

Let's talk about loops in Python and say a few words about iteration. What it is, what it's for, and who needs it. We'll discuss different types of loops: `for` loops (step-by-step loops), `while` loops (regular loops), and cover iteration and iterable objects.

But what does all this mean?

Loops are a programming concept used to execute some action, some piece of code, a specified number of times. Imagine you need to process 10 elements from an array. You need to perform some operations on each of them. Let's say these operations aren't just one line but complex processing. Actually, let's just take multiplication as an example. So what now?
A naive solution would look like this:

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> elements[0] *= 2
>>> elements[1] *= 2
>>> elements[2] *= 3
(...)
>>> elements[9] *= 3
```

Nightmare. Now think about having more elements. Say a million, because that's how many users you have. You can't edit this manually, unless we hire a finite number of students or outsource it. Still, it would take an incredibly long time. And this is exactly where loops come in to save the day.

## For Loop

### Brief Characteristics

Let's start with what's called a for loop or step-by-step loop. This is a loop that allows us to 'walk through' the elements of a given object and enables us, step by step, or element by element, to process each element. This means that the `for` keyword allows us to iterate over elements of an iterable object.

### Iterable Object

What is an iterable object? It's an object that, when passed to the `iter()` function, returns us an iterator. And an iterator is something we call `next()` on. You've already seen several examples of iterable objects: Lists, Dictionaries, Tuples.

These are objects that have implemented the `__iter__` method and subsequently `__next__`, which in short means the programmer told Python how to take subsequent elements from a given object/structure and which returns an iterator object.

In lists, dicts, tuples, we have this by default as part of the language. If we create our own specialized classes, we can also make them iterable by implementing these methods. So in short, it's something you can iterate over.

To iterate means to go step by step through the elements of a given structure. Clear? Hopefully. If not, Google it or look at the code below.

How does this look in practice? Let's modify our example from above.

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for index, element in enumerate(elements):
...     elements[index] *= 2
...
>>> elements
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

Instead of a million lines, we have two. Nice, right? But wait, what's this magical `enumerate` function? It's a built-in Python function that allows us to number the elements of a given object. In simpler terms, it's a wrapper, an overlay on our given object, like a list, which besides the given element from the object also returns its index.

The whole thing, translated into plain English instructions, looks like this:

1. Take the elements object. Elements is a list.
2. Pass the elements object as an argument to the enumerate function.
3. The enumerate function returns a new object. This object is something that returns us subsequent elements of the original object and attaches an index/number to them.

Then when we have this newly returned object, the for loop comes into play and does its thing.

1. Take the newly returned object
2. Under the hood call `__iter__()`, which will return us an iterator for this list, unless we already have an iterator passed by default
3. Call `next()` with the received iterator as an argument
4. Next will return the next element that the iterator has to pass
5. When there are no more elements, the iterator will raise a StopIteration exception, which is correct behavior for iterators that have no more elements to pass.

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
>>> next(l)
16
>>> next(l)
18
>>> next(l)
20
>>> next(l)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

This is how it looks in practice and this is more or less what happens under the hood when we use a for loop and iterate over a given object. In short, as I wrote, we simply step through all elements, receiving a single element at our disposal and being able to process it in some way.

This has many applications, and the for loop is often daily bread in Python. You'll see it many more times. Get familiar with it quite well, because it will probably be your friend.

## While Loop

### Brief Characteristics

The while loop, as I call it, is simply the `while` loop. While the for loop executes by going through elements of a given iterable object, the while loop executes as long as a given condition is true. The concept is somewhat similar to the for loop, but slightly different.

### Examples of Loop Usage

```python
counter = 0
while True:
    counter += 1
    if counter >= 10:
        break
```

And that's probably it. The rest is for independent analysis.

## Comprehensions

Comprehensions are nothing more than a kind of syntactic sugar that makes certain typical behaviors describable more concisely in Python. These behaviors relate to for loops and using them to create new objects, lists, tuples, etc.

Example of how to use comprehensions:

```python
list_comprehension = [x for x in range(10)]
dict_comprehension = {x: x**2 for x in range(10)}
set_comprehension = {x for x in range(10)}
set_comprehension_variation = set(x for x in range(10))
tuple_comprehension = tuple(x for x in range(10) if x % 2)
```

Read a bit more and experiment on your own. Remember that comprehensions can be nested, meaning you can have a list comprehension made up of a list comprehension. Book. Inception.

I'll just additionally mention that personally, I like to write longer list comprehensions in the following way:

```python
list_comprehension = [
    value
    for value in range(10)
    if value % 2
]
```

That is, in three lines, with each line having successive elements. If the comprehension is short, I don't do this, but for more complex ones I do. In my opinion, this improves readability.

## Generators

Since we're talking about loops and iteration, I'll mention generators. What are they?

Generally, these are functions that `yield` something instead of returning. What does this mean in practice and what's it all about, what's it for?

Speaking in simple terms, it's simply about the fact that sometimes we have data sets that are too large to load into RAM at once, as RAM is finite, large but finite and limited. What to do then? A generator is one of the strategies for dealing with such a situation. Generators allow us to process large data sets step by step.

Generators are actually just regular loops under the hood, wrapped in functions that `yield` some value. What does this mean? Instead of returning a given element and ending execution, a generator yields a given value, 'saves' or 'remembers' its current state and waits for a signal to return the next element. In the meantime, we can process and do something with the given values.

Generators can work on finite sets, they can be infinite. Many variations.

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

Generators also have the characteristic that they are one-time use. This means that once initialized, a generator can only be traversed once. This plus the fact that we don't load data into memory all at once is the main difference between generators and traditional lists or tuples.

## Walrus Operator

Since Python 3.8, we have something called the Walrus operator or assignment expression. It allows us to assign variables not only in statements but also in expressions, using the operator `NAME := expr`.

Alright, but what does this mean in practice. Let's look at the code.

```python
data = None
if our_function_getting_json(some_arg) is not None:
    data = our_function_getting_json(some_arg)
    data.do_stuff()
```

Rather simple to understand, reasonable, right? Example taken from some code. An ugly example. The above code sucks in this context. How could we improve it?

```python
data = our_function_getting_json(some_arg)
if data is not None:
    data.do_stuff()
```

We can do something like this, but is it the shortest possible, the best possible? Currently probably yes, but... 

It would be nice if we could declare that variable right there in the if statement - simply store the function's result where it's originally used. This is important when we want to perform some operations on the result of an expression that we executed, for example in a condition, but because we currently can't assign variables in expressions, we have to store it ourselves, earlier. Whether in loops, list comprehensions, lambda functions, or others.

Unless we use the walrus operator.

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
# or something like below
stuff = [[y := f(x), x/y] for x in range(5)]
y = y1 := f(x) # ERROR
bar(x = y := f(x)) # ERROR
bar(x = (y := f(x))) # OK
something := 'lalala' # ERROR
something2 = 'hey' # OK	
```

## Summary

Loops, generators, list comprehensions etc. are useful tools for every programmer and fundamental building blocks of any code. It's good to be very well acquainted with them.

## Questions and Exercises

1. Write examples of for and while loops. 3 different ones each.
2. Write an article comparing the for loop with the while loop.
3. Add a comparative characterization of for loops and comprehensions.
4. Write code that finds the largest and smallest number in a list.
5. Write code that counts words in a given string.
6. Then count letters.
7. And their frequency of occurrence.
8. Check if in a given list, there are two numbers – a and b, whose sum equals a given number.
9. Write code that from any list (numbers only) will display only those that are less than 5.
10. Ask the user for a number and then print all divisors of that number.
11. Get two numbers from the user and then return the square of their sum.
12. Write code that will read a string from the user and then display the first three letters of that string, consecutively, without new lines. E.g., "MelonTusk" -> "MelMelMel"
13. Get a string from the user and then display it with letters in reverse order
14. Based on the f-string benchmarking code from the previous chapter, conduct an analysis of what's faster: list(), [] or list comprehensions. Each should contain natural numbers from 1 to 10.

Remember that you can post your answers on GH here - https://github.com/grski/junior-python-exercises, and I'll check your solutions and give feedback. More about this in the 'Interactive Part' subsection.

\pagebreak 