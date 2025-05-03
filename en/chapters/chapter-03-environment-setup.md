\pagebreak

# Setting Up Your Environment

Let's finally get to something concrete - let's get our hands dirty, as so far I've just been talking and talking. We'll start by setting up the environment/installing Python and something for text editing. Just a moment, what exactly? There are two options - a simple text editor or an IDE. Which one will we choose?

## What to Use for Writing Code Initially?
What should you use for writing code at the beginning? IDE/Text editor? PyCharm? Sublime? VS Code?

When I think back to my first days of learning programming, one of many things that constantly confused me and caused quite a bit of trouble in deciding was choosing the environment in which I would write my first programs.

This shouldn't be surprising - nowadays, practically every language has at least several free IDEs, plus paid ones, and then there are text editors and so on. It's easy to get lost. At least that's what happened to me, and instead of learning programming, I spent several days sitting and thinking about which environment to choose.

### IDE? Text Editor?

So how is it really? IDE or text editor? And what is an IDE anyway? Find this out yourself - as an IT professional, your basic task is processing information. So look up the meaning of this acronym on the Internet, search for the differences between an IDE and a text editor.

I won't hand this to you on a silver platter because the ability to search for information is a key trait that makes a good IT professional/programmer, which needs to be practiced from the beginning, and this is what I'll try to develop in you throughout the pages of this book.

So what to choose? The answer might surprise you - it's: it doesn't really matter. Let me explain.

Whether you choose CodeBlocks, VisualStudio, or Atom doesn't make much difference in my opinion, as these are just tools. Tools in the hands of a programmer, and it's up to them how well these tools will be used. It's similar with languages.

Even the best IDE won't help you if you don't know how to use it. On the other hand, if you master seemingly prehistoric programs by today's standards like Vim or Emacs, you can work wonders.

Therefore, I recommend not paying too much attention to which environment you choose, as practically any can be adapted and made to work excellently.

Despite this, we can probably outline one path that's worth taking and which I think is quite reasonable. What path is that?

### Basics

Regardless of whether we use an IDE or some text editor, it's good to know how everything works under the hood, which I've already repeated several times and will repeat many more times.

So it's not like someone without their IDE can't compile a piece of C++ code or run a Python script from the console. Such basic things need to be learned because they allow you to better understand how programs are created and how everything works. Sometimes this information is simply essential.

Besides, at the beginning, code completion should be turned off. By typing out instruction names, methods, or classes ourselves, we'll learn them faster. At least that's how it was for me. Using auto-completion, often it was enough to type two or three letters, hit tab, and bam - done.

The problem appeared when auto-completion was missing, for example, when I had to write something quickly in a regular text editor/use someone else's computer or, horror of horrors, went for a job interview where I had to write code on a whiteboard with a marker. I won't tell you how stupid I looked several times because of this.

Suddenly everything flew out of my head and I forgot half the commands I supposedly knew so well. Therefore, at the very beginning, I gave up auto-completion in favor of manual typing.

So at the beginning, it's better to forget about syntax suggestions, especially if you're planning to go for a job interview sometime soon. Although I doubt it, since you're reading this book.

Later, when I had memorized enough keywords and instructions, I returned to it. However, I would advise against auto-completion at the very beginning.

### How It Looked for Me

What environment did I choose?

To be honest, I tried many different ones, following roughly this path while learning Python:

At first, I wrote in the browser, doing a course at one of the interactive programming academies - I didn't need to download any program, but later, when I wanted to start writing something of my own on disk, I looked online and found various threads where PyCharm and several other popular IDEs were usually recommended. So I downloaded them. But not for long.

They were too overwhelming for me - the vast number of options, complexity. Besides, my aging laptop struggled with the hardware requirements of such IDEs. Working in them was basically not very possible.

So I switched to SublimeText, where I stayed a bit longer, slowly getting used to the console and the fact that I had to do some things myself. After a while, I started missing something in Sublime, so I started searching again - I found Vim and used it for some time.

A wonderful tool. A Swiss army knife - you can do everything with it. It can be a light text editor or basically a full-fledged IDE with the right number of plugins. I liked it for its configurability, the magic you can perform in it.

At first it was difficult, but then I got somewhat used to it. Nevertheless, I rather wouldn't recommend Vim as a first text editor, as it's still somewhat different in operation than standard programs.

I changed Vim to SublimeText for short and simple scripts, and I write all other applications in PyCharm. It offers too many useful options not to use it, and two, it has become somewhat of a standard in our industry and there are really few companies that don't use it.

I started missing something in Sublime, so... Back to Vim+PyCharm. And this has been my final stack for several years now.

For the purposes of this book, SublimeText will be completely sufficient for you, then we might switch to PyCharm. Let's move on to installation, since we already know what we'll need.

## Windows?! Linux?! macOS?! What to Choose?

It doesn't matter.

Soon there will appear here or somewhere else fanatics of one or another system who will try to convince you that it's precisely their chosen system that's the best and only suitable for use/programming/anything.

Don't bother with them. The system is just a tool and it's up to you whether you use it efficiently or not. Unless you're interested in languages that somehow limit the freedom of choice, because, for example, wanting to write iOS apps in Swift, you probably won't be sitting on Windows, similarly writing software in pure C#, you probably won't be using macOS. Simple matter.

This doesn't concern us though. We're simple Python folks. And it runs quite nicely everywhere.

However, it's good to have at least basic familiarity with Linux. Why? Practically every server where we host our applications on the web runs on Linux. Sooner or later you'll encounter it, and if you're somewhat familiar with it earlier, it won't be a painful collision with reality where you bang your head against a wall, but rather a meeting over a beer with a good friend you haven't seen in a while. That's one. Two, generally certain things on Linux you have at hand, where on Windows you have to bother with some things yourself, install them, etc. Does this mean you have to install a new system to get to know Linux, otherwise you can't live?

Absolutely not. A virtual machine with any distribution will be enough for this. I personally recommend Ubuntu, despite not being fond of Canonical, and the second option, Manjaro. Both are Linuxes, but with some differences. Personally, when I use Linux, it's Manjaro. On the desktop at least. Because on servers Manjaro rather doesn't count.

Virtual machine, what, how, where? Browse the table of contents, in this book you should find the answer, just probably it will be a bit further.

Moreover, there's another option available recently. WSL. Windows Subsystem for Linux. This is a Microsoft toy that enables you to have Linux integrated with your Windows. Linux in Windows from Microsoft. Boom. Advantages include ease of installation, easier integration, etc. Generally recommended.

To summarize briefly, both Linux and Windows have their advantages and disadvantages, they're just tools. I, personally, however, use (finally) Linux as the host. If you're on Linux, that's cool, if not then definitely install WSL.

## Installation on Windows
Usually in Python books we find a step-by-step description of Python installation, helpful screenshots and so on. Well, not here. We'll install the things we need in a somewhat unusual way for Windows. Using the console. No, I haven't gone mad.

I don't know if you're aware, but Linux users usually install programs in a somewhat different way than Windows users.

Namely, every popular Linux distribution contains something called a package manager. You can think of it as a 'program' that manages all officially supported and available programs for a given distribution. Understandable, right?

Thanks to these so-called package managers, Linux users can do something cool - most programs can be installed on Linux with a single command, similarly with their updates, system updates, or removing 'programs'. On Windows it's a bit different. In my opinion, Linux's way of managing packages is more convenient and probably many people will agree with me at this point.

Unfortunately, by default, Windows doesn't have a sensible package manager, however, I didn't use the word 'by default' without reason. Namely, a very nice tool called chocolatey was created, which enables us to obtain functionality similar to what pacman or apt provide.

In short, thanks to it, installing a large part of programs is reduced to:

```bash
choco install program_name
```

And that's it. Convenient, right? Therefore, we'll use this package manager to install what we need.

### Installing Choco
Detailed instructions can be found on the [chocolatey website](https://chocolatey.org/install) and that's where you need to go to find out how to install choco.

### Installing What We Need Using Choco
Chocolatey installed? Excellent, now just one command separates us from the finish line.

```bash
choco install python sublimetext3 -y
```

And done. What about when we want to update all/selected programs?

Again, nothing simpler:

```bash
choco upgrade all
```

or

```bash
choco upgrade program_name
```

I probably don't need to explain. The list of packages available for installation this way can be found here. Most popular programs are there.

If we don't want to click 'y' for every upgrade question, we can just add `-y` at the end of the command, similarly to the example with installing SublimeText.

Now we just open SublimeText, create a directory anywhere, and in SublimeText click File → Open Folder, selecting the previously created folder that will serve as the main folder for files from this book.

## Installation on Linux/macOS
As for instructions for Linux or macOS users. Well, there aren't any for you.

But how? What kind of discrimination is this? Well, you probably already have Python installed, just check which version. How?

```bash
python --version
```

(two hyphens) in the console and done, or, depending on the distribution, it might be

```bash
python3 --version
```

Depends on which distribution you're using and which Python version it uses as default.

Best if it's Python version >= 3.7.0. If not, upgrade it.

How to do it? Let's be honest, if you're using Linux, you probably don't need to ask me about this. Similarly with installing SublimeText. And if you really have no idea then... Remember what I said about the most important skill of an IT professional - processing information. So search for it.

And if you're on a Mac, use the `brew` tool. That's it.

And as I mentioned, it doesn't have to be SublimeText - you can use your favorite editor. Doesn't matter. Just please, don't use Windows Notepad for this. Every time you do this, a kitten dies somewhere in the world. Don't do it.

## Let's Get to Programming! Finally!

Well, almost. Now we still need to, using the console of course, navigate to the main code directory for this book that we created recently.

To do this, you need to open the console again, this time you won't need administrator mode, so open it as a regular user, whether on Linux or Windows.

And now what? Time to get acquainted with the basic commands that might be useful. Mainly it's about four basic ones and these are what I'll discuss, there are of course many more and some of them that you might need in daily work, we'll discuss later.

I simply don't want to overwhelm you at the very beginning with information that won't be needed right now, and will only add things to the list of topics you need to understand.

## The Four Horsemen of the Console

1. `dir` (Windows) or `ls` (Linux). This command lists the contents of the directory where we currently are in the console. How to know where we are? Simple - our working directory (CWD - current working directory) is displayed to the left of our terminal cursor or by typing pwd on Linux/iOS. Windows users google it. They wanted systems from MS. Now you have it. What does it give us that we're in some directory?
Namely, our commands will be executed relative to this path. So if we type `python file.py`, if we're in the folder, let's say, `C:\Users\Olaf`, then Python will look for this file, file.py, in this folder.

2. `mkdir` - common for both systems, creates a directory with the given name, e.g., mkdir folder will create a folder named folder in the current working directory. Makes sense.

3. `del` (Windows) and `rm` (Linux) these commands are used to delete files. If we want to delete a folder, we can use rd on Windows or rm -rf on Linux. Example usage: rm -rf file.txt.

4. `cd` - common for both systems. Cd, meaning change directory. Changes the current working directory to the specified one. Example usage - cd .. - this command will move us to the parent directory in the file structure. So if we're in `C:\Users\Olaf\Test\`, using cd .. will move us to `C:\Users\Olaf\`.

Useful information: pressing TAB causes the console to auto-complete directory or file names for us;

On Linux (usually) the ~ character denotes the user's home directory, so if you want to go to it, you don't need to provide the full path. Just type cd ~ and you're there.

One more note, not all Linuxes have the current working directory imported to PATH, so sometimes there might be a need to type, as the file location in the current CWD, ./file.txt instead of file.txt, depending on the distro. This can be easily fixed by adding CWD to PATH. The same might be with Python itself. Remember to add it to PATH during installation. Or if not during installation, add it manually.

How? Google it, Linux user. You wanted to install Linuxes, now you have it. Struggle, struggle, as you wanted!

We can navigate now, but we'll return to the console. How to run our source code?

Simple matter.

```bash
python filename.py
```

Note, if you're on Linux and had Python 2 installed earlier, you might need to use the python3 command to run it, but you probably know that.

And to run the Python interpreter, just type:

```bash
python
```

And that's it. This will launch the interpreter for us. The difference between the interpreter and running from a file is that in the interpreter we type commands and Python interprets them on the fly. In the case of a file, we have a less interactive approach. Play around and see for yourself.

Environment set up, console navigation too. Let's finally get to work!

\pagebreak 