\pagebreak

# Python Tools Ecosystem

A bit about cool tools that you should know. I assume you'll install each of these tools and play around with them.

## The README file - what it should contain and how it should look

There's one thing that every proper project should contain. A README file. A well-written, readable, and comprehensive README file is the basic form of documentation for any project, containing elementary information about the project itself, but in my opinion, not only that. A well-written README file should contain a bit more. What exactly? Let me describe it.

### Technology

Usually when we work with README files, they have the `.md` extension, meaning by convention we write them in Markdown. Markdown is something that allows us to format text. Using it in README is not a requirement, but a fairly widely accepted standard that makes our life easier and gives us more possibilities than a plain text file.

### What sections should a good README file contain?

Below we'll discuss what sections, describing what, a good README file should contain.

### Title

We start a README with a title, of course. To do this, simply type the title on a line and add `#` before it, which will mark that line as a Markdown header.

### Project Description

Here we place elementary information about the project.

1. What kind of system component is it? E.g., API, Worker, frontend, library.
2. What functionalities is it responsible for? E.g., This is an API for an invoice generation system.
3. What is the context? A bit of additional context, you can never have too much. E.g., These invoices are then sent to customers, (...). We use the standard template from the company's design book here.
4. Who are the stakeholders - who is the recipient of this project?
5. What business problem does this project solve?
6. Who are its end users?

The summary should be written in the domain language of the given problem. What does this mean? Well, its description, the description of project functionalities should contain vocabulary from the field we're working in. If we're doing a project about tractors, let's use tractor driver terminology. When in Rome, do as the Romans do. This is the preferred approach compared to using pure, dry technical jargon.

### Technology Stack

In this section, we describe the most important technologies used in creating the project. Dependencies, external applications used, services, etc.

This will allow the reader to quickly familiarize themselves with the technological choices made in the project, used to solve the given problem.

Technologies should be briefly described, with appropriate materials linked for the reader's convenience.

### Local Environment Setup Instructions

Here we place the steps that need to be taken to set up the environment locally. Additionally, this is where we place instructions on how to perform frequently used operations, which commands are most commonly used, such as clearing the database, or creating it, migrations, etc. This is also where knowledge that is very specific to the given project lands, e.g., how the problem of localization and internationalization was solved using, e.g., PhraseApp or OneSky.

I recommend describing this section particularly well, keeping in mind less technical users who may need to set up the environment locally for testing purposes. Sometimes these are non-technical people, testers, stakeholders, product owners, etc. They also deserve the ability to have a local environment. Additionally, the entire environment setup process should be as automated as possible.

### Deployment

In a few sentences, concisely and briefly, describe how the application is deployed, what environment it lives in, where to look for a more detailed architecture description, and so on. Plus a few words about CI/CD.

### Authors

A list of the main people in the project. Useful when jumping to a new project and quickly wanting to establish who holds the context and who is best to ask about things because they have the most knowledge about the project.

### Summary

The README file is an important and integral part of the system. Now you know what it should look like.

## pdoc3

Automatic generation of the most important thing in the world, namely documentation. This tool plus comprehensive and sensible docstrings == happy developer.

Recommended reading: https://pdoc3.github.io/pdoc/

## PyCharm/Visual Studio Code

The best IDE/editor for Python. I'm personally #teamPyCharm, but Visual Studio Code also does the job.

## Taking Notes

There are a million tools for this. I personally recommend Notion, for example. Other options?

Recommended reading: https://bootcamp.uxdesign.cc/i-tried-40-project-note-taking-apps-what-i-chose-and-my-top-10-list-1d39d41852e4

## Pyenv, poetry and other shenanigans

Pyenv, poetry, and other shenanigans - modern dependency and Python version management, meaning contemporary Python versions, environments, and dependency management.

#### PIP

Pip is a tool that most of you should already know. It's used for installing packages used in Python development and has been shipped with Python by default for several versions now. But what exactly does installing packages mean?

In short, pip provides tools for downloading packages from the Python Package Index - PYPI. This is the default Python package index where almost anyone can add packages. Default is a good word because pip allows us to use different indexes. So, for example, your company may have its own, hosted version of packages, and then use it as a private version of pypi. This allows, for example, better verification of packages, only private network connections during CI/CD/development processes. This is quite an interesting option, especially considering recent malicious attacks on popular Python open source packages.

#### Package Index
What exactly is a package index?

Actually, nothing complicated. It's simply an http server, let's say, that provides a list of Python packages and certain metadata about them. Nothing more.

An interesting homework assignment to experiment with something new: try to implement your own version of pypi and add some features to it, such as token-protected access to packages or even more - tokens with granular permissions functionality.

#### Default Package Installation

Usually, we have one, maximum two backward-incompatible versions of Python installed on our computer. In the past, this was Python2 & Python3, now most of the time only Python3 is installed since Python2 died, perished, disappeared into the depths of the past.

Anyway. This means that in the Dark Ages or by default, packages were installed globally, for the entire system. This is bad for many reasons. As for what installing a package means, in very short terms, it's nothing more than downloading a Python code package with a specific structure, which gets downloaded and placed in the given Python installation directory, with additional steps possible in between.

What if project A requires package Z in version 1.0.0, but project B requires package Z in version 2.0.0? Would you reinstall this package every time you switch to different projects?

#### virtualenv
To combat the problem described in the previous paragraph -> packages installing globally, virtualenv appeared. In short, it's something that allows us to "create" a different "instance" of Python installation. E.g., only for a given project instead of system-wide.

This way we can have different versions of a Python package for different projects.

A subset of virtualenv functionality is integrated into the default CPython installation since version 3.3 as the venv module.

#### Poetry
What if pip and virtualenv had a child that was also on steroids? Well, we'd get Poetry.

The problem with pip is usually dependency version management. Even if we know that our project A requires package Z in version 1.0.0, pip usually doesn't tell us at first glance about the dependencies of that package Z. This introduces the possibility of problems when your project reaches a point where it has quite a few more packages installed. Because these packages also have dependencies, and their dependencies also have dependencies. Dependencyception.

Usually, it's not dependency hell like in JS worlds, but at some point, it can also become somewhat tricky if you only lock dependencies at the top level. And at some point, problems are almost guaranteed. And besides - if the versions of these dependencies aren't guaranteed by default, what about debugging? I mean, one build might have version 1.2.3 of some dependency, but another build, made 10 minutes earlier might have 1.2.2, if versions aren't resolved in a deterministic, guaranteed way, this enables nasty bugs to appear.

It's also a security risk because if you don't know exactly what version of a dependency you have, a malicious version can find its way in without our explicit knowledge, which is quite an easy way to shoot yourself in the foot. How to remedy this?

We have something called dependency resolving and dependency locking. Basically, it's just a process of making sure we know the dependencies of our dependencies and their dependencies, and also have a clear list of their versions, usually hash-signed. This allows for something called deterministic builds, which is one of the key elements of modern CI/CD and applications that follow the Twelve-factor app pattern.

This is exactly what Poetry does. And it does it elegantly.

Besides that, while we're at it, Poetry also makes project management easier, takes care of creating and managing virtualenvs for you, and enables easier, more centralized project configuration by introducing pyproject.toml. pyproject.toml is now usually the new standard configuration file for Python projects. And it also makes building packages easier since it can package/bundle your Python code and publish it to the package index of your choice, e.g., pypi.

Overall, Poetry is awesome.

#### Pyenv

Python is a peculiar little creature that sheds its skin from time to time. This means that Python itself, just like our dependencies, also has its versions. Each version contains new features, various improvements. Some of them are sometimes even backward-incompatible. It's not trivial by default to install different versions of Python and manage them so they don't conflict with each other.

But why do this at all? Well, just like with dependencies. One project may depend on Python 3.10, another on 2.7, and yet another on 3.12. We need something like virtualenv that would provide isolation, but instead of at the project level, at the system level, and not for packages but for Python versions.

How to do this? Using pyenv. Pyenv has been enhanced with a neat plugin that allows us to create something like virtualenvs, but from different Python versions/interpretations. Pyenv + pyenv-virtualenv integrates beautifully with Poetry.

Anyway. We have pyenv-virtualenv, which is a wrapper for pyenv, which in turn is a wrapper around Python version management, working with Poetry, which is a wrapper for pip and pip-tools, integrated with virtualenv, which is also a kind of wrapper.

So we have a wrapper of a wrapper working on top of a wrapper of a wrapper. Wrapperception, dependencyception, wild animals everywhere.

### Piptools
If your project is simple enough or you don't want to bother with all this, you can use pip-tools to pin your dependencies and be done with it. pip-tools is good enough for some projects, but for convenience and other things that poetry offers, I actually use it pretty much everywhere I can. Convention over configuration.

## Hitting Python with Hardware

Sometimes you need to hit Python with hardware, equipment, or in other words, tooling. Since when did I start sounding like that? Something went wrong with writing this paragraph. Let's start over.

Formatting and static analysis of Python code, i.e., its tooling, is an important element of a lazy person's approach to ensuring code quality. These are things that work and care about quality for us, to make work easier. We'll talk a bit about them, but first about Pipelines.

### Pipelines
What are they and why do we need them? Automation to the rescue. When we want to take care of our Python code quality, we usually want to care about things like formatting, consistent import patterns, security, and keeping our standards up to date. If we want to do this in our repo/in the cloud automatically, we can use pipelines.

Pipelines are simply a set of steps that make up our CI/CD process. It's more or less just a piece of code that performs certain steps for us. Usually, pipelines are defined as a yaml file that specifies what steps/actions we want to take as part of our CI/CD process, i.e., analyzing, checking quality, formatting our code, and building/deploying it.

The most commonly known tools for this in the cloud include: GitHub Actions, GitLab CI/CD, Bitbucket Pipelines, CircleCI, Azure DevOps. Usually, these are things that fire when, for example, we create a merge/pull request, push some code to the repo, merge one branch into another. They run various checks, builds, tests, and whatnot.

The flow looks like this:

Trigger is received (e.g., Branch is pushed to repo) -> pipeline is fired -> various checks/actions are performed -> based on this, the pipeline can succeed or fail.

Besides pipelines being there in the cloud, I believe some of their parts are also an integral part of local development. Mainly the parts related to quality control/formatting/etc.

### What makes code good?

Currently, the trend in Python is to care about certain things that, while not crucial, contribute to the quality, readability, and maintainability of a project over time. At a high level, in my opinion, every piece of Python code would benefit from having:

1. Consistent formatting
2. Organized imports that are divided into sections
3. Absolute imports instead of relative ones
4. Using modern standards that comply with new conventions
5. No unused imports and unused variables
6. Security/vulnerability scanning

### The Dark Side of the Force - black

Time to go to the dark side of the force.

#### A few words about formatting and black
More often than not, in projects that aren't as automated as they could and should be, you can find people in pull requests arguing about which formatting is better. How to change formatting? Which is better? Which is more pep8 compliant?

This can be a nightmare that's so counterproductive it's unbelievable.

To get rid of such problems and have it handled for us, in Python we have something like Black. Black is a code formatter that, well, just formats code for you. You can make black automatically format your code before committing it. This way you can avoid all kinds of pep8 arguments and code formatting preferences by reviewers/authors, which makes the entire project have a consistent formatting pattern, which makes it easier to read and so on. The easier the code is to read, the better. The lazy person's approach. If you know what to expect, you won't be surprised. The less on your mind, the better.

#### ' vs "

One thing worth noting is that Python as a language allows the use of both ' and " to denote strings. Black by default prefers double quotes over single quotes. Why? Readability, the use of single quotes in English and having to escape them every time we use them inside our strings isn't very nice. That plus it's harder to make mistakes.

And so on. You can argue here, I stand on the side of double quotes because IMO it's a better approach. Readability is king.

### Isort
Have you heard of import sorting? It makes sense, believe it or not, and it's not a whim at all. Why should you properly sort your imports? The bigger the project we work on, usually the more things we import from other parts of the code.

Over time, these imports can become indecently large/numerous. This often happens. Isort is something that helps us with this, optimizing our imports, sorting them appropriately, alphabetically, grouping them in sections, and so on. I know this may look like a small thing, but it's these small things that add up to the overall code quality. Google an example of code changes after isort and see what it looks like.

### Imports like vodka - Absolute

The new standard in Python is to use absolute imports. Why this is the case you can read on your own. There have been many debates on this topic, the result of which is: we prefer absolute imports whenever possible. They make for less ambiguity and provide clearer distinction of what we're really using, from which package. We also have a tool for this purpose, which is absolufy-imports. This tool is particularly useful for older projects where you may need to fix imports in many files to match the new convention. This tool does it for you.

This:

```python
from .notifications.some_important_file import SomeClass
from .another_important_file import AnotherClass
```

Gets converted to this:

```python
from em.jobs.notifications.some_important_file import SomeClass
from em.jobs.notifications.another_important_file import AnotherClass
```


### Bandit
Static analysis of our code for potential security shortcomings.

#### Why you sometimes need a bandit in your life
When we write our code, we should keep security in mind. Unless you want to expose your company to potential loss of millions. I'm exaggerating with this example, but still. Security is important. Somehow we can make simple mistakes, due to forgetfulness and negligence, that could have been prevented otherwise. To remind us and warn us, there are various tools that can be used.

Among them is bandit. Bandit is a static analysis tool that scans your code for potentially dangerous code fragments and warns you about them. When you run bandit on your code, you get a report and a list of places in the code where potential problems exist.

### autoflake
The less you have...

#### Slimming down the code
Sometimes it happens that in our code we may have unused import declarations or unused variables. It happens to the best of us. To automatically take care of this, we may want to include autoflake in our projects. It's a tool that simply handles this - removes unused imports and variables. There's no magic here.

### pyupgrade
This piece of software automatically updates some old syntax patterns to new ones. That's all.

### bumpversion
There's this thing called semantic versioning or semver. It's a convention that tells us to version our code according to the following pattern: MAJOR.MINOR.PATCH

For example: v0.2.12

The major part is incremented when we go through major rollouts that change a lot.

Minor is incremented when we do normal releases, e.g., with larger features.

Patch is something we use for smaller features, patches, fixes, etc. This element grows the fastest.

So that we don't have to manage this manually, we have a tool called bumpversion. It updates the version, creates a commit with the changes, creates a git tag, and so on, all automatically. It's a neat tool to have in your CI/CD. This makes version management, changelog creation, commit filtering, and noticing changes, bugs, versioning packages/api, etc., easier. You can see an example commit history and bumpversion usage in my project's commit history - braindead. Check it out.

Do we run all this manually? No. We want to be lazy.

### Git hooks & pre-commit
Automate boring tasks, live long and prosper.

#### Git hooks and pre-commit
If you want all this to happen automatically, you can create git-hooks that are run, e.g., during a commit or before a commit. One way is to simply create a .pre-commit file and place it in the .git folder and use, e.g., Makefile or use something like the pre-commit tool. It's a nice, handy tool that takes care of this for you. You need to install it and create a config for it to tell it which things to do before the commit. There's no magic here.

I'll let you google the details yourself.

### Summary
Black, isort, absolufy-imports, pyupgrade, autoflake, bandit, bumpversion are tools that will make your life a bit easier.

Maybe it's a good idea to include them in your local development workflow and pipelines?

## Questions and Tasks

1. Write a short summary with conclusions about which tool is for what and with usage examples, then send the results of your work.

\pagebreak

