\pagebreak

# Data Types

In the previous chapter, we talked about variables. While on that topic, it's worth mentioning the types of data our variables can store in Python. We'll talk about this specific language, but a similar division exists in most languages.

As I wrote in previous chapters, Python doesn't require us to define types for our variables; it doesn't have static typing. Remind yourself what that meant and answer the question - what does the lack of static typing mean? What is dynamic typing? What are its advantages/disadvantages? Look in the book, maybe in the answers to previous chapters. Do it now.

Despite this, it's good to know what types we usually divide variables into. Why? Because Python uses them too, it just kind of guesses what type we used. Depending on the type, different operations can be performed on the variable. If we think about it, it's logical, because although underneath it's all the same - binary code, on certain fragments that we interpret as X, we want to perform only operations from set Z, and when we interpret G, only from F. Speaking more simply, when we mark something as text, we'll treat it differently, or we can apply different modifications than when something is a number. On numbers we can perform arithmetic operations, while in text we can search for our name, for example. Different operations depending on the type. Logical, right?

So in Python we distinguish the following basic data types among others:

1. Numbers
2. Strings
3. Bytes
4. Boolean/logical type

From the more complex ones we have:

1. Lists
2. Tuples
3. Dictionaries
4. Sets

We'll discuss all of them in order shortly. Let's start with numbers, because that will probably take the longest.

## Numbers

### Brief Characteristics

So my dear friends, in Python we distinguish three main types of numbers: integers, floating-point numbers, and complex numbers, so like ints, floats, complex.

What does this mean?

### Integers

This should be simple, right? `1, -1, 5, 0, 938, -24861` are examples of integers, which are simply `regular` numbers without any commas, oddities, or inventions. I won't elaborate much more on them because there's no need.

Or is there?

Notice that in the examples above we have a negative number, less than zero. In the case of text, it's easy to write - just put a minus in front and done. As humans, we're taught to interpret this as a negative number. But how does the computer do it?

### Example Way of Representing Negative Numbers

Let's recall the previous chapters and what we discussed there. I showed, among other things, how the computer saves numbers in memory and how it represents them, namely using the binary system, bits, bytes, all that stuff. Now, a question arises: how then does the computer indicate that a given number is negative? After all, it can't just put a `minus` in memory somehow.

Well, let me present how it looks, again, in C. There have been many ways and ideas to solve this problem, and there still are, but let's just discuss one. Let's assume we're operating with some type that happens to be 1 byte in size. This means it has 8 bits in length. So how many values/numbers does it support maximum? Answer this question please, calculate.

Okay, having 8 bits, we have 8 zeros and/or ones at our disposal. So we can represent a maximum of 256 values, right? For example, numbers from 0 to 255. Well, not quite!

In the default case, we'll have 256 values available, true, but from a different range: from **-128** to **127**. This can be determined by the formula: from $-2^{n-1}$ to $2^{n-1}-1$, where n is the number of bits, so for 8 bits: from $-2^7$ to $2^7-1$

Where does this change come from? Well, because we take one bit to indicate whether the given number is positive or negative, in a nutshell. In C, if we know we're not interested in negative values, we can tell the compiler to shift the negative range to positive. Signed variables vs unsigned variables.

By the way, while we're at it, I'll add another curiosity. Did you know that even the way bits are ordered in memory is conventional? What does that mean? Well, some people couldn't agree on what's better, writing the highest-value bit first or last. Hence we have two standards: big endian and little endian. What does this mean and what does it look like in practice? Simple stuff.

Let's say we're talking about Big Endian. We want to write the value e.g. 0x4A3B2C1D at address 100. It would look like this:

| 100  | 101  | 102  | 103  |
| ---- | ---- | ---- | ---- |
| 4A   | 3B   | 2C   | 1D   |

And Little Endian?

| 100  | 101  | 102  | 103  |
| ---- | ---- | ---- | ---- |
| 1D   | 2C   | 3B   | 4A   |

So reversed. It's basically about which to write where. It makes a difference when converting/reading these values. Which is better? Big Endian will probably be easier to grasp, as it's analogous to the notation we use daily in the decimal system.

Different processors have different conventions, fortunately you don't have to worry about this in your code - the Python interpreter will do it for you.

### Floating-Point Numbers and the Imprecision of Their Representation

What are we dealing with here? Nothing other than numbers with a `decimal part` in simple terms. And basically that's it. If we see a number somewhere in Python where there's a dot - e.g. `1.0`, we must know that we're dealing with a floating-point number. Why is this important knowledge? Well...

Here, unlike integers, there are oddities, and big ones, but under the hood. It's a longer topic, but generally it comes down to the so-called imprecision of floating-point number representation in the binary system. Yes yes. Clear, right? I'll just say mysteriously that you should always and everywhere remember that using regular floats/doubles for precise calculations or storing information about money is not a great idea, because sometimes `0.1+0.2 != 0.3`. Why? Because try to exactly represent e.g. 1/3 using powers of two. Hard, isn't it? But what exactly do I mean?

Let's consider a simple program in C (the matter applies to practically every language):

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

Simple code, right? I think anyone should understand it if they know even the basics of programming. The expected result for many people would be printing 'Equal' in the console, right? I also thought so at first. But check for yourself what happens when you compile and run the code.

Surprisingly "Equal" wasn't displayed. Why? Did something go wrong? The numbers are seemingly the same, because here's 0.1 and there's 0.1, what's up? Hm, maybe the variable was saved incorrectly. Let's print it and see.

```c
    printf("%f", example_float);
```

Add this line of code after the finished if. Run the code... And? Here's the result:

```
0.100000
```

Wait. So something is actually working incorrectly in our program, right? Because `example_float` is equal to 0.1, right? Well, no.

Here it's not visible because the precision is too low, but let's correct that, let's force the `printf` function to display our float with greater precision than the default, because as you can see, printf by default displays only 6 digits after the decimal point.

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

A slight modification to our code and everything's clear. Our `example_float` is not exactly equal to 0.1, but a tiny bit more. Why?

It all stems from the fact that the computer 'operates' in binary language. This means that when creating numbers, only powers of two are available, multiplied appropriately by 1 or 0, which can be summed (greatly simplified, we've talked about this already). It's no wonder then that our float looks like this. Because try from such numbers `{..., 1/128, 1/64, 1/32, 1/16, 1/8, 1/4, 1/2, 0, 1, 2, 4, 8, 16, ...}` to build exactly 0.1. It usually can't be done perfectly. Theoretically, in an imaginary world where we had an infinite amount of memory available and infinite time, we could get infinitely close, even reach it sometimes, to any number. But if you want more on that, read about limits or remember from high school and mathematics.

Hence this imprecision - it results only from how floating-point numbers are represented in computer memory. While in most cases, with a finite amount of memory, satisfactory precision can be achieved, there are cases where unfortunately that precision won't be sufficient.

For such cases, we have special libraries or perhaps a special approach that handles the topic differently, nevertheless it's worth knowing about this. That's why, if we're writing a program that has anything to do with money, it's worth thinking twice before using a float or double. Maybe it's better to keep dollars in a separate int and cents in a separate one? Who knows.

The solution to many problems related to floating-point numbers can be found in the `decimal` and `fractions` modules.

For reading:

1. https://docs.python.org/3/library/decimal.html
2. https://docs.python.org/3/library/fractions.html

### Complex Numbers

Very rarely encountered, but sometimes when someone does scientific calculations or other strange things, this knowledge might come in handy - these are numbers consisting of a real and imaginary part. Mathematical topics. If you don't know what it's about, don't worry.

We define them like this: `test = 21 +3j` or `some_complex_number = complex(32, 3)`. And we can perform the same operations on them as on numbers - division, multiplication, addition, and so on. Sometimes useful.

And that's it. For now that's all you need to know about things we qualify as numbers in Python. There are also e.g. decimals or rationals, but about those another time!

### Operations on Numbers

As I mentioned with complex numbers, on numbers we can perform all basic mathematical operations and they will work more or less as we'd expect. I'm talking about addition, subtraction, multiplication, division, floor division, modulo operation, and other basic arithmetic operations.

Operators that Python understands are:

| Operator | Action                                                       |
| -------- | ------------------------------------------------------------ |
| *        | Multiplication                                               |
| **       | Exponentiation, so 2 ** 3 means two to the power of three.   |
| /        | Regular floating-point division                              |
| +        | Addition                                                     |
| -        | Subtraction                                                  |
| //       | Floor division, so 5 // 2 equals 2, -11 // 3 equals -4 (note negative numbers) |
| %        | Modulo, so e.g. 5 % 2 is nothing other than the remainder of dividing 5 by 2, which is 1 |

It's also worth remembering that if we have several different types of numbers in one expression, Python will cast the result of the whole expression to the most complex type. What does this mean? The result of `1.0 + 1` will be not `2` but `2.0`, the result of `1 + 1.0 + 3 +0j` will be `5+0j`. So the order of complexity is:

Integer -> Floating-point -> Complex.

Worth remembering, as this carries certain consequences - just be careful with those dots, because sometimes you can get caught out.

Additionally, I'll mention syntactic sugar that allows us to shorten the notation of popular operations. It looks like this:

```python
foo = 2
foo = foo + 2 # this line is equivalent to the one below
foo += 2
```



### Numeric Conversions

Numbers can be 'converted' between each other, or perform a kind of `type casting` as we'd say in other strongly typed static languages. How? Examples below. Analyze them a bit yourself.

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

Play with the functions `int`, `float`, `complex`. Then describe what each of them does. What values they accept, what causes errors. The last example `int("1.3")` caused an error. Translate it and try to explain what happened here.

It's worth noting one important thing that Python provides out of the box, which not necessarily every language has. These functions understand that `"1"` is 1. In other languages it's different. Why? Well, during type casting, an operation often happens directly on the value in memory. Let's recall that fragment about how the computer stores text in memory. ASCII, UTF-8, Unicode, and so on. Go back to previous chapters if you need to.

So how exactly? As numbers appropriately mapped later. So, in other languages it happens that instead of interpreting `"1"` as 1, it often casts to the numeric value that hides behind the character `1` in the given character set/encoding. In our case `"1"`, meaning one in text is not marked as `0b1` but as `49` which is `0b110001` or `0x31`.

By the way - a small note. For quick conversions, you might be interested in the functions you can see in the snippet below.

```python
>>> ord('1')
49
>>> bin(49)
'0b110001'
>>> hex(49)
'0x31'
>>> oct(49)
'0o61'
>>> chr(49)
'1'
```

Namely `ord`, `bin`, `hex`, `oct`, `chr`. Play and read. Where? In [Python documentation (https://docs.python.org/3/)](https://docs.python.org/3/). Best in English. Summarize your conclusions and play results by writing an article in which you describe what each function is about, briefly characterize each type. Give examples for which functions don't work and guesses why. Alternatively use the `help` function e.g. `help(int)`

Also, I'll show you a little trick:

```python
>>> dir(float)  # alternatively: dir(1.0)
['__abs__', '__add__', '__bool__', '__ceil__', '__class__',
 '__delattr__', '__divmod__', '__doc__', '__eq__', '__float__',
 '__floor__', '__floordiv__', '__format__', '__ge__',
 '__getattribute__', '__getnewargs__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__int__', '__le__',
 '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
 '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__',
 '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__',
 '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__',
 '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex',
 'imag', 'is_integer', 'real']
>>> dir(str)  # alternatively: dir("text")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']
```

The `dir` function. The dir function is a function that returns all available methods/attributes of a given object.

For now, don't worry about those that start with `__` or `_` and focus on those that start with normal letters. But what are they? Methods starting with `__` are the so-called Python Magic Methods/Dunder Methods. It's something we'll talk about later, but these are special types of methods/functions of a given object that are meant to fulfill specific roles. Those that start with a single underscore `_` are private methods.

In Python there's no encapsulation, which means that generally if we add some attribute/method to a class/object, we can't very effectively prevent others from calling it, even if we want the user not to be able to do so, because e.g. the method is only auxiliary, **private**. The convention therefore says to put an underscore before private variables, methods, and we as programmers shouldn't use them unless it's inside the definition. We'll talk about this more later. In the meantime, you can google about encapsulation.

To summarize: using `dir` you can check what can be done on a given object, what methods/functions it has, etc. Useful.

Play with this now on types you know.

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

Strings/text, character sequences, so-called strings. It's simply text. Usually at least, because they can also be some collections of bytes sort of, but about that another time.

In Python3 for regular strings, UNICODE and usually utf-8 reign. Of course, you can use other encodings using appropriate methods, but for now we probably don't have to worry about this. In Python 2 it was a bit different, so only for historical knowledge I'll mention it and won't elaborate too much on how the process looked there, since it's already somewhat archaic and all modern programming languages assume the use of UNICODE and utf-8.

Strings in Python are declared as follows

```python
some_text = "foo"  # first way
another_text = 'bar'  # second way using ' instead of "
longer_text = """hahah
another line """
```

So it's simply text surrounded by `"` or `'`. Python allows using both double and single quotes. My practice is to prefer `"`. Technically speaking, the standard allows using both one and the other, just don't mix them in one project. What does that mean?

If we already have some codebase/code/project, and we decide to use `'` instead of `"` that's okay, let it be so, although it's not my preference, but let's not mix styles. The convention is to stick to one and have a unified style throughout the code. That means if we start using single quotes somewhere, let's use them everywhere in that project. If double, then double. Did I mention that I prefer double and consider them better? So do the creators of the code formatting tool - `black` plus objectively double quotes have their advantages like better readability or easier use with the English language where we have a lot of `'` characters in text. No need to add escape characters.

Ah yes, escape characters. Let's talk about special characters. What if in our text, which we defined using `"`, we'll need to use that character too? Let's try.

```python
quote = "I would like to quote "Paulo Coelho" here but I don't know if I can"
```

The given code won't work. Why? Python can't guess that you specifically want to quote here and this character should be treated specially, not as usual. You have to tell it. How? Simple thing.

```python
quote = "I would like to quote \"Paulo Coelho\" here and I know I can"
```

Simply add `\` before the given character that we want to treat specially. Now you might get a hint why `"` > `'`. Well, in the English language, single quotes occur frequently. If we use them to define strings, then a problem arises in the form of having to often use escape characters. If we use double quotes, it's less frequent. So the reason is laziness and code readability, which is basically also laziness. Yay!

Anyway, let's get back to the main topic.

Strings defined this way must fit on one line. If we want our text to be multiline in code, we must use the Triple character - so either `"""` or `'''` instead of one. This will cause Python to read not only to the end of the line but until finding the closing character, which can be in another line.

It's also worth noting that for commenting in code we use `#` for single-line comments and multiline strings as multiline comments.

```python
class RedirectMixin:
    """
    Mixin that is used for the purpose of...
    """
```

Example above.

Remember to use `dir` on strings and look through the basic methods that Python has in the standard library, which allow us to manipulate strings.

### Single Characters

Hm, if strings are character chains, what about individual links in these chains? Well, imagine that you can iterate over text strings like over a list, plus we have access to its individual elements, slicing, etc. NEAT!

### Variables in Text

Besides simple strings that just contain hardcoded text, for example:

```python
name = "Aryo"
```

There's the ability to perform operations on strings that allow us to insert variables into text, add strings, etc. There are several ways to achieve this. Instead of writing about it, I'll just present it.

```python
age = 23
name_and_age = f"Olaf {age}"
name_and_age = "Olaf {}".format(age)
name_and_age = "Olaf " + str(age)
```

The first way we call f-strings. They're elegant. Beautiful. Cool. Proper.

The second option is the format function.

The third is so-called concatenation.

Which to use and when? F-strings ftw. Format is fine, if you can't do otherwise then concatenation.

### Using Variables in Text - Performance

I'm quite a big fan of f-strings in Python. I like them, they're elegant, readable, and easy to use. However, I was curious how they perform under the hood, because well, that elegance probably has some hidden cost. Nothing in life is free, right? I decided to check and compare different string manipulation methods in Python in terms of performance.

The competition included: f-strings, string concatenation (adding), the join() method, the format() method. The % operator wasn't included in the comparison. Why? I just don't like it honestly. My personal preference. I think it should rather be avoided for certain reasons. A relic of the past, we have better solutions today.

#### Testing Methodology

I'll be testing using the timeit module built into Python, calling commands from the terminal. All variables used in the modified string will be defined and loaded before timing begins.
Each command will be run in loops of 1000000 iterations, each such loop will be run 3 times. From that loop, the shortest single iteration run will be determined. Let's get to the testing.

#### Comparison.

Let's begin then. Below is the code I used. Forgive the primitive variable names, but I wrote it completely off the cuff.

``` bash
python3 -m timeit -s "x = 'f'; y = 'z'" "f'{x} {y}'" # f-string
python3 -m timeit -s "x = 'f'; y = 'z'" "x + ' ' + y" # concatenation
python3 -m timeit -s "x = 'f'; y = 'z'" "' '.join((x,y))" # join
python3 -m timeit -s "x = 'f'; y = 'z'; t = ' '.join" "t((x,y))" # join2
python3 -m timeit -s "x = 'f'; y = 'z'" "'{} {}'.format(x,y)" # format
python3 -m timeit -s "x = 'f'; y = 'z'; t = '{} {}'.format" "t(x,y)" # format2
```

Everything quite simple. I considered two options, one standard and one where finding the method happens in setup, and in the timed part only its invocation.

What do I mean when I say the method will be found using the . operator? Well, Python under the hood does something like keeping the attributes of a given class/method names and so on, hashed in a dictionary. So when we write `object.attribute`, under the hood there's a search in dictionary/dictionary lookup for whether something like this is in this class. This obviously adds execution time because the lookup instructions themselves take time, granted not much, almost nothing, but still, plus there's the time needed to allocate memory and add elements to the dict under the hood when constructing the instance. For certainty, I tested different cases. I'll note, however, that in the case of production code, rather refrain from these kinds of optimizations, okay? At a junior level, it's rather rare that you'll be processing such large data sets and your code will require such performance to do such things. Just a warning. Anyway.

I did similarly with join and format. Here I considered two options - normal call with lookup and without it.

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

I'll be honest, I didn't expect that f-strings are not only an elegant solution but also the fastest! This makes me very happy.
In second place came concatenation, join without lookup, join, format without lookup, format, and at the very end template string. Because the optimization I made is quite impractical and nobody will create such monsters in code except for certain exceptions that perhaps should be written in C and not Python, I'm not including results without lookups in the ranking, which looks like this:

1. f-string
2. Concatenation
3. join()
4. format()

#### A Slightly More Complicated Example

I showed a simple example - inserting two variables separated by a space. What if we have slightly more than 2 variables? Let's assume a case with 13 variables that we want to join with a space. Code:

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
" ".join((a, b, c, d, e, f, g, h, i, j, k, l, m))
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

Based on previous results, they didn't surprise me much. Why?
Let's start with what changed. Join jumped from 3rd place to 1st. Concatenation dropped from 2nd to second-to-last. Format to 3rd from fourth. Pretty justified, here's why.

First place for join in such a situation is obvious - look at what we're doing there - we're joining many strings together with a common string, which is exactly what join was created for. I'm almost certain that under the hood at the implementation level of the method or even interpreter there are optimizations made for this, which is why join handles a large number of arguments well. This makes me happy - again, the solution that looks most elegant in this case comes first.

Second place for f-string. I wasn't surprised here either. Why? Well, f-strings, originally were slow, very slow - in the first implementation they were "compiled" into nothing other than a set of appropriate joins or formats, I don't remember. Nevertheless, in the next implementation, f-strings got their own optimized OPCODE in CPython, which allowed for significant savings and better adaptation of the C code underneath.

Why did format beat concatenation? Well, I guess. It seems to me it's about evaluation. Perhaps Python, because strings are immutable in Python, every time it performed an addition operation on two strings, had to allocate a new piece of memory that would fit X characters, where X is the sum of lengths of two strings, then copy them there to get the final value. From experience with how Python works, I'd bet that in our case, when we had code in the form a + ' ' + b + ..., Python executed each addition operation separately. That is, probably the instructions underneath looked like this:

1. Allocate memory that will fit variable a and string ' '.
2. Copy value of a
3. Copy value of ' '
4. Add the received result to variable b.
5. Allocate memory that will fit the previous result and variable b.
6. ...

And so on. And all this costs time - new allocations, copying. At least I think that's how it worked, I'm not sure, however, whether Python developers didn't make some optimizations for this case and maybe they do it differently? I don't know, I didn't look that deep, but looking at the results, I don't think so.

#### Summary - on Performance

In Python, mechanisms that seem to look elegant in a given situation are usually optimized and prepared for it, hence it's worth using them. Beautiful snake, simply. Elegant code.

So use f-strings wherever you can and enjoy life, where there are many strings to join in a predictable way, join. This way your code will be not only prettier but also faster!



### Examples of Basic String Operations

```python
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__',
 '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
 '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle',
 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']
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

Note that strings are immutable. Meaning we can't modify them and each modification causes a new string to be created as a result. We'll talk about mutability a bit later when we discuss lists and tuples.

## Bytes

### Brief Characteristics

Hmmm, bytes. It's indeed a basic and simple type in Python, it's simply a sequence of bytes as the name suggests. Useful for file operations. Read on your own.

## Boolean/Logical Type

### Brief Characteristics

Here things are simple - the logical type is the so-called bool - either true or false. A type 1 bit long. Either 0 or 1, either `True` or `False`.

### Truthy vs Falsy Values

Usually used for conditions, setting some flags, and so on. It's worth noting that in Python the logical type is somewhat extended. This means that anything that can be evaluated to certain things will be treated as a logical type. Speaking more simply, False is zero or something empty. True is any number other than zero or something non-empty. An empty string is False, some text is True. An empty list is False. Non-empty is the opposite.

```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool(0.1)
True
>>> bool([])
False
>>> bool(["f"])
True
>>> bool("String")
True
>>> bool("")
False
```

A small note. The `bool` function is something in Python that tries to 'convert' the given value to a `boolean`, i.e., logical/boolean type. The rules I presented above. Other types also have their equivalents, play with them.

### Examples of Basic Operations on Boolean Type

## Lists

### Brief Characteristics

What is a list? A list is nothing other than a mutable collection of elements. A kind of 'array'. You can think of it in terms of a string. Why? Because what is a string if not a list of characters? It's simply a certain area in memory that is mutable. What does that mean? Well, it means that a list is a collection of elements that can be freely modified after declaration. A list can be reduced, elements can be deleted from it. Elements can be added to it. They can be removed again. The size of the list can be changed. Individual elements can be overwritten. Whatever you want, you have it.

A list can consist of practically any elements, meaning almost any Python object can be put into a list. It's not always so. In other programming languages, it's often the case that when we define an array, first of all its length is known in advance, unless we use dynamic arrays, two, its elements are often limited to only one type for various reasons. Why?

### Lists from a Low-Level Perspective

One of the reasons will be something that refers back to the very beginning of this book, where we described the issue of when the program knows where to stop reading memory when reading a variable from a given address.

Well, here a similar analogy applies. E.g., in C when declaring an array/list, you give its length and type. Why? So that the compiler/program can figure out how much memory to allocate and how to handle addresses, where to stop reading, etc.

So a 10-element char array will allocate memory of size `10 * size(char)` in C. The computer will know where, and what, and how to read, when to finish.

Let's assume our array is at address `0x1` and inside it are 4 elements, each one byte in size:

| Bit (hex)   | 0x01 | 0x02 | 0x03 | 0x04 |
| ----------- | ---- | ---- | ---- | ---- |
| **Value** | A    | B    | C    | D    |

Here, recall how memory looks, how many bits we standardly use to write a single character, let's assume ASCII in this case, and how to convert from hexadecimal to decimal/binary.

We've now visualized a bit how it looks in the case of e.g., C and an array/list with the same type and known length. What about Python?

### References and Values

In Python, it's a bit different, but similar. Well, one could ask: so how does Python know when to stop reading a given address, since underneath it's also most often C, at least in CPython's case? Well, a list in Python isn't really a list of values with given types but rather a list of references. What's that? Well, Python, when we create a list, actually stores a collection of references to given values, not the values themselves. So going back to our earlier analogy and comparison with C, where we had to declare the type of values in the array, suddenly everything makes sense. It turns out that in Python, underneath, we also have in a sense one kind of value - references. References are, simplified, pointers to some objects. An object can be e.g., another list or an instance of some class.

So in Python, our array in memory will look +/- like this:

| Bit (hex)   | 0x01        | 0x09        | 0x11        | 0x19        |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **Value** | Reference1 | Reference3 | Reference2 | Reference4 |

Random order. Now when we read a value from the list, Python will go to what e.g., `Reference1` hides and take what it needs, regardless of type. This is how seemingly different types can be in one list in Python without causing problems.

One complication explained. Time for the second -> dynamic size.

### Dynamic Size of Lists

Okay, time to explain how it magically happens that lists in Python have dynamic size, despite the fact that e.g., in C, so far, I wrote about needing to give the size. Well, the thing is, in Python, underneath, it's the same. The Python interpreter looks at how many elements we created the list with and then 'guesses' how many elements to allocate in the array.

What happens when we change the list size/add new elements?

### Allocating Beyond Needs - The Greedy and Cunning Snake

Generally, the case here is that Python during declaration of some list allocates more memory than we need! WHAT?! HOW?!

Yep. Generally it's usually about $2n$ assuming $2n>=2$ where n is the number of elements. So even when we initialize an empty list, Python underneath allocates space for at least two elements, or more. I don't even remember. Why? Well, because the interpreter expects that we'll be adding more elements. If we reach the given size and try to add another element, then new memory allocation happens, again the process described a moment ago and memory reallocation, after which values from the old place in memory/old list are copied to the new place where we have a larger fragment of memory allocated, and the whole thing is dynamically swapped where needed in such a way that we, as programmer/end user, don't even notice.

As you can see, Python does many things for us so we don't have to worry about them. Of course, this has its cost in computational or memory performance, but unfortunately, something for something. Python isn't fast, but it's fast enough, but you've already read that essay - in the chapter about Python's pros and cons.

I'm describing the whole process here in very simplified terms, but more or less that's how it looks.

### Accessing List Elements

Access to list elements happens by giving the index of the element we want to reach. Because we know the size of the reference, we know by how much to offset in memory. We've already talked about this. In code it looks like this:

```python
war_crimes = ["Russia on Ukraine", "Israel on Palestine"]
>>> war_crimes[0]
'Russia on Ukraine'
>>> war_crimes[1]
'Israel on Palestine'
>>> war_crimes[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Quite logical. Exceeding the array length will cause an error. One important note. In programming, we usually index from zero. Why? You'll find the basics of the answer in chapters 4 and 5, but for certainty I'll explain. Of course, there are exceptions to the rule, some languages index from 1 because they do and that's it, but we're talking about proper languages like C, Python, or Rust.

### Negative Indices

While usually in other languages such an institution as negative indices in the case of lists doesn't necessarily exist, in Python's case it certainly does. Using negative indices causes Python to start counting from the end of the list upward. Quite a simple concept.

```python
>>> numbers = [1,2,3,4]
>>> numbers[-1]
4
>>> numbers[-2]
3
```

### Slicing Lists

So-called slicing. What's it about? Well, having some list, we might get the need to operate on its piece or something. Who knows, people have strange needs. So what now? Copy, iterate through the given list ourselves? Absolutely not. Python has, as always, a built-in solution that allows us to simply and pleasantly achieve this effect. It's called slicing in English. How does it work?

```python
>>> numbers = [1,2,3,4, 5, 6, 7, 8]
>>> numbers[3:6]
[4, 5, 6]
# from first to fifth
>>> numbers[:4]
[1, 2, 3, 4]
# from fourth to end
>>> numbers[3:]
[4, 5, 6, 7, 8]
# from first to last
>>> numbers[::]
[1, 2, 3, 4, 5, 6, 7, 8]
# from first element of list, selecting every other element -> 2n+1
>>> numbers[::2]
[1, 3, 5, 7]
# from second element of list, then selecting every other element -> 2n
>>> numbers[1::2]
[2, 4, 6, 8]
 # from last element of list to end selecting then every other element
>>> numbers[-1::2]
[8]
 # from last element of list to end so just the last element
>>> numbers[-1:]
[8]
>>> numbers[-4:]
[5, 6, 7, 8]
>>> numbers[:-4]
[1, 2, 3, 4]
>>> numbers[::-1]  # easy way to reverse a list
[8, 7, 6, 5, 4, 3, 2, 1]
```

Slicing has the following syntax

```python
given_list[start_element:end_element:step]
```

Start or end element is a rather known concept. Step is simply information about which element to take.

Important information: slicing creates copies of the list, a fresh, brand new copy of the list. However, it's a shallow copy, not a deep one. What that means, I'll describe a bit further. Proof:

```python
>>> numbers is numbers[:]
False
```

As you can see, slicing causes copying and creating a new list underneath. Or differently. Memory will be copied to another place and duplicated this way, but the references inside will be the same. If the list contains references to an object that is pass-by-reference, then modifying that object will cause the value to change in both lists, the copied one too, but if something is pass-by-value (immutable types in most cases), then modification will affect only the list whose element we modified.

```python
>>> pass_by_reference = [[1,2,3], 1, 2, 3]
>>> new_pass_by_reference = pass_by_reference[:]
>>> pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> new_pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> pass_by_reference is new_pass_by_reference  # two different lists
False
# the first element of the list is another list
# lists are mutable and we pass them by reference
>>> pass_by_reference[0]
[1, 2, 3]
# here we modify the second element of that inner list from the original
>>> pass_by_reference[0][1] = "test"
>>> pass_by_reference[0]
[1, 'test', 3]
# somehow the list in the copy also changed
>>> new_pass_by_reference
[[1, 'test', 3], 1, 2, 3]
>>> new_pass_by_reference[0]
[1, 'test', 3]
```

Think about it. We'll probably talk more about this topic when discussing keys in dictionaries.

### Why We Index from Zero

I once stated somewhere that indexing from zero is logical and has its reasons, it's natural and is as they commanded. However, a comment came that it's actually the opposite and we, programmers, index from 0 just because we got used to it.

Well, no. [Although I once thought similarly myself](https://4programmers.net/Mikroblogi/View/8661#entry-8661), indexing from 0 is logical and has its justification. What?

```C
#include <stdio.h>

int main(void) {
    int numbers[] = {1,2,3,4};
    printf("numbers in general: %p -- %p\n", &numbers, numbers+0);
    for (int i = 0; i < sizeof(numbers)/sizeof(numbers[0]); i++) {
        printf("number no. %i: %p -- %p -- value: %d\n",
               i, &numbers[i], numbers+i, *(numbers+i));
    }
    printf("int size: %d\n", sizeof(int));
    return 0;
}
```

The code above compiled and run gives us:

```bash
numbers in general: 0x7ffc9f728f20 -- 0x7ffc9f728f20
number no. 0: 0x7ffc9f728f20 -- 0x7ffc9f728f20 -- value: 1
number no. 1: 0x7ffc9f728f24 -- 0x7ffc9f728f24 -- value: 2
number no. 2: 0x7ffc9f728f28 -- 0x7ffc9f728f28 -- value: 3
number no. 3: 0x7ffc9f728f2c -- 0x7ffc9f728f2c -- value: 4
int size: 4
```

Let's analyze a bit what's going on here.

Before we do, I'll just note that you, if you ran this code on your machine, might have gotten slightly different results. That's normal.

For most people unfamiliar with C/C++, this code may seem somewhat cryptic, but essentially it's quite simple.

Let's maybe start with the line

```c
printf("numbers in general: %p -- %p\n", &numbers, numbers+0);
```

I assume the first part of the print is understandable to everyone, maybe except `%p` - it just tells us that the argument to print will be a specific data type.

And what about this whole `&numbers` - the & operator says that I want to get the address of the given variable - that is, its location in memory. Because as we well know, variables are allocated in memory, in some place chosen by the computer. Again - we've already talked about this in chapters 4 and 5.

This place is usually described as an 'address' - that is, the number of bytes/bits from the 'beginning' of memory that the processor must 'jump' to reach the given variable.

Our array (which is kind of like a list from Python, but not quite), is at address: 0x7ffc9f728f20 (hexadecimal notation), and this is at the same time the address of our first element.

However, the compiler must know at what address the next element of our array is located. How? I've already explained and I'm counting on your answer. You'll find mine below.

We declared that the elements of our array will be of type `int`. The `int` type on the computer I'm using happens to be 4 bytes, or 32 bits. This is essentially the standard (although officially the standard says that int should simply be at least 16 bits, it doesn't specify its size exactly), but sometimes there are deviations from the rule, depending on the architecture, hence that `sizeof(int)` in the code - it returns the size of the given type in the current environment.

Therefore, if 0x7ffc9f728f20 is the address of the first element, which occupies 4 bytes in memory at addresses:

- `0x7ffc9f728f20`,
- `0x7ffc9f728f21`,
- `0x7ffc9f728f22`,
- `0x7ffc9f728f23`,

we can conclude that the next element of this array will be after it, at address `0x7ffc9f728f24`, that is, 4 bytes further. The next one again another 4 bytes and so on, up to the last element. From this we can extract a simple formula.

The address of a specific array element can be determined by the formula:

$first\_element\_address+(index*type\_size)$.

*The computer uses this formula - every time you write `numbers[index]` the compiler internally translates this to *

$(numbers+(index*type\_size))$.

What does `*` mean for the compiler? Nothing other than 'go to the given address and take the value located at that address.'

So when we write numbers[0], our compiler translates this to

$(0x7ffc9f728f20+0)$=$(0x7ffc9f728f20)$,

which in turn means: take the value from this address and put it here.

In the case of e.g., numbers[1], it will be

$0x7ffc9f728f20+(1*sizeof(int))$ = $0x7ffc9f728f20+(1*4)$

$0x7ffc9f728f20+(1*4)$ = $0x7ffc9f728f20+4$

which is

`0x7ffc9f728f24`.

Clear? Seems like it to me. If you have trouble understanding this concept, don't worry, many people don't fully understand pointers, addresses, and memory. I also had trouble with it. At least at the beginning.

You can help yourself with [videos from Gynvael - Gynvael's Code: Pointers #1](https://www.youtube.com/watch?v=bewTJaboGIw) or [lectures from CS50 - a course from Harvard](https://www.youtube.com/watch?v=PYJYiBlto5M) they, as people with much greater knowledge, explain the whole issue much better than I do.

### What Would It Look Like If We Indexed from 1?

Let's assume we index from 1. Then the formula would have to be modified - and it would look like this:

$first\_element\_address+((index-1)*type\_size)$

Another solution would be to shift the location of the first array element 4 bytes forward relative to the address of the array itself, but then our array would take up additional space in memory unnecessarily, because those first x bytes, where x is the size of the given data type, would simply be empty. That's one thing, two, you'd have to remember that the array address is not the address of its first element.

Both these solutions are senseless, because while it's supposedly not much - a few bytes on each array, or one subtraction operation, when we multiply it by the number of such variables we have in memory, we get quite a substantial sum of bytes/operations that are essentially unnecessarily occupied.

Additionally, how much code is already based on indexing from 0. It would be impossible to change all of that.

Of course, there are also other arguments for indexing or counting elements from zero, such as [those proclaimed by Dijkstra - Why numbering should start at zero](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html). He's a rather well-known and important gentleman, for those who don't know ;)

Overall, I used some simplifications and mental shortcuts here, but the general concept is conveyed.

### Examples of Basic List Operations

## Tuples

### Brief Characteristics

A tuple is really nothing other than an immutable list. What does that mean? More or less that after declaring a tuple, it can no longer be modified. We declare once and that's it. This carries many consequences I'll talk about shortly.

The only thing you can do with a tuple is read it, copy it, or redeclare a variable with a given name. Examples below.

Why do we need these tuples? Generally, immutability of data often makes it harder to shoot yourself in the foot with certain things. Also, it's an approach more similar to functional programming, let's say. Immutability is quite cool.

Besides that, we have one more advantage here. Performance.

### Efficient Beast

Well, if it's an immutable data structure, then the Python interpreter knows exactly how much memory to allocate plus for certain reasons this process happens faster. So here, allocation beyond needs doesn't happen plus the instruction executes sort of faster, Python knows what types are used, knows the specific data we used, etc.

As an anecdote, I'll share a story when using tuples reduced our memory usage from 4 GB to ~2.1 GB in a certain small webapp. In other cases, the reduction was even more dramatic.

### Examples of Basic Tuple Operations

```python
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__',
 '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
 '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
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

What is this magically sounding dictionary also called a Dict/HashMap? Well, it's nothing other than a kind of dictionary/mapping. Just like in a regular dictionary we have a kind of mapping of **keys** to **values** in the form of a word and its meaning, similarly in a Python dictionary/hashmap.

To the point.

A dictionary in Python is a data structure that allows us to store arbitrary values under specified keys. Imagine a list, but instead of a numeric index, you have an index in the form of a specified key.

In practice it looks like this:

```python
>>> test_dict = {"test": "some_string", 1: "hehe", 2: 3}
>>> test_dict["test"]
'some_string'
>>> test_dict[1]
'hehe'
>>> test_dict[2]
3
```

Predictable. The rest also works similarly to a list.

What's different from list behavior is that while in a list there's a guarantee that elements will always be in the order we put them in. A hashmap by definition doesn't provide such a thing. The current CPython implementation, from version 3.7, nevertheless provides something like this additionally, meaning from a regular `Dict` we got an `OrderedDict`, however it's better not to rely on this, because Python version like 3.6 is quite old, but there are still many projects written in it. What of it? Well, the code you'll write will probably be run on a Python version that doesn't account for and doesn't guarantee preserving insertion order of elements, so better not to rely on it too much, because in most cases that order will be preserved anyway, but it's not guaranteed by implementation, meaning there will always be that 1% where something will go wrong. Then try to get such a bug to investigate.

Of course, if you're aware and know what you're doing, plus you have a guarantee of what Python versions your code will run on, then go ahead. However, remember, in the latest Python version -> fine, below 3.8 or 3.7 not necessarily. Check exactly which version introduced `OrderedDict` as default.

### How Does the Process of Adding Elements to a Dict Work?

Well, generally just like in the case of a list we had a numeric index, with which Python calculated the offset in memory, in the case of a dict we have something called a hash function. This function takes the key we use as an argument and based on it tries to generate a fairly unique hash. Then based on the hash, usually through modulo operations, we figure out the address/offset where the given value is stored.

Logical? So yes, every time someone writes `some_dict["key"]`, underneath something happens like the Python interpreter, to get the address from which to read the value for the given key, takes that key, throws it into a hash function, I don't know, let's say `hash("key")`, this function returns some fairly unique hash generated/calculated based on the given key. From the hash we conjure an address/offset. Something like that.

Why fairly unique?

### Hash Collision

Hash collision is something that sometimes happens. Why? Well, the hash function can't be completely random. It must be stable and repeatable. This means, for a given argument it must always return the same thing, hash generation must happen in a predictable way. Why? Well, if it were otherwise, and for one key several hashes could be generated, then a problem would arise in that we could never, or sometimes couldn't, hit the exact address where we originally assigned the value. What does this mean?

The lack of complete randomness means that hash algorithms are limited to some degree. They're also limited by performance and time the computer can spend on hashing, which happens quite often, without cost to the user. A compromise had to be found between the complexity of the hash function and its resource-hungriness, execution time, and uniqueness of provided hashes for different keys.

Currently, smart heads have come up with some golden mean, however these days it happens to operate on data sets so large that hash collisions do occur and the hash function will generate the same hash for two different keys, whereby one key overwrites another. Very, very rare case. However, if you have a million trillion records to process, then suddenly very rare cases have about 100% chance of appearing.

### What Can Be a Key?

A key in a dictionary can be any value/variable/object that is hashable. What does that mean? Well, that in its definition it contains an implementation of the `__hash__` method. In a nutshell. So those objects for which a hash function has been implemented can be keys. Makes sense, because if we don't have a method to hash a given object, we can't calculate the hash. Can't calculate the hash from the key, can't figure out the address/offset. Without that, we don't know where in memory to store the value. So we must have this method implemented. Logical.

### Pass by Value & Pass by Reference

What's this about? About passing content by reference or by value. More specifically, it's about the fact that Python will copy some objects, as is the case with list slicing and getting its copy in a way that shares internal elements of that object for both the copy and the original. I wrote about this a bit already when writing about lists.

It seems to me it was explained fairly clearly there. Now - why am I mentioning this in the context of dicts? Well, mutable data types are often passed by reference, meaning instead of the object itself, we get a reference to it. For this reason, e.g., a list can't be a key in a dictionary - it's mutable, passed by reference and for this reason doesn't implement the `__hash__` method, making it unhashable, so the dictionary implementation in Python, when trying to establish a new key that is a list, will throw an error.

Let's recall the code I used to illustrate passing by reference vs by value.

```python
>>> pass_by_reference = [[1,2,3], 1, 2, 3]
>>> new_pass_by_reference = pass_by_reference[:]
>>> pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> new_pass_by_reference
[[1, 2, 3], 1, 2, 3]
>>> pass_by_reference is new_pass_by_reference  # two different lists
False
# the first element of the list is another list
# lists are mutable and we pass them by reference
>>> pass_by_reference[0]
[1, 2, 3]
# here we modify the second element of that inner list from the original
>>> pass_by_reference[0][1] = "test"
>>> pass_by_reference[0]
[1, 'test', 3]
# somehow the list in the copy also changed
>>> new_pass_by_reference
[[1, 'test', 3], 1, 2, 3]
>>> new_pass_by_reference[0]
[1, 'test', 3]
```

Worth being careful about this, especially when e.g., choosing arguments for functions or setting default values. Pass by reference -> we return the address and modification of the given object happens there. Pass by value -> we return just the value and its 'copy' happens fresh instead of modifying the variable at the given address, we get a new one. Another example:

```python
student = {"Putler": 10}
def test(student):
    new = {"Zelensky": 20, "Defender": 21}
    student.update(new)
    print("Inside function", student)
test(student)
print("Outside function:", student)
```

As you can see above, dict is passed by reference, meaning like an address. Python therefore goes to the given address and modifies the object, whereby changes are spread to places where an inexperienced programmer might not expect. In the case of passing by value, it's different. The original object isn't modified, only its copy.

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

I don't know if this makes sense, maybe we'll come back to it. Analyze and search a bit on the internet on your own on this topic to additionally clarify the situation.

### Shallow Copy and Deep Copy and Dictionary Keys

We have all this passing references, values, etc. Let's talk now about shallow and deep copies. Briefly because briefly, but worth mentioning.

When we used slicing as a method of copying a list, we got a so-called shallow copy of that list. What does shallow mean? Well, only the initial object was copied, the object from the very top. Everything inside that was passed by reference was not duplicated. Only references were copied. This is a shallow copy.

A deep copy is a copy where the interpreter 'enters' the object we're copying and copies everything by value, not by reference. This means we get an actual, independent duplicate of the given object and not just its 'top level' as in the case of a shallow copy.

Sometimes needed. Worth knowing, because in some cases we think we have two different objects after copying using a shallow copy, we modify one object and bam, changes in both. This can cause really ugly bugs to debug. I don't recommend.

### dict.values() keys() items()

Pay attention to these three methods. Play with them and summarize your conclusions. I'll only point out one thing.

What type of objects do functions dict.keys(), dict.values(), dict.items() return? dict.items() - obvious. A list of tuples. But not quite. Because if you look closer, it's the dict_items class, which isn't quite a list - it's sort of an extended class, because it allows us to perform operations on it like on sets. Similarly with keys() and values(). So on objects returned by these functions, you can perform union, difference, or intersection operations from sets. Tldr - these functions return iterable set-like objects.

### Examples of Basic Dictionary Operations

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

What are sets? Analogous to mathematics. It's like a list, but without repetitions. At least seemingly. Underneath it's a bit different, because underneath sets are closer to a hash map. Actually, it is sort of a hashmap. Why and what for? Well, let's ask ourselves what the attributes of sets are. Each element occurs only once. Insertion order isn't necessarily preserved. Sounds familiar? Yup. Sets are like hashmaps where values are also keys sort of.

What's the advantage of a set? First is deduplication of elements -> each occurs exactly once. We can extract 'statistics' from a given element, how many times it was added to the set, but in the set itself it will appear only once. The second is performance-related.

### Search Faster Than Light

Searching in a set has computational complexity of O(1) - constant time. What does that mean? Regardless of the set size, to check membership of a given element in the set, we perform an operation that is characterized by constant execution time independent of size. So even for very, very large sets, if they fit in memory, we can super quickly determine whether they're in the given set.

In the case of a list, it's not so easy, especially if the data is unsorted.

Why is that? Well, because underneath there's sort of a hashmap, to check if an element belongs to the set, it's enough to just calculate the hash of that element and then check if everything matches. Hence O(1) regardless of set size.

This in turn imposes restrictions on what we can put into a set. What? The same as with dictionary keys.

Additionally, the Python set also supports similar operations to mathematical sets. Conjunction, alternative, difference. A regular list can't handle all of this.

### Examples of Basic Set Operations

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

Phew, finally. Quite a chunk of text, huh? And that's just selected Python types.

It's worth knowing them well, playing with them, and getting familiar. Why? Well, in Python's standard library there are already so many goodies, so many different things that make life easier, that it's mind-boggling. It's a shame to reinvent the wheel and implement something yourself when the language provides its version.

Moreover, implementing from scratch is often also senseless for a very important reason. Your own implementation may be full of holes, because you check it, maybe people at Code Review, and that's it. However, when it comes to code in Python's standard library and implementations from contributors, it's code that has been tested and reviewed by thousands of people. Mishaps happen, true. However, where are we more likely to find a bug? In code reviewed by thousands of people, tested in millions of production applications, and covered by many tests? Or in code reviewed by you and perhaps your team? There's no comparison.

Plus I'd bet my hand on this, believing that thanks to the effort of thousands of contributors, code from Python's standard library will be better optimized. Use what's been built and don't reinvent the wheel creating your own naive implementations of sorting algorithms or something. Sometimes such a need arises, true, but I doubt you'd have such needs as a wannabe junior.

That's why good knowledge of Python's standard library is a necessity. Leave your own implementations for learning or fun purposes, to understand how something works. In production code, let's try to avoid it in favor of proven solutions from the standard library.

This not only makes the task easier but makes the code more solid, more optimized, and probably faster to deliver. It's easier to assemble something from ready blocks than to build a house yourself starting from extracting clay and firing bricks.

## Questions and Tasks

1. Does Python have dynamic typing? Or maybe static?
2. What does this mean? What are the disadvantages, what are the advantages.
3. Name the basic data types in Python.
4. And the more complex ones?
5. What are the differences between basic numeric types?
6. What does it mean that a value is `truthy` or `falsy` in Python? Give examples distinguishing what is what.
7. What are the ways of declaring text in Python?
8. What is an escape character and why do we use it?
9. What functions facilitating character to number conversion, to other encodings, did I mention?
10. Prepare an article in which you describe what each function is about, briefly characterize each basic type. Give examples for which functions don't work and guesses why. The target audience is other beginners. Let it be an extensive article full of your personal notes and not just copy-paste from documentation. Give live examples.
11. Prepare a summary list for basic data types you know in which you present and briefly describe what methods/attributes each type has and what each method does. Skip those starting with `__`. What command do you need to use here?
12. Same as in 11., but for complex types. Describe very thoroughly. You can combine the articles. Focus on showing practical use. Comment on the code and show examples other than here.
13. Send the articles from 12. and 11. to olafgorski@pm.me and I'll check them and give feedback :)
14. Prepare a comparison table: list vs tuple vs set.
15. Experiment with really large numbers. Describe your conclusions.
16. Create code that will take a number from the user and then tell whether it's even or not. How to get something from the user? Google it if you don't remember.
17. Create a string and then swap its last letter with the first.

\pagebreak
