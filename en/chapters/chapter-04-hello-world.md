\pagebreak

# Hello, World!

Finally, we're starting to code! Phew, it took us a while, didn't it? About 50 pages or so. Anyway.

## Printing Text to the Screen

Hello, World! These words are quite popular in programming, at least their English version - Hello World!

It's traditionally considered the text that a beginner programmer's first program will print to the console - printing 'Hello World!' on the screen.

We'll do something similar, but slightly differently, in two ways. Why? Well, you often hear opinions on the internet that Python already has a solution for everything, ready-made code that someone else created, and we just import it and use it - and that's basically what programming in Python is all about.

Like building a program from ready-made blocks. The key is knowing which blocks to use.

Well, that's often true. Very often. And it's no different with hello world. The examples shown here should be typed into a file and run as described in the previous chapter, or typed directly into the interpreter. I recommend the second option, at least while we're dealing with one-liners/few lines. For longer things, I recommend working with files rather than just the interpreter.

In Python, the standard Hello World can be replaced with:

```python
import __hello__
```

What will appear before our eyes?

```
Hello world!
```

Yup. Python even has a ready solution for hello world, but that's more of a curiosity - now I'll show you how to print something to the screen using Python in the normal way.

```python
print("Hello, World!")
```

And that's basically it. The console will display: "Hello, World!". That's all there is to it.

A small note for complete beginners: if you don't know where to enter this code, it's simple - create any file with a .py extension in your working directory (CWD), check the chapter about the four horsemen of the console if you've forgotten what that means.

Then enter this line in that file using a text editor. After that, all you need is:

```bash
python your_file_name.py
```

and you're done. Or instead of python, you might need to type python3, depending on how you installed everything.

What happened here? We used one of Python's built-in functions that are included in the language's standard library - a collection of functions that every Python3 installation has. This function is called print - from English, meaning to print.

Hmm, so what might a function called "print" do? Good question. I think this will be the real test of whether you're cut out to be a programmer. If you can figure out what the print function does, you probably have what it takes to be a programmer. Congratulations.

We pass this function an argument (something for the function to act on) in the form of what we want to print. It will be displayed on the screen, along with a newline character. The newline character, which Python automatically adds to what we print, means that if we now use another print to print something else, our value from the second print will be displayed on a new line.

Because the computer needs to know when to display a 'new line' and end the current line. To let it know when to do this, we have something called a 'newline character'. When you press enter in Word, this character is inserted underneath. So:

```python
print("Line 1")
print("Line 2")
```

Will give us, as expected:

```
Line 1
Line 2
```

The newline character is usually `\n`. So in reality, instead of just displaying "Line 1", Python displays "Line 1\n". 

Is all this simple? Anti-climactic? Yes. At least apparently. Because underneath, many very, very interesting things are happening that you have no idea about yet.

The fact that today, with one line of code, you can print some text in the console is the result of decades of work and foundation-building by the fathers of computer science. I know it might sound funny, but that's how it is. Look at Assembly code, for example, the language everyone used to write in.

The code fragment below is Assembly, a very low-level language that allows very detailed direct interaction with computer memory, processor, basically everything. This gives the programmer the ability to manage and optimize almost everything, but it comes at a price - since you have to manage everything yourself, well... You have to do it yourself. It has its pros and cons. Let's not worry about it too much right now, I'm just mentioning it so it stays somewhere in your mind. Assembly = fast, low-level language where you have to do a lot of things yourself, which is very close to the processor/memory, with a low level of abstraction.

```nasm
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

And I'll note right away - don't worry if you completely don't understand this code. Relax. I don't understand much of it either. It doesn't matter. It's just to show you interesting, old ways.

And you know what's even more interesting?

The fact that currently, underneath, Python looks exactly like this. That is, not Python itself - because Python is just a language - a set of rules, definitions, but I'm talking about CPython - the implementation of the Python interpreter, and those can be arbitrary, I wrote about this earlier, you can read about it. It's worth remembering that CPython is Python's default implementation.

The difference between Python and CPython is that Python is simply a language, meaning a set of instructions and a description of what functions this language has and how it should behave in given situations.

And CPython is already a specific implementation of this - translation into computer behaviors, a specific program executing commands in a specific way. So CPython != Python.

So let's repeat once again. Python is a language. The Python interpreter is already some program that interprets code written in Python and executes specific commands. Usually, when we talk about the Python interpreter, we mean its default implementation, CPython - a Python interpreter written in C, but there are others. Remember. Also remember that the implementation details of Python interpreters differ from each other. The language authors allowed certain behavioral decisions to be made by the people implementing the interpreter. Therefore, CPython may, but doesn't have to, sometimes behave differently than Jython. So it's good practice not to rely on interpreter implementation details but on the language specification itself. But let's get back to the topic.

## Binary Language - The Only Thing a Computer Understands

I don't know about you, but I've always found it interesting how a computer works. How it happens that after pressing some magic button, electrical energy starts 'flowing' through this wonderful machine, various characters appear on the screen, and everything is so beautiful and nice.

Well, the matter is simple. At the very foundations of how computers work lies nothing else but two simple things: True and False, 0 and 1, yes and no. I'm talking about the binary system, machine language.

What do I mean by that? Well, a computer is nothing more than a huge, huge group of conductors/semiconductors stuck together, like 'switches' that can be 'on' or 'off' - they have two states. These states are regulated by the voltage of the current flowing through the conductors, it determines whether one is on or off.

Depending on what combination we have, which 'conductors' we have turned on, which turned off, the computer will do different things. It's like with a washing machine - depending on which buttons you leave pressed, it will do something different.

Since we have two states here, anything that has to do with this is often adorned with the adjective 'binary'. Binary number system. Binary choice. Binary tree. Binary people living in a probabilistic world, and so on. 

Anyway. So we establish one thing. Our computer operates only on two values - 0 and 1, or no/low voltage and high voltage. That's all. In a great simplification, this is exactly what is the complete basis of the entire computer and nothing more.

I assume my readers are smart people. So a question should appear right away - But how? If a computer only understands 0 and 1, how can I type different letters here, read them later, move the mouse, enter numbers other than 0 and 1. What? You're making this up, Mr. Górski.

Well, nothing could be further from the truth. Your computer really only understands 0 and 1. Everything else is the result of various calculations, conversions, and encoding of other values to these 0s and 1s.

This text is a perfect example.

## How a Computer Sees Letters - Binary System

Imagine that all the letters you see here are actually nothing more than a number, written in binary system.

For precision - what is a number written in binary system? It's nothing else than a normal number, just expressed using only 0s and 1s. We, as humans, chose decimal system as our basic one. Probably because that's how many fingers we have, but who exactly knows.

Anyway - we operate on the assumption that we have 10 digits, each order of magnitude can have 9 or 10 possible states, or may not exist at all, and orders of magnitude are based on powers of ten.

In the binary system, it's actually similar, except instead of 10 digits, we have only two and two values. Additionally, we calculate subsequent orders of magnitude not based on powers of ten but on powers of two.

Let's take, for example, the number 123. How do we calculate its value? Well.

1 - number of hundreds, third digit
2 - number of tens, second digit
3 - number of ones, first digit

$1*10^2+2*10^1+3*10^0$ = $1*100+2*10+3*1$ = $100+20+3$ = 123

As you can easily see, the exponent is a number equal to the digit number, counting from the right side, decreased by 1.

This all sounds complicated because we don't think about it this way - we do certain things naturally due to experience, so it might take some practice to switch to thinking about it this way.

The situation in binary notation will be analogous. How do we calculate the value of a given number in binary notation? Let's assume we want to know what value the number 101101 has.

```
1 - 6th digit of the number
0 - 5th digit of the number
1 - 4th digit of the number
1 - 3rd digit of the number
0 - 2nd digit of the number
1 - 1st digit of the number
```

Therefore: \
$1*2^5+0*2^4+1*2^3+1*2^2+0*2^1+1*2^0$ \
$1*32+0*16+1*8+1*4+0*2+1*1$ \
$32+0+8+4+0+1$=45

So 101101 is nothing else than the equivalent of 45 in decimal system. And how to convert from decimal to binary? Very simple.
You divide the number by two and write out the remainder each time. \
$45/2$ = 22 remainder 1 \
$22/2$ = 11 remainder 0 \
$11/2$ = 5 remainder 1 \
$5/2$ = 2 remainder 1 \
$2/2$ = 1 remainder 0 \
$1/2$ = 0 remainder 1

Now, we read the remainders from BOTTOM to top: 101101. Does it match? Yep.

Analyze this slowly and carefully for now. It's nothing if something isn't clear at first, it's just a way of converting from one system to another.

Knowledge of powers of two values comes in handy here. When you have some of them in memory, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16386 etc., some conversions become easier and faster.

Anyway. Let's get back to the topic. So... Ah yes. Letters are also numbers. 

## Character Encoding - ASCII

Right. Since a computer understands only and exclusively numbers, those in binary system, meaning essentially zeros and ones, how do we tell it to store some letter?

Can you imagine a world where instead of reading my words on the screen using letters, you would read each letter written somehow using binary system, manually translating it to human on paper? I can't, but that's more or less how it looks in reality, only the computer does it for us.

Well, a few smart gentlemen gathered once and decided that it would be a good idea to create a kind of translation - a translation, mapping of alphabet letters to... numbers.

Each letter of the alphabet received its unique code in the form of some number. Why? Because how do you tell a computer that 'k' is 'k'? You can't. The computer is stupid, it doesn't understand the concept of a letter. At least for now, in a few or several dozen years, who knows.

Numbers in decimal system, however, we can easily convert to numbers in binary system, meaning to something that the computer will already understand.

And so we created something called the ASCII standard, which stands for American Standard Code for Information Interchange. It's a kind of table that contains mapping of English alphabet characters, punctuation marks to numbers. Like a dictionary of sorts, which letter corresponds to which number.

For example, 'A' - capital A, was marked as 0100 0001, or 65. 'a' is 97. The newline character is 0000 1010, or 10. Why? Because that's how it is and that's it. That's what the American wise guys came up with and that's it. It's kind of a conventional matter.

A small note, we usually write numbers in binary system with the prefix `0b`, so it's clear that we're dealing with binary. Because how do you distinguish between 10 in decimal and 10 in binary? The notation is the same but the values are different. It's like in that joke that there are only 10 types of people in the world, those who understand binary language and everyone else. Hehehe, a programmer's dad joke, sorry.

B in ASCII encoding is 0b0100 0010, or 66. C will have the number 67. And so on. Guess what D will have?

Every letter you see here is translated in a similar way and stored on your computer's disk as a sequence of ones and zeros. Then, when reading, the computer, after interpreting what letter a given number is, displays the specific letter. However, it completely doesn't understand that this 'k' is some letter, and not a piece of binary code. Simply.

What distinguishes ASCII? ASCII is an encoding where each element can be expressed using 7 bits. What does it mean, using 7 bits? A bit is nothing else than a 'digit' in binary system.

At least that was the original assumption. It therefore allows for the translation of 128 characters, to numbers from 0 to 127, inclusive.

Many people, at least those who had some contact with programming or computer science, will be surprised. What do you mean - 7-bit ASCII? Everyone often learns that it's 8-bit. Well, no, originally ASCII was designed as a 7-bit system, having 128 characters.

The fact that today we often think about ASCII in the context of 8-bit comes from the fact that during the creation of ASCII, 8-bits wasn't yet such a standard. Many encoding systems were 7-bit, and they used the 8th bit for their own various strange needs.

What does it mean that 8 bits is a 'standard'? Well, nowadays we have something called a byte. A byte is a collection of 8 bits. Like 1111 0000 or 1000 0000.

It's such a very small unit of your computer's memory that you can use. Whether in RAM or disk memory.

It's clearly defined and simple. But... A byte wasn't always defined as 8 bits. There were systems where 1 byte, the basic unit, was defined completely differently - as 2 bits, 7 bits, 6 bits. Pick your poison. Free for all.

In general, many things in computer science or programming, like in mathematics, are conventional. Get used to the fact that sometimes we do something in a specific way just because that's how it is. Computer scientists basically come from mathematicians in a straight line, so we're strange people.

That's why today, despite ASCII originally being a 128-character 7-bit system, it's written using 8 bits, giving it 256 possible characters, officially, 8-bit ASCII we call extended ASCII, but colloquially, usually when we say ASCII, we mean this 256-character one - with several additional characters.

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

Simply put, there was chaos before. And from chaos emerged order. And computer science was born. In this place, order and chaos coexisted in harmony so you could show me your wares. Okay, enough nerdy references to Gothic.

Well, anyway. Because I lost the thread.

We have this encoding, in this case ASCII, and it's elegant. Although not completely, because a problem appears. We use ASCII on 8 bits now, right? Yes. 8 bits, that's 8 zeros or ones, right? Yes. Using 8 zeros or ones, we can express 256 numbers.

Taking into account that 1 number = 1 letter, we'll quickly see that we have a maximum of 256 characters to use.

That's a bit small to accommodate all the world's alphabets, right? Indeed. Let's also consider that 'A' and 'a' are two different letters for a computer - lowercase and uppercase characters are not the same. Add periods, commas, and other punctuation marks.

It quickly turns out that not much space is left for just letters.

That's why ASCII encoding contains only Latin alphabet letters. You can't write in other languages in ASCII because there aren't enough characters. What now?

Well, you see, so that Poles and other nations, like Chinese or Japanese people, who have quite a lot of these characters because each word can be a different character, meaning like a different letter for us, wouldn't feel disadvantaged, new encodings started to appear. Many encodings. Way too many. We won't talk about them. We'll skip straight ahead to times of clarity.

## And Then UNICODE And UTF-8 Enter All in White

Currently, however, the standard is something called UTF-8. It's a UNICODE character encoding system that uses 1 to 4 bytes for storage. Oh, important information. Up to 4 bytes. 4 bytes, how much was that? 1 byte, 8 bits, 4 bytes, 32 bits. And what does it mean that UTF-8 is a UNICODE character encoding system? UNICODE is our whole mapping of which letter/character corresponds to which number, and UTF-8 is a way of writing this, converting to bits, because when you have slightly more than 1 byte, the matter becomes less obvious, hence these characters/mappings can be presented differently. UTF-8 is one of the ways to do this. Going back to the bytes topic...

32 bits means 32 ones or zeros, so using them we can write many different numbers, therefore also different characters. Now this becomes quite a lot, because it gives us about 4,294,967,296 possible characters. Quite a lot, right? It's still less than the 70 million that Sasin wasted on elections that didn't happen, but that's nothing. Even if we put all those Asian characters in, there will still be plenty of space left. Beautiful, idyllic. A dream.

A dream, because in reality, since RFC 3629, UTF-8 handles at most 2,097,152 characters. This is due to various historical circumstances, implementation details, and other strange things that you don't need to worry about, neither you, dear reader, nor I, but rather big brains like Ken Thompson and company, somehow it turned out that some bits are reserved for special purposes, some bytes must have a specific format to know various useful things, and so on.

And what's this whole RFC about? Generally, these are standards that certain brains set. On what basis? On whatever they decide. Similar to ASCII - because that's how it is. In general, I'm simplifying, and essentially when making various decisions, decision-makers are guided by more rational arguments.

That many characters is enough for us on a daily basis. Currently in UNICODE we have defined standardly about 143,859 characters. So we even have some reserve in case we need to add new characters later.

Or rather `codepoints`, but let's simplify, not delve into it and just say characters. What is a codepoint? Usually when discussing various encodings, instead of 'character', the term codepoint is used. Small difference. From your perspective, it doesn't really matter much.

So: remember that when UTF-8, then generally also Unicode. Keep these two terms together in memory, but UNICODE is not the same as UTF-8 and that's very important.

Plus another note. There's also something called UTF-16. How does it differ from UTF-8? In word length. Meaning in UTF-8 one word has 8 bits, in UTF-16 it has 16 bits. And that's it. There's also UTF-32. Here there's always one word, such 32-bit.

Just to be clear - they have the same number of bytes in the upper limit, meaning maximum 4, and in the case of UTF-16, minimum 2 (well, because 16 bits). What is a word? It's not a word like from the dictionary. Word, meaning machine word, is kind of like a byte, but not quite. A way to group bits into X pieces simply.

In UTF-8 some characters can be expressed with 1 word, meaning 1 byte, in UTF-16 the smallest size is 2 bytes and in UTF-32 it's already 4 bytes. Meaning regardless of what character we use, e.g., `A`, meaning 65, meaning something that fits in 1 byte, with UTF-32, the computer will still write everything in 4, wasting quite a lot of memory. In UTF-16 it will write in 2, in UTF-8 in one. More economical. But UTF-32 is easier to find in memory because you know that each character is 4 bytes and that's it. And in UTF-8 there are different lengths, one character will have 1 byte, another 4, well and try to guess here, human, what is what, what ends when and where, but somehow we manage with it.

You don't need to worry about this too much, but somewhere there maybe remember.

UTF-8 is 100% compatible with ASCII - text in ASCII is valid UTF-8, but UTF-8 does NOT have to be valid ASCII. This is very important! Why? Because UTF-8 mainly contains characters that we can't fit in one byte, making them absent in ASCII. Therefore, ASCII is a subset of UNICODE.

By the way, interesting fact - when you write some messages on Facebook and send emojis, they are often encoded in UNICODE too, they have their specific numbers!

## Summary

Let's summarize what we managed to do and learn.

We have in Python a function called **print**, which, attention, prints text on the screen. This text in reality is not text for the computer, but nothing else than a sequence of zeros and ones, because the computer doesn't understand anything else, due to how it's built - voltage or lack/low voltage - that's all it really understands.

Therefore, something called the binary system was created. It's a counting system, slightly different from decimal, where we express numbers using two digits and only that. It's somewhat more sprawling compared to decimal - writing the same number as in decimal takes up more space, you could say, but generally it's not some complicated concept, it can be grasped.

And now having something that the computer can understand, meaning the **binary system**, based on two values, we can build something on that.

We, as clever people, built something called **character encoding**. Well, we figured out that in certain cases, a given number in binary system would mean not a specific number but e.g., a character.

And thus was born one of the first more popular encodings, namely **ASCII**. ASCII was cool, but it had this flaw that the creators didn't anticipate many characters, let's say. You know, Uncle Sam, center of the world, didn't think about other nations, only about characters from their alphabet.

So something new came along, which I use to this day, which is somewhat better - **UTF-8**. UTF-8 is a way of encoding **UNICODE** characters. Unicode is a kind of 'mapping' of numbers to given characters. To avoid problems with backward compatibility, meaning so that old texts and programs would work on new computers, UTF-8 is **backward compatible** with ASCII, meaning text in ASCII is also valid UTF-8 text. In the other direction, not necessarily - not every UTF-8 is valid ASCII.

I'm probably boring you a bit, aren't I? I warned at the beginning - there will also be some theory and other things because this won't be just a book about Python. Although I admit honestly that I personally find all these topics very exciting, interesting.

It's amazing to me what we've created as humanity and how all these processes work. Beautiful thing. I hope that at least partly I'll manage to interest you, reader, during this reading, with such topics - not just Python itself, but computer science, science in general.

On the other hand, I think that such an approach that I present here - discussing a broader scope, some history and theory, and not just dry saying, "Oh here you have print and it prints text." is much better. It gives you insight into the fundamental theories that lie at the feet of what you'll use every day. You'll know the tool and its construction, application, you'll be aware. In my opinion, this is necessary to be a good programmer.

We'll move on to tasks/questions soon. Besides them, I'd like you to play a bit yourself after each chapter with what I write about - we're talking about print, do some printing yourself. I know it seems boring, but do it. Please. Plus, you can Google a bit more and delve into the topics discussed here. It will help.

## Tasks and Questions

Some will be super basic, but answer them anyway. Well. If you don't completely know the answer, don't worry, read some piece again if necessary, try to think.

Best to take a piece of paper and write down your answers to questions that don't require programming on it. This will make you remember better. Formulate the answer based on the text. Later I'll give you the answers.

1. What function in Python is used to print text to the screen?
2. Does this function print anything besides the entered text, or not? Hint: what will happen if you use it again to print something new on the screen? Will the text be on the same line?
3. How does the computer know when to start printing on a new line?
4. What is the binary system?
5. What is a bit? And what is a byte?
6. What length is a byte currently? Were bytes always this length?
7. What values does a computer understand at its very foundations? Why?
8. What's the deal with ASCII? What is it?
9. How does a computer internally represent the text you type?
10. And this whole UTF-8 - what is it?
11. How many characters approximately (order of magnitude) can be represented using the two encodings we talked about in this chapter?
12. Convert the following numbers from decimal to binary: 5, 10, 32, 127, 256.
13. Now in the other direction, from binary to decimal: 0000 1101, 1000 0000, 0010 0100.
14. Are these two character systems we discussed backward compatible? In both directions? That is A with B and B with A? Or only in one direction?
15. What's the difference between UTF-8 and UNICODE? What is what?
16. Differences between UTF-8, UTF-16, and UTF-32. Which uses the least memory usually? Which uses the most? Why sometimes it's worth choosing the less memory-optimal variant?

You'll find the answers on the next page.

## Answers

1. The print function.
2. Yes, it prints an additional newline character at the end of our text, which means that if we print something new, it will be on a new line.
3. The computer knows to print text on a new line if it encounters a special character, known as the newline character. It doesn't display it to us, but interprets it itself.
4. It's a number system using 2 digits - 1 and 0.
5. A bit is the basic and smallest unit of information used to write binary values - it's such a basic particle that takes one of two values. A byte is nothing else than 8 bits.
6. Currently, it's generally accepted that a byte is 8 bits. It wasn't always like this, before the spread of the 8-bit convention, you could find bytes of completely different lengths.
7. A computer, at its very foundations, understands only two values. 1 and 0. Nothing else. Everything above is human abstraction. This results from how it's built - the binary system is based on the computer operating on two values: voltage and lack/low voltage.
8. ASCII is a character encoding system. A kind of translation where we assign appropriate numbers to specific characters. Something like the ciphers created in childhood. We simply agree that X means Y.
9. The same as everything else - using 1s and 0s, meaning numbers. Then it translates these numbers into specific characters.
10. UTF-8 is a UNICODE encoding system. So kind of like ASCII, but newer. Allows representing more characters and so on.
11. ASCII - 256, UTF-8 - 2,097,152
12. I don't want to do this.
13. This either.
14. Yes, UTF-8 is backward compatible with ASCII. ASCII is not compatible with UTF-8, meaning any valid text encoded in ASCII will be valid in UTF-8/Unicode, but not every text in UTF-8 will be valid ASCII.
15. UTF-8 is a way of encoding UNICODE characters. UNICODE is the mapping of numbers to characters.
16. UTF-8 uses variable length encoding (1-4 bytes), UTF-16 uses 2-4 bytes, and UTF-32 always uses 4 bytes. UTF-8 usually uses the least memory for English text as most ASCII characters only need 1 byte. UTF-32 always uses the most memory but provides constant-time character access since every character is exactly 4 bytes.

\pagebreak 