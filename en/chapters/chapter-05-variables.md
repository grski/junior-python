# Chapter 5: Variables

## Let's Start with This Code

Let's begin with this code:

```c
#include <stdio.h>

void main() {
    short a = 1;
    a += 1;
    short b = 4;
    char z = ##### SECRET #####;
    printf(z);
    int c = 4;
    int h = 5;
    printf(c);
}
```

Try to analyze this code on your own and think about what's happening here. It's not that difficult. Basically, we've declared several variables - `a, b, c, h, z` and printed `z` and `c`.

We'll discuss the rest below, but try to figure some things out on your own first!

Now, here's a little trick. We'll look at what code the compiler generates from this. In this case, we're using `x86-64 gcc 9.3`. Let's see what assembly instructions our compiler produced for the processor. Due to size, the code is on the next page.

\pagebreak

```assembly
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

Whoa. What's going on here? Don't worry, let's break it down piece by piece.

```assembly
main:
        push    rbp
        mov     rbp, rsp
        sub     rsp, 16
```

Let's skip this part - it's not relevant to this specific example.

```assembly
        mov     WORD PTR [rbp-2], 1
```

This is what interests us. This is equivalent to our: `short a = 1;` And what's happening here? Let's use some magical illustrations to help!

![Detailed breakdown of the above instruction](./chapters/resources/images/zmienne.png)

Okay, I've broken it down a bit in the illustration. Now let's go into deeper explanations.

Our declaration `short a = 1;` simply means creating a variable `a` of type `short` and assigning it the value `1`. `short` is a small integer, in this implementation it's 16 bits, or 2 bytes. In Python, a similar (at some level) notation would simply be `a = 1`. So we're creating a variable `a` with value 1. This is how it looks in C. Time to go one level lower. And what's one level lower? What language? Remember from previous chapters or Google it.

`mov` tells the processor to move the value of the second argument to the location specified in the first argument.

The first argument is the entire expression `WORD PTR [rbp-2]`. It means nothing more, nothing less than that at (PTR) the address, specifically address [rbp-2], which is `rbp` minus two bytes, we have a `WORD`, which is a word, and a word in this implementation is 2 bytes, or 16 bits. What `rbp` is - let's not worry about that now, it's not very important. Imagine it's some address, reference in memory, pointer to something, whatever.

And as the second argument, we have the value that needs to be placed there, which is `1`.

Take your time to analyze this, it's not that complicated. Pay attention to the fact that the type `short`, which has a size of 2 bytes in this implementation, or 16 bits, somehow sounds similar to the size the compiler used in the first argument, there's `WORD` - also 2 bytes and 16 bits. Coincidence?

Go back a bit and look at the rest of this code, especially the declarations of the next variables, their types, and the fragments with X PTR [rbp-XD].

After all this, a light bulb should go off in your head. Answering the question from the beginning of the chapter - how does the program know when to stop reading? Well, during compilation, something like `a` disappears. Its occurrences are replaced by something like `WORD PTR [rbp-2]`. Having this, the program knows exactly when to stop reading and when to start, because we have both the address and the number of bytes to read.

Spend some time on this, think about it. It doesn't have to click immediately. First analyze the entire code. Take it easy. Only then move forward.

## Everything's Fine, But Python is Different

Now here's a very important note. Throughout the examples in this chapter, I've been using code from the C language and describing the process that happens there during compilation and so on.

In Python, however, things look a bit different, as I've already mentioned. This comes from the different natures of these two languages - statically compiled C and dynamically interpreted Python. The knowledge I'm sharing here is universal, because while at the higher level, which is just below the surface, Python doesn't look like this, at the lowest level it definitely does - after all, CPython is written in... C.

In Python, the mechanism of variable declaration looks a bit different (we'll talk about how another time) and so on, but the logic is, let's say, preserved somewhere. However, it's easier for me to explain using C and Assembly examples. Why? Because in Python, during interpretation, millions of different optimization tricks are applied and various strange things happen there. For example - during Python's startup alone, about 50,000 different objects, variables, and other things are initialized! Not bad, right? That's why for now we're operating on "simpler" C. Later we'll probably get into these Python optimization threads, but for now it's not necessary. So when you sometimes hear compiler instead of interpreter, you might think something got mixed up and so on, but don't worry.

Also, don't worry at all if the above isn't obvious to you, this fragment with the code. Take it easy. Spend some time on it, it's not that simple! Think about it, analyze it on your own, even Google it. The fact that you don't understand what's happening there after a second doesn't mean you're unintelligent or stupid. So keep going!

## Another Difference

While we're talking about Python's differences, let's say a few words, literally two sentences, about how Python, as an interpreted language, is different from compiled languages, but only apparently.

In the traditional model, as we've already discussed, we have code, then this code is compiled into machine code, then run. In Python, we have an implemented interpreter that executes/interprets our code. That's how it works, at least apparently.

If we look a bit deeper, it turns out that... Python is interpreted, but compilation also happens here? But how, one might ask. What's going on?

Well, the Python code you write is also compiled, but not to machine code. Python compiles to `bytecode` that's understandable for the Python interpreter, something like a virtual machine in Java (JVM), but differently.

Then, our compiled bytecode is executed by the Python interpreter, and the Python interpreter is nothing else but another code compiled to machine code, that is, a regular program. In short, Python is a compiled interpreted language, so to speak.

Have you ever wondered what and why `.pyc` files are created after you run your code? This is a form of optimization and remembering by Python of the intermediate compilation step. Python looks at the source file, based on it calculates some sum from this file, or 'number', after all, every file underneath is nothing else but some very long binary string. Binary strings can be translated, calculated into a regular number, in simplification. So Python does this underneath, looks if a `.pyc` file exists, if not, it creates it. Then it checks if this number, which is unique for each source file, is the same. If it is, it doesn't perform the compilation step again, it immediately jumps to interpreting.

If we make any change in the code, Python will catch the change, because this 'number' will change and before interpreting, it will conduct the 'compilation' process again.

## Memory Management

One might ask, how does Python know when to 'delete' variables from memory? Because we know when to allocate. How does Python know when a variable is no longer needed and can free the allocated memory? If Python didn't know and didn't do this manually, didn't conduct so-called `Garbage Collection`, then every run of our program would permanently clog, at least until restart, our computer's RAM. How does it happen that this doesn't occur in most cases?

Well, the Garbage Collector in Python, which cleans up variables we no longer need and frees memory for reuse, keeps a list. In this list, it keeps the reference count for each object. If this count reaches 0, it means that the object is no longer needed, because nothing refers to it, so the memory can be freed.

What about when one object refers to another, but nowhere else? Then we have a loop of dependencies, so to speak. That is, theoretically the reference count is greater than 0, but the object isn't being used.

Here comes the system for detecting reference loops. Python is able to detect this and then also free the memory. Linked list and such. Read up on it yourself.

It's also worth adding that Python is a clever beast. It has an optimization mechanism that most often checks newly created objects. If an object is fresh, there's a good chance it won't be needed soon. Old objects that have survived until now have a good chance of surviving further. Those who have, will have more added to them, those who have nothing, will have it taken away. Or something like that. It's like with fashion and trends. New ones pass, but the old core continues.

## Summary

Due to the fact that quite a lot of information has flowed onto your heads in this chapter, my dear readers, I've decided to end it here, somewhat earlier than originally planned.

Let's remind ourselves of what I wrote about in this chapter.

Our computer is quite good at remembering things, much better than our brains, so it's worth taking advantage of this. Usually during programming, we use **RAM** to remember certain things for some time.

By the way, a note - the expression `RAM memory` is a linguistic pleonasm, because RAM means `Random Access Memory`, so writing RAM memory is like writing butter butter. But let's get back to the topic - we use RAM. When?

We do this, for example, by using **variables/constants**, which are nothing else but some **name, alias** that we create for what we want to remember, through which the computer knows where in its memory, at what address, to be more precise, to look for a given thing, and it's easier for us to type and remember `first_name` as a variable name/reference/alias instead of `0xA1FBA`.

When creating these `aliases` or **naming our variables, we must follow certain rules**, such as not starting them with digits. Variable names should be descriptive but short, similar to the entire code. This has fundamental significance when it comes to the readability of the code we create and its quality.

Besides the binary system, we also have something called the **hexadecimal system**, which we use to write more concisely what would take us much longer in binary. It all converts on a similar principle as from decimal to binary.

The computer associates an **address**, variable size depending on what's inside. Based on the Assembly/C code, more or less we learned how it looks underneath. But just, we examined the process in C more precisely, in **Python it all looks a bit different, because it's interpreted**, but the general mechanics remain similar somewhere, hence it's good to know it.

## Exercises and Questions

Now it's time for questions. Remember, some of them will require searching for information on the Internet or general knowledge. That's not a bad thing!

1. What types of memory does your computer have that we discussed? List their characteristics and which is used to store what kind of data?
2. How do you declare a variable in Python? Declare several in the interpreter.
3. What rules do you know about names we can give to variables in Python?
4. Polish characters in variable names are a good idea. Do you agree with this statement? If yes, why? If no, why?
5. In the chapter, there's a piece of code with a function called `redirect_logged_in_user`. Translate this entire fragment line by line and describe in your own words what it does, what each piece of this code does, or what you think it does. In the chapter text, you already have some description, but do it now independently and go deeper into the details.
6. What does computer memory look like, figuratively speaking? How does the computer move through it, simplifying?
7. What is the hexadecimal system?
8. Convert several numbers from decimal to hexadecimal. Which ones? 2, 8, 19, 32, 111.
9. How much RAM does your computer have? How many bytes is that? Pay attention to whether we're talking about bits or bytes ;) How to express this number in hexadecimal? And in binary?
10. How does the computer know where to look for the value we saved for a given variable?
11. How does the computer know when to stop reading the value at a given address?
12. In the code from point `8.6`, there's a fragment shrouded in mystery - the value for variable `z` isn't expressed. By analyzing the assembly code below, try to guess what value was assigned there. I'll just hint that the `char` type is nothing else but some `character`, that is, a character. Hint: remember a bit about how we represent/encode characters/text.

## Answers

1. I'm talking about RAM and hard disk memory. Their characteristics - look them up yourself. In short, RAM is usually (generalizing) faster but less persistent, disk the opposite.
2. `variable_name = "value"` for example.
3. So far we've only talked about not starting with digits but with letters or underscore.
4. It's not a good idea. Why? We shouldn't necessarily write code in Polish, except for really few exceptions.
5. I won't add details here, let this be a small challenge ;)
6. More or less you can think of it as a sequence of cells placed in a straight line, containing ones or 0s.
7. A number system based on 16 as its base.
8. Again - do it yourself.
9. See above.
10. By the address that it manages 'underneath' and reads from there - at this specific location in memory.
11. We talked about this in `8.6`.
12. If we analyze the line `BYTE PTR [rbp-5], 102` we can conclude that this `char` definition says something about the number 102. 102 in ASCII/UNICODE is nothing else but `f`.

Remember that you can post your answers on GH here - https://github.com/grski/junior-python-exercises, and I'll check your solutions and give feedback. More about this in the 'Interactive Part' subsection.

\pagebreak 