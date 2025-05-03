\pagebreak

# Loops and Iteration

Let's talk a bit about loops in Python, and also a few words about iteration. What it is, what it's for, and who needs it. We'll talk about different loops, `for`, which is a step loop, `while`, which is a regular loop. About iteration and iterable objects.

But what does this even mean?

Loops are a concept in programming used to perform some action, some piece of code, a specified number of times. Imagine you need to process 10 elements from an array. Perform some operations on each of them. Let's say these operations aren't just one line but complicated processing. Although no, let's take multiplication for our example. And now what?
A naive solution would look like this:

```python
>>> elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> elements[0] *= 2
>>> elements[1] *= 2
>>> elements[2] *= 3
(...)
>>> elements[9] *= 3
``` 