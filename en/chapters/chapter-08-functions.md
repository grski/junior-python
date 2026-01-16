\pagebreak

# Functions

Functions are a fundamental element of programming that allows you to group code for reusable purposes. They are also used to divide a program into smaller, more understandable fragments, which makes it easier to create and maintain, improving readability. And I've mentioned that readability is critically important, right? After all, you write code once but read it dozens of times. You and other people.

What are functions and why are they important in programming? We'll talk about this more broadly in a moment. Let's start with regular functions.

## Regular Functions/Methods

First, let's discuss traditional functions, or if we're talking about functions defined in classes, methods.

#### Syntax for Defining Functions in Python

In Python, a function definition starts with the keyword `def`, followed by the function name and parentheses with arguments. The code inside the function is indented. Example of a function definition:

```python
def function_name(arg1, arg2):
    # function code
    return result
```

#### Passing Arguments to Functions

To call a function, you need to provide its name and the appropriate arguments. Depending on what arguments are required by the function, you need to provide the correct number of arguments.

#### Returning Values from Functions

Functions in Python can return values using the `return` keyword. When a function is called, the code inside the function is executed, and then the value is returned and assigned to a variable or used in some other way. If a function doesn't return any value, it returns `None` by default.

#### Using the `return` Keyword to Return Values from a Function

To return a value from a function, use the `return` keyword along with the expression to be returned. For example:

```python
def increment(x):
    return x + 1

a = 5
b = increment(a)
print(b)  # Output: 6
```

#### Multiple Return Values

In Python, it's possible to return multiple values from a function using a tuple or dictionary. To return multiple values as a tuple, simply separate them with commas. Example:

```python
def min_max(x):
    return min(x), max(x), x

a = [1, 2, 3]
min_a, max_a, _ = min_max(a)
# alternatively:
result = min_max(a)
min_a = result[0]
max_a = result[1]
print(min_a)  # Output: 1
print(max_a)  # Output: 3
```

By the way, the line where this function is called is an example of so-called tuple unpacking.

A useful and important thing.

If you decide that the second argument returned by a function is unnecessary, or that in a function that returns three arguments you only want the first, or only the second, or maybe the last, that's also possible. How? Analyze the code below.

```python
def min_max(x):
    return min(x), max(x), x

a = [1, 2, 3]
min_a, max_a, _ = min_max(a)
# the third argument will be ignored and not assigned to
# any variable - _ is a placeholder that Python recognizes
*_, last_argument = min_max(a)
first, *all_the_rest = min_max(a)
first, _, the_third = min_max(a)
first, *_, the_third = min_max(a)
```

Play with the code above and see what conclusions you draw. Additionally, I recommend trying to create functions with more arguments to return.

To return multiple values as a dictionary, simply create a dictionary and return it using the `return` keyword. Nothing groundbreaking.

```python
def min_max(x):
    return {'min': min(x), 'max': max(x)}

a = [1, 2, 3]
min_max_dict = min_max(a)
print(min_max_dict['min'])  # Output: 1
print(min_max_dict['max'])  # Output: 3
```

#### Default Argument Values

In Python, you can define default values for function arguments, which means these arguments don't have to be passed to the function when it's called. The default value is used when the argument isn't passed to the function. However, there's one important thing to remember when defining default values, which I'll mention shortly.

Here's an example of a function with default arguments:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('Alice')  # prints "Hello, Alice!"
greet('Bob', 'Hi')  # prints "Hi, Bob!"
```

In the example above, the argument `name` has no default value, so it must be passed to the function when calling it. However, the argument `greeting` has a default value of `'Hello'`, so it can be omitted when calling the function. If you do pass a second argument to the function, its value will be used instead of the default.

The second argument can be passed in two ways:

```python
greet('Bob', 'Hi')  # prints "Hi, Bob!"
greet('Bob', greeting='Hi')  # prints "Hi, Bob!"
```

The second way uses keyword arguments - arguments with default values that are optional. Arguments without default values can also be passed as keyword arguments.

```python
greet('Bob', 'Hi')  # prints "Hi, Bob!"
greet(name='Bob', greeting='Hi')  # prints "Hi, Bob!"
```

The argument name is used as a key. You can use keyword arguments to pass arguments to a function in any order, regardless of the order in which they were defined in the function definition, but it's better to stick to the conventional order. Just because you can doesn't mean you should.

Here's an example of using keyword arguments:

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet(name='Alice')  # prints "Hello, Alice!"
greet(greeting='Hi', name='Bob')  # prints "Hi, Bob!"
```

In the example above, the argument `name` is passed to the function using the keyword argument `name`, and the argument `greeting` is passed using the keyword argument `greeting`. You can swap the order of these arguments when calling the function, and the function will still work correctly.

Note: keyword arguments must be placed after positional arguments (those not specified by name) when calling the function and when defining it.

```python
def greet(name, greeting='Hello'):
  print(f'{greeting}, {name}!')

greet('Alice', greeting='Hi')  # correct
greet(greeting='Hi', 'Alice')  # SyntaxError
def greet(greeting='Hello', name):
  print(f'{greeting}, {name}!')  # error
```

### One-Time Initialization Gotcha

Default argument values are evaluated only once - the Python interpreter looks at them once, does its thing, and doesn't bother with them again. What does this mean? Well, the interpreter works in such a way that when possible, it initializes default arguments only once. While this isn't a problem with strings or numbers, with mutable objects a problem arises. Can you guess what?

Each subsequent function call, contrary to what you might expect, won't create a new instance of the default element but will simply use a reference to the initially initialized object, such as a list. Consider the example below.

 ```python
 >>> def xd(default_list=[]):
         default_list.append(1)
         return default_list
 >>> xd()
 [1]
 >>> xd
 <function xd at 0x7fd52a695510>
 >>> xd()
 [1, 1]
 >>> xd([1,2,3])
 [1, 2, 3, 1]
 ```

Look at this code and think about it. This often comes up in interviews as a gotcha :-)

#### Functions as Objects

In Python, it's possible to assign functions to variables and pass them as arguments to other functions.

Because functions are objects, you can assign them to variables just like assigning a value to a variable. You can also pass a function as an argument to another function. Example:

```python
def increment(x):
    return x + 1

def apply_to_list(function, l):
    return [function(x) for x in l]

a = [1, 2, 3]
b = apply_to_list(increment, a)
print(b)  # Output: [2, 3, 4]
```

#### Pure Functions

Pure functions are functions that always return the same value for the same inputs and don't affect the program's state outside their scope. In other words, pure functions don't modify global state, don't cause any side effects (such as changing a global variable or displaying something on the screen), and always return the same value for a given set of inputs. It's somewhat like the mapping of a mathematical function. Mapping values for each argument.

Here's an example of a pure function:

```python
def add(x, y):
  return x + y

print(add(1, 2))  # prints 3
print(add(1, 2))  # prints 3
print(add(1, 2))  # prints 3
```

The `add` function above is pure because it always returns the same value for a given set of inputs (here 1 and 2) and has no side effects.

Pure functions are often used in functional programming because they are easy to test and easy to understand. Additionally, pure functions are often more reliable than functions that cause side effects because there's no risk that their behavior will depend on global state or other undefined variables.

Personally, I quite like them. Certain aspects of functional programming are fairly close to me, and even when used in OOP, they improve code quality. When I try to write reasonably pure functions, I often notice that the code turns out better. Of course, everything in moderation - I don't recommend being a purist or fanatic. Know when to make an exception.

#### *args, **kwargs

The keywords `*args` and `**kwargs` are used to pass any number of arguments to a function.

`*args` is used to pass any number of non-keyword arguments (so-called "positional arguments") to a function. These arguments are passed as a tuple.

Example:

```python
def func(*args):
    print(args)

func(1, 2, 3)
# Output: (1, 2, 3)
```

`**kwargs` is used to pass any number of keyword arguments to a function. These arguments are passed to the function as a dictionary.

Example:

```python
def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)
# Output: {'a': 1, 'b': 2, 'c': 3}
```

The keywords `*args` and `**kwargs` are particularly useful when you want to pass any number of arguments to a function without knowing their exact number or names. You can also use both keywords simultaneously if you want to pass both positional and keyword arguments. You can use them together - `*args, **kwargs`.

#### Tips

To write readable and efficient code using functions, keep in mind a few important tips:

- Divide code into smaller fragments using functions. This will make it easier to read and understand.
- Name functions to describe what they do. Names should be understandable to code readers.
- Try to avoid repeating code and the copy-paste method. Create atomic, small, and reusable functions.
- Clearly specify what arguments are required by the function and what values it returns. Type Hinting and Docstrings are your friends.
- Ideally, a function has as few side effects as possible - it doesn't depend on things from outside itself.
- Try to limit the number of arguments passed to a function to a minimum. The fewer arguments, the easier it will be to understand.
- A function with one argument is ideal. Two is almost as good. Above that, think about it. Maybe it's worth wrapping those arguments in some class/object?
- Remember to test functions. Test each function to make sure it works correctly. Small, short, pure functions are easy to test.

## Anonymous Functions/Lambda

This will be really short. Anonymous functions/lambdas are simply one-line functions that we don't give a name to because we only use them in a specific local place or for passing a function as an argument to another function.

It's not a good practice to overuse them, but in certain situations, they have their applications. I usually prefer regular functions because they allow me to more extensively and descriptively indicate what a given code does, to give it a name. There are, of course, trivial examples and places where lambdas make sense. However, it's worth remembering not to create monsters that contain a million nested lambdas or complicated logic.

Below are examples.

```python
# Regular function
def add(x, y):
    return x + y

# Lambda function
add = lambda x, y: x + y
```

### Where Do We Use Lambdas Most Often?

Lambda functions are often used in combination with functions like `map()`, `filter()`, and `reduce()`, which take functions as arguments, `sorted()`, etc.

### Examples

Here's an example of using a lambda function with `map()` as well as a few other examples:

```python
numbers = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers)
# doubled is now [2, 4, 6, 8]

# lambda function returning the square of a given number
square = lambda x: x**2
print(square(5))  # prints 25

# lambda function returning the larger of two numbers
max_number = lambda x, y: x if x > y else y
print(max_number(4, 5))  # prints 5

# lambda function taking a list and returning the sum of its elements
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3]))  # prints 6

# lambda function taking a list and returning a list of even elements
even_elements = lambda lst: [x for x in lst if x % 2 == 0]
print(even_elements([1, 2, 3, 4, 5]))  # prints [2, 4]
```

In the code above, lambda functions were used to create short functions that return the square of a given number, the larger of two numbers, the sum of list elements, and a list of even elements.

Remember that lambda functions are limited to one line and cannot be used for more complex tasks. In such cases, it's better to use a regular function.

An example from somewhat more real-world code:

```python
def sort_timestamp(orders):
    return sorted(orders, key=lambda x: x.timestamp)
# another example
class Foo:
    def _create_transactions(
        self,
        book_side: dict[(int, list)],
        new_order: Order,
        start: int = None
    ) -> Order:
        """Here we take care of creating transaction and
        fulfilling orders if a match is found in the orderbook.
        When we process the book it's important to reverse the
        ordering based if it's a bid/ask side of orderbook.
        Orders that are fulfilled are removed from the book.
        If no orders are present for given price
        internally it's removed from the order book. Orders that
        are filled partly are added to the orderbook with
        the remaining quantity."""
        sorted_prices = sorted(book_side.keys(), reverse=new_order.is_ask)
        sorted_prices = sorted_prices if start is None else sorted_prices[start:]
        for price in sorted_prices:
            if new_order.is_fulfilled or new_order.price_doesnt_match(book_side_price=price):
                break

            orders_at_price: list[Order] = book_side[price]
            sorted_orders_at_price = sorted(
                orders_at_price,
                key=lambda order: order.timestamp
            )
           	(...)
```

The code above sorts objects by one of their attributes.

For further reading:

1. https://realpython.com/python-lambda/
2. https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/
3. https://www.geeksforgeeks.org/intersection-two-arrays-python-lambda-expression-filter-function/?ref=lbp

\pagebreak

