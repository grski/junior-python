\pagebreak

# Python - What's It All About?

## Python - What's It All About?

Before we dive into learning Python, let me tell you a bit about the history of the language, where it comes from, its goals and assumptions, how it evolved and changed over the years, and what it looks like today, where it's used and why.

## How to Use This Book

Hold on a moment. I'd like to tell you how I think you should use this book. First, I tried to write it in a way that naturally progresses from one topic to the next - from simple topics to more complex ones. Thanks to its linear structure, it should be easy to understand.

However, if you're already a more experienced programmer, or if you just want to refresh certain concepts, feel free to jump around - most chapters are relatively self-contained components.

Another thing I want to mention, or rather repeat, is that in this book you won't find information exclusively about Python. Beyond information about the language itself, I'll also try to introduce you to certain concepts from computer science in general, so you'll know a bit more, understand how things work, and why they work that way.

I believe this is essential knowledge to become a good programmer who grows and goes far. Such chapters will be somewhat more theoretical in nature, but that doesn't mean they're boring - quite the opposite, in my opinion.

If you want to properly absorb the information contained here and really learn something new, I strongly advise: first, take notes - short, concise, and simple ones.

Second - type out the code. Don't use the Copy-Paste method. Type it out yourself, period.

Finally, number three - independently complete the exercises that I'll place at the end of chapters, but that's not all - experiment with the code. Change it, see what effects these changes have. Experience it in practice, analyze your modifications, think about them and their results, how they affect the program's operation. This is the best method of learning. This is the basic assumption that guided me while writing - that you will independently complete exercises, read additional articles, books, and conduct experiments with code.

You can read more about how one should learn and what methods work in Gynvael Coldwind's blog post - Beginner Programmer's Guide. Grski recommends it. In fact, I recommend the entire blog. There are few places on the Internet where you can find such good and interesting content. Google it, because it's worth it.

Additionally, I want to point out that I won't write about every tiny detail in this book. This isn't a Python encyclopedia; the assumption here is that you'll look up the details of various things yourself. I want to draw attention to often overlooked things. **Therefore, I recommend that alongside this book, you read materials from Django documentation, Python documentation, the excellent book Learning Python, 5th edition, and the CS50 course**. I more want to make you aware of certain things and explain some concepts, additionally dealing with this often overlooked practical knowledge, an honest account of my experiences.

## Interactive Part

On my GitHub, you'll find the repository `junior-python-exercises - https://github.com/grski/junior-python-exercises`. If you'd like your exercise solutions and answers to be checked, fork this repo (you'll learn what that means later), then in the appropriate chapter folder add a folder with your GitHub nickname and put your answers inside. I'll do a code review/look through these answers and give some feedback :)

## Python 2 - Python 3?

Python currently exists mainly in two versions - Python 2 and Python 3. These are two 'main' releases of the same language, however version 3 is newer and introduces certain new things that are not backward compatible with version 2, hence the version number jump.

The introduction of Python 3 happened many years ago, and currently, we're in times when Python 2 is no longer being developed. It's dead and that's it. The only projects in it are some heavy legacy ones. Besides that, somewhere there are slowly some whispers about Python 4.

What does this mean from your perspective as a beginner? Nothing. Just know that you're currently learning Python 3 and that's it. It's still the same language, but there are some differences between it and Python 2 that you can easily learn in a few moments if needed. I choose the newest version to present you with the freshest information, and honestly, Python 2 is slowly becoming a relic of the past, and whoever creates new software in it now is making a mistake, although I don't think such cases can still be found anywhere, except for a few corporate exceptions.

If anything, Python 2 is now only used to maintain old applications written in it, and believe me, more often than not, you don't want to work on maintaining old behemoths. Unless they pay you a lot of money. A lot, lot of money. Even more than a lot. Seriously. Although it's still not worth it. What good is money when you literally change professions from programmer to sewage diver, diving in the programming excrement of some people who hated their lives more than usual, so they created a monster?

Python 2 is passing into history and that's good, nevertheless I'll occasionally mention the differences, basically as a matter of interest.

## A Brief History of Python's Long Journey

Python is quite an old language, so to speak. Older than me, although that's no achievement actually.

Currently, there are plenty of new languages in the market - children like Scala, Dart, Elm, Elixir, Kotlin, and many, many others. Compared to them, Python is an old-timer, as it appeared at the beginning of 1991 at CWI - the Center for Mathematics and Computer Science in Amsterdam. While it's not as ancient as C from 1972, it's definitely a full-fledged middle-aged language.

Its main creator was Guido van Rossum, who until recently had the nickname "Benevolent Dictator for Life" (or rather had, as we'll discuss shortly) and is generally considered the highest authority in the Python world.

Speaking of unusual facts, if you manage to find Guido's email address somewhere on the web (it's not difficult) and send him an interesting email with a question or anything, there's a good chance he'll respond. At least that's what many other Python users have experienced.

The language name itself doesn't come, as one might think, from the snake species, but from a TV series broadcast in the seventies by BBC - "Monty Python's Flying Circus", of which Guido was a fan and thought that naming his programming language 'Python' would be something. And well, it is. Just this alone should be enough to encourage you to use this language.

Python began its public life in version 0.9.0, but didn't stay in it for long, with new versions coming out quickly. This involved various changes, as van Rossum himself, as well as the most important team members, changed their 'home' many times, moving from one organization to another. Code is code, but you have to live on something.

Everything settled down with the arrival of version 2.1, which was released under the Python Software Foundation - a non-profit foundation that operates to this day and is modeled after the Apache Software Foundation.

Python was intended to be the successor to the ABC language - another prehistoric creation that we won't discuss much, despite its evident influence on Python.

Besides ABC, Python shows clear influences or elements borrowed from languages such as: C, C++, Haskell, Java, Perl, and Lisp. Should this mean anything to you? Definitely not if you're a beginner. Just know that Python has some elements in common with other languages and isn't some strange oddity.

## Guido's Abdication

Around the time of writing this book, right at the beginning (well, I can say I took long breaks...), something unprecedented happened: Guido van Rossum, Python's creator, decided to distance himself from the Python decision chain and drop his BDFL title, slowly retiring altogether. This was all caused by PEP 572, which was proposed by Guido himself, among others, and which triggered quite unfavorable reactions from the community. What was it about?

About the := operator and assignment in expressions. A large part of the community started criticizing this idea very loudly and strongly, often without any basis, as, at least to me, the PEP itself seems rather well-thought-out and nice, this functionality will definitely be useful somewhere in Python. We'll talk about this PEP later, so no details for now.

Below I include the text of the email published by Guido, translated by me:

"Now that PEP 572 is done, I don't ever want to have to fight so hard for a PEP and find that so many people despise my decisions.

I would like to remove myself entirely from the decision process. I'll still be there for a while as an ordinary core dev, and I'll still be available to mentor people - possibly more available. But I'm basically giving myself a permanent vacation from being BDFL, and you all will be on your own.

After all, this is what you all want. And it even fits the natural pattern of things - Guido's retirement has been anticipated for more than a decade, and there's no reason to believe that I'm going to get smarter (or less stubborn) as I age.

I am not going to appoint a successor.

So what are you all going to do? Create a democracy? Anarchy? Dictatorship? A federation?

I'm not worried about the day to day decisions in the issue tracker or on GitHub. Very rarely I get asked for an opinion, and usually it's not actually important. I'm happy to leave that to the core devs.

The big issue is how are PEPs going to get decided. We may need a voting process. There might be a bunch of small decisions to make, like:
- establish the voting process
- establish the criteria for voting (e.g. who gets to vote)
- establish criteria for accepting/declining PEPs
- decide how to select new core developers
- decide how to kick people out
- establish a CoC (if it's not there already)
- establish a ban process

We may be able to write up processes for these things as PEPs (maybe those get accepted by a different process).

Note that there's still the CoC - if you don't like that document your only option might be to leave this group.

I'll still be here, but I'm trying to let you all figure something out for yourselves. I'm tired, and need a very long break."

What more can be said here.

It was a sad moment in Python's history, especially since Guido is Python and Python is Guido.

That's it. Shocking news.

Well, may you fare well, Mr. Guido.

While I don't fully sympathize with him due to various strongly politically correct behaviors, bordering on paranoid I'd say, but still. He did a great job and deserves respect for that.

But the question is how will the Python world look without this man? What direction will it choose? It's an opportunity for growth, but also a threat that we might lose the direction that is currently quite nice.

Anyway... A new wind will blow in the sails, where will it lead us? Time will tell. In a year, two, five. We'll decide about it, the community that creates Python, which means soon you too, dear reader.

Note: from the perspective of time, it's still good. Guido's departure hasn't changed Python for the worse.

## Python's Goals

With Python, the situation is that it's really worth using. Personally, I believe it's one of the best languages for learning programming basics, which was its intended purpose. It allows you to quickly move on to understanding certain programming concepts because the student doesn't have to focus too much on mastering complicated syntax or complex expressions, as sometimes happens in other languages.

Python is concise and simple - most code can be very easily understood by anyone who speaks even a little English or has a dictionary handy, and the code itself is usually short and elegant.

Only a few symbols need explanation, used to shorten notation. Beyond that, Python reads very much like sentences in English. This is also the first snake goal - simplicity over complexity.

Python was meant to be simple, pleasant, and elegant. I believe it absolutely is.

Another goal is portability. Python can run on almost all currently popular platforms - Windows, almost any Linux, macOS. Until version 3.7, released on 27.06.2018, something as strange as FreeBSD version <= 9 was even officially supported.

Thanks to this, Python can run almost anywhere, as long as the hardware resources allow it.

The next goal that Python had was openness. Some languages are quite 'hermetic' - they can only be used after paying for a license or only under specific conditions, purposes.

Python doesn't have this problem - it's completely free to use, modify, distribute, and whatever else the user wishes.

Additionally, Python is open-source, and its development is community-driven. What does this mean in practice? Everyone has access to the language sources for one thing, and two, if you don't like something in Python, you think something could be done better, then...

No problem. Take that function and just add it, change it. If the community finds your changes justified and useful, they'll end up in the language itself. Therefore, everyone can have a real impact on what Python looks like, how it works. Great thing.

These are just a few of the ideas behind Python; I won't describe all of them here, but I think I've managed to cover the most important ones.

## The Snake Sheds Its Skin from Time to Time

What do I mean? About the fact that Python and its applications are constantly changing. Like a snake, it sheds its old skin and gains a new one.

Originally, it was a language that was used rather as a scripting language. Automation of certain processes on servers, some operations on files, text, and so on. Boring things in general. Python didn't take the market by storm; it took some time. At the very beginning, it was rather niche. With time and evolution of the language itself, its advantages and beauty began to be widely recognized.

That's why over the years, Python became increasingly popular when it comes to developing backend parts of web applications, and as we know, these have been experiencing constant growth since the beginning of the last millennium, really. The matter was facilitated by the appearance of various Python frameworks on the market, designed specifically for creating web applications, such as Flask, Pyramid, Pylons, Web2py, and finally Django, which was a real game-changer. Here's an interesting fact. When you browse Instagram, do you know what it runs on? Well, on Django precisely.

Thanks to this, Python became quite popular as a language used for writing web applications, but that's not all. In recent years, we can observe a continuous increase in demand for various specialists related to Data Science, Artificial Intelligence, Machine Learning, or Neural Networks.

All these and related industries are developing incredibly, and the language that essentially rules there is Python. It has a competitor in the form of R, and a rapidly growing contender in the form of Julia, but still, our snake holds strong.

Why? Look at the ideas behind Python - it explains itself. An analyst doesn't have to be a good coder; their task is to process data, so they need a language that will quickly allow them, without unnecessarily delving into syntax or how the language itself works, to translate their thoughts into code.

Python is perfect for this due to its simplicity and versatility. I can already imagine such an analyst sitting and checking whether they've definitely freed all the previously allocated memory in their super beautiful code written in C or C++. There's just no such option. And that's good.

True, this creates a certain problem in the form of performance, but more on that later, because it's something that can be overcome and solved much more easily than trying to teach everyone C/C++.

Of course, Python is still used in various scripts, automation, and so on, nevertheless I believe that this is no longer its main application, as it was years, years ago.

So, as you can see, Python is developing and appearing in an increasing number of projects, fields, and areas related to broadly understood computer science. Personally, I believe that this trend will rather continue, just as it has so far, and Python will gain more and more popularity year by year, but let's get into the details - why?

## Python's Advantages

### Expressiveness

Python is very expressive. What does this mean? Well, in Python, you can achieve with relatively little code what in other languages might take several times as much. To not be unfounded, let's look at an example of the classic program that begins programming learning - Hello World, or in Polish, Witaj Świecie. Which is actually ironic, because when you start programming, you should rather say goodbye to the world, because you won't be seeing much of it anymore from your basement.
In Python it looks like this:

```python
print('Hello World')
```

Pretty simple and understandable, right? One line and done.
Let's look at other languages though.
Let's start with Java:
```java
public class HelloWorld{
    public static void main(void) {
        System.out.println("Hello World");
    }
}
```

Here it's still fairly clear, despite a few seemingly mysterious commands, you can still easily read what the program does, but let's take, say, C++ in our sights:

```cpp
#include <iostream> 
using namespace std;
int main() {
    cout << "Hello World!";
    return 0;
}
```

Here it's a bit less obvious what the program does, right? Plus look at the number of lines used to perform the task. There's no comparison.

I note, however, that in both these languages, you could print hello world with shorter code, I don't know these ways because I'm not a Java guy or C/C++ person, simultaneously too lazy a bum to look for them, nevertheless I'm trying to show the idea here.

Another example of how short code can be in Python compared to comparable code in C++/Java or other languages is below, this is slightly more complicated code, but maybe you'll understand something from it. It was provided to me in a comment by @jacekw on Steemit and it's his authorship. Thanks :)

So what will our assigned code do? Its task is simple:

1. create a list of numbers in descending order 19 to 0
2. Skip even numbers
3. Square each number
4. Sort in ascending order
5. Print the result

By the way, this is a form of algorithm, presented in step form, something we'll return to in the future. Currently remember one thing - an algorithm is simply an unambiguous set of instructions serving to accomplish some goal.

Anyway.

Let's start with *C++* maybe this time.

```cpp
#include <iostream> 
#include <vector> 
#include <algorithm> 
#include <functional> 
using namespace std; 

int main() { 
    vector<int> s, a; 
    for (int i = 20; i > 0; i--) s.push_back(i);
    copy_if (s.begin(), s.end(), back_inserter(a), [](int x) { 
        return x % 2 == 1;});
    transform(a.begin(), a.end(), a.begin(), [](int x){
        return x*x;});
    sort(a.begin(), a.end()); 
    for (auto&& i : a) cout << i << " "; return 0; 
} 
```

I don't know about you, but for me this is quite a convoluted piece of code. As a beginning programmer, I would have trouble understanding it. Lots of strange symbols, marks. What exactly is going on here?

Hard to say at first glance.

The next participant in this comparison is...

*Java*

```java
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        int[] a = IntStream.range(0, 20)
                .map(i -> 20 - i - 1)
                .filter(x -> x % 2 == 1)
                .map(x -> x * x)
                .sorted()
                .toArray();
        System.out.println(Arrays.toString(a));
    }
}
```

*Python*:

```python
a = filter(lambda x: x % 2 == 1, reversed(range(20)))
a = list(map(lambda x: x*x, a))
print(list(sorted(a)))
```

Alternatively, my version in Python would look like this:

```python
print(sorted([i*i for i in reversed(range(20)) if i % 2]))
```

I'll leave it without comment. Finally, I'll add, as a curiosity, an example from another language - Haskell.

```haskell
sort $ map (^2) $ filter odd [20, 19..1]
```

Also interesting, right?

Does this mean these languages are worse and Python is king? Absolutely not, never think that.

Each language is like a tool - it has its applications where it's good, excellent, but it also has ones where it's completely unsuitable. That's how it is here. That's how it is everywhere. Yes, sometimes there are fanatics of certain technologies or solutions whose language-technological brain inflammation obscures objective judgment, but that's nothing. We don't want to be like that. Let's be wise and reasonable, make our lives easier by using appropriate tools for appropriate tasks.

Nevertheless, Python allows us to write more in less code. This of course comes at a certain price that must be paid, and which makes Python good in certain situations and not in others.

### Simplicity

Let's return to the previous point - if we look at Python code, you could say that it's basically just written commands in English. What does the word print mean? Nothing other than print/output.

You can immediately guess that the programmer wants the computer to output something to the screen. The case is similar with other elements of the language; really, just knowing English and we can almost understand a large part of Python. Many languages are similar, but they're not as close to English as Python.

Really, I haven't encountered another language this simple, and I've happened to use quite a few, at least superficially - whether JavaScript, Java, C, C++, Dart, Scala.

The only language that might compete with Python in simplicity is probably C - but that's because the core of that language is just tiny. When it comes to memory management, pointers, and other equally fun things from C, you start missing Python.

### Python as a Dynamically Typed Language

What does this mean? Well, if you're a programming novice, you might have absolutely no idea what this is about, but that's okay.

In short, the matter concerns the fact that in statically typed languages, during variable declaration, you need to specify what type of data this variable will store. Let Java serve as an example here:

```java
int someNumber = 123;
```

The above notation tells the 'program' that will execute our code that we want to create a variable named someNumber that will contain data of type int - integer, which is nothing other than whole numbers. And what does it mean that it has to create a variable?

I'll try to explain it quite simply, but I might not succeed, and if you don't fully understand how this mechanism works, or if it's difficult to imagine how it functions, don't worry, we'll return to the topic later.

This command will cause 'telling' our computer something like this:

Listen computer, here you have some data, (in this case '123'), remember this value, write it down somewhere, because I'll want to use it for something in the future, and from now on, whenever I write `someNumber` in the program, know that I mean exactly the value stored in that place.

Trying to save other data to this variable, let's say, an array or a floating-point number, won't end too well or according to our wishes.

In Python, there are no such restrictions and requirements. First, during variable initialization, we don't need to specify its type, and second, later we can easily change the kind of data we store in a given variable, so the equivalent of the above notation in Python would be the code:

```python
some_number = 123
```

Later we can easily write:

```python
some_number = 'Hi there'
```

What this results from, you'll learn a bit later in the book, but mainly it's about the fact that in Python variables are actually references to an object, not the object per se. As I said, we'll return to this, you don't need to worry about it for now. Just remember that Python makes your life easier and doesn't impose too much, does the work for you, the good snake.

### Community

Python has one really big advantage. It's its community, which one, is really helpful, and two, its size is impressive. Thanks to this, the amount of available materials, tutorials, libraries, frameworks, and scripts can simply positively surprise you.

Thanks to Python's open-source culture, many amazing tools are daily put into our hands for use, completely free, just like that.

This causes that often we don't have to reinvent the wheel - just import some library that someone has already written. This often saves time and worries, allowing us to focus on what's important in our implementation.

Besides, what to do when we get stuck somewhere in program writing and don't know what next, when we encounter some error that we can't solve? Well, due to Python's age and the size of its community, we can assume in most cases that someone before us has already encountered a similar problem and asked about it on the Internet, or described the solution to that problem.

People are quite willing to share knowledge contrary to appearances. Thanks to this, we don't have to search for a solution for hours, digging through documentation, sources, or just experimenting. We can simply ask someone, because many people know Python, or find answers from others who solved this problem before us. Not every language has such a developed knowledge base and community.

As a counter-example, I'll give the Dart language. A rather new language, not very popular, overall small community. Nevertheless, I sometimes created in this language and it happens not rarely that I encounter some problem about which I can't find information anywhere, because simply no one else has encountered it yet, or no one else has described it, so I have to search for a solution myself, combing through documentation, sources and just experimenting.

This, in turn, is often a road through torment.

Additionally, sometimes there's the inconvenience that some things that have already been written by someone else in Python or Java, nicely packaged into a package and distributed for use, aren't necessarily available in Dart and need to be written independently.

Similarly, when it comes to learning the language itself - there are significantly fewer materials, they're often outdated due to the fact that Dart is a constantly developing language and strongly at that, new versions come out every week, at least they used to, whether it's still like that, I don't know, and due to low popularity few people write about it, even fewer create books or tutorials about it.

This doesn't make learning easier, especially for beginning programmers. Good thing that at least the documentation is quite good, although not as good as Django's documentation, for example, but still - it's not bad.

That's why I claim that Python's community is its greatest advantage and it's this community, literally, that creates this wonderful language, making it what it is.

### Multiple Applications

Python is a general-purpose language. You can create practically anything in it, except for a certain, rather narrow group of applications for which it's completely unsuitable and for which it wasn't designed.

Knowing Python, we can create desktop applications, games, web applications, scripts, emulators, interpreters, compilers, scientific calculation applications, data visualization and scraping applications, machine learning, and so on. The list is really long.

Of course, Python is better for some tasks and worse for others, because for example, it's rare that desktop applications or games are created in Python, as there are better languages for that, but anyway, it's possible and not too difficult honestly.

What helps in the fact that Python can be used for many things is what I wrote about above - namely the large community creating huge amounts of libraries, frameworks, and ready scripts.

This allows for convenient use of Python in various fields and it's thanks to this and the language's simplicity itself that it's taking other fields by storm, beyond webdev and devops, like Data Science, Artificial Intelligence, Neural Networks, or scientific calculations in general.

Sometimes creating a program in Python really comes down to importing some module and adding a few small commands telling it what to do for us. It can't get simpler than that.

### Readability

Python was designed with readability in mind. In Python, code block membership is indicated by indentation, which is somewhat different from most languages where brackets or parentheses are usually used for this purpose, or alternatively keywords like BEGIN or END.

In Python, indentation counts, and its incorrect use causes runtime errors. This results in the fact that practically every correct Python code is relatively elegant and easily readable. Of course, there are exceptions to this norm, but I'm talking about the general code where good practices or standards are applied, such as PEP8, for instance, which we'll talk about later.

When we add to this the simplicity and expressiveness of the language itself, it quickly turns out that code in Python is often simply beautiful, easy to read, modify, and friendly to novices.

Yes, people coming from other languages might find it strange, at least at the beginning, that in Python we use indentation instead of brackets or braces, but it's a nice solution in my opinion.

Additionally, Python lacks one more thing - semicolons at the end of expressions aren't necessary. One character less writing per line and cleaner code.

Of course, we sometimes use semicolons in Python, but these are rare situations and predetermined, really few.

This is probably also another thing that might surprise programmers of other languages, although in current times it's not such a rare practice for a language not to require semicolons.

Why is readability important at all? A programmer's time is expensive, our brains have very limited capabilities. It's good when certain things are immediately visible, when we don't have to think about something because it's obvious.

If a program is very readably written, we'll be able to understand it faster, and this is critical in completing tasks - contrary to appearances, a programmer's work doesn't consist of constant code typing, quite the opposite.

Personally, I spend most of my time at work reading other people's code - whether it's colleagues' code, or authors of libraries, frameworks, and sometimes even my own. Readable appearance helps a lot, and this is important because reading and understanding code is much harder than writing it.

### Automatic Memory Management

In Python, memory management happens automatically - the programmer has no part in it, the language itself does it for us through such a mechanism as the Garbage Collector, it takes care of properly freeing resources and memory for objects we no longer use.

So we don't have to worry about things like memory allocation and de-allocation, as is the case in C or C++, for example.

Why is this an advantage? Because improper memory management can lead to very serious errors that put the entire system at risk, and ensuring that such errors don't occur is on the programmer's shoulders and often isn't a simple thing, ha! Sometimes even simple constructions related to memory allocation and de-allocation, things that seem obvious, have complicated backgrounds that lead to serious errors if misunderstood.

In Python's case, it's not like that - the programmer generally doesn't even have access to direct memory operations. This is a very wise limitation, useful in this type of language. It's similar in, for example, Java.

### Support for Various Programming Paradigms

There are languages that strongly support basically only one programming paradigm - like Java or Smalltalk, which are designed to strictly fulfill the assumptions of the object-oriented paradigm, or Haskell, which is a functional language and only functional, but there are also ones like Python that support many paradigms. What's this all about, in human terms?

In Java or Haskell, you have somewhat predetermined how you should 'think' and in what key you should implement solutions to certain problems through code. What this means exactly, we'll discuss another time.

In Python, however, you have freedom of choice. You yourself decide which approach you like and which you'd like to use. I consider this an advantage because again — in some situations, some solutions work better, in others, different ones. Having a choice, you can use the right one and that's it.

### Many Supported Platforms

As I mentioned somewhere earlier, Python supports practically any platform used today. Windows, Linux, AIX, IBM, macOS, OS/390, z/OS, Solaris, VMS, HP-UX. Whatever someone wishes for, almost certainly exists. Okay, supposedly now we only use Windows, Linux, and macOS, practically speaking, but even these systems aren't supported by some languages.

### Maturity

Python is a language that has been around since 1991 - it's almost 30 years old now. During this time, its ecosystem, tools, and libraries have had time to mature, go through the growing pains that some languages still have ahead of them.

This means more or less that Python can usually be trusted. As long as the programmer doesn't cause something themselves, the language rather won't let us down, because it has survived the test of time, and most errors and glaring bugs have long been caught and patched.

Does this mean it's a perfect language or without errors? In no way. Nevertheless, because it has been used in hundreds of thousands of important business applications, it can be safely said that it's worth giving our snake a certain dose of trust.

### Ease of Integration with Other Languages

Python can be quite easily integrated with other languages on various platforms. Programs written in Python usually quite easily cooperate with other programs, written in, for example, different languages.

Not every language has this feature, as some languages create quite hermetic, specific, and closed culture, where connecting or integrating them with other environments is extremely or unnecessarily difficult.

An additional advantage of Python is that you can write 'extensions' for it in C or C++, which will work much faster than Python itself. Thanks to this, we can have most of the application written in Python - code simple, short, and pleasant where it can be, and just some narrow bottleneck of it that needs to execute really fast, in C or C++. This isn't usually used, but sometimes there are various, strange reasons why it's worth it.

### Speed of Code Creation

Due to Python's simplicity and multitude of libraries, applications, as well as the code itself, can be created in it literally lightning fast. This is undoubtedly an advantage, especially in times when most clients want their product to be done yesterday, and deadlines are always tight.

Moreover, usually this quickly made code is also of quite decent quality.

And it's also a fact that even if we don't want to use Python in production, we can still use it to create a tiny MVP. What's MVP? Minimal viable product - that is, such an app that will have minimum functionality, but somewhere someone will already want to pay for it because it will be useful for something, which will please investors and people in general, because it's super, we have MVP, VCs will throw money again, another round of financing, cash and hype checks out, our ship called startup sails on.

Remember this abbreviation - MVP is a hot buzzword in the crazy world of STARTUPS!

Ending the digression, even if we don't use Python in production but only for MVP, or creating some prototype simply, in Python we can do it lightning fast, check if a given solution works, if so, well, we can always implement the production version in another language. Some faster one.

## Python's Disadvantages

Now let's talk about those worse sides.

### Python as a Dynamically Typed Language

Wait a moment, just a second ago, I wrote that this is an advantage. What's going on? Do you have split personality, or what? Who said that? Hello. But seriously...

Python's dynamic typing is an advantage that allows us to create some great mechanisms, but also, in the hands of an inexperienced programmer, a disadvantage.

It allows for creating code that will cause completely unexpected, difficult to debug errors, which could be prevented in a statically typed language, where such code wouldn't even compile.

In Python, or other dynamically typed languages, there is no such mechanism, so you need to be somewhat careful here not to create an error that will later be difficult to diagnose and debug.

Of course, currently we have tools that make this task easier for us, or even somewhat make Python similar to statically typed languages, as there are, for instance, type annotations, allowing us to specify what type a variable/function should have.

However, this is not a mandatory or necessary element of the language and it won't cause an error during application startup attempt, at most a warning from the IDE or code analyzer, which can be simply ignored.

So dynamic typing is somewhat like a knife, on one hand you can use it to do something nice, make a good meal for example, and on the other hand, you have to live with the awareness that you need to pay special attention when handling it because you might cut yourself.

However, should we give up the benefits and applications it has because of this fact? I'll throw in a classic - Nothing could be more wrong!

I don't know about you, but I read this sentence with a special accent and certain voice in my head.

### Performance

One thing is clear - when it comes to strictly performance issues, Python is far from being king. Generally, nice this Python, such not too fast one might say.

Of course, this is changing now, but the very nature of Python as an interpreted language means that it will never be as fast as C compiled to native code, or other languages of this type. You have to accept this and that's it.

Of course, I'm not claiming here that Python is very slow or sluggish. No. Python isn't slow, quite the opposite - thanks to various optimizations made over the years, Python has really gained in speed and today I firmly state that it's a language fast enough, but it must be strongly emphasized that it's not the fastest language. And that's it.

And while we're talking about performance, I'll mention sizes too - Python's hardware requirements mean that we simply won't run it on some platforms. There are certain areas of the embedded world where C or Assembly rules, Python doesn't exist there and there's no point in discussing this.

Of course, there are also projects like RaspberryPi, where actually, Python also rules everything.

So if you want to write highly efficient games with beautiful graphics, or maybe multi-threaded applications that handle huge amounts of calculations in real-time, or maybe tiny micro-controllers, then well, Python isn't really a good choice then.

In other cases, Python will handle it and you don't need to worry about execution speed/resources. Why? Well, we live in times when server time is much cheaper than developer time. This means it's better if the language is maybe a bit slower, but if you write in it much faster, we choose it. It's just cheaper, better, healthier this way.

This doesn't mean we have permission here to write any kind of code that works clumsily and slowly, but works. Absolutely not! You need to respect user time, hardware resources we have, and several other things. Save RAM wherever you are. Like in everything - you need to know moderation and limits. I'm talking more about theoretical situations here, where we have some code handling a server request.

Let's say the request passing through the network takes a second. Python execution and returning the response will take about 0.1 seconds. Then back to the user, another second. Total 2.1 seconds.
We can rewrite this code in another language, let's say, Java - the code will be several times longer, writing it will take more time, but it will execute, say, 10 times faster. So instead of waiting 2.1 seconds, the user will wait 2.01 seconds, because usually it's not the server itself and our application code that is the bottleneck, but for example the database, network connection, or disk.

Does this make sense in most cases? The jump from 2.1 to 2.01s? Answer that yourselves. These are the situations I'm talking about - then usually there's no point in playing with optimizations and Python is simply fast enough.

That's at least how it is in the vast majority of projects, because those that can't afford this minimal slowdown are not very many. Besides, you - as a beginning programmer, probably won't even see such projects at the start of your career, because it's not time for that.

### GIL

In Python, we have something called GIL - Global Interpreter Lock. I won't go into details of this mechanism here, it's enough that you'll know that because of it Python isn't exactly an ideal choice when it comes to multi-threaded applications, because only one thread at a time can have access to the interpreter in a process, because GIL blocks the rest.

And what's this about with multi-threading and so on? In short and great simplification, this is about performing many things simultaneously, most often using multiple processor cores, to speed up the operation of some application.

Because I don't know if you're aware, but you have something called CPU in your computer - the so-called processor. This processor is responsible for most calculations, computations, and executing your commands, in great shorthand.

During technology development, we reached a point at some stage where it was difficult to make one core faster. So, to make everything work even faster, and you could play five applications in the background, currently processors have several cores.

Cores are like small processors inside processors. Imagine a worker. 1 core = 1 worker. And going back to this earlier - a worker as a worker has limited capacity, because they're limited by physics, for example. Well, one person, no matter how strong, can't carry more concrete bags than X per hour. We, after some time, came to this moment when technologically we created a worker, that is, a processor, that approached this X, let's say.

So a problem appeared, because we have worker efficiency X. We have one worker on the construction site, we want to finish work faster, how can we do it, since getting more than X bags per hour out of this one worker will be difficult or impossible at the moment? We can try to make them even more efficient and, for example, fund them a good steroid treatment to make them stronger, or feed them cocaine/amphetamine, making efficiency increase by those 5%, but the cost of this undertaking would be completely disproportionate to the results obtained. So what to do? Hire more workers. Then, when we employ several workers, they can even be weaker than that one, but there will be several of them. Total processing power will increase.

More or less this is how the situation looks with processors and the fact that they are currently multi-core.

Here comes Python, which is kind of a handicapped foreman. He handles managing 1 worker well, but if he has to handle, for example, 4, he already has certain limitations that you need to be aware of.

True, this can now be worked around quite easily, but still something like this remains and you need to learn to deal with it, because you can fall into a trap.

### High Expressiveness

Again, something that is an advantage is also a bit of a disadvantage. Why? Python hides certain things from you, the programmer, which causes that you don't always know how it's done 'under the hood'. This isn't entirely good, because sometimes it's useful to know how certain things were implemented and why just like that.

This explains a lot. A simple example of this is the frequent question - why do we index lists or arrays from 0? If you're a C/C++ programmer, you most likely know the answer.

High-level language programmers, however, don't always know it. Ha! I would even say rarely. Don't be afraid if you don't know, we'll address this topic in the book, but a bit later.

However, this is a small price to pay compared to what this expressiveness and high abstraction offers.

It's just an easy problem to fix - just need a bit of willingness to read a bit more. And the time we'll spend on exploring these various topics is much shorter than the time we would spend writing our program in a language with a lower degree of abstraction/expressiveness.

### Python Doesn't Exist in the Mobile World

Mobile applications and Python are rather two different worlds. Just like that and that's it. Sure, there are projects trying to achieve something in this area, but there's no point in kidding ourselves that knowing only Python, we'll create a nice app for Android.

If someone tells you otherwise, better ignore the guy, because Python has gotten too strong in them and they're talking nonsense.

### Too Much Comfort

It can often be that after you start writing in Python, switching to other languages, where you have to do certain things completely differently, is a bit painful. This is also a potential disadvantage of Python.

You write your programs happily in Python, you do a lot of things with one line of code, it's nice and beautiful, but suddenly you have to write something in Java and there's a brutal collision with reality, which causes you to land in the depths of darkness, despair and depression, your life loses meaning and your wife has to throw you out of bed in the morning to get you up. No, I'm joking, writing in Java isn't that bad, I have nothing against the language. It's just that few languages are as nice as Python.

### That's It

Writing about Python's advantages and disadvantages, I tried to be relatively objective. Of course, this is not very possible due to the fact that this book is about Python, and I myself am its enthusiast. Nevertheless, I believe I managed to present you with Python's strengths and weaknesses, thanks to which you can decide whether it's worth learning it. In my opinion, absolutely yes!

Besides, darn it, since you already have this book, use it and learn!

## Who Uses Python?

In this case, it would be better to ask who doesn't use Python.

For example, however, I'll give you a few more or less known companies that use Python, these are: ILM, Google, Facebook, Instagram, Spotify, Quora, Netflix, Dropbox, Reddit, NASA, NSA, Red Hat, Nokia, IBM, Nasdaq, Sephora, Citi, Toyota, Gartner, Atlassian, Evernote, Lego, WebMD, Telefonica.

The entire YouTube basically stands (stood) on Python. At Google they say: 'Where we can - Python, where we must - C++' (supposedly).

Quite a lot, right? Well, no wonder, given that Python, according to the TIOBE index, is currently the 3rd most popular programming language in the world. Above it are only Java, C, C++. Additionally, Python gains more popularity every year and grows in strength. As someone once said, not necessarily wise, `you can't stop this force anymore`.

Below you can see a table with the TIOBE index, which, let's say, is a standard in the programming world when it comes to measuring the popularity of certain technologies, trends, and so on.


|Sep 2019|Sep 2018|Change|Programming Language|Ratings|Change|
|--- |--- |--- |--- |--- |--- |
|1|1||Java|16.661%|-0.78%|
|2|2||C|15.205%|-0.24%|
|3|3||Python|9.874%|+2.22%|
|4|4||C++|5.635%|-1.76%|
|5|6||C#|3.399%|+0.10%|
|6|5||Visual Basic .NET|3.291%|-2.02%|
|7|8||JavaScript|2.128%|-0.00%|
|8|9||SQL|1.944%|-0.12%|
|9|7||PHP|1.863%|-0.91%|
|10|10||Objective-C|1.840%|+0.33%|
|11|34||Groovy|1.502%|+1.20%|
|12|14||Assembly language|1.378%|+0.15%|
|13|11||Delphi/Object Pascal|1.335%|+0.04%|
|14|16||Go|1.220%|+0.14%|


As you can see, Python easily beats languages like C#, PHP, JavaScript, SQL, R, or Ruby. The latter actually by 8 times.

This snake has a future.

I really think that we are currently at a point, or quite close to such a point, where too much code has been written in Python for it to be displaced in the future. Let's look at how Python gains popularity over the years.


|Programming Language|2019|2014|2009|2004|1999|1994|1989|
|--- |--- |--- |--- |--- |--- |--- |--- |
|Java|1|2|1|1|9|-|-|
|C|2|1|2|2|1|1|1|
|Python|3|7|5|6|23|21|-|
|C++|4|4|3|3|2|2|2|


Impressive, right? 20 years ago Python wasn't even in the top 20. In 2004 already 6th. And now? On the podium.

Look also at the old monster - COBOL - despite the fact that it wasn't a very well-thought-out or beautiful language, it is still being developed and used today because at one time a lot of software was written in it, especially for banks, and simply getting rid of all systems operating based on this language and rewriting them to something newer would be too costly.

So despite COBOL being quite a specialized language with narrow application, it's still used, and yet the first mentions of COBOL come from 1959, so if someone wants to, they can program today in technology from basically 60 years ago and find work in it.

It's not among the pleasant ones, but well. Can you? You can.

As I mentioned earlier about Python - you can't stop this force anymore. Python came, made itself at home, and for now isn't going anywhere, and probably will stay for good.

I'm not sure about the latter, of course as a Python programmer I'll try to make it happen - adding my brick and creating as much code in Python as possible, nevertheless I (still) can't give a guarantee that it will stay with us forever.

I can give it for something else - that within the next 15 years Python won't be displaced from generally understood popular programming and it won't be a problem to find work knowing this language, so if you're afraid of that, you have my word that it won't be like that.

So going into Python, you're making quite a smart move when it comes to your career. So do it, listen to Górski, and get to work.


## Python Compared to...

### Java/C#

I'll throw these two languages into one bag, to some people's outrage. Fan boys will come at me with hate right now, but whatever.

Nevertheless, let's start with the fact that both these languages are supported by/directed by large corporations. Python isn't. For some it's a disadvantage, for others an advantage. Python is also definitely simpler to learn than these two languages, without two words.

It's also much more expressive - the code is usually shorter, much shorter.

Unfortunately, often also slower than both.

Python is also less popular than Java, which is currently at the very top and that's without two words, but then again also clearly more popular than C#.

Additionally, Java/C# is more often used by large corporations than Python. Huge projects are often the domain of Java or C#. For me another disadvantage.

### Perl

Well, few people currently use Perl, but because these two languages were often compared in the past, I'll mention it too. Personally, I've never written in Perl, but I've happened to see code written in it.

It can evidently be sometimes not very readable, and the amount of parentheses used in Perl can overwhelm a person. Python is also much more popular than Perl now. Overwhelmingly more popular. I won't elaborate further on this comparison then, because it makes no sense.

### C

C is a 'small' language - its core is small, but giving amazing possibilities, nevertheless it's still a language with certain limitations.

C rules in places where Python has no reason to exist - drivers, embedded, applications where speed or performance is really critical. In C the programmer is able to manage memory used by their program down to the byte. In Python? Forget about something like that.

Python is therefore much slower than C, takes up more memory. In return, we gain much greater expressiveness, speed of writing code and safety - Python is simply a simpler language compared to C, but rather they're never compared. Why?

Because the default implementation of Python is written in... C for one thing, and two, they serve completely different tasks. These are languages that I would say are complementary, not opposite, as they well complement each other in their weaknesses.

Many libraries that are written in C for speed have their wrappers written in Python precisely. What are these wrappers? Think about your car. Inside it probably has quite a complicated computer. You, as a user, are able to simply interact with it through various buttons, switches, menus and so on - easy thing. However, you're not able to modify by yourself how this system specifically works, what it does in what situation etc., but this doesn't really bother much, because in 99% there's no such need, and for that 1% there's no point in abandoning the car and starting to walk on foot. And when you already need to change something in how this computer works... Such things can be done by a mechanic using specific tools and software modifications.

Python and its programmer is you here, and C is the car's onboard computer.

Where incredible performance is needed, which probably only Assembly can beat, you can use C, where readability and speed of code production are more important, you can use Python. Super combo. By the way, a large part of Python programmers also knows C. This is probably the natural order of things.

End of these comparisons, because you could go on endlessly. At this point you should know well Python's strong sides, as well as those weak ones.

## Python Implementations

Python has several implementations. The most popular and default one is CPython - written in C, hence the name. This is the implementation we'll be using.

There are also others, like:

- Jython - Python implementation for the JVM (Java Virtual Machine)
- IronPython - Python implementation for .NET
- PyPy - Python implementation written in Python (RPython to be precise)
- Stackless Python - Python implementation focused on concurrency
- MicroPython - Python implementation for microcontrollers

Each of these implementations has its advantages and disadvantages, but we won't go into details here. Just know that they exist and that's enough for now.

## Questions

1. What are Python's main advantages?
2. What are Python's main disadvantages?
3. What is GIL and why is it important?
4. Why is Python's dynamic typing both an advantage and a disadvantage?
5. What makes Python a good choice for beginners?
6. In what areas is Python particularly strong?
7. In what areas should Python not be used?
8. What are the main differences between Python and C?
9. What companies use Python?
10. What is Python's position in the TIOBE index and what does this mean?
11. What are the different Python implementations available?
12. Why is Python's readability considered an advantage?
13. How does Python's memory management differ from languages like C?
14. What makes Python's community special?
15. Why is Python's expressiveness both an advantage and a potential drawback?

These questions should help you review and understand the key points discussed in this chapter. Try to answer them without looking back at the text - this will help you assess how well you've understood the material. 