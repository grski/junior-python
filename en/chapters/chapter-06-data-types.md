# Data Types

In the previous chapter, we talked about variables. While on this topic, it's worth mentioning the types of data that our variables can store in Python. We'll discuss this specific language, but similar divisions exist in most languages.

As I wrote in previous chapters, Python doesn't require us to define types for our variables - it doesn't have static typing. Remember what this meant and answer the question - what does the lack of static typing mean? What is dynamic typing? What are its advantages/disadvantages? Look in the book, maybe in the answers to previous chapters. Do this now.

Despite this, it's good to know what types we typically divide variables into. Why? Because Python uses them too, it just somehow guesses what type we used. Depending on the type, different operations can be performed on the variable. When we think about it, this is logical, because even though underneath it's all the same - binary code, on certain fragments that we interpret as X, we want to perform only operations from set Z, and when we interpret G, only from F. Speaking more simply, if we mark something as text, we'll treat it differently, or apply different modifications than when something is a number. On numbers, we can perform arithmetic operations, while in text we can search for our name, for example. Different operations depending on the type. Logical, right?

So in Python, we distinguish the following basic data types:

1. Numbers
2. Strings
3. Bytes
4. Boolean type

Among the more complex ones, we have:

1. Lists
2. Tuples
3. Dictionaries
4. Sets

Let's discuss them all one by one. Let's start with numbers, as it will probably take the longest.

## Numbers

### Brief Characteristics

So, my dear readers, in Python we distinguish three main types of numbers: integers, floating-point numbers, and complex numbers, or in order: ints, floats, complex.

What does this mean?

### Integers

This is probably simple, right? `1, -1, 5, 0, 938, -24861` are examples of integers, or simply `ordinary` numbers without any decimal points, peculiarities, or inventions. I won't elaborate too much on them because there's no need.

Or is there?

Note that in the examples above, we have a negative number, less than zero. In the case of text, it's simple to write - we put a minus in front and we're done. As humans, we're taught to interpret this as a negative number. But how does a computer do this?

### Example Way of Representing Negative Numbers

Let's recall previous chapters and what we talked about there. I showed, among other things, how a computer stores numbers in memory and how it represents them, namely using the binary system, bits, bytes, those things. Now, the question arises: how then does the computer indicate that a given number is negative? After all, it can't put a `minus` in memory in some way.

Well, I'll show you how it looks, again, in C. There were many ways and ideas to solve this problem, and there still are, but let's discuss just one. Let's assume we're operating on some type that is exactly 1 byte in size. This means it's 8 bits long. How many values/numbers can it handle at most? Please answer this question, calculate.

Good, having 8 bits, we have 8 zeros and/or ones at our disposal. So we can represent a maximum of 256 values, right? That is, for example, numbers from 0 to 255. Well, not exactly!

In the default case, we'll have 256 values at our disposal, right, but from a different range: from **-128** to **127**. This can be determined by the formula: $(+/-)2^7-1$

Where does this change come from? Well, we take one byte to indicate whether a given number is positive or negative, in a nutshell. In C, if we know we're not interested in negative values, we can tell the compiler to shift the negative range to positive. Variables with sign vs variables without. Signed variables vs unsigned variables.

By the way, while we're at it, I'll add another interesting fact. Did you know that even the way of writing the order of bits in memory is conventional? What does this mean? Well, some people couldn't agree on what's better - writing the highest-value bit first or last. Hence we have two standards: big endian and little endian. What does this mean and how does it look in practice? Simple thing.

Let's assume we're talking about Big Endian. We want to write the value 0x4A3B2C1D at address 100. It would look like this.

| 100  | 101  | 102  | 103  |
| ---- | ---- | ---- | ---- |
| 4A   | 3B   | 2C   | 1D   |

And Little Endian?

| 100  | 101  | 102  | 103  |
| ---- | ---- | ---- | ---- |
| 1D   | 2C   | 3B   | 4A   |

So the opposite. It's generally about which to write where. This makes a difference when calculating/reading these values. Which is better? Big Endian will probably be easier to understand, as it's analogous to the notation we use daily in the decimal system.

Different processors have different conventions, fortunately you don't have to worry about this in your code - the Python interpreter will do it for you.

### Floating-Point Numbers and the Inaccuracy of Their Representation

What are we dealing with here? Nothing other than numbers with a `decimal part`, speaking in simple terms. And that's basically it. If we see a number in Python where there's a dot - e.g., `1.0`, we need to know we're dealing with a floating-point number. Why is this important knowledge? Well...

Here, unlike with integers, there are peculiarities, and big ones, but underneath. It's a longer topic, but it basically comes down to the so-called inaccuracy of floating-point number representation in the binary system. Yes, yes. Clear, right? I'll just say mysteriously that you should always and everywhere remember that using regular floats/doubles for precise calculations or storing information about money is not a very good idea, because sometimes `0.1+0.2 != 0.3`. Why? Because try to represent, for example, 1/3 exactly using powers of two. Hard, right? But what am I getting at?

Let's consider a simple program in C (this issue concerns practically every language):

```c
    #include <stdio.h>

    int main()
    {
        float example_float = 0.1;
        if(example_float == 0.1)
        {
            printf("Equal");
        }
        return 0;
    }
```

Simple code, right? I think everyone should understand it if they know at least the basics of programming. The expected result of running this code for a large part would be printing 'Equal' in the console, right? I thought so too at the beginning. Check for yourself what happens when you compile and run the code.

Surprisingly, "Equal" didn't display. Why? Did something go wrong? The numbers appear to be the same, because here 0.1 and here 0.1, what's going on? Hmm, maybe the variable was written incorrectly. Let's print it and see.

```c
    printf("%f", example_float);
```

Add this line of code after the finished if. Run the code... And what? Here's the result:

```
0.100000
```

Wait. So something is wrong in our program, right? Because `example_float` is equal to 0.1, right? Well, no.

We can't see it here because the precision is too low, but let's force the `printf` function to display our float with greater precision than default, because as you can see, printf by default displays only 6 decimal places.

```c
    #include <stdio.h>

    int main()
    {
        float example_float = 0.1;
        if(example_float == 0.1)
        {
            printf("Equal");
        }
        printf("%.16f", example_float);
        return 0;
    }
```

Gives us

```
0.1000000014901161
```

A slight modification of our code and everything is clear. Our `example_float` is not exactly equal to 0.1, but a bit more. Why?

Everything results from the fact that the computer 'operates' in binary language. This means that when creating numbers, only powers of two are available, multiplied appropriately by 1 or 0, which can be summed (in great simplification, we talked about this already). So it's no wonder our float looks like this. Try to build exactly 0.1 from these numbers `{..., 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 0, 1, 2, 4, 8, 16, ...}`. It can't usually be done perfectly. Theoretically, in an imaginary world where we would have an infinite amount of memory at our disposal and an infinite amount of time, we could get infinitely close, sometimes even achieve, any number. But if you want to know more about this, read about limits or recall from high school mathematics.

Hence this inaccuracy - it results only from how floating-point numbers are represented in computer memory. While in most cases, satisfactory accuracy can be achieved using a finite amount of memory, there are cases where this accuracy won't be sufficient.

For such cases, we have special libraries or perhaps a special approach that deals with the topic differently, but it's worth knowing about this. Therefore, if we're writing a program that has anything to do with money, it's worth thinking twice before using a float or double. Maybe it's better to keep zlotys in a separate int, and grosze in a separate one? Who knows.

Solutions to many problems related to floating-point numbers can be found in the `Decimal` and `Fraction` modules.

To read:

1. https://docs.python.org/3/library/decimal.html
2. https://docs.python.org/3/library/fractions.html

### Complex Numbers

Very rarely encountered, but sometimes when someone is doing some scientific calculations or other strange things, this knowledge might be useful - these are numbers consisting of a real part and an imaginary part. Mathematical topics. If you don't know what this is about, don't worry.

We define them like this: `test = 21 +3j` or `some_complex_number = complex(32, 3)`. And we can perform the same operations on them as on numbers - division, multiplication, addition, and so on. Sometimes useful.

And that's it. For now, that's all you need to know about things we qualify as numbers in Python. There are also decimals or rationals, but we'll talk about them another time!

### Operations on Numbers

As I mentioned regarding complex numbers, we can perform various basic mathematical operations on numbers, and they will work more or less as we would expect. I'm talking about addition, subtraction, multiplication, division, integer division, modulo operation, and other basic arithmetic operations.

Operators that Python understands are:

| Operator | Action                                                       |
| -------- | ------------------------------------------------------------ |
| *        | Multiplication                                               |
| **       | Exponentiation, so 2 ** 3 means two to the power of three.   |
| /        | Regular floating-point division                              |
| +        | Addition                                                     |
| -        | Subtraction                                                  |
| //       | Division without remainder, so 5 // 2 equals 2, -11 // 3 equals -4 (note negative numbers) |
| %        | Remainder of, so for example 5 % 2 is nothing other than the remainder of dividing 5 by 2, which is 1 |

It's also worth remembering that if we have several different types of numbers in one expression, Python will cast the result of the entire expression to the most complex type. What does this mean? The result of `1.0 + 1` will be not `2` but `2.0`, the result of `1 + 1.0 + 3 +0j` will be `5+0j`. The order of complexity is thus:

Integers -> Floating-point -> Complex.

It's worth remembering this, as it carries certain consequences - just watch out for those dots, because sometimes you can get caught out.

Additionally, I'll mention a syntactic sugar that allows us to shorten the notation of popular operations. It looks like this:

```python
foo = 2
foo = foo + 2 # this line will be equivalent to the one below
foo += 2
```

### Numeric Conversions

Numbers can be 'converted' between each other, or we can perform a kind of `type casting` as we would say in other strongly typed static languages. How? Examples below. Analyze them a bit yourself.

```python
>>> int(1.3)
1
>>> int(1.6)
1
>>> int(1.9)
1
>>> int(1.4444)
1
>>> int("1")
1
>>> int("5")
5
>>> int("52")
52
>>> int("-52")
-52
>>> float(1)
1.0
>>> float(3)
3.0
>>> float("2")
2.0
>>> complex(2)
(2+0j)
>>> int("1.3")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '1.3'
```

Play around with the `int`, `float`, `complex` functions. Then describe what each of them does. What values they accept, what causes errors. The last example `int("1.3")` caused an error. Translate it and try to explain what happened here.

It's worth noting one important thing that Python provides out of the box, which not every language necessarily has. All these functions understand that `"1"` is 1. In other languages, it's often different. Why? Well, during type casting, an operation often occurs directly on values in memory. Let's recall that fragment about how a computer stores text in memory. ASCII, UTF-8, Unicode, and so on. Go back to previous chapters if you need to.

Exactly, so how? As numbers appropriately mapped later. Therefore, in other languages, instead of interpreting `"1"` as 1, it's often cast to the numeric value that hides behind the character `1` in a given character set/encoding. In our case, `"1"`, that is, one in text is marked not as `0b1` but as `49` which is `0b110001` or `0x31`.

By the way - a small note. For quick conversion, you might be interested in the functions visible in the snippet below.

```python
>>> ord('1')
49
>>> bin(49)
'0b110001'
>>> hex(49)
'0x31'
>>> oct(49)
'061'
>>> chr(49)
'1'
```

So `ord`, `bin`, `hex`, `oct`, `chr`. Play around and read about them. Where? In the [Python documentation](https://docs.python.org/3/). Best in English. Summarize your conclusions and the effects of playing by writing an article in which you describe what each function is about, briefly characterize each type. Give examples for which functions don't work and guesses why. Alternatively, use the `help` function, e.g., `help(int)`.

Additionally, I'll show you a small trick:

```python
>>> dir(float)  # alternatively: dir(1.0)
['__abs__', '__add__', '__class__', '__coerce__', 
 '__delattr__', '__div__', '__divmod__', '__doc__',
 '__eq__', '__float__', '__floordiv__', '__format__', 
 '__ge__', '__getattribute__', '__getformat__', '__getnewargs__',
 '__gt__', '__hash__', '__init__', '__int__', '__le__', 
 '__long__', '__lt__', '__mod__', '__mul__', '__ne__', 
 '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__',
 '__radd__', '__rdiv__', '__rdivmod__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__',
 '__rpow__', '__rsub__', '__rtruediv__', '__setattr__',
 '__setformat__', '__sizeof__', '__str__', '__sub__', 
 '__subclasshook__', '__truediv__', '__trunc__', 
 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 
 'imag', 'is_integer', 'real']
>>> dir(str)  # alternatively: dir("text")
['__add__', '__class__', '__contains__', '__delattr__', 
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
 '__hash__', '__init__', '__le__', '__len__', '__lt__', 
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
 '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', 
 '_formatter_parser', 'capitalize', 'center', 'count', 'decode',
 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index',
 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

So the `dir` function. The dir function is a function that returns all available methods/attributes of a given object.

For now, don't worry about those that start with `__` or `_` and focus on those that start with normal letters. What are they though? Methods starting with `__` are so-called Python Magic Methods/Dunder Methods/Magic Methods. This is something we'll talk about later, but these are special types of methods/functions of a given object that are supposed to fulfill specific roles. Those that start with a single underscore `_` are private methods.

Python doesn't have encapsulation, which means that generally when we add some attribute/method to a class/object, we can't very effectively prevent others from calling it, even if we want the user not to have the ability to do so, because, for example, a given method is only auxiliary, **private**. The convention thus says that we should put an underscore before private variables, methods, and we as programmers shouldn't use such unless it's inside the definition. We'll talk about this later. In the meantime, you can Google about this whole encapsulation.

To summarize: using `dir` you can check what you can do on a given object, what methods/functions it has, etc. Useful.

Play around with this on the types you know.

### Examples of Basic Operations on Numbers

```python
>>> integer = 4
>>> second_integer = 9
>>> first_float = 2.0
>>> second_float = 6.0
>>> help(integer.conjugate)
>>> help(integer.numerator)
>>> integer.numerator
4
>>> integer.numerator
4
>>> integer.as_integer_ratio
<built-in method as_integer_ratio of int object at 0x7f5443904150>
>>> integer.as_integer_ratio()
(4, 1)
>>> integer.bit_count()
1
>>> integer.bit_length()
3
>>> integer.imag
0
>>> integer.real
4
>>> 4 * 2
8
>>> 4 ** 2
16
>>> 4 // 3
1
>>> 4 / 3
1.3333333333333333
>>> 5 // 3
1
>>> 5 % 3
2
>>> first_float.is_integer()
True
>>> first_float.as_integer_ratio()
(2, 1)
```

## Strings

### Brief Characteristics

Strings/text, character sequences, so-called strings. It's simply text. Usually at least, because they can also be some kind of byte collections, but we'll talk about that another time.

In Python3, UNICODE and usually utf-8 reign for regular strings. Of course, you can use other encodings using appropriate methods, but for now, we probably don't need to worry about that. In Python 2, it was somewhat different, so I'll only mention this for historical knowledge and won't elaborate too much on how the process looked there, as this is already a somewhat archaic approach and all modern programming languages assume the use of UNICODE and utf-8.

Strings in Python are declared in the following way:

```python
some_text = "foo"  # first way
another_text = 'bar'  # second way using ' instead of "
longer_text = """hahah
another line """
```

So it's simply text surrounded by `"` or `'`. Python allows the use of both double and single quotes. My practice is to prefer `"`. Technically speaking, the standard allows using either one or the other, as long as we don't mix them in one project. What does this mean?

If we already have some codebase/code/project, and we decide to use `'` instead of `"`, that's okay, let it be so, although it's not my preference, but let's not mix styles. The convention is to stick to one and have a unified style throughout the code. This means that if we start using single quotes somewhere, we should use them everywhere in that project. If double, then double. Did I mention that I prefer double quotes and consider them better? The creators of the code formatting tool - `black` - think the same, plus objectively double quotes have their advantages like better readability or easier use with English where we have a lot of `'` characters in text. No need to add an escape character.

Ah yes, the escape character. Let's talk about special characters. What if in our text, which we defined using `"`, we need to use that character too? Let's try.

```python
quote = "chciałbym tutaj zacytować "paula coelho" ale nie wiem czy moge"
```

The given code won't work. Why? Python can't guess that you want to quote here and this character should be treated specially, not as usual. You need to tell it about this. How? Simple thing.

```python
quote = "chciałbym tutaj zacytować \"paula coelho\" i wiem, że mogę"
```

Simply add `\` before the character you want to treat in a special way. Now it might dawn on you why `"` > `'`. In English, single quotes often appear. If we use them to define strings, a problem arises in the form of having to often use the escape character. If we use double quotes, then less often. So the reason is laziness and code readability, which is also laziness. Yay!

Anyway, let's get back to the main topic.

Strings defined this way must fit in one line. If we want our text to be multiline in the code, we need to use triple quotes - so either `"""` or `'''` instead of one. This will cause Python to read not only to the end of the line but until it finds the closing character, which can be in another line.

It's also worth noting that for commenting in code, we use `#` for single-line comments and multiline strings as multiline comments.

```python
class RedirectMixin:
    """
    Mixin that is used for the purpose of...
    """
```

Example above.

Remember to use `dir` on strings and review the basic methods that Python has in the standard library that allow us to manipulate strings.

### Single Characters

Hmm, if strings are character sequences, what about single links in these chains? Well, imagine that you can iterate over text strings like over a list, plus we have access to their individual elements, to slicing, etc. NEAT!

### Variables in Text

Besides simple strings that just contain hardcoded text, for example:

```python
name = "Aryo"
```

There is the possibility of performing operations on strings that allow us to insert variables into text, add strings, etc. There are several ways to achieve this. Instead of elaborating, I'll just present them.

```python
age = 23
name_and_age = f"Olaf {age}"
name_and_age = "Olaf {age}".format(age)
name_and_age = "Olaf " + str(age)
```

The first method is called f-strings. They are elegant. Beautiful. Awesome. Proper.

The second option is the format function.

The third is so-called concatenation.

Which one to use and when? F-strings ftw. Format is okay, and concatenation when you can't use anything else.

### Using Variables in Text - Performance

I'm quite a big fan of f-strings in Python. I like them, they're elegant, readable, and simple to use. However, I was curious about how they perform under the hood, because, well, that elegance probably has some hidden cost. Nothing in life is free, right? I decided to check and compare different methods of string manipulation in Python in terms of performance.

In the competition were: f-strings, string concatenation (addition), the join() method, and the format() method. The % operator was not included in the comparison. Why? I don't really like it, to be honest. My personal preference. I believe it should be avoided for certain reasons. A relic of the past, we have better solutions today.

#### Testing Methodology

I tested using Python's built-in timeit module, running commands from the terminal. All variables used in the modified string were defined and loaded before timing began.
Each command was run in loops of 1,000,000 iterations, with each such loop run 3 times. From this loop, the shortest single iteration time was selected. Let's move on to the testing itself.

#### Comparison

Let's begin then. Below is the code I used. Forgive the primitive variable names, but I wrote it completely on the fly.

```bash
python3 -m timeit -s "x = 'f'; y = 'z'" "f'{x} {y}'" # f-string
python3 -m timeit -s "x = 'f'; y = 'z'" "x + ' ' + y" # concatenation
python3 -m timeit -s "x = 'f'; y = 'z'" "' '.join((x,y))" # join
python3 -m timeit -s "x = 'f'; y = 'z'; t = ' '.join" "t((x,y))" # join2
python3 -m timeit -s "x = 'f'; y = 'z'" "'{} {}'.format(x,y)" # format
python3 -m timeit -s "x = 'f'; y = 'z'; t = '{} {}'.format" "t(x,y)" # format2
```

Everything is quite simple. I considered two options, one standard and another where the method lookup would occur in the setup, and in the measured time only its call would occur.

What do I mean when I say the method will be found using the . operator? Well, Python underneath stores class attributes/method names and so on in a hashed dictionary. So when we write `object.attribute`, underneath there's a dictionary lookup to see if such a thing exists in that class. This of course adds to the execution time because the lookup instructions take time, albeit very little, almost nothing, but still, plus the time needed to allocate memory and add elements to the dict underneath when constructing the instance. For certainty, I tested different cases. I'll note, however, that in production code, you should generally avoid this type of optimization, okay? At a junior level, it's rare that you'll be processing such large datasets and your code will require such performance that you need to do these things. Just a warning. Anyway.

I did the same with join and format. Here I considered two options - normal call with lookup and one without it.

And here are the results:

```
f-string: 10000000 loops, best of 3: 0.0791 usec per loop
concatenation: 10000000 loops, best of 3: 0.0985 usec per loop
join without lookup: 10000000 loops, best of 3: 0.112 usec per loop
join: 10000000 loops, best of 3: 0.144 usec per loop
format without lookup: 1000000 loops, best of 3: 0.232 usec per loop
format: 1000000 loops, best of 3: 0.264 usec per loop
```

#### Surprise

I'll be honest, I didn't expect that f-strings would not only be an elegant solution but also the fastest! This makes me very happy.
In second place was concatenation, join without lookup, join, format without lookup, format, and at the very end template string. Since the optimization I made is quite impractical and probably no one would create such monsters in code except for certain exceptions that perhaps should be written in C rather than Python, I'm not including the results without lookups in the ranking, which looks like this:

1. f-string
2. Concatenation
3. join()
4. format()

#### A Slightly More Complex Example

I showed a simple example - inserting two variables separated by a space. What if we have more than 2 variables? Let's assume a case with 13 variables that we want to join with a space. Code:

```python
a, b, c, d, e, f, g, h, i, j, k, l, m = [str(s) for s in range(13)]
# f-string
f"{a} {b} {c} {d} {e} {f} {g} {h} {i} {j} {k} {l} {m}" 
# concatenation
"a + ' ' + b + ' ' + c + ' ' + d + ' ' + e + ' ' + f + \
' ' + g + ' ' + h + ' ' + i + ' ' + j + ' ' + k + ' ' + l + ' ' + m"
# format
"{} {} {} {} {} {} {} {} {} {} {} {} {}".format(
    a, b, c, d, e, f, g, h, i, j, k, l, m
)
# join
" ".join((a, b, c, d, e, f, g, h, i j, k, l, m))
```

I ran the code above analogously to the previous time.

I'm curious how the situation will look here.

Results:

```
join: 1000000 loops, best of 3: 0.352 usec per loop
f string: 1000000 loops, best of 3: 0.399 usec per loop
format: 1000000 loops, best of 3: 0.872 usec per loop
concat: 1000000 loops, best of 3: 1.13 usec per loop
```

Based on the previous results, they didn't surprise me much. Why?
Let's start with what changed. Join jumped from 3rd place to 1st. Concatenation dropped from 2nd to second to last. Format to 3rd from fourth. Quite reasonable, why.

First place for join in such a situation is obvious - look at what we're doing - we're joining many strings with a common string, which is exactly what join was created for. I'm almost certain that underneath at the implementation level or even interpreter level, there are optimizations made for this, thanks to which join handles a large number of arguments very well. This makes me happy - again, the solution that looks most elegant in this case comes out on top.

Second place f-string. Here I wasn't surprised either. Why? Well, f-strings, originally they were slow, very slow - in the first implementation they were "compiled" to nothing else than a set of appropriate joins or formats, I don't remember. However, in the next implementation, f-strings got their own, optimized OPCODE in CPython, which allowed for significant savings and better adaptation of the C code that's underneath.

Why did format overtake concatenation? Well, I suspect. It seems to me that it's about evaluation. Perhaps Python, because strings are immutable in Python, each time it performed an addition operation on two strings, had to allocate a new piece of memory that would fit X characters, where X is the sum of the lengths of two strings, then copy them there to get the final value. Based on experience with how Python works, I'd bet that in our case, when we had code in the form a + ' ' + b + ..., Python performed each addition operation separately. That is, probably the instructions underneath looked like this:

1. Allocate memory that will fit variable a and string ' '.
2. Copy value a
3. Copy value ' '
4. Add the obtained result to variable b.
5. Allocate memory that will fit the previous result and variable b.
6. ...

And so on. And all this costs time - new allocations, copying. At least that's how I think it worked, I'm not sure if Python developers haven't made some optimizations for this case and maybe they do it differently? I don't know, I haven't looked that deep, but looking at the results, I don't think so.

#### Summary - About Performance

In Python, mechanisms that seem elegant in a given situation are usually optimized and prepared for such, hence it's worth using them. This snake is simply beautiful. Elegant code.

So use f-strings wherever you can and enjoy life, where you have many strings to join in a predictable way, use join. This way your code will be prettier but also faster!

### Examples of Basic String Operations

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', 
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
 '__hash__', '__init__', '__le__', '__len__', '__lt__', 
 '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', 
 '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', 
 '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', 
 '_formatter_parser', 'capitalize', 'center', 'count', 'decode',
 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index',
 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 
 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 
 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text = "some text"
>>> text.capitalize()
'Some text'
>>> text.count("t")
2
>>> text.replace("t", "f")
'some fexf'
>>> coolest_org = "NAFO"
>>> coolest_org.lower()
'nafo'
>>> coolest_org_lower = coolest_org.lower()
>>> coolest_org + coolest_org_lower
'NAFOnafo'
>>> "RuSSia" + "HATE" "CLUB"
'RuSSiaHATECLUB'
>>> 'test' * 10
'testtesttesttesttesttesttesttesttesttest'
>>> coolest_org = "nafo"
>>> coolest_org = coolest_org.upper()
>>> coolest_org
>>> 'NAFO'
>>> coolest_org.swapcase()
>>> 'nafo'
>>> coolest_org.isalpha()
>>> True
>>> coolest_org.find("F")
>>> 2
>>> "AaBbCcDd"[::2]
>>> 'ABCD'
```

Note that strings are immutable. This means that we cannot modify them and any modification results in a new string being created. We'll talk more about mutability later when we discuss lists and tuples.

## Bytes

### Brief Characteristics

Hmm, bytes. Yes, this is a basic and simple type in Python, it's simply a sequence of bytes as the name suggests. Useful for file operations. Read about it yourself.

## Boolean Type

### Brief Characteristics

Here things look simple - the boolean type is the so-called bool - either true or false. A type of length 1 bit. Either 0 or 1, either `True` or `False`.

### True Values vs False Values

Usually used in conditions, setting flags, and so on. It's worth noting that in Python the boolean type is somewhat extended. That is, anything that can be evaluated to certain things will be treated as a boolean type. Simply put, False is zero or something empty. True is any number other than zero or something non-empty. An empty string is False, some text is True. An empty list is False. A non-empty one is the opposite.

```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool(0.1)
True
``` 

The code above when compiled and run will give us:

```bash
numbers in general: 0x7ffc9f728f20 -- 0x7ffc9f728f20
number no. 0: 0x7ffc9f728f20 -- 0x7ffc9f728f20 -- value: 1
number no. 1: 0x7ffc9f728f24 -- 0x7ffc9f728f24 -- value: 2
number no. 2: 0x7ffc9f728f28 -- 0x7ffc9f728f28 -- value: 3
number no. 3: 0x7ffc9f728f2c -- 0x7ffc9f728f2c -- value: 4
int size: 4
```

Let's analyze what's going on here.

Before we do that, I'll just note that if you ran this code on your machine, you might have gotten slightly different results. That's normal.

For most people unfamiliar with C/C++, this code might seem a bit cryptic, but it's actually quite simple.

Let's start with the line:

```c
printf("numbers in general: %p -- %p\n", &numbers, numbers+0);
```

I assume the first part of the print is understandable to everyone, except maybe `%p` - this simply tells us that the argument to print will be a specific data type.

And what's this whole `&numbers` - the & operator says that I want to get the address of a given variable - that is, its location in memory. Because as we well know, variables are allocated in memory, in a certain place chosen by the computer. Again - we talked about this in chapters 4 and 5.

This place is usually described as an 'address' - that is, the number of bytes/bits from the 'beginning' of memory that the processor must 'jump' to reach a given variable.

Our array (which is kind of like a Python list, but not quite) is located at address: 0x7ffc9f728f20 (hexadecimal notation), and this is also the address of our first element.

However, the compiler needs to know at what address the next element of our array is located. How? I've already explained this and I'm counting on your answer. You'll find mine below.

We declared that the elements of our array will be of type `int`. The `int` type on the computer I'm using is 4 bytes, or 32 bits. This is basically standard (although officially the standard says that int should just be at least 16 bits, it doesn't specify its size exactly), but sometimes there are exceptions to the rule, depending on the architecture, hence the `sizeof(int)` in the code - it returns the size of a given type in the current environment.

Therefore, if 0x7ffc9f728f20 is the address of the first element, which occupies 4 bytes in memory at addresses:

- `0x7ffc9f728f20`,
- `0x7ffc9f728f21`,
- `0x7ffc9f728f22`,
- `0x7ffc9f728f23`,

then we can deduce that the next element of this array will be after it, at address `0x7ffc9f728f24`, that is, 4 bytes further. The next one again another 4 bytes and so on, until the last element. A simple formula can be extracted from this.

The address of a specific array element can be determined by the formula:

$first\_element\_address+(index*type\_size)$.

*The computer uses this formula - every time you write `numbers[index]` the compiler internally translates it to*

$(numbers+(index*type\_size))$.

What does `*` mean for the compiler? Nothing else than 'go to the given address and take the value at that address.'

So when we write numbers[0], our compiler will translate it to

$(0x7ffc9f728f20+0)$=$(0x7ffc9f728f20)$,

which in turn means: take the value from this address and insert it here.

In the case of numbers[1], for example, it will be

$0x7ffc9f728f20+(1*sizeof(int))$ = $0x7ffc9f728f20+(1*4)$

$0x7ffc9f728f20+(1*4)$ = $0x7ffc9f728f20+4$

that is

`0x7ffc9f728f24`.

Clear? For me it is. If you have trouble understanding this concept, don't worry, many people don't fully understand pointers, addresses, and memory. I had trouble with it too. At least at the beginning.

You can help yourself with [Gynvael's videos - Gynvael's Code: Pointers #1](https://www.youtube.com/watch?v=bewTJaboGIw) or [lectures from CS50 - Harvard course](https://www.youtube.com/watch?v=PYJYiBlto5M) they, as people with much more knowledge, explain the whole issue much better than I do.

### What Would It Look Like If We Indexed from 1?

Let's assume we index from 1. Then the formula would have to be modified - and it would look like this:

$first\_element\_address+((index-1)*type\_size)$

Another solution would be to shift the location of the first array element 4 bytes forward relative to the array's address itself, but then our array would occupy additional space in memory unnecessarily, as those first x bytes, where x is the size of the given data type, would simply be empty. That's one thing, and two, you would have to remember that the array's address is not the address of its first element.

Both these solutions are nonsensical, because while it's not much - a few bytes on each array, or one subtraction operation, when we multiply it by the number of such variables we have in memory, it adds up to quite a substantial sum of bytes/operations that are, in essence, unnecessary.

Additionally, how much code is already based on zero-based indexing. It would be impossible to change all of this.

Of course, there are also other arguments for indexing or counting elements from zero, such as [those advocated by Dijkstra - Why numbering should start at zero](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html)]. That's quite a well-known and important gentleman, for those who don't know ;)

Overall, I used some simplifications and mental shortcuts here, but the general concept is conveyed.

### Examples of Basic Operations on Lists

## Tuples

### Brief Characteristics

A tuple is really nothing more than an immutable list. What does this mean? More or less that after declaring a tuple, it can't be modified anymore. We declare once and that's it. This carries many consequences which I'll tell you about soon.

The only thing you can do with a tuple is read it, copy it, or redeclare a variable with a given name. Examples below.

Why do we need these tuples? Generally, data immutability often makes it harder to shoot yourself in the foot with certain things. Plus it's an approach more similar to functional programming, let's say. Immutability is quite cool.

Besides this, we have one more advantage here. Performance.

### Efficient Beast

Well, if it's an immutable data structure then the Python interpreter knows exactly how much memory to allocate plus for certain reasons this process happens somewhat faster. So here allocation beyond needs doesn't take place plus the instruction executes somewhat faster, Python knows what types are used, knows the specific data we used etc.

As an anecdote, I'll mention a story where using tuples reduced our memory usage from 4 GB to ~2.1 GB in a certain small web app. In other cases, the reduction was even more drastic.

### Examples of Basic Operations on Tuples

```python
dir(tuple)
['__add__', '__class__', '__contains__', '__delattr__',
 '__doc__', '__eq__', '__format__', '__ge__', 
 '__getattribute__', '__getitem__', '__getnewargs__', 
 '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', 
 '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 
 'count', 'index']
In [9]: some_tuple = ("f", 1, 2)
In [10]: some_tuple[1]
Out[10]: 1
In [11]: some_tuple[1] = 2
In [13]: some_tuple.count(1)
Out[13]: 1
In [14]: some_tuple.count(2)
Out[14]: 1
In [15]: some_tuple.count(3)
Out[15]: 0
``` 

## Dictionaries

### Brief Characteristics

What is this magically sounding dictionary also known as Dict/HashMap? Well, it's nothing other than a kind of dictionary/mapping. Just as in a regular dictionary we have some kind of mapping of **keys** to **values** in the form of a word and its meaning, similarly it is in Python's dictionary/hashmap.

To the point.

A dictionary in Python is a data structure that allows us to store any values under specified keys. Imagine a list, but instead of a numerical index, you have an index in the form of a specified key.

In practice, it looks like this:

```python
>>> test_dict = {"test": "some_string", 1: "hehe", 2: 3}
>>> test_dict["test"]
'some_string'
>>> test_dict[1]
'hehe'
>>> test_dict[2]
3
```

Predictable. The rest works similarly to a list.

What's different from how a list works is that while in a list there is a guarantee that elements will always be in the order we put them into the list. A hashmap by definition doesn't provide such a thing. The current implementation of CPython, from version 3.8 or so, nevertheless provides something like this additionally, meaning that a regular `Dict` became an `OrderedDict`, however it's better not to count on this, as Python versions like 3.6 or 3.7 are quite new and there are lots of projects written in them. What does this mean? Well, that the code you will write will probably be run on a Python version that doesn't take into account and doesn't guarantee preservation of element insertion order, so it's better not to rely on this too much, because in most cases this order will be preserved anyway, but it's not guaranteed by implementation, meaning there will always be that 1% where something goes wrong. Then try getting such a bug for investigation.

Of course, if you are aware and know what you're doing, plus you have guarantees about which Python versions your code will run on, then go ahead. However, remember, in the newest version of Python -> okay, below 3.8 or 3.7 not necessarily. Check exactly in which version `OrderedDict` was introduced as default.

### How Does the Process of Adding Elements to a Dict Work?

Well, generally just as in the case of a list we had a numerical index, using which Python calculated the offset in memory, in the case of a dict we have something called a hash function. This function takes as an argument the key we're using and based on it tries to generate a fairly unique hash. Then based on the hash, usually through modulo operation, we figure out the address/offset where the given value is held.

Logical? So yes, every time someone writes `some_dict["key"]`, underneath something happens where the Python interpreter, to get the address from which to read the value for a given key, takes this key, throws it into a hash function, I don't know, let's say `hash("key")`, this function then returns us some possibly unique hash generated/calculated based on the given key. From the hash we conjure up an address/offset. Something like that.

Why fairly unique?

### Hash Collision

Hash collision is something that happens sometimes. Why? Well, the hash function can't be completely random. It must be stable and repeatable. This means that for a given argument it must always return the same thing, hash generation must happen in a predictable way. Why? Well, if it were otherwise, and for one key it would be possible to generate several hashes, then a problem would arise in the form that we could never, or sometimes we couldn't, hit the exact address where we originally assigned the value. What does this mean?

The lack of complete randomness means that hashing algorithms are limited to some extent. They are also limited by efficiency and the time that a computer can devote to hashing, which happens quite often however, without costs to the user. Therefore, a compromise had to be found between the complexity of the hash function and its resource consumption, execution time, and the uniqueness of provided hashes for different keys.

Currently, smart heads have figured out some golden mean, however in today's times it happens to operate on such large data sets that hash collision happens and the hash function generates the same hash for two different keys, causing one key to overwrite the other. A very, very rare case. However, if you have to process a million trillion records, then suddenly very rare cases have about 100% chance of appearing.

### What Can Be a Key?

A key in a dictionary can be any value/variable/object that is hashable. What does this mean? Well, that in its definition it contains an implementation of the `__hash__` method. In a big shortcut. That is, those objects for which a hash function has been implemented can be keys. Quite logical, because if we don't have a method to hash a given object then we won't calculate the hash. We won't calculate the hash from the key then we won't figure out the address/offset. Without this, we don't know where in memory to store the value. And therefore we must have this method implemented. Logical.

### Pass by Value & Pass by Reference

What's this about? About passing content by reference or by value. More precisely, it's about the fact that some objects Python will copy, as is the case with list slicing and getting its copy in a way that will share the internal elements of this object for both the copy and the original. I wrote about this a bit already when writing about lists.

I think it was explained fairly clearly there. Now this - why am I mentioning this in the context of dicts? Well, mutable data types are often passed by reference, meaning instead of the object itself, we get a reference to it. For this reason, for example, a list cannot be a key in a dictionary - it is mutable, passed by reference, and for this reason doesn't implement the `__hash__` method, making it unhashable, and therefore the dictionary implementation in Python, when trying to establish a new key that is a list, will throw an error.

Let's recall the code with which I illustrated passing by reference vs by value.

```python
>>> pass_by_reference = [[1,2,3], 1, 2, 3]
>>> new_pass_by_reference = pass_by_reference[:]
>>> pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> new_pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> pass_by_reference is new_pass_by_reference  # two different lists
False
# first element of list is another list
# lists are mutable and we pass them by reference
>>> pass_by_reference[0]  
[1, 2, 3]
# here we modify second element of this internal list from original
>>> pass_by_reference[0][1] = "test"
>>> pass_by_reference[0]
[1, 'test', 3]
# somehow list in copy also changed
>>> new_pass_by_reference
[[1, 'test', 3], 1, 2, 3]
>>> new_pass_by_reference[0]
[1, 'test', 3]
```

It's worth being careful about this, especially when choosing function arguments or establishing default values. Pass by reference -> we return the address and there the modification of the given object occurs. Pass by value -> we return the value itself and its 'copying' occurs fresh instead of modifying the variable at the given address, we get a new one. Another example:

```python
student = {"Putler": 10}
def test(student):
    new = {"Volodia": 20, "MonkeyMan": 21}
    student.update(new)
    print("Inside function", student)
test(student)
print("Outside function:", student)
```

As seen above, dict is passed by reference, that is by address so to speak. Python therefore goes to the given address and modifies the object, causing changes to spread to places where an inexperienced programmer might not expect. In the case of passing by value, the matter is different. The original object is not modified, only its copy.

```python
>>> student_name = "NAFO"
>>> def test(name_name):
...     student_name = name_name + " <3"
...     print("Inside: ", student_name)
>>> student_name
'NAFO'
>>> test(student_name)
('Inside: ', 'NAFO <3')
>>> student_name
'NAFO'
```

I don't know if this makes sense, maybe we'll come back to this. Analyze and search a bit on the net yourself about this topic to additionally clarify the situation.

### Shallow Copy and Deep Copy and Dictionary Keys

We have all this passing by reference, value etc. Let's talk now about shallow and deep copies. Briefly but briefly, but worth mentioning.

When we used slicing as a method of copying a list, we got a so-called shallow copy of this list. What does shallow mean? Namely, only the initial object, the object from the very top was copied. Everything inside that was passed by reference was not duplicated. Only references were copied. This is a shallow copy.

A deep copy is a copy where the interpreter 'enters' the object we're copying and copies everything by value, not by reference. This means that we get an actual, independent and standalone duplicate of the given object and not just its 'top level' as in the case of a shallow copy.

Sometimes needed. Worth knowing, because in some cases we think we have two different objects after copying using a shallow copy, we modify one object and bam, changes in both. This can cause really ugly bugs to debug. Not recommended.

### dict.values() keys() items()

Pay attention to these three methods. Play with them and summarize your conclusions. I'll just point out one thing.

What type of objects do the functions dict.keys(), dict.values(), dict.items() return? dict.items() - obvious. List of tuples. But not quite. Because if you look closer it's a dict_items class, which isn't quite a list – it's kind of an extended class, because it allows us to perform operations on it like on sets. Similarly with keys() and values(). So on objects returned by these functions, you can perform operations of sum, difference, or intersection from sets. Tldr – these functions return an iterable set-like object.

### Examples of Basic Operations on Dictionaries

```python
In [17]: dir(dict)
Out[17]:
[(...)
 'clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values']
In [18]: some_dict = {"NAFO": "OK", "SS": "NOT OK"}
""" dict_values is a set-like object on which
you can perform operations like on sets"""
In [19]: some_dict.values()  
Out[19]: dict_values(['OK', 'NOT OK'])
# dict_keys similarly
In [20]: some_dict.keys()
Out[20]: dict_keys(['NAFO', 'SS'])

In [21]: some_dict.items()
Out[21]: dict_items([('NAFO', 'OK'), ('SS', 'NOT OK')])
```

## Sets

### Brief Characteristics

What are sets? Analogously as in mathematics. It's kind of like a list, but without repetitions. At least apparently. Underneath it's somewhat different, because underneath sets are closer to a hash map. Actually, it is somewhat a hashmap. What for and why? Well, let's ask ourselves, what are the attributes of sets. Each element occurs only once. Not necessarily preserved insertion order. Starting to sound familiar? Yup. Sets are like hashmaps where values are also keys in a way.

What is the advantage of a set? First is element deduplication -> each occurs exactly once. We can extract 'statistics' from a given element, how many times it was added to the set, but in the set itself it will appear only once. The second is performance.

### Search Faster than in Warsaw's Wola

Searching in a set has computational complexity at the level of O(1) - constant time. What does this mean? Regardless of the size of the set to check membership of a given element in the set, we perform an operation that is characterized by constant execution time independent of size. So even for very very large sets, if they fit in memory, we can determine super quickly whether they are in a given set.

In the case of a list, it's not so easy, especially if the data is unsorted.

Why is this? Well, because underneath it's somewhat a hashmap, to check if an element belongs to the set it's enough to just calculate the hash of this element and then check if everything matches. Hence O(1) regardless of set size.

This in turn forces restrictions on what we can throw into the set. What kind? The same as with keys in dictionaries.

Additionally, the Python set also handles similar operations as a mathematical set. Conjunction, alternative, difference. A regular list can't handle all of this.

### Examples of Basic Operations on Sets

```python
In [22]: some_set = {1,2,3,4}
In [23]: another_set = {3, 4, 5}
In [24]: some_set
Out[24]: {1, 2, 3, 4}
In [25]: some_set | another_set
Out[25]: {1, 2, 3, 4, 5}
In [26]: some_set & another_set
Out[26]: {3, 4}
In [27]: some_set - another_set
Out[27]: {1, 2}
In [30]: dir(set)
Out[30]:
[(...),
 'add', 'clear', 'copy',
 'difference', 'difference_update', 'discard', 'intersection',
 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
 'pop', 'remove', 'symmetric_difference',
 'symmetric_difference_update', 'union', 'update']
In [31]: some_set.add(7)
In [32]: some_set
Out[32]: {1, 2, 3, 4, 7}
In [33]: some_set.add(7)
In [34]: some_set
Out[34]: {1, 2, 3, 4, 7}
```

## Summary

Phew, finally. Quite a chunk of text, right? And these are just selected Python types.

It's worth knowing them well, playing with them and getting familiar. Why? Well, in Python's standard library there are so many goodies, so many different things that make life easier, it's mind-boggling. It's a shame to reinvent the wheel and implement something yourself when the language provides its version.

Moreover, implementing from scratch is often also pointless for one very important reason. Well, your own implementation might be flawed because you check it, maybe people on Code Review, and that's it. However, when it comes to code that's in Python's standard library and contributors' implementations, the matter is that this code has been tested and reviewed by thousands of people. Mistakes happen, that's true. However, where are we more likely to find a bug? In code that has been reviewed by thousands of people, which is tested in millions of production applications and covered by many tests? Or in code that you and maybe your team reviewed? There's no comparison.

Additionally, I'll bet my hand, believing that thanks to the effort of thousands of contributors, code from Python's standard library will be better optimized. Use what has been built and don't reinvent the wheel by creating your own naive implementations of sorting algorithms or something. Sometimes there is such a need, true, but I doubt that you would have such as a junior wannabe.

That's why good knowledge of Python's standard library is necessary. Leave your own implementations for learning or fun purposes, to understand how something works. In production code, let's try to avoid this in favor of proven solutions from the standard library.

This not only makes the task easier but makes the code more solid, more optimized, and probably delivered faster. It's easier to put something together from ready-made blocks than to build a house yourself starting from extracting clay and firing bricks.

## Questions and Exercises

1. Is there dynamic typing in Python? Or maybe static?
2. What does this mean? What are its disadvantages, what are the advantages.
3. List the basic data types in Python.
4. And the more complex ones?
5. What are the differences between basic numeric types?
6. What does it mean that a value is `truthy` or `falsy` in Python? Give examples distinguishing what is what.
7. What are the ways of declaring text in Python?
8. What is an escape character and why do we use it?
9. What functions facilitate converting characters to numbers, to other encodings, which I mentioned?
10. Prepare an article in which you describe what each function is about, briefly characterize each basic type. Give examples for which functions don't work and guesses why. The target audience is other beginners. Let it be an extensive article full of your personal notes and not just Copy Paste from documentation. Give live examples.
11. Prepare a summary list for the basic data types you know in which you will present and briefly describe what methods/attributes particular types have and what each method does. Skip those that start with `__`. What command do you need to use here?
12. The same as in 11., but for complex types. Describe very thoroughly. You can combine the articles. Focus on showing practical use. Comment on the code and show examples other than here.
13. Send articles from 12. and 11. to olafgorski@pm.me and I'll check them and give feedback :)
14. Prepare a comparison table: list vs tuple vs set.
15. Experiment with really large numbers. Describe your conclusions.
16. Create code that will get a number from the user and then say whether it's even or not. How to get something from the user? Google if you don't remember.
17. Create a string and then swap its last letter with the first.

Remember that you can put your answers on GH here - https://github.com/grski/junior-python-exercises, and I'll check your solutions and give feedback. More about this in the 'Interactive Part' subchapter. 