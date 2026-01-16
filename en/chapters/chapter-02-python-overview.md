\pagebreak

# Python, What's It About?

## Python - What's It About?

Before we start learning Python, I'll tell you a bit about the history of the language itself, where it comes from, what its goals and assumptions are, how it has evolved and changed over the years, what it looks like now, where it's used, and why.

## How to Use This Book

Wait, stop. I'd like to tell you a bit about how I think you should use this book. First, I tried to write it so that it naturally transitions from one topic to the next - from simple topics to more complex ones. Thanks to its linear structure, it should be easy to understand.

However, if you're already a more experienced programmer, or just want to refresh certain things, feel free to jump around - most chapters are fairly self-contained components.

Another thing I want to mention, or rather repeat, is that in this book you won't find information only about Python. In addition to information about the language itself, I'll also try to introduce you to certain concepts from computer science in general, so that you know a bit more, so you have an idea of how something works, why this way and not another.

I think this is essential knowledge to become a good programmer who develops and goes far. Such chapters will be somewhat more theoretical in nature, but that doesn't mean they're boring - quite the opposite in my opinion.

If you want to absorb the information contained here well and really learn something new, I advise you: first, take notes, short, concise and simple.

Second - type out the code. Don't use the Copy Paste method. Type it yourself and that's it.

Finally, three - do the exercises I'll place at the end of chapters yourself, but that's not all - experiment with the code. Change it, see what the effects of those changes will be. Experience it in practice, analyze your modifications, think about them and their results, how they affect the program's operation. This is the best learning method. This is the basic assumption that guided me in writing - that you will do the exercises yourself, read additional articles, books, experiment with code.

More about how you should learn and what methods work, you can read in Gynvael Coldwind's blog post - Beginner Programmer's Guide. Highly recommended. I recommend the whole blog actually. There are few places on the Internet where you can find such good and interesting content. Google it, it's worth it.

Additionally, I want to note that I won't be writing about every tiny detail in this book. This is not a Python encyclopedia - the assumption here is that you'll reach for the details of various things yourself. I want to draw attention to often overlooked things. **I therefore recommend reading materials from Django documentation, Python documentation, the excellent book Learning Python, 5th edition, and the CS50 course alongside this book**. I want to make you aware of certain things and explain some concepts, additionally dealing with this often overlooked practical knowledge, an honest account of my experiences.

## Interactive Part

On my GitHub you'll find a repository `junior-python-exercises` - https://github.com/grski/junior-python-exercises. If you want your solutions and answers to exercises to be reviewed, fork this repo (you'll learn what that means later) then in the folder appropriate for the chapter add a folder with your GitHub username and answers inside. I'll do code review/look through those answers and give some feedback :)

## Python 2 - Python 3?

Python currently exists mainly in two versions - Python 2 and Python 3. These are two 'major' releases of the same language, however version 3 is newer, introduces certain new things that are not backward compatible with version 2, hence the version number jump.

The introduction of Python 3 happened many years ago, we're now in times when Python 2 is no longer developed. It's dead and done. The only projects using it are some larger legacy ones. Besides, there are already some quiet whispers about Python 4 somewhere.

What does this mean from your perspective as a beginner? Nothing. Just know that you're currently learning Python 3 and that's it. It's still the same language, but there are certain differences between it and Python 2, which you can easily learn in a few moments if needed. I choose the newest version to give you the freshest information, and honestly, Python 2 is slowly becoming a relic of the past, and whoever creates new software in it now is making a mistake, although I don't think such cases can still be found anywhere, aside from a few corporate exceptions.

If anything, Python 2 is now only used for maintaining old applications written in it, and believe me, more often than not, you don't want to work on maintaining old behemoths. Unless they pay you a lot of money. A lot, a lot of money. Even more than a lot. Seriously. Although it's still not worth it. What good is money when you literally change your profession from programmer to sewage diver, diving in the programming excrement of people who more than usual hated their lives, so they created a monster?

Python 2 is passing into history and that's good, but I'll occasionally mention the differences, just as a curiosity basically.

## A Short Description of Python's Long History

Python is quite an old language, so to speak. Older than me, although that's no achievement really.

There are currently plenty of new languages on the market - young ones like Scala, Dart, Elm, Elixir, Kotlin, and many, many others. Compared to them, Python is an old-timer, appearing at the beginning of 1991 at CWI - the Centre for Mathematics and Computer Science in Amsterdam. It's not a grandpa like C from 1972, but a full-fledged middle-aged language, absolutely.

Its main creator was Guido van Rossum, who still has the nickname "Benevolent Dictator for Life" (well, he had it, more on that in a moment) and is basically considered the highest authority in the Python world.

As for such unusual facts, if you manage to find Guido's email address somewhere on the web (it's not hard) and send him an interesting email with a question or anything, there's a good chance he'll respond. At least that's what the experiences of many Python users suggest.

The language name doesn't come, as one might think, from the snake species, but from a TV show broadcast in the seventies by the BBC - "Monty Python's Flying Circus," of which Guido was a fan and decided that naming his programming language 'Python' would be something. And it is. This alone should be enough to encourage you to use this language.

Python began its public life in version 0.9.0, but didn't live in it for long - new versions came out quickly. Various perturbations were associated with them, as van Rossum himself, as well as the most important team members, changed their 'home' many times, moving from one organization to another. Code is code, but you have to make a living somehow.

However, everything settled down with the advent of version 2.1, which was released under the banner of Python Software Foundation - a non-profit foundation that operates to this day and is modeled after the Apache Software Foundation.

By design, Python was meant to be a successor to the ABC language - another prehistoric creation we won't dwell on too much, despite its influence being evident in Python.

In addition to ABC, Python shows clear influences or elements borrowed from languages such as: C, C++, Haskell, Java, Perl, and Lisp. Should this mean anything to you? Definitely not if you're a beginner. Just know that Python has certain elements in common with other languages and isn't some great oddball.

## Guido's Abdication

Around the time of writing this book, at the very beginning actually (what can I say, I took long breaks...), something unprecedented happened - Guido van Rossum, the author of Python, decided to withdraw from the decision-making chain in the Python world and relinquish his BDFL title, gradually retiring altogether. The whole thing was caused by PEP 572, which Guido himself proposed, among others, and which sparked rather unfavorable reactions from the community. What was it about?

About the := operator and assignment in expressions. A large part of people very loudly began to criticize this idea, often without any basis, because, at least to me, the PEP itself seems rather well thought out and nice, this functionality will certainly be useful somewhere in Python. We'll talk about this PEP later, so no details for now.

Below I include the text of the email that Guido published, translated by me.

"Now that PEP 572 is done, I don't ever want to have to fight so hard for a PEP and find that so many people despise my decisions.

I would like to remove myself entirely from the decision process. I'll still be there for a while as an ordinary core dev, and I'll still be available to mentor people -- possibly more available. But I'm basically giving myself a permanent vacation from being BDFL, and you all will be on your own.

After all, what's the point of being BDFL when you feel that there's a truck around every corner ready to run you over? And I'm not getting younger either... I'm sparing you from having to hear the list of my medical conditions.

I am not going to appoint a successor.

So what are you all going to do? Create a democracy? Anarchy? A dictatorship? A federation?

I'm not worried about the day-to-day decisions in the issue tracker or on GitHub. Very rarely do I get asked to make pronouncements there, and usually only for minor issues. That will continue to be the case and I'm fine with that.

What's going to be needed is some process to decide:
- How are PEPs decided;
- How to choose core devs;

I think we can try to define processes for those as PEPs that will serve as our new constitution. The catch is that I'm not going to be the one determining those processes -- you'll have to figure it all out yourselves.

Just remember that there's still a Code of Conduct, and if you don't like that you can leave. Maybe this should also give us something to think about: when to expel someone (ban them from python-dev or python-ideas).

Finally, I'll remind you that the archives of this mailing list are publicly available.

I'm not leaving entirely, I'm still here, but I want you to become independent. I'm tired and need a long, long break." --Guido van Rossum

What more can you say here.

It was a sad moment in Python's history, all the more so because Guido really is Python and Python is Guido.

That's it. Shocking news.

Well, may things go well for you, Mr. Guido.

The question is, what will the Python world look like without this man? What direction will it take? This is an opportunity for growth, but also a threat that we'll lose the direction, which is currently pretty good.

In any case... A new wind will blow into the sails, where will it take us? Time will tell. In a year, two, five. We, the community that creates Python, will decide - so basically soon you too, dear reader.

Note: from a time perspective, it's still fine. Guido's departure hasn't changed Python for the worse.

## The Snake's Goals

With this Python, the thing is that it's really worth using. I personally think it's one of the best languages for learning programming basics, which is what it was meant to be. It allows you to quickly get to understanding certain programming concepts because the student doesn't have to focus too much on mastering complicated syntax or convoluted expressions, as is sometimes the case in other languages.

Python is concise and simple - most code can be very easily understood by anyone who speaks a little English, or has a dictionary handy, and the code itself is usually short and elegant.

Only a few symbols used to shorten notation really need explanation. Other than that, Python reads really similarly to sentences in English. This is also the first snake goal - simplicity over complexity.

Python was designed to be simple, pleasant and elegant. I think it absolutely is.

Another goal is portability. Python can be run on probably most currently popular platforms - Windows, almost any Linux, macOS. Up to version 3.7, released on 27.06.2018, even something as strange as FreeBSD version <= 9 was officially supported.

Thanks to this, Python can be run almost anywhere, as long as hardware resources allow.

The next goal Python had before it is openness. Some languages are quite 'hermetic' - you can only use them after paying for a license or only under certain conditions, for certain purposes.

With Python, there's no such problem - it's completely free to use, modify, distribute, and whatever else the user desires.

Additionally, Python is open-source, and its development is driven by the community. What does this mean in practice? Everyone has access to the language sources, and if you don't like something in Python, you think something could be done better, then...

No problem. Just take that function and write it, change it. If the community decides that your changes are justified and useful, they'll end up in the language itself. Everyone can therefore have a real impact on what Python looks like, how it works. Great stuff.

These are just a few of the ideas that guide Python - I won't describe all of them here, but I think I managed to include the most important ones.

## The Snake Sheds Its Skin From Time to Time

What do I mean? The fact that Python and its uses are constantly changing. Like a snake, it sheds its old skin and gets a new one.

Originally it was a language that was used rather as a scripting language. Automation of certain processes on servers, some file and text operations, and so on. Boring stuff in general. Python didn't take the market by storm - it took a while. At the very beginning, it was rather niche. Over time and with the evolution of the language itself, its advantages and beauty became widely recognized.

That's why over the years Python has become increasingly popular for developing backend parts of web applications, and as we know, these have been experiencing constant growth since the beginning of the last millennium. The matter was helped by the appearance on the market of more Python frameworks designed specifically for creating web applications, such as Flask, Pyramid, Pylons, Web2py, and finally Django, which was a real game-changer. Fun fact: when you're browsing Instagram, do you know what it runs on? Django, that's right.

Thanks to this, Python has become quite popular as a language used for writing web applications, but that's not all. In recent years we can see a constant increase in demand for various specialists related to Data Science, Artificial Intelligence, Machine Learning, and Neural Networks.

All these and related industries are developing tremendously, and the language that practically reigns there is Python. It has its competitor in R, and a fast-growing contender in Julia, but still, our snake holds strong.

Why? Look at the ideas guiding Python - it explains itself. An analyst doesn't have to be a good coder - their task is to process data, so they need a language that will quickly allow them, without unnecessary delving into syntax or how the language itself works, to translate their thoughts into code.

Python is ideal for this because of its simplicity and versatility. I can already imagine an analyst sitting there checking whether they released all the previously allocated memory in their super beautiful code written in C or C++. That's just not an option. And that's good.

Of course, a certain problem arises here in the form of performance, but more on that later, because it's something that can be overcome and solved much more easily than trying to teach everyone C/C++.

Of course, Python is still used in various scripts, automation, and so on, but I don't think this is its main use anymore, as it was many, many years ago.

So, as you can see, Python is developing and appearing in more and more projects, fields, and areas related to general IT. I personally think this trend will continue, just as it has been, and Python will gain more and more popularity year after year. Let's get into the details though - why?


## Python's Advantages


### Expressiveness


Python is very expressive. What does that mean? Well, in Python with a relatively small amount of code, you can achieve what in other languages would sometimes take several times as much. To not be unfounded, let's look at an example of the classic program that starts programming education - Hello World. Which is ironic, because when you start programming, you should rather say goodbye to the world, because you won't be seeing much of it from your basement anymore.

In Python it looks like this:

``` python
print('Hello World')
```

Pretty simple and understandable, right? One line and done.
Let's look at other languages though.
Let's start with Java:
``` java
public class HelloWorld{
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

Here it's still fairly clear, despite a few seemingly mysterious commands, you can still easily read what the program does, but let's take, say, C++:

``` cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello World!";
    return 0;
}
```

Here it's a bit less obvious what the program does, right? Also look at the number of lines used to accomplish the task. No comparison.

I should note that in both these languages you could print hello world with shorter code, I don't know those methods because I'm no Java or C/C++ guy, too lazy to look them up, but my point here is just to show the idea.

Another example of how short code can be in Python compared to similar code in C++/Java or other languages is below - this code is a bit more complex, but you might understand something from it. It was provided to me in a comment by @jacekw on Steemit and this code is his creation. Thanks :)

So what will our code do? Its task is simple:

1. Create a list of numbers in descending order from 19 to 0.
1. Skip even numbers.
1. Square each number.
1. Sort ascending.
1. Print the result.

By the way, this is a form of algorithm, presented in step form, something we'll return to in the future. For now, remember one thing - an algorithm is simply an unambiguous set of instructions for accomplishing some goal.

Anyway.

Let's start with *C++* this time.

``` cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    vector<int> s, a;
    for (int i = 19; i >= 0; i--) s.push_back(i);
    copy_if (s.begin(), s.end(), back_inserter(a), [](int x) {
        return x % 2 == 1 ;} );
    transform(a.begin(), a.end(), a.begin(), [](int x){
        return x*x;});
    sort(a.begin(), a.end());
    for (auto&& i : a) cout << i << " "; return 0;
}
```

I don't know about you, but for me that's a pretty convoluted piece of code. As a beginner programmer, I would have trouble understanding it. Lots of strange symbols, characters. What exactly is going on here?

Hard to say at first glance.

The next participant in this comparison is...

*Java*

``` java
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

``` python
a = filter(lambda x: x % 2 == 1, reversed(range(20)))
a = list(map(lambda x: x*x, a))
print(list(sorted(a)))
```

Alternatively, my version in Python would look like this:

``` python
print(sorted([i*i for i in reversed(range(20)) if i % 2]))
```

I'll leave that without comment. Finally, as a curiosity, I'll add an example from another language - Haskell.

``` haskell
sort $ map (^2) $ filter odd [20, 19..1]
```

Also interesting, right?

Does this mean these languages are worse and Python is king? Absolutely not, never think that.

Every language is like a tool - it has applications where it's good, excellent, but also those where it's completely unsuitable. This is true here too. This is true everywhere. Sure, sometimes there are fanatics of certain technologies or solutions whose language-technological brain inflammation clouds their objective judgment, but that's nothing. We don't want to be like that. Let's be smart and sensible, let's make our lives easier by using the right tools for the right tasks.

Nevertheless, Python allows us to write more with less code. This of course comes at a certain price that must be paid, and which makes Python good in certain situations, and not so good in others.

### Simplicity

Let's go back to the previous point - if we look at Python code, you could say it's basically just a command written in English. What does the word print mean? Nothing other than print/display.

You can immediately guess that the programmer wants the computer to display something on the screen. The same goes for other elements of the language - really, just knowing English and you can almost understand a large part of Python. Many languages are similar, but they're not as similar to English as Python.

Really, I haven't encountered another language this simple yet, and I've used a few, at least superficially - JavaScript, Java, C, C++, Dart, Scala.

The only language that can compete with Python in simplicity is probably C - but that's because the core of this language is just tiny. When it comes to memory management, pointers, and other equally fun things in C, you start missing Python.

### Python as a Dynamically Typed Language

What does that mean? Well, if you're a newbie to programming, you might have no idea what's going on, but that's okay.

In short, the matter concerns the fact that in statically typed languages, when declaring variables, you need to specify what type of data that variable will store. Let Java serve as an example here:

``` java
int someNumber = 123;
```

The notation above tells the 'program' that will execute our code that we want to create a variable named someNumber that will contain data of type int - integer, meaning nothing other than whole numbers. And what does it even mean to create a variable?

I'll try to explain it simply, but I might not succeed, and if you don't fully understand how this mechanism works, or it's hard to imagine how it functions, don't worry, we'll return to the topic later.

This command will 'tell' our computer something like this:

Listen computer, here's some data (in this case '123'), remember this value, save it somewhere, because I'll want to use this for something in the future, and from now on, every time I write `someNumber` in the program, know that I mean the value stored in that place.

An attempt to save other data to this variable, say, an array or a floating-point number, won't end well or as we intended.

In Python, there are no such restrictions and requirements. First, when initializing a variable, we don't have to specify its type, and second, later we can easily change the type of data we store in a given variable, so the equivalent of the above in Python would be:

``` python
some_number = 123
```

Later, without any problem, we can write:

``` python
some_number = 'Hi there'
```

You'll learn why this is possible a bit further in the book, but mainly it's because in Python variables are really references to an object, not the object itself per se. As I said, we'll return to this, for now you don't have to worry about it. Just remember that Python makes your life easier and doesn't impose too much, it does the work for you, good old snake.

### Community

Python has one really big advantage. It's its community, which is both really helpful and impressively large. Thanks to this, the amount of available materials, tutorials, libraries, frameworks, and scripts can just positively surprise you.

Thanks to Python's open-source culture, many amazing tools are given to us every day for use, completely free, just like that.

This means that we often don't have to reinvent the wheel - just import some library that someone already wrote. This often saves time and worries, allowing us to focus on what's important in our implementation.

Besides, what do you do when you get stuck somewhere in writing a program and don't know what to do next, when you encounter an error you can't solve? Well, due to Python's age and the size of its community, you can assume in most cases that someone before you encountered a similar problem and asked about it online, or described the solution to that problem.

People willingly share knowledge, believe it or not. Thanks to this, we don't have to search for a solution ourselves for hours, digging through documentation, sources, or just experimenting. We can simply ask someone, because many people know Python, or find answers from others who solved the problem before us. Not every language has such an extensive knowledge base and community.

As a counterexample, I'll give the Dart language. A fairly new language, not very popular, small community overall. Nevertheless, I sometimes created in this language and it happens quite often that I encounter a problem I can't find information about anywhere, because it just hasn't happened to anyone else yet, or no one else has described it, so I have to find the solution myself, combing through documentation, sources, and just experimenting.

This is often a painful path.

On top of that, sometimes there's the inconvenience that some things that have already been written by someone else in Python or Java, nicely packaged and distributed for use, in Dart may not exist and need to be written yourself.

Similarly, when it comes to learning the language itself - there are significantly fewer materials, they're often outdated because Dart is a constantly evolving language, new versions come out every week, or at least they used to, and due to low popularity, few people write about it, even fewer create books or tutorials about it.

This doesn't make learning easier, especially for beginner programmers. Good thing at least the documentation is quite good - not as good as Django documentation, for example, but still - it's not bad.

That's why I claim that Python's community is its greatest advantage and it literally creates this wonderful language, making it what it is.

### Multitude of Applications

Python is a general-purpose language. You can create practically anything in it, except for a certain, rather narrow range of applications for which it's completely unsuitable and wasn't designed for.

Knowing Python, we can create desktop applications, games, web applications, scripts, emulators, interpreters, compilers, applications for scientific calculations, data visualization and web scraping, machine learning, and so on. The list is really long.

Of course, Python is better for some tasks, worse for others, because for example it's rare that desktop applications or games are created in Python, as there are better languages for that, but in any case, it's possible and not too hard honestly.

Python's ability to be used for many things is helped by what I wrote above - a large community creating huge amounts of libraries, frameworks, and ready-made scripts.

This allows convenient use of Python in various fields, and that's why, along with the simplicity of the language itself, it's taking over other areas beyond webdev and devops, like Data Science, Artificial Intelligence, Neural Networks, and scientific computing in general.

Sometimes creating a program in Python simply comes down to importing some module and adding a few small commands telling it what to do for us. It doesn't get simpler than that.

### Readability

Python was designed with readability in mind. In Python, code belonging to a given block is marked with indentation, which is a bit different from most languages, where curly braces or parentheses are usually used for this purpose, or keywords like BEGIN or END.

In Python, indentation matters, and incorrect use causes runtime errors. This results in practically every correct Python code being fairly elegant and easy to read. Of course, there are deviations from this norm, but I'm talking about code in general, where good practices or standards are applied, like PEP8, for example, which we'll talk about later.

When we add the simplicity and expressiveness of the language itself, it quickly turns out that code in Python is often simply beautiful, easy to read, modify, and friendly to newcomers.

Sure, people coming from other languages may find it strange at first that Python uses indentation instead of parentheses or curly braces, but I think it's a nice solution.

Additionally, Python lacks one more thing - semicolons at the end of statements aren't necessary. Less typing by a whole character per line and cleaner code.

Of course, sometimes we use semicolons in Python, but these are rare and predefined situations, really few.

This is probably another thing that might surprise programmers from other languages, although nowadays it's not such a rare practice for a language not to require semicolons.

But why is readability important at all? A programmer's time is expensive, our brains have severely limited capabilities. It's good when certain things are immediately visible, when we don't have to think about something because it's obvious.

If a program is written very readably, we'll understand it faster, and that's critical to getting the job done - contrary to appearances, a programmer's job isn't about constantly typing code, quite the opposite.

Personally, I spend most of my time at work reading other people's code - whether it's coworkers, or authors of libraries, frameworks, and sometimes even my own. Readable appearance makes things much easier, and that's important, because reading and understanding code is much harder than writing it.

### Automatic Memory Management

In Python, memory management is automatic - the programmer has no part in it, the language does it for us using a mechanism called the Garbage Collector, which takes care of properly freeing resources and memory after objects we no longer use.

So we don't have to worry about things like allocation and deallocation of memory, as is the case in C or C++.

Why is this an advantage? Because improper memory management can lead to very serious errors that jeopardize the entire system, and ensuring that such errors don't occur is on the programmer's shoulders and often isn't simple - sometimes trivial constructs related to memory allocation and deallocation, things that seem obvious, have complicated underlying issues that lead to serious errors if misunderstood.

In Python's case, this isn't the case - the programmer generally doesn't even have access to direct memory operations. This is a very smart limitation, useful in this type of language. It's similar in Java, for example.

### Support for Different Programming Paradigms

There are languages that strongly support basically only one programming paradigm - like Java or Smalltalk, which are designed to strictly meet the assumptions of the object-oriented paradigm, or Haskell, which is a functional language and only functional, but there are also those like Python, which support multiple paradigms. What's this all about in plain terms?

In Java or Haskell, you're somewhat imposed upon how you should 'think' and in what way you should implement solutions to certain problems using code. We'll discuss exactly what this means another time.

In Python, on the other hand, you have freedom of choice. You decide which approach you like and which you'd like to use. I consider this an advantage because again - some solutions work better in some situations, others in different ones. Having a choice, you can use the right one and that's it.

### Many Supported Platforms

As I mentioned somewhere earlier, Python supports practically any platform used today. Windows, Linux, AIX, IBM, macOS, OS/390, z/OS, Solaris, VMS, HP-UX. Whatever anyone wants, it's almost certainly there. Okay, we practically only use Windows, Linux, and macOS now, but even these systems are unsupported by some languages.

### Maturity

Python is a language that has been developing since 1991 - it's currently almost 30 years old. During this time, its ecosystem, tools, and libraries have matured, gone through the problems of infancy that some languages still have ahead of them.

This means more or less that Python can usually be trusted. Unless the programmer himself is at fault, the language rather won't let us down, because it has survived the test of time, and most errors and glaring bugs have long been caught and patched.

Does this mean it's a perfect or error-free language? Not at all. Nevertheless, because it was/is used in hundreds of thousands of important business applications, you can safely say that our snake deserves a certain degree of trust.

### Simplicity of Integration with Other Languages

Python can be quite easily integrated with other languages on various platforms. Programs written in Python usually cooperate quite easily with other programs, written in different languages, for example.

Not every language has this feature, as some languages create a fairly hermetic, specific, and closed culture, where connecting or integrating them with other environments is excessively or unnecessarily difficult.

An additional advantage of Python is that you can write 'extensions' for it in C or C++, which will run much faster than Python itself. Thanks to this, we can have most of the application written in Python - simple, short, and pleasant code where it can be, and some narrow bottleneck that needs to run really fast in C or C++. It's rarely used, but sometimes various strange reasons appear for which it's worth it.

### Speed of Code Creation

Due to the simplicity and multitude of libraries in Python, applications, as well as the code itself, can be created incredibly quickly. This is an undeniable advantage, especially in times when most clients want their product done yesterday, and deadlines are always tight.

Moreover, usually this code done quickly is also of quite decent quality.

And it's also a fact that even if we don't want to use Python in production, we can still use it to create a tiny MVP. What's an MVP? Minimal viable product - an app that will have minimum functionality, but someone will already want to pay for it, because it will be useful for something, which will make investors happy and people in general, because it's great, we have an MVP, VCs will throw in money again, another round of financing, money and hype are right, our ship called a startup sails on.

Remember this abbreviation - MVP is a hot buzzword in the crazy world of startups!

Ending the digression, even if we don't use Python in production but only for MVP, or just creating some prototype, in Python we can do it incredibly fast, check if a given solution works, and if so, well, you can always implement the production version in another language. A faster one.


## Python's Disadvantages

Now for the worse aspects.

### Python as a Dynamically Typed Language

Wait, a moment ago I wrote that this is an advantage. What's going on? Are you bipolar or what? What? Who said that? Hello. But seriously...

Python's dynamic typing is an advantage that allows us to create certain great mechanisms, but also, in the hands of an inexperienced programmer, a disadvantage.

It allows the creation of code that will cause completely unexpected, hard-to-debug errors, which could be prevented in a statically typed language, where such code wouldn't even compile.

In Python, or other dynamically typed languages, there's no such mechanism, so you have to be a bit careful not to create an error that will later be hard to diagnose and debug.

Of course, nowadays we have tools that make this task easier, or even make Python somewhat similar to statically typed languages, because there are, for example, type annotations that allow us to specify what type a variable/function should have.

Nevertheless, this is not a mandatory or necessary element of the language and won't cause an error when trying to run the application, but at most a warning from the IDE or code analyzer, which can simply be ignored.

So dynamic typing is a bit like a knife - on one hand you can use it to do something cool, a good meal for example, and on the other hand, you have to live with the awareness that you need to pay special attention when handling it, because you can cut yourself.

But should we give up the benefits and applications it has because of this fact? I'll throw a classic - Nothing could be further from the truth!

### Performance

One thing is clear - when it comes to strictly performance matters, Python is far from being king. Overall this Python is nice, kind of not too fast you could say.

Of course, this is changing now, but the very nature of Python as an interpreted language means it will never be as fast as C compiled to native code, or other languages of this type. You have to accept this.

Of course, I'm not claiming here that Python is very slow or sluggish. No. Python isn't slow, quite the opposite - thanks to various optimizations made over the years, Python has really gained speed and today I firmly state that it's a fast enough language, but it must be strongly noted that it's not the fastest language. And that's it.

And while we're talking about performance, I'll also mention size - Python's hardware requirements mean we simply can't run it on some platforms. There are certain areas of the embedded world where C or Assembly reign supreme, Python doesn't exist there and there's no point discussing it.

Of course, there are also projects like RaspberryPi, where Python also rules everything.

So if you want to write highly efficient games with beautiful graphics, or maybe multi-threaded applications that process huge amounts of calculations in real time, or maybe tiny microcontrollers, then well, Python isn't really a good choice in that case.

In other cases, Python will manage and you don't have to worry about execution speed/resources. Why? Because we live in times when server time is much cheaper than developer time. That means it's better if a language is maybe a bit slower, but if you write in it much faster, you choose it. It's simply cheaper, better, healthier.

This doesn't mean we have permission to write shoddy code that works clumsily and slowly, but works. Absolutely! You need to respect the user's time, the hardware resources we have, and a few other things. Save RAM wherever you are. As with everything - you need to know moderation and limits. I'm more talking about theoretical situations where we have some code handling a server request.

The request going through the network takes, say, one second. Execution and returning a response by Python will take about 0.1 seconds. Then the return to the user again, another second. Total 2.1 seconds.

We can rewrite this code in another language, say Java - the code will be several times longer, writing it will take more time, but it will execute, say, 10 times faster. So the user, instead of waiting 2.1 seconds, will wait 2.01 seconds, because usually it's not the server and our application code that's the bottleneck, but e.g., the database, network connection, or disk.

Does this make sense in most cases? The jump from 2.1 to 2.01s? Answer for yourselves. That's the kind of situation I mean - then it usually doesn't make sense to mess with optimization and Python is simply fast enough.

At least that's how it is in the vast majority of projects, because those that can't afford this minimal slowdown aren't that many. Besides, you - as a beginner programmer - probably won't even see such projects at the start of your career, because it's not time for that.

### GIL

In Python we have something called GIL - Global Interpreter Lock. I won't go into details of this mechanism here, it's enough that you know that because of it Python isn't exactly an ideal choice when it comes to multi-threaded applications, because only one thread at a time can have access to the interpreter in a process, because GIL blocks the rest.

And what's this multithreading about and so on? In short and greatly simplified, it's about executing many things simultaneously, most often using multiple processor cores, to speed up the operation of some application.

Because I don't know if you're aware, but you have something called a CPU in your computer - the so-called processor. This processor is responsible for most calculations and executing your commands, in a nutshell.

During the development of technology, at a certain stage we reached a point where it was hard to make one core faster. So, for everything to work even faster, and for you to be able to run five applications in the background, processors now have multiple cores.

Cores are like little processors inside processors. Imagine a worker. 1 core = 1 worker. And going back to before - a worker is a worker, has limited efficiency, because they're limited by e.g., physics. Well, one person, no matter how strong, can't carry more bags of cement than X per hour. We, after some time, reached precisely this point where technologically we created a worker, meaning a processor, that approached this X, let's say.

So a problem appeared, because we have worker efficiency X. We have one worker on the construction site, we want to finish work faster, how can we do it, since getting more than X bags per hour from this one worker will be difficult or impossible at the moment? We can try to make them even more efficient and e.g., fund them a good steroid treatment, so they get stronger, or feed them cocaine/amphetamines, making their efficiency increase by those 5%, but the cost of this undertaking would be completely disproportionate to the results obtained. What to do then? Hire more workers. Then, when we put several workers to work, they can even be weaker than that one, but there will be several of them. Total processing power will increase.

More or less, that's the situation with processors and why they're multi-core now.

Here comes Python, which is a bit of a limited foreman. It does well managing 1 worker, but if it has to handle e.g., 4, it has certain limitations that you need to be aware of.

While this can now be worked around fairly easily, it still remains and you have to learn to deal with it, because you can fall into a trap.

### High Expressiveness

Again, something that is an advantage is also a bit of a disadvantage. Why? Python hides certain things from you, the programmer, which means you don't always know how it's done 'under the hood'. This isn't entirely good, because sometimes it's useful to know how certain things were implemented and why exactly that way.

It explains a lot. A simple example of this is a common question - why do we index lists or arrays from 0? If you're a C/C++ programmer, you probably know the answer.

Programmers of high-level languages, however, don't always know. In fact, I'd even say rarely. Don't worry if you don't know, we'll cover this topic in the book, but a bit later.

However, this is a small price to pay compared to what this expressiveness and high abstraction offer.

It's simply an easy problem to fix - just a bit of willingness to read a little more. And the time we spend delving into these various topics is much shorter than the time we would spend writing our program in a language with a lower level of abstraction/expressiveness.

### Python Doesn't Exist in the Mobile World

Mobile apps and Python are rather two different worlds. That's just how it is. There are certainly projects trying to do something in this area, but there's no point in hoping that knowing only Python, we'll create a cool Android app.

If someone tells you otherwise, better ignore them, because Python got too deep into their head and they're talking nonsense.

### Too Much Comfort

It may often happen that after you start writing in Python, switching to other languages where certain things have to be done completely differently is a bit painful. This is also a potential disadvantage of Python.

You're happily writing your programs in Python, doing a lot of things with one line of code, it's nice and beautiful, but suddenly you have to write something in Java and a brutal collision with reality occurs, which causes you to land in the depths of darkness, despair, and depression, your life loses meaning. No, just kidding, writing in Java isn't that bad, I have nothing against the language. It's just that few languages are as cool as Python.

### That's It

Writing about Python's advantages and disadvantages, I tried to be fairly objective. Of course, this isn't entirely possible because this is a book about Python, and I myself am an enthusiast. Nevertheless, I think I managed to present Python's strong and weak sides, so you can decide if it's worth learning. In my opinion, definitely yes!

Besides, come on, if you already have this book, use it and learn!

## Who Uses Python?

In this case, it would be better to ask who doesn't use Python.

For example, however, I'll give a few more or less known companies that use Python, they are: ILM, Google, Facebook, Instagram, Spotify, Quora, Netflix, Dropbox, Reddit, NASA, NSA, Red Hat, Nokia, IBM, Nasdaq, Sephora, Citi, Toyota, Gartner, Atlassian, Evernote, Lego, WebMD, Telefonica.

The entire YouTube basically runs (ran) on Python. At Google they say: 'Where we can - Python, where we must - C++' (supposedly).

Quite a lot, right? Well, no wonder, since Python, according to the TIOBE index, is currently the 3rd most popular programming language in the world. Above it are only Java and C. Additionally, Python is gaining more and more popularity every year and growing in strength. As someone once said, not necessarily wise, `you can't stop this force now`.

Below you see a table with the TIOBE index, which is, let's say, the standard in the programming world when it comes to measuring the popularity of certain technologies, trends, and so on.


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


As you can see, Python easily beats languages like C#, PHP, JavaScript, SQL, R, or Ruby. The last one basically 8-fold.

This snake has a future.

I really think we're currently at a point, or quite close to one, where too much code has been written in Python for it to be displaced in the future. Let's look at how Python has been gaining popularity over the years.


|Programming Language|2019|2014|2009|2004|1999|1994|1989|
|--- |--- |--- |--- |--- |--- |--- |--- |
|Java|1|2|1|1|9|-|-|
|C|2|1|2|2|1|1|1|
|Python|3|7|5|6|23|21|-|
|C++|4|4|3|3|2|2|2|


Impressive, right? 20 years ago Python wasn't even in the top 20. In 2004 already 6th. And now? On the podium.

Also look at the old monster - COBOL - despite not being a very well-thought-out or beautiful language, it's still developed and used to this day because at one time a lot of software was written in it, especially for banks, and simply getting rid of all systems running on this language and rewriting them to something newer would be too expensive.

So despite COBOL being a fairly specialized language with narrow applications, it's still used, and the first mentions of COBOL come from 1959, meaning if someone wants, they can program today in technology from basically 60 years ago and find work in it.

It's not pleasant, but well. Can you? You can.

As I mentioned earlier about Python - you can't stop this force now. Python came, made itself at home, and isn't going anywhere for now, and will probably stay for good.

I'm not sure about that last part, of course as a Python programmer I'll try to make it happen - adding my contribution and creating as much code in Python as possible, but I can't (yet) guarantee that it will stay with us forever.

I can guarantee something else - that in the next 15 years Python won't be displaced from generally popular programming and it won't be a problem to find work knowing this language, so if that's what you're afraid of, you have my word that it won't happen.

So by going with Python, you're making a pretty smart move for your career. So do it, listen to me, and get to work.


## Python Compared to...

### Java/C#

I'll throw these two languages in the same bag, to the outrage of some. Fan boys will immediately show up with hate, but whatever.

Nevertheless, let's start with the fact that both these languages are supported/directed by large corporations. Python isn't. For some that's a disadvantage, for others an advantage. Python is also definitely simpler to learn than these two languages, no doubt about it.

It's also much more expressive - the code is usually shorter, much shorter.

Unfortunately, it's often also slower than both.

Python is also less popular than Java, which is currently at the very top without a doubt, but also clearly more popular than C#.

Additionally, Java/C# is more often used by large corporations than Python. Huge projects are often the domain of Java or C#. For me, another disadvantage.

### Perl

Well, few people use Perl nowadays, but since these two languages were often compared in the past, I'll mention it too. I've never personally written in Perl, but I've seen code written in it.

It's clearly sometimes not very readable, and the amount of parentheses used in Perl can overwhelm a person. Python is also currently much more popular than Perl. Overwhelmingly more popular. I won't go further into this comparison, because it makes no sense.

### C

C is a 'small' language - its core is small but gives amazing possibilities, but it's still a language with certain limitations.

C reigns in places where Python has no reason to exist - drivers, embedded, applications where speed or efficiency is really critical. In C, a programmer can manage memory down to the byte used by their program. In Python? Forget about something like that.

Python is therefore much slower than C, takes more memory. In return, we gain much greater expressiveness, speed of writing code, and safety - Python is simply a simpler language compared to C, but they're rarely compared. Why?

Because the default implementation of Python is written in... C, that's one thing, and two, they serve completely different tasks. These are languages, I'd say, complementary, not opposite, because they complement each other well in their weaknesses.

Many libraries, which for speed are written in C, have their wrappers written in Python. What are these wrappers? Think about your car. Inside it probably has a fairly complicated computer. You, as a user, can easily interact with it through various buttons, switches, menus, and so on - easy thing. However, you can't modify by yourself how this system specifically works, what it does in what situation, etc., but this doesn't bother you much, because in 99% there's no need, and for that 1% there's no sense in abandoning the car and starting to walk on foot. And when you do need to change something in how this computer works... A mechanic can do such things using specific tools and software modifications.

Python and its programmer is you here, and C is the car's onboard computer.

Where incredible performance is needed, which can probably only be beaten by Assembly, you can use C, where readability and speed of code production are more important, you can use Python. Super combo. By the way, a large part of Python programmers also know C. It's probably a natural course of things.

End of these comparisons, because you could go on forever. At this point you should know Python's strong sides as well as the weak ones.

## Alternative Implementations

As I mentioned somewhere along the way, Python is a language that has its interpreter for running programs written in this language. So it's a program for running programs. Inception. We need to go deeper.

By default, this interpreter is written in C - that's CPython. However, there are other implementations of this interpreter that sometimes have different priorities than CPython, extend its functionality, or are simply written in a different language, because why not, because you can. Who will stop the rich.

Of course, not all of them fully meet the assumption of full compatibility with the entire Python standard, some deviate from it somewhat, aren't something practical, but rather a proof-of-concept - simply something done just because you can.

### Stackless Python

Let me start with an implementation called Stackless Python, which is based on CPython, except it focuses on concurrency, multithreading, so it basically extends CPython, improving certain things that it's not particularly good at by default. Various topics related to GIL and the like.

### Cython

Cython is nothing other than, basically, a Python compiler to... C. You write code in Python, and as a result you get a program running at the speed of a program written in C. Not bad. It's not a complete implementation of the language but, as I mentioned, a 'translator' to C, but I'll write about such tools too.

### PyPy

Python written in... Python. Inception. We need to go deeper. On the other hand, nothing strange, after all, from what I recall, from a certain version, the Go compiler is also written in Go. Similarly with other modern languages.

This is one of three implementations that are pretty much 100% compatible with the standard Python implementation. What's so interesting about this implementation?

Well, the fact that it has JIT - a Just In Time compiler, known, for example, from Java. What is it?

A JIT compiler is a compiler that only works after a given program is launched and compiles our currently used code fragment on the fly, often to a form native to the given CPU, and two, the JIT compiler usually has information about the runtime environment, which allows it to make better optimizations compared to a static compiler that doesn't have this information. What's this about?

CPython 'compiles' our Python code to bytecode understandable by the Python virtual machine, which then executes the given bytecode, which was compiled before the script was run. PyPy does this 'on the fly', having the ability to make better optimizations than a static compiler.

Why then isn't PyPy the default implementation, if it's faster, supposedly better? Well, for code to execute faster, several conditions must be met.

First of all, PyPy and its JIT need a moment to 'warm up' - meaning our script must run for at least a few seconds to have the opportunity to gain acceleration from using PyPy.

The second requirement is that the bottleneck of our program must be Python instructions, and not e.g., instructions contained in some internal modules written in C.

If these requirements are met, it's very likely that using PyPy will speed up our program's execution and possibly even reduce memory usage. In other cases... Well... We probably won't gain much from using PyPy. Even Python's creator himself - Guido van Rossum - speaks about PyPy.

> "If you want your code to run faster, you should probably just use PyPy." Guido Van Rossum - creator of Python

Additionally, PyPy by default implements e.g., features from Stackless Python, and Sandboxing, which is currently more of a prototype than a production implementation, but still.

### IronPython

Python and C#. What distinguishes it? First of all, it doesn't have GIL, you can use the .NET library, it can easily be embedded in .NET applications. The second of the main alternative implementations that pretty much meets the Python standard.

### Jython

Python on the Java virtual machine. Advantages? Easy integration with Java programs, possible compilation of Python programs to Java classes. Programs running on the Jython virtual machine have full access to Java classes and API. It can also be compiled statically and create servlets, applets, beans. Jython is also multi-threaded in the true sense of the word, meaning we don't have to worry about GIL here. The third, last, practically 100% compatible implementation.

### Brython

Brython is an invention that makes your code, written in Python, work in... the browser, on the client side by translating Python to JavaScript. Actively maintained and fairly up to date. Interesting project.

Other implementations supporting compilation to JS include: RapydScript, Transcrypt.

### MicroPython

I said Python on microcontrollers isn't really a thing, right? Well, this project aims to change that. Similarly like PyMite.

### CLPython

Python implemented in Common Lisp. Like Jython or IronPython, CLPython can mix Python code with code from the language it was written in, has access to its libraries.

### TinyPy

Python in 64Kb of code. Just because.


Besides these, there are Python implementations in Haskell, PHP, JavaScript, Rubinius, and various other inventions like combining LOLCODE with Python or Like, Python.

## Summary

Enough of all this theory and talk, let's sum up what I've said so far.

Python is a general-purpose dynamically typed interpreted language, whose advantages are expressiveness, community, amount of ready-made solutions, speed of application creation, and readability of code created in it, ease of learning.

It works well in webdev, scripts, scientific applications, related to Data Science and similar fields. It does a bit worse in multi-threaded applications, those that require very high performance, or in environments with severely limited resources. Additionally, Python doesn't exist in the world of mobile app creation, games, or desktop applications.

Nevertheless, there are solutions to various Python problems related to these issues, some better, some worse, but they exist. This doesn't change the fact that it's better suited for some tasks than others, and it's worth thinking about this when choosing technology for a given application.

## Questions
1. What version of Python will we focus on and why?
1. Give at least 3 examples of currently popular uses of Python.
1. In what applications is Python not very good?
1. Give several advantages of Python, as well as its disadvantages. Who uses it? What can you use it for?
1. Give examples of alternative Python implementations - besides CPython.
1. What are Python's main assumptions?
1. How does Python compare to Java? Main differences/goals.
1. Does Python work on many platforms? If so, which ones? List 3+.
1. What type of language is Python, statically or dynamically typed? What does that mean?
1. How does GIL limit us - in short?

\pagebreak
