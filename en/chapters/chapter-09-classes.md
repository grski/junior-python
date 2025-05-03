# Classes and OOP

## Classes

You can think of classes, in simplified terms, as collections of functions. Functions created inside a class are suddenly called `methods`.

Classes can be 'connected', which is called inheritance. When one class inherits from another, it takes on its methods unless we override them. Example of a class:

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
        return min(self.bids.keys()) if self.bids else float("-inf")

    @property
    def minimum_ask(self) -> int:
        return min(self.asks.keys()) if self.asks else float("inf")
```

For reading:
1. https://realpython.com/inheritance-composition-python/

### super() and MRO

`super()` is nothing more than a way to call a method from the class we inherit from. That's all there is to it. It's like when a mother shouts "call the old man".

If we inherit from multiple classes, which is allowed and quite common in Python, and they implement the same method, which method will be used is decided by MRO. Method Resolution Order.

Method Resolution Order (MRO) is the way Python maps multiple inheritance in classes. MRO determines the order in which Python searches for methods in classes when calling a method on an object and from which class it fires the method.

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

If we now call the `method` method on object `D`, Python will use MRO to determine which version of the method will be called. In this case, since class `D` inherits from class `B` first, Python will call the version of the method from class `B`. If class `B` didn't have this method, Python would search class `C`, and then class `A`.

MRO works according to the C3 algorithm, which ensures consistent and predictable results. You can see the MRO for a given class using the `__mro__` function:

```python
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

MRO is important because it allows control over how multiple inheritance is mapped in code. This can be particularly useful in the case of classes that inherit from multiple base classes and want to ensure that methods are called appropriately.

The C3 algorithm works as follows:

1. All classes are placed on a list, in the order they are given as inheritance arguments. For example, in class `D` defined as `class D(B, C)`, class `B` comes before class `C`.
2. For each class on the list, add its base class to the end of the same list.

So first from top to bottom, then left to right.

I'll skip the rest.

The C3 algorithm has been used in Python since version 2.3. It is considered more elegant and simpler than the previous algorithm used in Python (algorithmic depth-first search). The C3 algorithm ensures consistent and predictable results for MRO, which enables better control over multiple inheritance in classes and fewer surprises in production :)

For reading: https://www.educative.io/answers/what-is-mro-in-python

## Classmethods, staticmethods

A concept worth knowing to create nice interfaces and sensible classes is class method and static method.

What does this mean? A class method/classmethod is a method that doesn't need an instance of a given class, only the class itself. This means we won't have access to the initialized object and its attributes that we define in `__init__`, but only to variables at the class level, i.e., in its scope.

A static method is a method that doesn't even need variables from the class and doesn't refer to them, nor does it refer to other methods from the given class.

So in short: if we need the object's state or the object itself, regular methods. If only things from the given class, then a class method, if none of the above then just a static method. Examples below.

```python
from datetime import date
 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # regular method using instance attributes
    def print_name(self):
        print(self.name)
 
    # class method creating instances of the given class
    # based on year
    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year - year)
 
    # static method for checking adulthood
    @staticmethod
    def is_adult(age):
        return age > 18
 
 
person1 = Person('hejto', 21)
person2 = Person.from_birth_year('Sasin', 1996)
 
print(person1.age)
print(person2.age)
print(Person.is_adult(22))
```

For reading: https://www.geeksforgeeks.org/class-method-vs-static-method-python/?ref=lbp

## Context Managers

Context managers are classes that define `__enter__` and `__exit__`. These are the things we use together with the `with` clause. In short, these classes simply define magic methods that are triggered when entering the code block with with and after completing the processing of this block and exiting it. They allow us to, well, set some specific context and then clean up after it.

A good example here are file operations. First we want to open the file, set the cursor appropriately, etc., and only then work on it. When we finish working on the file, we'd like to close it so nothing hangs in memory. Instead of doing this manually each time, we use a context manager that comes in all white.

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

For reading: https://realpython.com/python-with-statement/

## Typehints

Type hinting is a mechanism in Python that allows us to "hint" to the programmer what type of data we expect in a given place in the program. In Python, there is no need to declare variable types, so type hinting is an optional tool that can be used to facilitate coding or document code.

Type hinting can be used in several different places in the code, such as function declarations, variables and methods, and in comments.

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

The advantage of using type hinting is that it can help document code and make it easier to read for other programmers. Type hinting can also help detect errors at compile time, as the interpreter can report errors if data of the expected type is not passed to a function or method.

The disadvantage of using type hinting is that it can be cumbersome to implement, especially in large projects where it is necessary to manually add type hinting to many places in the code. Additionally, since type hinting is not mandatory in Python, some programmers may not use it in their projects, which can make collaboration and code reading by others more difficult, but forget them. Type hinting is great, I recommend it.

For reading:

1. https://towardsdatascience.com/12-beginner-concepts-about-type-hints-to-improve-your-python-code-90f1ba0ac49
2. https://docs.python.org/3/library/typing.html

## Docstrings

Docstrings (short for "documentation strings") are strings placed in Python code that serve as documentation for the code. They are placed directly after the declaration of a function, method, class, etc., and are usually placed in triple quotes.

Docstrings are often used to describe what a given function, method, or class does, what arguments it takes, and what values it returns. Docstrings are later used by documentation tools (e.g., Sphinx) to automatically generate code documentation.

Here's an example of using docstrings in Python:

```python
def add(x, y):
  """
  Function that adds two numbers.

  Args:
    x (int): first number to add
    y (int): second number to add

  Returns:
    int: sum of two numbers
  """
  return x + y
```

In the above example, the docstring describes what the `add` function does, what arguments it takes, and what values it returns.

Note: remember that docstrings must be placed directly after the function declaration and must be enclosed in triple quotes. Docstrings cannot contain any code instructions or be used as regular comments.

Docstrings and type hints are devilishly useful things that I really highly recommend using. Even when you're working independently on an amateur project. Why? Because you also forget what a given code did. It's much easier to return to your own project even then, when it's well documented with type hints or docstrings and concise comments.

Nonsense like "Good code doesn't need comments" let's leave between fairy tales.

## The is Operator

The `is` operator in Python is used to check if two variables point to the same memory location. Whereas the `==` operator is used to check if two variables contain the same value.

Here's an example of using the `is` and `==` operators:

```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # will print True
print(x is z)  # will print False
print(x == y)  # will print True
print(x == z)  # will print True
```

In the above example, variables `x` and `y` point to the same memory location (both variables point to the same list), so the `is` operator returns True. Variable `z` contains the same value as variable `x`, but points to a different memory location, so the `is` operator returns False. Whereas the `==` operator only checks the values of both variables, so it returns True for both `x == y` and `x == z`.

Note: remember that the `is` operator is faster than the `==` operator because it doesn't have to compare variable values, but only checks if they point to the same memory location. Therefore, the `is` operator is often used in places where speed is important, and comparison accuracy is not necessary.

Additionally, `is` is a language element, 'immutable' let's say. Whereas the use of the `==` operator depends on how the magic (dunder) method `__eq__` or `__equals__`? I don't remember, check. What does this mean? Well, we can define ourselves how Python will compare objects with `==`. Read about it.

\pagebreak 