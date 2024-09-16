# Before you begin {#sec:before_you_begin}


*This chapter serves to get the practicalities out of the way so you can start programming. Read the whole chapter once carefully before you install anything*

## Install Python  {.unnumbered}

In this course, we use the Python programming language, and we need the Python program to run the code we will  write. We will use a distribution of Python called *Anaconda*. Anaconda is the easiest way of installing Python on Windows, macOS (Mac), and Linux. To install Anaconda, head to [this](https://www.anaconda.com/products/individual) site. Click "Download". When the download has completed, double-click the file you just downloaded and follow the instructions on the screen. It is important that you accept all the suggested installation settings.

## The text editor  {.unnumbered}

You will also need a *text editor*. A text editor is where you write your Python code. For this course, we will use *Visual Studio Code* - or *VScode* for short. You can download it from [this page](https://code.visualstudio.com/download). If you open *VScode*, you should see something like [@fig:figure0]. You may wonder why we cannot just Word to create and edit files with programming code. The reason is that a text editor made for programming, such as VScode, only saves the actual characters you type. So unlike, Word, it does not silently save all kinds of formatting, like margins, bold face text, headers, etc. With VScode, what you type is *exactly* what ends up in the file when you save it. In addition, where Word is made for prose, VScode is made for programming and has a lot of features that you will make your programming life easier. 

![Visual Studio Code (VScode)](./images/vscode.png){#fig:figure0 width=80%}

## The terminal  {.unnumbered}

The last thing you need is a tool to make Python run the programs you write. Fortunately, that is already installed. On **OSX** this is an application called *Terminal*. You can find it by typing "Terminal" in Spotlight Search. When you start you will see something like @fig:terminal. You may be presented with the following text:

```
The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
```
 
![The Terminal app on Mac](./images/terminal.png){#fig:terminal width=85%} 

![Anaconda Powershell Prompt app on Windows](./images/powershellprompt.png){#fig:anacondaprompt width=75%}

Do __*not*__ update your account __*after*__ you install Anaconda (see below). If you do, *Terminal* will not be able to find the Anaconda Python (If you did so by mistake anyway, you change back using this command: `chsh -s /bin/bash`.

On **Windows** the tool you need is called the *Anaconda Powershell Prompt* and was installed along with Anaconda Python. You should be able to find it from Start menu. Make sure you open *Anaconda Powershell Prompt* and **not** *Anaconda Prompt*. They are different programs. If you open *Anaconda Powershell Prompt* you should see something like @fig:anacondaprompt.

What is *Anaconda Powershell Prompt* and this *Terminal* thing, you ask. Both programs are what we call *terminal emulators*. They are programs used to run other programs, like  the ones you are going to write yourself. I will informally refer to both *Terminal* and *Anaconda Powershell Prompt* as "the terminal" So if I write something like "open the terminal", you should open *Anaconda Powershell Prompt* if you are running Windows and the *Terminal* application if you are running OS X.

The terminal is a very useful tool. To use it, however, you need to know a few basics. First of all, a terminal lets you execute commands on your computer. You simply type the command you want and then hit enter. The place where you type is called a prompt (or command prompt) and it may look a little different depending on which terminal emulator you use. In this book we represent the prompt with the character `$`. So a command in the examples below is the line of text to the left of the `$`. When you open the terminal you'll be located in a folder. You can see which folder you are in by typing `pwd`, and then press `Enter` on the keyboard. When you press `Enter` you tell the terminal to execute the command you just wrote. In this case, the command you typed simply tells you the path to the folder we are in. If I do it I get:

```
$ pwd
/Users/kasper/programming
```

If I had been on a windows machine it would have looked something like: 

```
$ cd
C:\Users\kasper\programming
```

So right now I am in the folder `programming`. `/Users/kasper/programming` is the path or "full address" of the folder with dashes (or backslashes on windows) separating nested folders. So `programming` is a subfolder of `kasper` which is a subfolder of `Users`. That way you not only know which folder you are in but also where that folder is. Let us see what is in this folder. You can use the `ls` command (l as in Lima and s as in Sierra). When I do that and press `Enter` I get:

```
$ ls
notes projects
```

It seems that there are two other folders, one called `notes` and another called `projects`. If you are curious about what is inside the `notes` folder, you can "walk" into the folder with the `cd` command. To use this command you must specify which folder you want to walk into (in this case `notes`). We do this by typing `cd`, then a space and the then name of the folder. When I press enter I get:

```
$ cd notes
$
```

It seems that nothing really happened, but if I run the `pwd` command now to see which folder I am in, I get:

```
$ pwd
/Users/kasper/programming/notes
```

Just to keep track of what is happening: before we ran the `cd` command we were in the directory `/Users/kasper/programming` folder, and now we're in `/Users/kasper/programming/notes`. This means that we can now use the `ls` command to see what is in the `notes` folder:

```
$ ls
$
```

Again it seems like nothing happened. Well, `ls` and `dir` do not show anything if the folder we are in is empty. So `notes` must be empty. Let us go back to where we came from. To walk "back" or "up" to `/Users/kasper/programming` we again use the `cd` command, but this time we do not need to name a folder. Instead, we use the special name `..` to say that we wish to go to the parent folder called `programming`, i.e. the folder we just came from:

```
$ cd ..
$ pwd
/Users/kasper/programming
```

Now when we run the `pwd` command we see that we are back where we started. Let us see if the two folders are still there:

```
$ ls
notes projects
```

They are! 

Hopefully, you are now able to use navigate your folders and see what is in them. You will need this later to go to the folders with the code you write for the exercises and projects during the course.

| Action | OSX |
|:---|:---|
| Show current folder | `pwd` |
| List folder content | `ls` |
| Go to subfolder "notes" | `cd notes` |
| Go to parent folder | `cd ..` |

<!-- The terminal is a very useful tool. To use it, howevever, you need to know a few basics. First of all, a terminal lets you execute commands on your computer. You simply type the command you want and then hit enter. The place where you type is called a prompt (or command promt) and it may look a little different depending on which terminal emulator you use. In this book we represent the prompt with the character `$`. So a command in the examples below is the line of text to the left of the `$`. When you open the terminal you'll be located in a folder. You can see which folder you are in by typing `pwd` on OSX and `cd` on windows, and then press `Enter` on the keyboard. When you press `Enter` you tell the terminal to execute the command you just wrote. In this case, the command you typed simply tells you the path to the folder we are in. If I do it I get:

```
$ pwd
/Users/kasper/programming
```

If I had been on a windows machine it would have looked something like: 

```
$ cd
C:\Users\kasper\programming
```

So right now I am in the folder `programming`. `/Users/kasper/programming` is the path or "full address" of the folder with dashes (or backslashes on windows) separating nested folders. So `programming` is a subfolder of `kasper` which is a subfolder of `Users`. That way you not only know which folder you are in but also where that folder is. Let us see what is in this folder. On OSX you type the `ls` command (l as in Lima and s as in Sierra). On windows you type `dir`. When I do that and press `Enter` I get:

```
$ ls
notes projects
```

It seems that there are two other folders, one called `notes` and another called `projects`. If you are curious about what is inside the `notes` folder, you can "walk" into the folder with the `cd` command. To use this command you must specify which folder you want to walk into (in this case `notes`). We do this by typing `cd`, then a space and the then name of the folder. This is the same OSX and Windows. When I press enter I get:

```
$ cd notes
$
```

It seems that nothing really happened, but if I run the `pwd` command (`cd` on Windows) now to see which folder I am in, I get:

```
$ pwd
/Users/kasper/programming/notes
```

Just to keep track of what is happening: before we ran the `cd` command we were in the directory `/Users/kasper/programming` folder, and now we're in `/Users/kasper/programming/notes`. This means that we can now use the `ls` command (`dir` on Windows) to see what is in the `notes` folder:

```
$ ls
$
```

Again it seems like nothing happened. Well, `ls` and `dir` do not show anything if the folder we are in is empty. So `notes` must be empty. Let us go back to where we came from. To walk "back" or "up" to `/Users/kasper/programming` we again use the `cd` command, but this time we do not need to name a folder. Instead, we use the special name `..` to say that we wish to go to the parent folder called `programming`, i.e. the folder we just came from:

```
$ cd ..
$ pwd
/Users/kasper/programming
```

Now when we run the `pwd` (or `cd`) command we see that we are back where we started. Let us see if the two folders are still there:

```
$ ls
notes projects
```

They are! 

Hopefully, you are now able to use navigate your folders and see what is in them. You will need this later to go to the folders with the code you write for the exercises and projects during the course.

| Action | Windows | OSX |
|:---|:---|:---|
| Show current folder | `cd` | `pwd` |
| List folder content | `dir` | `ls` |
| Go to subfolder "notes" | `cd notes` | `cd notes` |
| Go to parent folder | `cd ..` | `cd ..` | -->

## Create a conda envirionment for the course  {.unnumbered}

In bioinformatics, we install packages and programs so we can use them in our analyses and pipelines. Sometimes, however, the versions of packages you need for one project conflicts with the versions you need for other projects that you work on in parallel. Such conflicts seem like an unsolvable problem. Would it not be fantastic if you could create a small insulated world for each project, which then only contained the packages you needed for that particular project?. If each project had its own isolated world, then there would be no such version conflicts. Fortunately, there is a tool that lets you do just that, and its name is Conda.

> Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them.

The small worlds that Conda creates are called "environments". You can create as many environments as you like, and then use each one for a separate bioinformatics project, a course, a bachelor project, or whatever you would like to insulate from everything else. Conda also downloads and installs the packages for you and it makes sure that the software packages you install in each environment are compatible. It even makes sure that packages needed by packages (dependencies) are also installed. Conda is truly awesome.

When you install Anaconda, Conda makes a single base environment for you. It is called "base" and this is why it says "(base)" on your terminal.

In this course, you need to install programs, and python libraries that could conflict with the packages you need for other courses or future projects. So we will create an isolated Conda environment for Bioinformatics and Programming to avoid such conflicts. Conda is a program you run from the command line, just like `python` or `cd`. So open your terminal (i.e., the "Terminal" program if you are on a Mac and the "Anaconda Powershell Prompt" program if you are on Windows). Now copy/paste these command lines into the terminal *one at a time* and press return (enter) after pasting each one:

```
conda create -y -n bioprog
conda activate bioprog
conda config --env --add channels conda-forge
conda config --env --add channels sepandhaghighi
conda config --env --add channels kaspermunch
conda install -y python=3.9 pygments=2.16.1 textual=0.37.1 rich=13.6.0 art=6.1 bp-help
```

This commands run the Conda program and tells it to create a new environment with name "bioprog" and to install the packages we need in that environment. Once you hit enter on the last command, Conda works for some time and then writes a long list of packages in your terminal. These are all the packages and dependencies required in versions that all fit together. 

Notice how the command prompt changed from "(base)" to "(bioprog)" to show that you are now in the bioprog environment. Looks like nothing changed, but now you have access to terminal commands not available in the base environment. You will learn about these later. Try this command:

```
conda deactivate
```

Notice how it now again says "(base)" on your command prompt. That is because you are back in your base environment. Every time you start a new terminal window, you will need to run `conda activate bioprog` to activate the environment to be able to access the course tools.


## You are all set  {.unnumbered}

Well done! You are all set to start the course. Have a cup of coffee and look forward to your first program. While you sip your coffee, I need to you take an oath (one of three you will take during this course). Raise your right hand! (put the coffee in your left).

> **Oath 1:** I swear *never* to copy and paste code examples from this book into my text editor. I will always *read* the examples in then *type* them into my editor.

This serves three purposes (as if one was not enough):

1. You will be fully aware of each and every bit of each example.
2. You will learn to write code correctly and without omissions and mistakes.
3. You will get Python “into your fingers”. It sounds silly, but it *will* get into your fingers.









