\pagebreak

# Hello, World!

We're finally starting to have fun with coding! Phew, that took us a while, didn't it? About 50 pages or so. Anyway.

## Printing Text to the Screen

Hello, World! These words are a pretty popular phrase in programming.

This is something traditionally considered the text that the first program a beginner programmer creates will print - printing the message 'Hello World!' in the console.

We'll do something similar, but a bit different, because we'll do it in two ways. Why? Well, on the Internet, you can often come across the opinion that in Python, there's already a solution for everything, ready-made code that someone else created, we just import it, use it, and that's basically what all programming in Python is about.

Such gluing a program together from ready-made blocks. The key is knowing which blocks to glue together.

Well, often that's true. Very often. It's no different with hello world. The examples shown here should be typed into a file and run as described in the previous chapter, or typed on the fly into the interpreter. I recommend the second option, at least while we have one-liners/a few lines. For longer things, I recommend working with files, not just the interpreter.

So in Python, the standard Hello World can be replaced with:

```python
import __hello__
```

What will appear before our eyes?

```
Hello world!
```

Yup. Python even has a ready solution for hello world, but that's more of a fun fact - now I'll show you how to print something on the screen using Python the normal way.

```python
print("Hello, World!")
```

And that's basically it. In the console, you'll see: "Hello, World!". That's all there is to it.

A small note for the very beginners: if you don't know where to type this code, it's simple - create any file with a .py extension in your working folder, i.e., CWD, check the chapter about the four horsemen of the console if you've already forgotten what that means.

Then type this line in that file using your text editor. After that, just:

```bash
python name_of_created_file.py
```

and done. Alternatively, instead of python, you might need to type python3, depending on how you installed everything.

What happened here? We used one of Python's built-in functions, which are placed in the standard library of the language - a collection of functions that every Python3 installation has. This function is called print - as in, print something out.

Hmmm, so what might a function called "print" do? Good question. I think this is where the real test of whether you're cut out to be a programmer happens. If you can determine what the print function does, you're probably cut out to be a programmer. Congratulations.

We pass an argument to this function (that is, something for the function to work on) in the form of what it should print. It will be displayed on the screen, along with a newline character. The newline character, which Python automatically adds to what we print, means that if we now use another print to display something again, our value from the second print will be displayed on a new line.

Because the point is for the computer to know when to display a new 'enter' and end the current line. To let it know when to do this, we have something called a 'newline character'. When you press enter in Word, that's exactly what's being inserted underneath. So:

```python
print("Line 1")
print("Line 2")
```

Will return, as expected:

```
Line 1
Line 2
```

The newline character is usually `\n`. So in reality, instead of just displaying `"Line 1"`, Python displays `"Line 1\n"`.

Is all this simple? Anticlimactic? Yes. At least seemingly. Because underneath, there are many very, very interesting things happening that you have no idea about right now.

The fact that today, with a single line of code, you can print some text to the console is the result of decades of work and building foundations by the fathers of computer science. I know it might sound funny, but that's how it is. Look, for example, at Assembly code - the language everyone used to write in. \pagebreak

The code fragment shown below is Assembly, a very low-level language that allows very detailed direct interaction with computer memory, the processor, everything really. Thanks to this, a programmer can manage and optimize almost everything, but this comes at the cost that since you have to manage everything yourself... well, exactly. You have to do it yourself. This has pros and cons. Let's not worry too much about this for now; I'm just mentioning it so it can float around in your head somewhere. Assembly = fast, low-level language where you have to do a lot of things yourself, which is very close to the processor/memory itself, with a low level of abstraction.

``` nasm
segment .data
msg     db      "Hello World!", 0Ah

segment .text
        global  _start

_start:
        mov     eax, 4
        mov     ebx, 1
        mov     ecx, msg
        mov     edx, 14
        int     80h

; exit program
        mov     eax, 1
        xor     ebx, ebx
        int     0x80
```

Wait... What? So yeah. Appreciate what you have now.

Just to be clear - don't worry if you don't understand anything from this code. It's okay. I don't understand much of it either. It doesn't matter. The only point is to show you interesting, old ways.

And you know what's even more interesting?

The fact that currently, lower down, underneath, Python looks exactly like this. I mean, not Python itself - because Python is just a language - a set of rules, definitions, but I mean CPython - the implementation of the Python interpreter, and those can be arbitrary, I wrote about this earlier, you can read up on it. It's worth remembering that the default implementation of Python is CPython.

The difference between Python and CPython is that Python is simply a language, meaning a set of instructions and a description of what features this language has and how it should behave in given situations.

And CPython is already a concrete implementation of this - a translation into computer behavior, a specific program executing commands in a specific way. So CPython != Python.

So let's repeat one more time. Python is a language. The Python interpreter is a program that interprets code written in the Python language and executes specific commands. Usually, when we talk about the Python interpreter, we mean its default implementation, which is CPython - the Python interpreter written in C, but there are others too. Remember. Also remember that implementation details of Python interpreters differ between them. The language authors allowed certain decisions about specific behaviors to be made by the people implementing the interpreter. So CPython may, but doesn't have to, sometimes behave differently than Jython. Therefore, it's good practice not to rely on implementation details of the interpreter but on the language specification itself. But let's get back to the topic.

Why should we appreciate current abstractions?

Let's start with the fact that if you're using any reasonably modern computer, I'm almost certain you can see special characters in the printed text without any problems. You can see this text at all. Right?

It wasn't always this simple and obvious.

Why?

It's because of how computers work.

## Binary Language - The Only Thing a Computer Understands

I don't know about you, but for me it's always been interesting how a computer works. How is it that after pressing some magic button, electrical energy starts 'flowing' through this wonderful machine, various characters appear on the screen, and everything is so beautiful and nice.

Well, the matter is simple. At the very foundations of how computers work lies nothing other than two simple things: True and False, 0 and 1, yes and no. I'm talking about the binary system, machine language.

What do I mean by this? Well, a computer is nothing more than this huge, huge group of conductors/semiconductors glued together, like 'switches' that can be 'on' or 'off' - they have two states. These states are regulated by the voltage of the current flowing through the conductors; it determines whether each one is on or off.

Depending on what combination we have, which 'conductors' are on, which are off, the computer will do different things. It's like with a washing machine - depending on which buttons you leave pressed, it will do something different.

Because we have two states here, anything that has to do with this is often adorned with the adjective 'binary'. Binary number system. Binary choice. Binary tree. Binary people living in a probabilistic world, and so on.

Anyway. So we establish one thing. Our computer operates on only two values - 0 and 1, meaning no/low voltage and high voltage. That's everything. In a big simplification, this is exactly the complete foundation of the entire computer and nothing more.

I assume my readers are smart people. So a question should appear soon - But how? If the computer only understands 0 and 1, how is it that I can type different letters here, read them later, move the mouse, type numbers other than 0 and 1. What? You're making this up, mister.

Not at all. Your computer really only understands 0 and 1. Everything else is the result of various kinds of calculations, conversions, and encoding other values to exactly those 0s and 1s.

A perfect example here is this text.

## How a Computer Sees Letters - The Binary System

Imagine that all the letters you see here are actually, underneath, nothing more than a number written in the binary system.

For precision - what is a number written in the binary system? It's nothing more than a normal number, only expressed using only 0 and 1. We, as humans, chose the decimal system as our basic system. Probably because that's how many fingers we have, but who knows exactly.

In any case - we operate on the assumption that we have 10 digits, each order of magnitude can have 9 or 10 possible states, or it might not exist at all, and orders of magnitude are based on powers of ten.

In the binary system, it's actually similar, except instead of 10 digits, we only have two and two values. Additionally, we calculate successive orders of magnitude not based on powers of ten but on powers of two.

Let's take, for example, the number 123. How do we calculate its value? Well.

1 - number of hundreds, third digit
2 - number of tens, second digit
3 - number of ones, first digit

$1*10^2+2*10^1+3*10^0$ = $1*100+2*10+3*1$ = $100+20+3$ = 123



As you can easily notice, the exponent of the power is a number equal to the digit number, counting from the right side, minus 1.

This all sounds complicated because we don't think about it this way - we do certain things naturally due to experience, so switching to this way of thinking about it might require some practice.

The situation in binary notation will be analogous. How do we calculate the value of a given number in binary notation? Let's assume we want to find out what value the number 101101 has.

```
1 - 6th digit of the number
0 - 5th digit of the number
1 - 4th digit of the number
1 - 3rd digit of the number
0 - 2nd digit of the number
1 - 1st digit of the number
```

So: \
$1*2^5+0*2^4+1*2^3+1*2^2+0*2^1+1*2^0$ \
$1*32+0*16+1*8+1*4+0*2+1*1$ \
$32+0+8+4+0+1$=45

So 101101 is nothing other than the equivalent of 45 in the decimal system. And how to convert from decimal to binary? Very simply.
You divide the number by two and each time write down the remainder. \
$45/2$ = 22 remainder 1 \
$22/2$ = 11 remainder 0 \
$11/2$ = 5 remainder 1 \
$5/2$ = 2 remainder 1 \
$2/2$ = 1 remainder 0 \
$1/2$ = 0 remainder 1

Now, read the remainders from BOTTOM to top: 101101. Does it match? Yep.

Analyze this carefully and slowly for now. It's okay if something isn't clear at the beginning; this is just a way of converting from one system to another.

Knowing the values of powers of two comes in handy here. When you have some of them memorized, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, etc., some conversions will become easier and faster.

Anyway. Let's get back to the topic. So... Oh right. Letters are also numbers.

## Character Encoding - ASCII

Exactly. Since the computer only understands numbers, those in the binary system, meaning basically zeros and ones, how do we tell it to store some letter?

Can you imagine a world where instead of reading my words on the screen using letters, you would read each letter written somehow using the binary system, manually translating it on paper to human language? I can't, but more or less that's what happens in reality, only the computer does it for us.

So a few smart men got together once and decided that a good idea would be to create a kind of translation - translation, mapping of alphabet letters to... numbers.

Each letter of the alphabet received its unique code in the form of some number. Why? Because how do you tell a computer that 'k' is 'k'? You can't. The computer is dumb; it doesn't understand the concept of a letter. At least for now, in a few or several decades, who knows.

Numbers in the decimal system, however, can easily be converted to numbers in the binary system, i.e., to something the computer will understand.

So they established something called the ASCII standard, which is an abbreviation of American Standard Code for Information Interchange. It's a kind of table that contains mapping of English alphabet characters and punctuation marks to numbers. A kind of dictionary, which letter corresponds to which number.

For example, 'A' - capital A, was designated as 0100 0001, which is 65. 'a' is 97. The newline character is 0000 1010, which is 10. Why? Because that's how it is. That's what the American wise men decided, and that's it. The standard was established; follow it. It's basically a matter of convention.

A small note: usually numbers written in the binary system are written with the `0b` prefix, so it's clear that we're dealing with binary. Because how do you distinguish 10 in decimal from 10 in binary? The notation is the same but the values are different. It's like that joke that there are only 10 types of people in the world: those who understand binary and everyone else. Hehehe, programmer joke, sorry.

B in ASCII encoding is 0b0100 0010, which is 66. C will have the number 67. And so on. Guess what D will have?

Each letter you see here is translated in a similar way and saved on your computer's disk as a string of ones and zeros. Then, when reading, the computer, after interpreting which letter a given number represents, displays the appropriate letter. It completely doesn't understand that this 'k' is some letter and not a piece of binary code. Simple.

What distinguishes ASCII? ASCII is an encoding where each element can be expressed using 7 bits. What does it mean, using 7 bits? A bit is nothing more than a 'digit' in the binary system.

At least that was the original assumption. It therefore allows the translation of 128 characters to numbers from 0 to 127, inclusive.

Many people, at least those who have had some contact with programming or computer science, will be surprised. What - ASCII 7-bit? Everyone is taught that it's 8-bit. Well no, originally ASCII was designed as a 7-bit system, having 128 characters.

The fact that today we often think of ASCII in an 8-bit context stems from the fact that when ASCII was being created, 8 bits wasn't such a standard yet. Many encoding systems were 7-bit, and they used the 8th bit for their own various strange needs.

What does it mean that 8 bits is the 'standard'? Well, nowadays we have something called a byte. A byte is in turn a set of 8 bits. So for example 1111 0000 or 1000 0000.

It's a very small unit of your computer's memory that you can use. Whether in RAM or in disk storage.

This is clearly defined and simple. But... a byte wasn't always defined as 8 bits. There were systems where 1 byte, the basic unit, was defined completely differently - as 2 bits, 7 bits, 6 bits. Pick your poison. Free for all.

Generally, a lot of things in computer science, or programming, just like in mathematics, are conventional. Get used to the fact that sometimes we do something a specific way because that's how it is, not otherwise. Computer scientists basically trace their lineage directly from mathematicians, so we're strange people.

That's why nowadays, even though ASCII is originally a 128-character 7-bit system, it's written using 8 bits, giving it 256 possible characters. Officially, we call 8-bit ASCII extended ASCII, but colloquially, usually when we say ASCII, we mean the 256-character one - with a few additional characters.

Selected fragment of the ASCII character table:

|Decimal|Character|Binary|Decimal|Character|Binary
|--- |--- |--- |--- | --- |--- |
65 | A | 0b1000001 | 66 | B | 0b1000010
68 | D | 0b1000100 | 69 | E | 0b1000101
69 | E | 0b1000101 | 70 | F | 0b1000110
72 | H | 0b1001000 | 73 | I | 0b1001001
73 | I | 0b1001001 | 74 | J | 0b1001010
76 | L | 0b1001100 | 77 | M | 0b1001101
77 | M | 0b1001101 | 78 | N | 0b1001110
80 | P | 0b1010000 | 81 | Q | 0b1010001
81 | Q | 0b1010001 | 82 | R | 0b1010010
84 | T | 0b1010100 | 85 | U | 0b1010101
85 | U | 0b1010101 | 86 | V | 0b1010110
88 | X | 0b1011000 | 89 | Y | 0b1011001
89 | Y | 0b1011001 | 90 | Z | 0b1011010

Previously there was chaos. And from chaos emerged order. And computer science was born. Alright, enough nerdy references.

Anyway. Because I lost the thread.

So we have this encoding, in this case ASCII, and it's elegant. Although not entirely, because a problem appears. We now use ASCII on 8 bits, right? Yes. 8 bits is 8 zeros or ones, right? Right. Using 8 zeros or ones, we can express 256 numbers.

Considering that 1 number = 1 letter, it quickly turns out that we have a maximum of 256 characters to use. That's a bit little to fit all the alphabets of the world, right? Indeed. Let's also take into account that 'A' and 'a' are two different letters as far as the computer is concerned - lowercase and uppercase are not the same. Add periods, commas, and other punctuation marks.

It quickly turns out that not much room is left for just letters.

That's why ASCII encoding contains only Latin alphabet letters. You can't write in other languages with special characters in ASCII because there aren't enough characters. So what now?

Well, you see, so that various nations who have quite a lot of characters - like the Chinese or Japanese, where each word can be a different character, meaning kind of like a different letter for us - wouldn't feel wronged, new encodings started to emerge. Many encodings. Way too many. We won't talk about them. We'll skip straight ahead to times of clarity.

## And Then UNICODE and UTF-8 Enter All in White

Currently, however, the standard is something called UTF-8. This is a UNICODE character encoding system that uses 1 to 4 bytes for storage. Oh, important information. Up to 4 bytes. 4 bytes, how much is that? 1 byte, 8 bits, 4 bytes, 32 bits. And what does it mean that UTF-8 is a UNICODE character encoding system? UNICODE is our entire mapping, which letter/character reduces to which number, and UTF-8 is the way to write this, convert to bits, because when you have more than 1 byte, things become less obvious, hence these characters/mappings can be represented differently. UTF-8 is one of the ways to do this. Getting back to the topic of bytes...

32 bits, which is 32 ones or zeros, means you can use them to write many different numbers, and therefore many different characters. Well, this gets to be a lot, because it gives us about 4,294,967,296 possible characters. A lot, right? Even when we throw in all those Asian characters, there's still plenty of room left. Beautiful, idyllic. A dream.

A dream, because in reality, since the introduction of RFC 3629, UTF-8 supports at most 2,097,152 characters. It's because of various historical legacies, implementation details, and other strange things that you, dear reader, don't have to worry about, nor do I, only big brains like Ken Thompson and company do - somehow it turned out that some bits are reserved for special purposes, some bytes must have a specific format so you know various useful things, and so on.

And what's with this whole RFC thing? Generally, these are standards that certain minds set. Based on what? Whatever they decide. Just like with ASCII - because yes and that's it. Generally, I'm simplifying, and essentially when making various decisions, decision-makers are guided by more rational arguments.

That many characters should be enough for us on a daily basis. Currently in UNICODE, we have defined about 143,859 characters as standard. So we even have some reserve just in case, to add new characters later.

Or rather `codepoints`, but let's simplify, not get into it, and just say characters. What is a codepoint? Usually when discussing different encodings, instead of 'character', the term codepoint is used. Small difference. From your perspective, it doesn't really matter much.

So look: associate that UTF-8 also generally means Unicode. Keep these two terms together in your memory, but UNICODE is not the same as UTF-8, and that's very important.

Additionally, another note. There's also something called UTF-16. How does it differ from UTF-8? Word length. Meaning in UTF-8 one word has 8 bits, in UTF-16 it has 16 bits. That's it. There's also UTF-32. Here there's always one word, 32 bits long.

Just so you know - they have the same upper limit in bytes, meaning maximum 4, and in the case of UTF-16, minimum 2 (because 16 bits). What is a word? It's certainly not a word like from a dictionary. A word, meaning machine word, is kind of like a byte, but not quite. A way to group bits into X pieces, simply put.

In UTF-8, some characters can be expressed in 1 word, meaning 1 byte; in UTF-16, the smallest size is 2 bytes; and in UTF-32, it's already 4 bytes. So regardless of which character we use, e.g., `A`, which is 65, meaning something that fits in 1 byte, with UTF-32, the computer will still save everything in 4, wasting a lot of memory. In UTF-16, it saves in 2, in UTF-8 in one. More economical. But UTF-32 is easier to find in memory because you know that each character is 4 bytes and that's it. And in UTF-8 there are different lengths, one character will have 1 byte, another 4, and now try to guess, human, what is what, what ends when and where, but somehow we manage.

You don't have to worry about this too much, but maybe remember it somewhere.

UTF-8 is 100% compatible with ASCII - text in ASCII is valid UTF-8, but UTF-8 does NOT have to be valid ASCII. This is very important! Why? Because UTF-8 mainly contains characters that we can't fit in one byte, which is why they're absent in ASCII. So ASCII is a subset of UNICODE.

By the way, fun fact - when you write messages on social media and send emojis, they're also often stored in UNICODE; they have their specific numbers!

So look, just starting any conversation about how the basic function in Python works, shedding even a little light on what lies under its cover, took me quite a bit of text here.

And this is just the beginning - we've barely dipped our toes in the whole topic; if I had to describe everything about this one simple function, I probably wouldn't have enough book space.

Once upon a time, you actually had to have this knowledge - about all the low-level stuff - to write anything. Today?

Today we live in times where, based on decades of work by titans of computer science intellect, we can create such abstract languages that we don't need to know any of this. Just type print("xd") and it works. Times have changed, man. Programmers used to be different too; now they're not the same.

This is really something incredible, even though it seems trivial to us. This is the beauty of science, of computer science. Based on the work of others, we can create new, inconceivable things. Excellent.

Anyway.

## Summary

Let's do a summary of what we managed to do and learn.

In Python, we generally have a function called **print**, which, attention, prints text on the screen. This text, in reality, is not text for the computer, but nothing other than a string of zeros and ones, because the computer doesn't understand anything else, due to how it's built - voltage or no/low voltage - that's the only thing it really understands.

Therefore, something called the binary system was created. It's a counting system, a bit different from decimal, in which we express numbers using only two digits and that's all. It's a bit more spread out compared to decimal - writing the same number as in decimal takes up more space, you could say, but generally it's not some complicated concept, you can figure it out.

And now, having something the computer can understand, namely the **binary system**, based on two values, we can build on it.

We, as smart people, built something called **character encoding**. We figured out that in certain cases, a given number in the binary system would mean not a specific number but, for example, a character.

And so one of the first more popular encodings was created, namely **ASCII**. ASCII was cool, but it had the disadvantage that the creators didn't foresee many characters, let's say. You know, thinking they're the center of the world, they only thought about characters from their own alphabet.

So something new came along that we use to this day, something a bit better - **UTF-8**. UTF-8 is a way of encoding **UNICODE** characters. Unicode is a kind of 'mapping' of numbers to given characters. To avoid backward compatibility problems, meaning so that old texts and programs would work on new computers, UTF-8 is **backward compatible** with ASCII, meaning text in ASCII is also valid UTF-8 text. The other way around, not necessarily: not every UTF-8 is valid ASCII.

I'm probably boring you a bit, right? I warned you at the beginning - there will also be some theory and other things, because this won't just be a book about Python. Although I'll honestly admit that I'm actually very interested in all these topics.

It's incredible to me what we've created as humanity and how all these processes happen. Beautiful stuff. I hope that at least in part I'll manage to interest you, reader, during this reading, in such topics - not just Python itself, but computer science, science in general.

On the other hand, I think that the approach I present here - discussing a broader scope, some history and theory, rather than just dryly saying, "Here's print and it prints text." is much better. It gives you insight into the fundamental theories that lie at the feet of what you'll use every day. You'll know the tool and its construction, application; you'll be aware. In my opinion, this is necessary to be a good programmer.

We'll move on to exercises/questions shortly. Besides them, I'd like you to play around a bit on your own after each chapter with what I write about - we're talking about print, so print some things. I know it seems boring, but do it. Please. Besides that, you can google a bit more and delve into the topics mentioned here. It'll help.

## Exercises and Questions

Some will be super trivial, but answer them anyway. Well. If you don't fully know the answer, don't worry, maybe reread some part, try to think.

It's best to take a piece of paper and write down your answers to questions that don't require programming. This will make you remember better. Formulate an answer based on the text. I'll give you the answers later.

1. What function in Python is used to print text to the screen?
1. Does this function print something besides the text that was entered, or not? Hint: what happens when you use it again to print something new to the screen? Will the text be on the same line?
1. How does the computer know when to start printing on a new line?
1. What is the binary system?
1. What is a bit? And what is a byte?
1. What length is a byte currently? Were bytes always this length?
1. What values does the computer understand at its very foundations? Why?
1. What's the deal with ASCII? What is it?
1. How does the computer internally represent the text you type?
1. And this whole UTF-8 thing - what is it?
1. Approximately (order of magnitude) how many characters can be represented using the two encodings we talked about in this chapter?
1. Convert the following numbers from decimal to binary: 5, 10, 32, 127, 256.
1. Now the other way around, from binary to decimal: 0000 1101, 1000 0000, 0010 0100.
1. Are the two character systems we discussed backward compatible with each other? In both directions? That is, A with B and B with A? Or maybe only in one direction?
1. What's the difference between UTF-8 and UNICODE? What is what?
1. Differences between UTF-8, UTF-16, and UTF-32. Which one usually uses the least memory? Which one uses the most? Why is it sometimes worth choosing the less memory-optimal variant?


You'll find the answers on the next page.

## Answers

1. The print function.
1. Yes, it additionally prints a newline character at the end of our text, which causes anything new we print to be on a new line.
1. The computer knows it needs to print text from a new line when it encounters a special character known as the newline character. It doesn't display it to us, but interprets it itself.
1. It's a number notation system using 2 digits - 1 and 0.
1. A bit is the basic and smallest unit of information we use to store binary values, like a digit in the binary system - it's a basic particle that takes one of two values. A byte, on the other hand, is nothing more than 8 bits.
1. Currently, it's generally accepted that a byte is 8 bits. It wasn't always this way; before the 8-bit convention became widespread, you could encounter bytes of completely different lengths.
1. The computer, at its very foundations, understands only two values. 1 and 0. Nothing else. Everything above is human abstraction. This stems from how it's built - the binary system is based on the computer operating on two values: voltage and no/low voltage.
1. ASCII is a character encoding system. A kind of translation where appropriate numbers are assigned to specific characters. Something like ciphers you created as a child. We simply agree that X means Y.
1. The same way as everything else - using 1 and 0, i.e., numbers. These numbers are then translated into specific characters.
1. UTF-8 is a UNICODE encoding system. So kind of like ASCII, but newer. It allows representing more characters and so on.
1. ASCII - 256, UTF-8 - 2,097,152
1. I don't feel like doing this.
1. This one either.
1. Yes, UTF-8 is backward compatible with ASCII. ASCII is not compatible with UTF-8, meaning every valid text encoded in ASCII will be valid in UTF-8/Unicode, but not every text in UTF-8 will be valid ASCII.

\pagebreak
