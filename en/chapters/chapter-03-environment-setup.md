\pagebreak

# Setting Up Your Environment

Let's finally get to something concrete - time to get our hands dirty, because up until now I've just been talking and talking. We'll start by setting up our environment: installing Python and something to edit text with. But wait, what exactly? There are two options - a simple text editor or an IDE. What will we choose?


## What Should You Write Code In at the Beginning?
What should you write code in at the beginning? IDE/Text editor? PyCharm? Sublime? VS Code?

When I think back to my first days of learning programming, one of the many things that kept confusing me and caused quite a bit of trouble to resolve was choosing the environment in which I would write my first programs.

There's nothing surprising about this - nowadays, for practically every language, there are at least a few free IDEs, plus paid ones, plus text editors, and so on. It's easy to get lost. At least that's what happened to me, and I spent several days, instead of learning programming, sitting and pondering which environment to choose.

### IDE? Text Editor?

So how does it work in the end? IDE or text editor? And what even is an IDE? Find that out yourself - as a programmer, your basic task is processing information. So search the Internet for the meaning of this acronym, look up the differences between an IDE and a text editor.

I won't hand it to you on a silver platter, because the ability to search for information is a key trait that makes a good programmer, one that needs to be practiced from the beginning, and that's what I'll try to develop in you throughout the pages of this book.

So what should you choose? The answer might surprise you - it is: doesn't really matter. Let me explain.

Whether you choose CodeBlocks, VisualStudio, or Atom, it doesn't matter much, in my opinion, because these are just tools. Tools in the hands of a programmer, and it depends on them how well these tools will be used. Same with programming languages.

Even the best IDE won't help you if you don't know how to use it. On the other hand, if you master the seemingly prehistoric, by today's standards, programs like Vim or Emacs, you can work wonders.

That's why I recommend not paying too much attention to which environment you choose, because practically any of them can be adapted and made pleasant to work in.

Despite this, one path can probably be outlined that's worth taking and which I think is quite reasonable. What path is that?

### Basics

Regardless of whether we're using an IDE or some text editor, it's good to know how it all works under the hood, which I've repeated several times already and will repeat many more times.

So that it's not the case that someone without their IDE can't compile a piece of C++ code or run a Python script from the command line. Such basic things should be learned because they allow you to better understand how programs are created and how everything works - this information is sometimes simply essential.

Besides, at the beginning, the code suggestion feature should be turned off. By typing out the names of instructions, methods, or classes, you'll learn them faster. At least that's how it was for me. When using auto-completion, it was often enough for me to type two or three letters, hit tab, and boom - done.

The problem appeared when auto-completion wasn't available, because, for example, I had to write something quickly in a plain text editor, use someone else's computer, or, heaven forbid, I went to a job interview where you had to write code on a whiteboard with a marker. I won't say how silly I looked because of that a few times.

Then suddenly everything flew out of my head, and I forgot half the commands I supposedly knew so well. That's why at the very beginning I gave up automatic completion in favor of manual typing.

So at the beginning, better forget about syntax suggestions, especially if you're planning to go to a job interview sometime. Though I doubt it, since you're reading this book.

Later, once I had memorized the keywords and instructions sufficiently, I went back to it. For the very beginning, however, I would advise against auto-completion.

### How It Looked for Me

What environment did I choose?

I'll be honest, I tried many different ones, following roughly this path while learning Python:

At the beginning, I wrote in a browser, doing a course on one of the interactive programming academies - I didn't need to download any program, but later, when I wanted to start writing something of my own on disk, I looked around online and found various threads where PyCharm and a few other popular IDEs were usually recommended. So I downloaded them. But only briefly.

They were too overwhelming for me - the multitude of options, the complexity. Besides, my old laptop didn't cope well with the hardware requirements of such IDEs. Working in them was actually barely possible.

So I switched to SublimeText, where I stayed a bit longer, slowly getting familiar with the console and the fact that I had to do some things myself. After a while, I started to feel something was missing in Sublime, so I began searching again - I found Vim and used it for some time.

A wonderful tool. A Swiss army knife - you can do anything with it. It can be a light text editor or essentially a full-blown IDE, with the right amount of plug-ins. I liked it for its configurability, the magic you can perform in it.

At the beginning it was hard, but then I got a bit used to it. Nevertheless, I would advise against Vim as your first text editor - it's still a bit different in operation than standard programs.

I changed Vim to SublimeText for short and simple scripts, and I write all the rest of my applications in PyCharm. It offers too many useful options not to use it, and secondly, it has become somewhat of a standard in our industry, and there really aren't many companies that don't use it.

I started missing something in Sublime, so... Back to Vim+PyCharm. And that's been my final stack for several years now.

For the purposes of this book, SublimeText will be completely sufficient for you; later we might switch to PyCharm. Let's move on to the installation, since we now know what we'll need.


## Windows?! Linux?! macOS?! What to Choose?

Doesn't matter.

Soon fanatics of one system or another will show up here or somewhere else, and they'll persistently try to convince you that the system chosen by that particular person is the best and only suitable for use/programming/anything.

Don't pay attention to them. A system is just a tool, and it's up to you whether you use it efficiently or not. Unless you're interested in languages that somehow limit your freedom of choice - for example, wanting to write iOS apps in Swift, you probably won't be sitting on Windows; similarly, writing software in pure C#, you probably won't be using macOS either. Simple.

But this doesn't concern us. We're simple Pythonistas. And Python runs pretty nicely everywhere.

However, it's good to have at least a basic understanding of Linux. Why? Practically every server where we host our applications online runs Linux. Sooner or later, you'll encounter it, and if you're somewhat familiar with it beforehand, it won't be a painful collision with reality where you smash your head against a wall, but rather a meeting over a beer with a good buddy you haven't seen in a while. That's one. Two, generally certain things on Linux you have right at hand, whereas on Windows you have to deal with some things yourself, install stuff, etc. Does this mean you have to install a new system to learn Linux, otherwise life is impossible?

Absolutely not. A virtual machine with any distribution will be enough for you. I personally recommend Ubuntu, despite not being a fan of Canonical, and the second option, Manjaro. Both are Linux distributions, but with certain differences. Personally, when I use Linux, it's Manjaro. On desktop at least. Because on servers, Manjaro is not really an option.

Virtual machine, what, how, where? Look through the table of contents; you should find an answer in this book, just probably a bit further along.

What's more, recently another option has become available: WSL. Windows Subsystem for Linux. It's a Microsoft toy that allows you to have Linux integrated with your Windows. Linux in Windows from Microsoft. Boom. The advantages are ease of installation, easier integration, etc. I generally recommend it.

To summarize briefly, both Linux and Windows have their pros and cons; they're just tools. I personally, however, use (finally) Linux as my host. If you're on Linux, that's great; if not, definitely install WSL.

## Installation on Windows
Usually in Python books you'll find a step-by-step description of Python installation, helpful screenshots, and so on. Well, not here. We'll install the things we need in a somewhat unusual way for Windows. Using the command line. No, I haven't gone crazy.

I don't know if you're aware, but Linux users usually install programs in a somewhat different way than Windows users.

Every popular Linux distribution contains what's called a package manager. You can think of it as a 'program' that manages all officially supported and available programs for that distribution. Understandable, right?

Thanks to these package managers, Linux users can do something cool - most programs on Linux can be installed with a single command, and the same goes for updating them, updating the entire system, or removing 'programs'. On Windows, it's a bit different. In my opinion, the Linux way of managing packages is more convenient, and many people would probably agree with me on this.

Unfortunately, by default, Windows doesn't have a sensible package manager, however, I didn't use the phrase 'by default' for nothing. There's a very nice tool called chocolatey that allows us to get the functionality that pacman or apt provide.

In short, thanks to it, installing a large portion of programs is reduced to:

choco install program_name

and that's it. Convenient, right? That's why we'll use this package manager to install what we need.

Installing Choco
Exact instructions can be found on the [chocolatey website (https://chocolatey.org/install)](https://chocolatey.org/install), and that's where you need to go to learn how to install choco.



### Installing the Things We Need Using Choco
Chocolatey installed? Excellent, now just one command away from the finish line.

```bash
choco install python sublimetext3 -y
```

And done. What if we want to update all/selected programs?

Again, nothing simpler:

```bash
choco upgrade all
```

or

```bash
choco upgrade program_name
```

I don't think I need to explain. The list of packages available for installation this way can be found there. Most popular programs are there.

If you don't want to click 'y' for every upgrade prompt, just add `-y` at the end of the command, similar to the sublime text installation example.

Now just open SublimeText, create any folder anywhere, and in SublimeText click File -> Open Folder, selecting the folder you created earlier, which will serve as the main folder for files from this book.

## Installation on Linux/macOS
As for instructions for Linux or macOS and its users. Well, there are none for you.

But how? What kind of discrimination is this? Well, you probably already have Python installed; just check what version. How?

```
python --version
```

(two dashes) in the console and done, or, depending on the distribution, it might be

```
python3 --version
```

Depends on which distribution you're using and which version of Python it uses as default.

Ideally, it should be Python version >= 3.7.0. If it isn't, upgrade it.

How to do it? Let's be honest, if you're using Linux, you probably don't need to ask me about this. Same with installing SublimeText. And if you really have no idea then... Remember what I said about the most important skill of a programmer - processing information. So search.

And if you're on Mac, use the `brew` tool. That's it.

And as I mentioned, it doesn't have to be SublimeText - you can use your favorite editor. Doesn't matter. Just please don't use Windows Notepad for this. Every time you do that, somewhere in the world a kitten dies. Don't do it.

## Moving on to Programming! Finally!

I mean, wait. Now we still need to, using the console, of course, navigate to the main code folder for this book that we created recently.

To do this, you need to open the console again; this time you won't need administrator mode, so open it as a regular user, whether on Linux or Windows.

And now what? Time to get familiar with the basic commands that might be useful to you. I'm mainly talking about four basic ones, and those are what I'll discuss; there are of course many more, and some of them that might be useful in your daily work, we'll discuss later.

I just don't want to overwhelm you at the very beginning with information that you won't need yet, only adding things to the list of concepts you have to understand.

## The Four Horsemen of the Console

1. `dir` (Windows) or `ls` (Linux). This is a command that lists the contents of the directory we're currently in in the console. How to know where we currently are? Simple - our working directory (CWD - current working directory) is displayed to the left of our terminal cursor, or by typing pwd on Linux/macOS. Windows users, google it. You wanted Microsoft systems. Now you've got them. What does it mean that we're in some directory?
Well, our commands will be executed relative to this path. So if we type `python file.py`, and we're in the folder, let's say, `C:\Users\Olaf`, then Python will look for this file, file.py, right in that folder.
1. `mkdir` - common to both systems, creates a directory with the given name, e.g., mkdir folder will create a folder named folder in the current working directory. Makes sense.
1. `del` (Windows) and `rm` (Linux) these commands are used to delete files. If we want to delete a folder, we can use rd on Windows or rm -rf on Linux. Example usage: rm -rf file.txt.
1. `cd` - common to both systems. Cd, meaning change directory. Changes the current working directory to the specified one. Example usage - cd .. - this command will take us to the parent directory in the file structure. So if we're in `C:\Users\Olaf\Test\`, using cd .. will take us to `C:\Users\Olaf\`.

Useful information: pressing TAB makes the console auto-complete directory or file names for us;

On Linux (usually), the ~ symbol represents the user's home directory, so if you want to go there, you don't have to provide the full path. Just type cd ~ and you're there.

One more note: not all Linux distributions have the current working directory imported into PATH, so sometimes you might need to type, as the file location in the current CWD, ./file.txt instead of file.txt, depending on the distro. This can easily be fixed by adding CWD to PATH. The same might apply to Python itself. Remember to add it to PATH during installation. Or if not during installation, then add it manually afterward.

How? Google it, Linux user. You wanted to install Linux, so now you've got it. Suffer, suffer, as you wanted!

We can navigate now, but we'll come back to the console. How do we run our source code?

Simple.

```
python filename.py
```

Note: if you're on Linux and had Python 2 installed before, you might need to use the python3 command to run things, but you probably know that.

And to run the Python interpreter, just type:

```python
python
```

And that's it. This will start the interpreter. The difference between the interpreter and running from a file is that in the interpreter, you type commands and Python interprets them on the fly. With a file, it's a less interactive approach. Play around and see for yourself.

Environment set up, navigating the console too. Let's finally get to work!

\pagebreak
