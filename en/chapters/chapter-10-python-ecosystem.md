# Python Tools Ecosystem

A bit about cool tools that are worth knowing. I assume you'll install each of these tools and play around with them.

## README File - What It Should Contain and How It Should Look

There's one thing that every proper project should have - a README file. A well-written, readable, and comprehensive README file is the basic form of documentation for every project, containing elementary information about the project itself, but in my opinion, not only that. A well-written README should contain a bit more. What exactly? I'll explain.

### Technology

Usually, when we work with README files, they have a `.md` extension, meaning we write them in Markdown according to convention. Markdown is something that allows us to format text. Using it in READMEs is not a requirement, but it's a widely accepted standard that makes our lives a bit easier and gives us more possibilities than a plain text file.

### What Sections Should a Good README Contain?

Below we'll discuss what sections, describing what, a good README file should contain.

### Title

We start the README with a title, of course. To do this, simply type the title in a line and add `#` before it, which will mark that line as a Markdown header.

### Project Description

Here we place elementary information about the project.

1. What kind of system component is it? E.g., API, Worker, frontend, library.
2. What functionalities does it handle? E.g., This is an API for a system that generates invoices.
3. What is the context? A bit of additional context, you can never have too much. E.g., These invoices are then sent to clients, (...). We use the standard template from the company's design book here.
4. Who are the stakeholders - who are the recipients of this project?
5. What business problem does this project solve?
6. Who are its end users?

The summary should be written in the domain language of the given problem. What does this mean? Well, its description, the description of the project's functionality should contain vocabulary from the field we're working in. If we're doing a project about tractors, let's use tractor terminology. When among crows, caw like them. This is the preferred approach compared to using pure, dry technical jargon.

### Technology Stack

In this section, we describe the most important technologies used in creating the project. Dependencies, external applications used, services, etc.

This allows the reader to quickly familiarize themselves with the technological choices made in the project, used to solve the given problem.

Technologies should be briefly described, with appropriate materials linked for the reader's convenience.

### Local Environment Setup Instructions

Here we place the steps needed to set up the environment locally. Additionally, this is where we place instructions for frequently used operations, what commands are most commonly used, such as clearing the database or creating it, migrations, etc. This is also where knowledge that is very specific to the given project lands, such as how localization, internationalization was solved using, for example, PhraseApp or OneSky.

I recommend describing this section particularly well, keeping in mind less technical users who might need to set up the environment locally for testing purposes. Sometimes these are non-technical people, testers, stakeholders, product owners, etc. They also deserve the possibility of having a local environment. Additionally, the entire environment setup process should be as automated as possible.

### Deployment

In a few sentences, concisely and briefly, describe how the application is deployed, in what environment it lives, where to look for a more detailed description of the architecture, and so on. Add a few words about CI/CD.

### Authors

List of main people in the project. Useful when jumping to a new project and quickly wanting to establish who holds the context and who is best to ask about things because they have the most knowledge about the project.

### Summary

The README file is an important and integral part of the system. Now you know how it should look.

## pdoc3

Automatic generation of the most important thing in the world - documentation. This tool plus extensive and sensible docstrings == happy developer.

For reading: https://pdoc3.github.io/pdoc/

## PyCharm/Visual Studio Code

The best IDE/editor for Python. I'm personally #teamPyCharm, but Visual Studio Code also does the job.

## Note Taking

There are a million tools for this. I recommend Notion. Other options?

For reading: https://bootcamp.uxdesign.cc/i-tried-40-project-note-taking-apps-what-i-chose-and-my-top-10-list-1d39d41852e4

## Pyenv, Poetry, and Other Rascals

Pyenv, Poetry, and other rascals - modern dependency and Python version management, or about contemporary Python versions, environments, and dependency management.

#### PIP

Pip is a tool that most of you should already know. It's used to install packages used in Python development and has been included by default with Python for several versions. But what exactly does it mean to install packages?

In short, pip provides tools for downloading packages from the Python Package Index - PyPI. This is the default Python package index where almost anyone can add packages. Default is a good word because pip allows us to use different indices. So, for example, your company might have its own hosted version of packages and then use it as a private version of PyPI. This allows for better package verification, only private network connections during CI/CD/development processes. This is quite an interesting option, especially considering recent malicious attacks on popular Python open-source packages.

#### Package Index
What exactly is a package index?

Actually, it's nothing complicated. It's simply an HTTP server, let's say, that provides a list of Python packages/packages - packages and certain metadata about them. Nothing more.

An interesting homework task to experiment with something new: try implementing your own version of PyPI and add some features to it, such as token-protected access to packages or even more - tokens with granular permissions functionality.

#### Default Package Installation

Usually, we have one, maximum two backward-incompatible Python versions installed on our computer. In the past, this was Python2 & Python3, currently most of the time only Python3 is installed as Python2 has died, perished, disappeared into the depths of the past.

Anyway. This means that in the Dark Ages or by default, packages were installed globally, for the entire system. This is bad for many reasons. As for what package installation means, in a very big nutshell, it's nothing more than downloading a Python code package with a specific structure, which gets downloaded and placed in a given Python installation directory, with additional possible steps in between.

What if project A requires package Z in version 1.0.0, but project B requires package Z in version 2.0.0? Would you reinstall this package every time you switch between different projects?

#### virtualenv
To combat the problem described in the previous paragraph -> packages installing globally, virtualenv appeared. In short, it's something that allows us to "create" another, "instance" of Python installation. For example, just for a given project instead of system-wide.

This way we can have different versions of Python packages for different projects.

A subset of virtualenv's functionality is integrated into the default CPython installation since version 3.3 as the venv module.

#### Poetry
What if pip and virtualenv had a child that was also on steroids? Well, we'd get Poetry.

The problem with pip is usually dependency version management. Even if we know that our project A requires package Z in version 1.0.0, usually at first glance pip doesn't tell us about the dependencies of that package Z. This introduces the possibility of problems when your project reaches a point where it has a few more packages installed. Because these packages also have dependencies, and their dependencies also have dependencies. Dependencyception.

Usually, it's not dependency hell like in JS worlds, but at some point, it can also become a bit sneaky if you only pin dependencies at the top level. And at some point, it's almost guaranteed that there will be problems with this. And besides - if versions of these dependencies aren't guaranteed by default, what about debugging? I mean, one build might have version 1.2.3 of some dependency, but another build, done 10 minutes earlier, might have 1.2.2, if versions aren't resolved in a deterministic, guaranteed way, this enables nasty bugs to appear.

It's also a security threat because if you don't know exactly what version of a dependency you have, a malicious version might find its way without our explicit knowledge, which is quite an easy way to shoot yourself in the foot. How to remedy this?

We have something called dependency resolving and dependency locking. Basically, it's just the process of making sure we know the dependencies of our dependencies and their dependencies, and we have a clear list of their versions, usually signed with a hash. This allows for something called deterministic builds, which is one of the key elements of modern CI/CD and applications that follow the Twelve-factor app pattern.

This is exactly what Poetry does. And it does it pre-elegantly.

Besides, while we're at it, Poetry also makes project management easier, handles creating and managing virtualenvs for you, and enables easier, more centralized project configuration through the introduction of pyproject.toml. pyproject.toml is now usually the new standard configuration file for Python projects. And it also makes building packages easier because it can bundle your Python code and publish it in the package index of your choice, e.g., in PyPI.

Generally speaking, Poetry is pretty cool.

#### Pyenv

Python is a peculiar little animal that sheds its skin from time to time. This means that Python itself, just like our dependencies, also has its versions. Each version contains new features, various improvements. Some of them are sometimes even backward-incompatible. By default, it's not trivial to install different Python versions and manage them so they don't conflict with each other.

But why do this at all? Well, just like with dependencies. One project might depend on Python 3.10, another on 2.7, and yet another on 3.12. We need something like virtualenv that would provide isolation, but instead of at the project level, at the system level and not for packages but for Python versions.

How to do this? With pyenv. Pyenv has been enriched with a neat plugin that allows us to create such virtualenvs, but with different Python versions/interpretations. Pyenv + pyenv-virtualenv integrates beautifully with Poetry.

Anyway. We have pyenv-virtualenv, which is a wrapper for pyenv, which in turn is a wrapper around Python version management, working with Poetry, which is a wrapper for pip and pip-tools, integrated with virtualenv, which is also a kind of wrapper.

So we have a wrapper of a wrapper working on a wrapper of a wrapper. Wrapperception, dependencyception, wild, martens, raccoons.

### Piptools
If your project is simple enough or you don't want to bother with all this, you can use pip-tools to pin your dependencies and be done with it. pip-tools is good enough for some projects, while I, for convenience and other things that Poetry offers, use it practically everywhere I can. Convention over configuration.

## Python Tooling

In Python, sometimes you need to hit it with tooling. Since when do I sound like MMA bros on the scene? Something went wrong with writing this paragraph. Let's start over.

Formatting and static analysis of Python code, or its tooling, is an important element of the lazy person's approach to ensuring code quality. These are things that do and take care of quality for us, to make work easier. Let's talk a bit about them, but first about Pipelines.

### Pipelines
What are they and why do we need them? Automation of things? Pipelines to the rescue. How strange that sounds in Polish. When we want to take care of our Python code quality, we usually want to take care of things like formatting, consistent import patterns, security, and keeping our standards up to date. If we want to do this in our repo/in the cloud automatically, we can use pipelines.

Pipelines are simply a set of steps that make up our CI/CD process. It's more or less just a piece of code that performs certain steps for us. Usually, pipelines are defined as a YAML file that specifies what steps/actions we want to take as part of our CI/CD process, i.e., analyzing, checking quality, formatting our code, and building/deploying it.

Among the most commonly known tools for this in the cloud are: GitHub Actions, GitLab CI/CD, Bitbucket Pipelines, CircleCI, Azure DevOps. Usually, these are things that run when, for example, we create a merge/pull request, push some code to the repo, merge one branch into another. They run various checks, building, tests, and so on.

The flow looks like this:

Trigger is received (e.g., Branch is pushed to repo) -> pipeline is run -> various checks/actions are performed -> based on this the pipeline may succeed or fail.

Besides pipelines being in the cloud, I think some of their parts are also an integral part of local development. Mainly parts related to quality control/formatting/etc.

### What Makes Code Good?

Currently, the trend in Python is to take care of certain things that, while not crucial, over time contribute to the quality, readability, and maintainability of the project. At a high level, in my opinion, every piece of Python code would gain something by having:

1. Consistent formatting
2. Ordered imports that are divided into sections
3. Absolute imports instead of relative ones
4. Using modern standards that comply with new conventions
5. No unused imports and unused variables
6. Security/vulnerability scanning

### The Dark Side of the Force - Black

Time to go to the dark side of the force.

#### A Few Words About Formatting and Black
More often than in projects that aren't as automated as they could and should be, you can find people in pull requests arguing about which formatting is better. How to change formatting? Which is better? Which is more compliant with PEP8?

This can be a nightmare that is so counterproductive that it doesn't even fit in corporate.

To get rid of such problems and have it taken care of for us, in Python we have something called Black. Black is a code formatter that, well, just formats code for you. You can make Black automatically format your code before committing it. This way you can avoid all kinds of disputes about PEP8 and code formatting preferences by reviewers/authors, which makes the entire project have a consistent formatting pattern, making it easier to read and so on. The easier the code is to read, the better. The lazy person's approach. If you know what to expect, you won't be surprised. The less on your mind, the better.

#### ' vs "

One thing worth noting is the fact that Python as a language allows the use of both ' and " to mark strings. Black by default prefers double quotes over single ones. Why? Readability, the use of single quotes in English and the need to escape it every time we use it inside our strings isn't very nice. That plus it's harder to make a mistake.

And so on. You can argue here, I stand on the side of double quotes because IMO it's a better approach. Readability is king.

### Isort
Have you heard about sorting imports? It makes sense despite appearances and isn't a whim at all. Why should you sort your imports appropriately? The bigger the project we're working on, usually the more things we import from other parts of the code.

Over time these imports can become indecently large/numerous. Often they do. Isort is something that helps us with this, optimizing our imports, sorting them appropriately, alphabetically, grouping them in sections, and so on. I know it might look like a trifle, but it's these small things that add to the overall code quality. Google yourself an example of code changes after isort and see how it looks.

### Imports Like Vodka - Absolute

The new standard in Python is using absolute imports. Why this is the case you can read on your own. There have been many debates on this topic, the result of which is: we prefer absolute imports whenever possible. They make for less ambiguity and provide clearer distinction of what we're actually using, from which package. We also have a tool for this purpose, which is absolufy-imports. This tool is particularly useful in older projects where you might need to fix imports in many files to match the new convention. This tool does it for you.

This:

```python
from .notifications.some_important_file import SomeClass
from .another_important_file import AnotherClass
```

Gets changed to this:

```python
from em.jobs.notifications.some_important_file import SomeClass
from em.jobs.notifications.another_important_file import AnotherClass
```

### Bandit
Static analysis of our code for potential security vulnerabilities.

#### Why You Sometimes Need Bandits in Your Life
When writing our code we should keep security in mind. Unless sometimes you want to expose your company to potential loss of millions. I'm exaggerating with this example, but still. Security is important. Somehow we can make simple mistakes due to forgetfulness and neglect that could have been prevented in another way. To remind us of this and warn us, there are various tools that can be used.

Among them is Bandit. Bandit is a static analysis tool that scans your code looking for potentially dangerous code fragments and warns you about them. When you run Bandit on your code, you'll get a report and a list of places in the code where there are potential problems.

### autoflake
The less you have...

#### Slimming Down Code Like Putin Slims Down Citizens
Sometimes it happens that in our code we can have unused import declarations or unused variables. It happens to the best of us. To automatically take care of this, we might want to include autoflake in our projects. This is a tool that simply takes care of this - removes unused imports and variables. There's no magic here.

### pyupgrade
This piece of software automatically updates some old syntax patterns to new ones. That's all.

### bumpversion
There's something we call semantic versioning or semver. It's a convention that tells us to version our code according to the following pattern: MAJOR.MINOR.PATCH

For example: v0.2.12

The major part is increased when we move to major rollouts that change many things.

Minor is increased when we make normal releases, e.g., with larger features.

Patch is something we use for smaller features, patches, fixes, etc. This element grows the fastest.

So we don't have to manage this manually, we have a tool called bumpversion. It updates the version, creates a commit with changes, creates a git tag, and so on, all automatically. It's a neat tool that you can have in your CI/CD. This makes version management, creating changelogs, filtering commits and noticing changes, bugs, versioning packages/api, etc., easier. You can see an example commit history and bumpversion usage in the commit history of my project - braindead. Take a look.

Do we run all this manually? No. We want to be lazy.

### Git Hooks & pre-commit
Automate boring tasks, live long and prosper.

#### Git Hooks and pre-commit
If you want all this to happen automatically, you can create git-hooks that run, for example, during commit or before commit. One way is to simply create a .pre-commit file and place it in the .git folder and use, for example, Makefile or use something like the pre-commit tool. It's a nice, handy tool that takes care of this for you. You need to install it and create a config for it to tell it which things to do before commit. There's no magic here.

\pagebreak 