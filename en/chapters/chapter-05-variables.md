\pagebreak

# Variables, an Introduction

Alright, we've done some printing, and that's fine. But it's not exactly the most exciting thing in the world. Can Python do anything else? Otherwise, it would be a pretty weak language. Of course, it can do much more.

## Remembering Values

The next concept I'd like to introduce is the idea of variables.

What's this all about? Let me explain.

We have our computer. It has some memory, whether RAM or disk storage, right? Right. It's quite spacious, fast, and sometimes even persistent. So it would be nice to use it somehow while programming. Our brains are pretty good at thinking, but not so great at remembering things, especially in the long term.

The basic tool we use to save something to or retrieve from computer memory is variables/constants.

It's a way to store a value in the computer's memory and assign it a kind of identifier so we can use it normally later. What does this look like in Python? Simple stuff.

```python
variable_name = value
```

Where the value can be practically anything.

The name, however, is not so free - there are certain rules we must follow when naming variables, such as not starting with a digit; it must start with a letter or the _ character.


## Variable Names

We can also use Unicode characters in variable names, but let's not do that. Just don't.

We name variables in English, using snake_case - this is a practice where we separate individual words in the variable name with the _ character. Stick to this because it's important, very important.

Theoretically speaking, if you work in a 100% local team where you're certain that in the future NO ONE who doesn't know your language will ever read this code (which is basically never), then okay. Theoretically, you could write code in your native language, but... It's generally not a good practice, please don't do it if you can avoid it.

So here's the deal: we name variables and everything in our code descriptively, so it's immediately clear what a given piece of code does, what's in the variable. But let's not go overboard the other way - the variable name shouldn't be an entire poem. Also, in names, we generally use only letters, digits (less frequently), and underscores. Keep it conservative here. Concise, accurate names.

Why? Properly naming variables, functions, classes, and everything in your code makes it readable and understandable. Simply put. You have to do this. Yes, from the very beginning. It will develop a good habit in you, which is critically important.

Let me throw an example at you.

```python
def redirect_logged_in_user(self, request, *args, **kwargs):
    if self.redirect_authenticated_user:
        redirect_to = resolve_url(settings.REDIRECT_URL)
        if redirect_to == request.path:
            raise ValueError(
                "Redirection loop detected. Check that your"
                "REDIRECT_URL doesn't point to a login page."
            )
        return HttpResponseRedirect(redirect_to)
    return super().dispatch(request, *args, **kwargs)
```

Even without knowing the language well, but knowing English, you can quickly figure out what this code does. Just so you know - this is an authentic piece of production code. Slightly modified, but the meaning is preserved.

Specifically, it's some function/method or something that takes a request, so probably some web application, checks if logged-in users should be redirected, and then, if the user is logged in and redirection is enabled, it redirects them somewhere. Where to redirect depends on some REDIRECT_URL variable from settings, meaning configuration.

If you don't know English well, try translating this on your own. Google even word by word, and you'll find that you can really quickly figure out what the code does. All it takes is some language knowledge and a bit of IT context about the conventions programmers have for naming certain things, specific terms and their meanings.

And by the way, it also checks if that `somewhere` we're supposed to redirect the user to isn't the same place where we currently are, because then we'd create an infinite loop. Constant redirections. Infinite loop.

Now, for a counter-example, code with **somewhat** less descriptive names.


```python
   def rdr_lg_usr(self, r, *args, **kwargs):
        if self.rau and r.u.ath:
            to = rslv(stings.TO)
            if to == r.pt:
                raise VEr(
                    "Redirection loop detected. Check that your"
                    "REDIRECT_URL doesn't point to a login page."
                )
            return HttpRR(to)
        return super().dp(r, *args, **kwargs)
```

I don't know about you, but this code tells me basically nothing. Okay, based on certain information, I can guess some things, infer them from context, but...

This is not how it should look. Absolutely not. Every time I see any production code that looks something like this, I get cancer. Then my cancer gets cancer.

And so we both sit there, me and my cancer, crying because we both have cancer. And what was the point of reading such code? Even worse - sometimes you have to work with something like this because some fool decided that if they shortened `redirect` to `rr`, those 6 letters they saved would save their world, their beautiful fingers, the codebase, and everything else. Get out of here with that.

Sometimes, really, very, very rarely, there's a situation where you can actually shorten something. But these are definitely exceptions to the rule. These are places where even if you throw in an abbreviation, everyone will know what it means. Or if you have type annotations, that sometimes makes things easier and allows for certain compromises.

I should also note that I'm obviously exaggerating the example here, but the point is to show a certain fact.

So as you can see - names are critically important, and anyone who creates code like the second example deserves a) a disability pension due to lack of brain b) a 15-year sentence of coding in legacy C++ code, as a bonus.

So there you have it.

## Why Do I Need All This?
Again - a good question. As I said - the computer is better at remembering things than you are. That's first. Second, there's another matter - laziness. Let's say we have some name we want to remember.

A prophet enters our room and wants us to print several parts of their speech:

`Good evening. Something... something broke and I couldn't be heard, so I'll repeat once more(...)`

Why? Don't ask, just do it. Quickly, quickly, before we realize it's pointless.

```python
print("Good evening. Something... something broke...")
print("Good evening. Something... something broke...")
print("Good evening. Something... something broke...")
print("Good evening. Something... something broke...")
```

and done, right? Just like that. This is either a lot of typing or a lot of copy-paste (the copy-paste method involves copying and pasting something - a humble reminder for those less familiar). Both solutions aren't great.

And here's where variables come in, all in white, like UTF-8 in the previous chapter.

``` python
prophet_lyrics = "Good evening. Something... something broke..."
print(prophet_lyrics)
print(prophet_lyrics)
print(prophet_lyrics)
print(prophet_lyrics)
```

Another example - let's say we want to do some precise mathematical calculations that require PI with high precision. Are we going to write `3.14159265359...` every time, or maybe we'll just do this:

```python
PI = 3.14159265359
print(PI)
```

Shorter, right? I think so. This is obviously a rather weak example, but it illustrates what I want to show. And here's a note: normally don't do this, because Python already has PI defined; you just need to import it. We'll discuss what exactly this means later, but if you need PI in the following chapters, do this:

```python
from math import pi
print(pi)
```

And done!

## A Bit More Theory

Let's get back to what I like. That is, exploring the why, what, and how.

These variables of ours. How do they work? How does the computer understand them? Well, quite simply, so let me explain.

First, let's discuss a general model of how the computer sees variables.

The thing is, every time we create a new variable, our computer cleverly does something like associating the variable, or rather its name, with some specific address in memory.

Actually, it's not even the computer but the compiler/interpreter, but let's not get into that for now.

What does this mean in practice and where does it come from?

As we established earlier, the computer only understands zeros and ones. Nothing more. So it has to translate everything into things it can understand.

It's no different with variables. When we write something like this in code:

```python
new_variable = "TEXT"
```

Under the hood, the Python interpreter does this trick that associates (links) in a simple way a piece of text, namely `new_variable`, with some address in memory, some location. Because I don't know if you remember, but a moment ago I mentioned that variables are stored in memory. Exactly. So for the computer to know where exactly to look for a certain value, you give it the address where that value is located.

And what does computer memory look like? Nothing other than a very long line of numbered cells. Imagine an incredibly long row of cells placed next to each other. These cells can contain two values - 0 or 1. That's what computer memory looks like.

Now we save our variables, data in these cells. As I said, to be able to use them again later, for the computer to know where to read the previously saved data from, we need the address of that data. The address is nothing other than the so-called offset. It's the number of bits/bytes (depending on notation) you need to move from the beginning of memory to find the given value. Then our hardware jumps there, to the specific address. It reads what it needs and returns it to us so we don't have to remember.

## Hexadecimal Numbers

Now a small digression - remember when I said the binary system is a bit unwieldy? Well, because computer addressable memory typically has a very large number of possible addresses, we have something called the hexadecimal system, base 16. Similar idea to the binary system, but instead of two digits, or ten as in decimal, we have sixteen here.

Why sixteen? It's easy to convert between it and binary, and it's concise because large numbers can be expressed with a small number of digits, since we're dealing with powers of sixteen, and when powers are involved, growth/decline is exponential, same goes for notation length.

Additionally, binary numbers translate nicely to hex.

Everything is analogous to the theory from the binary system, so remember how that worked, e.g., with conversion, and just do it analogously in the hexadecimal system. If you can't do it on your own, google it. What are the 'digits'? Well, these:


| HEX | 0  |  1 | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | A  | B  | C  | D  | E | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| --- | --- |
| DEC |  0 |  1 |  2 |   3|   4|   5|  6 |  7 |  8 |  9 |  10 |  11 |  12 | 13  |14  | 15 |

So in short: digits from decimal + the first 6 letters of the alphabet.

In any case. Remember that we usually address memory using the hexadecimal system, and numbers written in it are usually marked with the prefix 0x, analogous to binary, where it was 0b.

![Memory representation](./chapters/resources/images/adresowanie1.png)

(Yes, I know, beautiful scribbles. I can't do professional illustrations, so they're hand-drawn.)

Getting back to the topic. An average computer now has at least 4 GB of RAM. That's about 4 billion bytes. That's 32 billion bits. A lot. That's why we address with hex. Addresses will be shorter in presentation. Much shorter.

Now imagine those 32 billion bits, each as one cell, those cells are next to each other in a continuous line. That's roughly what your computer's memory looks like, greatly simplified.

A small note. Since a bit is such a tiny unit, we currently address using bytes. So the memory address - nothing other than a number, is the number of bytes you need to shift from the beginning of memory to get to the given value.

So if the interpreter associates `new_variable` with address `0x123`, then every time we reference `new_variable`, our interpreter will shift by `0x123` bytes from the beginning of memory and take the value from there.

Just a moment, wait...

## When to Stop Reading?

Because it has the starting address, but not really the ending one. What now? Let me explain. We'll go back to C and other archaic things.

Let's start with this code:

```c
#include <stdio.h>

void main() {
    short a = 1;
    a += 1;
    short b = 4;
    char z = ##### MYSTERY #####;
    printf(z);
    int c = 4;
    int h = 5;
    printf(c);
}
```



Try to analyze this code yourself and think about what happened here. It's not that hard. Generally, we declared several variables - `a, b, c, h, z` and printed z and c.

We'll discuss the rest below, but try to figure something out on your own first!

And now, attention, we'll do a little trick. We'll look at what code the compiler will generate from this. In this case `x86-64 gcc 9.3`. Let's see what processor instructions our compiler spat out, what `Assembly` code was created.
Due to size, the code is on the next page.

\pagebreak

``` assembly
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
        mov     WORD PTR [rbp-2], 1
        movzx   eax, WORD PTR [rbp-2]
        add     eax, 1
        mov     WORD PTR [rbp-2], ax
        mov     WORD PTR [rbp-4], 4
        mov     BYTE PTR [rbp-5], 102

        movsx   rax, BYTE PTR [rbp-5]
        mov     rdi, rax
        mov     eax, 0
        call    printf

        mov     DWORD PTR [rbp-12], 4
        mov     DWORD PTR [rbp-16], 5
        mov     eax, DWORD PTR [rbp-12]
        cdqe
        mov     rdi, rax
        mov     eax, 0
        call    printf
        nop
        leave
        ret
```

\pagebreak

Whoa. What's going on here? Calm down, let's discuss. Piece by piece.

``` assembly
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
```

Let's skip this - it doesn't concern us in this specific example.

```assembly
        mov     WORD PTR [rbp-2], 1
```

This does concern us. This is the equivalent of our: `short a = 1;` And what's happening here? Magic illustrations to the rescue!

![Breakdown of the command above](./chapters/resources/images/zmienne.png)

Okay, I've broken it down a bit in the illustration, now let's move on to deeper explanations.

Our declaration `short a = 1;` simply means creating a variable `a`, of type `short` and assigning it the value `1`. Short is a small integer, in this implementation it happens to be 16 bits, or 2 bytes. In Python, a similar (at some level) notation would simply be `a = 1`. That is, we create a variable `a` with value 1. That's how it looks in C. Time to go down a level. And what's a level below? What language? Remember from previous chapters or Google it.

`mov` tells the processor to move the value of the second argument to the place specified in the first argument.

The first argument is the whole expression `WORD PTR [rbp-2]`. It means no more, no less than: under (PTR) the address, specifically address [rbp-2], meaning `rbp` minus two bytes, we have a `WORD`, and a word in this implementation happens to be 2 bytes, or 16 bits. What is `rbp` - let's not worry about that now, not very important. Imagine it's some address, a reference in memory, a pointer to something, whatever.

And as the second argument we have the value that needs to be put there, namely `1`.

Analyze this calmly, it's not that complicated. Pay attention to the fact that the type `short`, which has a size of 2 bytes in this implementation, or 16 bits, sounds somehow similar to the size the compiler used for the first argument, there it's `WORD` - also 2 bytes and 16 bits. Coincidence?

Also, go back a bit and look at the rest of this code, especially the declarations of the next variables, their types and the fragments with X PTR [rbp-XD].

After all this, a light bulb should turn on. Answering the question from the beginning of the chapter - how does the program know when to stop reading? Well, in the compilation process, something like `a` disappears. Its occurrences are replaced with something like `WORD PTR [rbp-2]`. Having this, in turn, the program knows perfectly well when to stop reading and when to start, because we have both the address and the number of bytes to read.

Spend some time on this, think. It doesn't have to click right away. Analyze all this code first. Calmly. Only then move on.

## All Good, But Python Is Different

Now - I need to make a very important note here. Throughout the examples in this chapter, I'm using C code and describing the process that happens there during compilation and so on.

In Python, however, things look a bit different, as I've mentioned. This is due to the different natures of these two languages, statically compiled C and dynamically interpreted Python. The knowledge I'm passing on to you here is universal, though, because while at a higher level, meaning what's just below the surface, Python doesn't look like this, at the lowest level it certainly does - after all, CPython is written in... C.

In Python, the variable declaration mechanism looks a bit different (how, we'll talk about another time) and so on, but the logic is, let's say, preserved somewhere. It's easier for me to explain using the example of C and Assembly, though. Why? Because in Python, during interpretation, a million different optimization tricks are applied and various strange things happen there. For example - during Python startup alone, about 50 thousand different objects, variables, and other things are initialized! Not bad, huh? That's why for now we're working with "simpler" C. Later we'll probably get into some of those Python optimization threads, but for now it's not necessary. So if sometimes you hear compiler instead of interpreter, it seems like something is mixed up and so on, don't worry.

Also, really don't worry if the above isn't obvious to you, this code fragment. Take it easy. Sit with it for a bit, it's not that simple! Think, analyze on your own, even google. The fact that you don't understand what's happening after a second doesn't make you unintelligent or stupid. So forward!

## Another Difference

Since we're talking about Python's differences, let's say a bit, literally two sentences, about how Python, as an interpreted language, is different from compiled languages, but only seemingly.

Well, in the traditional model, which we've already discussed, we have code, then that code is compiled to machine code, then executed. In Python, things are such that we have an interpreter implemented, which executes/interprets our code. That's how it is, at least seemingly.

If we look a bit deeper, it turns out that... Python is interpreted, but compilation also happens here? But how could that be, one might ask. What's going on?

Well, the Python code you write is also compiled, but not to machine code. Python compiles to `bytecode` understood by the Python interpreter, something like the Java Virtual Machine (JVM), but different.

Then, our compiled bytecode is executed by the Python interpreter, and the Python interpreter is nothing other than other code compiled to machine code, i.e., a regular program. In short, Python is a compiled interpreted language, sort of.

Have you ever wondered what *.pyc files are and why they're created after you run your code? It's a kind of optimization and Python's way of remembering the intermediate compilation step. Python looks at the source file, calculates some checksum or 'number' from it based on its content, because every file underneath is nothing other than some very long binary sequence. Binary sequences can be translated, calculated into a regular number, simplified. So Python does this under the hood, looks to see if a *.pyc file exists, if not, creates it. Then it checks if this number, which is unique for each source file, is the same. If so, it doesn't perform the compilation step again, it jumps straight to interpreting.

If we make any change to the code, Python will catch the change because this 'number' will change and before interpreting it will carry out the 'compilation' process again.

## Memory Management

One might ask, how does Python know when to 'delete' variables from memory? Because we know when to allocate. How does Python know when a variable is no longer needed and the allocated memory can be freed? If Python didn't know and didn't do this manually, didn't perform so-called `Garbage Collection`, then every run of our program would permanently clog, at least until reboot, our computer's RAM. How is it that this doesn't happen in most cases?

Well, the Garbage Collector in Python, meaning what cleans up variables that are no longer needed and frees memory for reuse, keeps a kind of registry. In this registry, it keeps the reference count for each object. If this count reaches 0, it means the given object is no longer needed because nothing refers to it, so the memory can be freed.

What about when one object refers to another, but nowhere else? We have a kind of dependency loop then. So theoretically the reference count is greater than 0, but the object isn't being used.

This is where the reference cycle detection system comes in. Python is able to detect this and will then also free the memory. Linked lists and such. Read up on your own.

It's also worth adding that Python is a clever beast. It has an optimization mechanism that most frequently checks newly created objects. If an object is fresh, there's a good chance it won't be needed soon. Old objects that have survived so far have a good chance of surviving further. Those who have will be given more, those who have nothing will have it taken away. Or something like that. It's like fashion and trends. New ones pass, but the old core continues.

## Summary

Because quite a lot of information has poured onto your heads in this chapter, my dear readers, I decided to end it here, a bit earlier than originally planned.

Let's remind ourselves of what I wrote about in this chapter.

Our computer is quite good at remembering things, much better than our brains, so it's worth using that. Typically, during programming, we use **RAM** to remember things for some time.

By the way, a note - the expression `RAM memory` is a linguistic pleonasm, since RAM means `Random Access Memory`, so writing RAM memory is like writing butter butter. But let's get back to the topic - we use RAM. When?

We do this using **variables/constants**, which are nothing other than some **name, alias**, which we create for what we want to remember, whereby the computer knows where in its memory, at what address more precisely, to look for the given thing, and it's easier for us to type and remember `first_name` as a variable name/reference/alias instead of `0xA1FBA`.

When creating these `aliases` or **naming our variables, we must follow certain rules**, such as not starting them with digits. Variable names should be descriptive but short, same with all code. This is of fundamental importance for the readability of the code we create and its quality.

Besides the binary system, we also have something called the **hexadecimal system**, which we use to write more concisely what would take us much longer in binary. It all converts on a similar principle as from decimal to binary.

The computer associates the **address**, the size of the variable depending on what's inside. Based on Assembly/C code, we more or less learned what it looks like under the hood. Only, well, we examined the process in C more closely; in **Python all this looks a bit different because it's interpreted**, but the general mechanics are preserved somewhere, hence it's good to know it.

## Tasks and Questions

Now it's time for questions. Remember, some of them will require searching for information on the Internet or general knowledge. That's fine!

1. What types of memory does your computer have that we talked about? List their characteristics and which is used to store what kind of data?
2. How do you declare a variable in Python? Declare several in the interpreter.
3. What rules do you know about the names we can give to variables in Python?
4. Unicode characters in variable names are a good idea. Do you agree with this statement? If so, why? If not, why?
5. In the chapter there's a piece of code with a function named `redirect_logged_in_user`. Translate this entire fragment line by line and in your own words describe what it does, what each piece of this code does, or what you think it does. There's already a bit described in the chapter text, but do it now independently and go deeper into the details.
6. What does computer memory look like, figuratively speaking? How does the computer move around it, simplifying?
7. What is the hexadecimal system?
8. Convert several numbers from decimal to hexadecimal. Which ones? 2, 8, 19, 32, 111.
9. How much RAM does your computer have? How many bytes is that? Pay attention to whether we're talking about bits or bytes ;) How would you express this number in hexadecimal? And in binary?
10. How does the computer know where to look for the value we saved for a given variable?
11. How does the computer know when to stop reading the value at a given address?
12. In the code from section `8.6` there's a fragment shrouded in mystery - the value for variable `z` is not expressed. Analyzing the assembly code below, try to guess what value was assigned there. I'll only hint that the `char` type is nothing other than some `character`. Hint: remember a bit about how we represent/encode characters/text.

## Answers

1. I mean RAM and hard disk memory. Their characteristics you can look up yourselves. In short, RAM is usually (generalizing) faster but less persistent, disk is the opposite.
2. `variable_name = "value"` for example.
3. So far we only talked about not starting with digits, for example, but with letters or underscores.
4. It's not a good idea. Why? We shouldn't necessarily write code in our native language, with really few exceptions.
5. I won't add details here, let it be a small challenge ;)
6. More or less you can think of it as a sequence of cells placed in a straight line, containing ones or 0s.
7. A number notation system based on 16 as the base.
8. Again - on your own.
9. See above.
10. By the address, which it figures out `under the hood` and reads from there - in this specific place in memory.
11. We talked about this in `8.6`.
12. If we analyze the line `BYTE PTR [rbp-5], 102` we can conclude that this `char` definition says something about the number 102. 102 in ASCII/UNICODE is nothing other than `f`.

\pagebreak
