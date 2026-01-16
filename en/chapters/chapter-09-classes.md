\pagebreak

# Classes and OOP



## Classes

You can think of classes, in simple terms, as collections of functions. Functions created inside a class are suddenly called `methods`.

Classes can be 'combined', which is called inheritance. When one class inherits from another, it adopts its methods, unless we override them. Here's an example of a class:

\pagebreak

```python
from collections import defaultdict
from queue import Queue

from orderbook.transaction import Transaction

class BaseOrderBook:
    pass


class OrderBook(BaseOrderBook):
    """
    This very simple order book implementation works
    within certain constrictions provided in the requirements.
    These constrictions in some aspects assume the 'happy path'
    hence the implementation will do the same and
    cover just these scenarios. Stubs may be provided in a place or
    two just for interface's sake or my sanity.
    We only implement two types of orders: Limit Order & Iceberg Order.
    """

    def __init__(self) -> None:
        self.asks = defaultdict(list)
        self.bids = defaultdict(list)
        self.order_ids = set()
        self.transactions: Queue[Transaction] = Queue()
        self.last_accessed_transaction_index = self.transactions.qsize() - 1

    def show_new_transactions(self):
        while not self.transactions.empty():
            if transaction := self.transactions.get():
                print(transaction)

    @property
    def maximum_bid(self) -> int:
        return max(self.bids.keys()) if self.bids else float("-inf")

    @property
    def minimum_ask(self) -> int:
        return min(self.asks.keys()) if self.asks else float("inf")

```

Recommended reading:

1. https://realpython.com/inheritance-composition-python/

### super() and MRO

`super()` is simply a way to call a method from the class we're inheriting from. That's all there is to it. It's like when mom yells 'go call your dad'.

If we inherit from multiple classes, which is allowed and quite common in Python, and they implement the same method, the decision about which method gets used is determined by MRO - Method Resolution Order.

Method Resolution Order (MRO) is how Python maps multiple inheritance in classes. MRO determines the order in which Python searches for methods in classes when calling a method on an object, and from which class it fires the method.

For example, if we have the following three classes:

```python
class A:
    def method(self):
        print("This method is from class A")

class B(A):
    def method(self):
        print("This method is from class B")

class C(A):
    def method(self):
        print("This method is from class C")
```

and then we create an object of class `D`, which inherits from both class `B` and `C`:

```python
class D(B, C):
    pass
```

If we now call the `method` on object `D`, Python will use MRO to determine which version of the method gets called. In this case, since class `D` inherits from class `B` first, Python will call the version of the method from class `B`. If class `B` didn't have this method, Python would search class `C`, and then class `A`.

MRO works according to the C3 algorithm, which ensures consistent and predictable results. You can see the MRO for a given class using the `__mro__` attribute:

```python
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

MRO is important because it allows control over how multiple inheritance is mapped in the code. This can be particularly useful for classes that inherit from multiple base classes and want to ensure that methods are called appropriately.

The C3 algorithm works as follows:

1. All classes are placed on a list, in the order they are given as inheritance arguments. For example, in class `D` defined as `class D(B, C)`, class `B` comes before class `C`.
2. For each class on the list, add its base class to the end of the same list.

So first from top to bottom, then left to right.

I'll skip the rest.

The C3 algorithm has been used in Python since version 2.3. It is considered more elegant and simple than the previous algorithm used in Python (algorithmic depth-first search). The C3 algorithm provides consistent and predictable results for MRO, which allows better control over multiple inheritance in classes and fewer surprises in production :)

Recommended reading: https://www.educative.io/answers/what-is-mro-in-python

## Classmethods, staticmethods

A concept worth knowing to create nice interfaces and sensible classes is the class method and static method.

What does this mean? A class method/classmethod is a method that doesn't need an instance of the class, only the class itself. This means we won't have access to the initialized object and its attributes that we define in `__init__`, only to variables at the class level, i.e., in its scope.

A static method is a method that doesn't even need variables from the class and doesn't reference them, nor does it reference other methods from that class.

So in short: if we need the object's state or the object itself, use regular methods. If we only need things from the class, use a class method. If neither of the above, just use a static method. Examples below.

```python
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # regular method using instance attributes
    def print_name(self):
        print(self.name)

    # class method creating instances of the class
    # based on birth year
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)

    # static method to check adulthood
    @staticmethod
    def is_adult(age):
        return age >= 18


person1 = Person('hejto', 21)
person2 = Person.from_birth_year('John', 1996)

print(person1.age)
print(person2.age)
print(Person.is_adult(22))
```

Recommended reading: https://www.geeksforgeeks.org/class-method-vs-static-method-python/?ref=lbp

## Context Managers

Context managers are classes that define `__enter__` and `__exit__`. These are the things we use with the `with` clause. In short, these classes simply define magic methods that are called when entering the code block with `with` and after completing processing of that block and exiting from it. They allow us to, well, set up some specific context and then clean up after it.

A good example here is file operations. First, we want to open the file, set up the cursor appropriately, etc., and only then work on it. When we finish working with the file, we'd like to close it so nothing hangs in memory. Instead of doing this manually every time, we use a context manager, which rides in to save the day.

```python
class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')


# context manager as a generator
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()

with open_file('some_file') as f:
    f.write('hola!')
```

Recommended reading: https://realpython.com/python-with-statement/

## Type hints

Type hinting is a mechanism in Python that allows you to "hint" to the programmer what type of data is expected in a given place in the program. In Python, there's no requirement to declare variable types, so type hinting is an optional tool that can be used to make coding easier or to document code.

Type hinting can be used in several different places in code, such as function declarations, variables and methods, and in comments.

Examples of type hinting usage:

```python
def greet(name: str) -> str:
    return "Hello, " + name

def sum_numbers(a: int, b: int) -> int:
    return a + b

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

```

The advantage of using type hinting is that it can help document code and make it easier to read for other programmers. Type hinting can also help detect errors at compile time, since the interpreter can report errors if data of the expected type is not passed to a function or method.

The disadvantage of using type hinting is that it can be tedious to implement, especially in large projects where manually adding type hints to many places in the code is necessary. Additionally, since type hinting is not mandatory in Python, some programmers may not use it in their projects, which can make collaboration and reading code by others more difficult, but forget about them. Type hinting is awesome, I highly recommend it.

Recommended reading:

1. https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49
2. https://docs.python.org/3/library/typing.html

## Docstrings

Docstrings (documentation strings) are strings placed in Python code that serve as documentation for the code. They are placed directly after the declaration of a function, method, class, etc., and are usually enclosed in triple quotes.

Docstrings are often used to describe what a given function, method, or class does, what arguments it accepts, and what values it returns. Docstrings are later used by documentation generation tools (e.g., Sphinx) to automatically create code documentation.

Here's an example of docstring usage in Python:

```python
def add(x, y):
  """
  A function that adds two numbers.

  Args:
    x (int): first number to add
    y (int): second number to add

  Returns:
    int: sum of two numbers
  """
  return x + y
```

In the example above, the docstring describes what the `add` function does, what arguments it accepts, and what values it returns.

Note: remember that docstrings must be placed directly after the function declaration and must be enclosed in triple ". Docstrings cannot contain any code instructions and cannot be used as regular comments.

Docstrings and type hints are devilishly useful things that I really warmly recommend using. Even if you're working solo on an amateur project. Why? Because you also forget what a given code was doing. It's much easier to return to your own project when it's well documented with type hints, docstrings, and meaningful comments.

Nonsense like "Good code doesn't need comments" should be left among fairy tales.

## The is operator

The `is` operator in Python is used to check whether two variables point to the same location in memory. The `==` operator, on the other hand, is used to check whether two variables contain the same value.

Here's an example of using the `is` and `==` operators:

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # prints True
print(x is z)  # prints False
print(x == y)  # prints True
print(x == z)  # prints True
```

In the example above, variables `x` and `y` point to the same location in memory (both variables point to the same list), so the `is` operator returns True. Variable `z` contains the same value as variable `x`, but points to a different memory location, so the `is` operator returns False. The `==` operator only checks the values of both variables, so it returns True for both `x == y` and `x == z` comparisons.

Note: remember that the `is` operator is faster than the `==` operator because it doesn't need to compare variable values, but only checks whether they point to the same location in memory. That's why the `is` operator is often used in places where speed is important and comparison accuracy is not necessary.

Additionally, `is` is a language element, 'immutable' so to speak. Whereas the use of the `==` operator depends on how the magic (dunder) method `__eq__` is implemented. What does this mean? Well, we can define ourselves how Python will compare objects with `==`. Check it out.

##

\pagebreak
