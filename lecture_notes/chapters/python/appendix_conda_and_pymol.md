# Appendix: Conda environment for BSF

*This chapter is only relevant to students following both Bioinformatics and Programming and Biomolekylær Struktur og Funktion.*

In bioinformatics, we install packages and programs so we can use them in our analyses and pipelines. Sometimes, however, the versions of packages you need for one project conflicts with the versions you need for other projects that you work on in parallel. Such conflicts seem like an unsolvable problem. Would it not be fantastic if you could create a small insulated world for each project, which then only contained the packages you needed for that particular project?. If each project had its own isolated world, then there would be no such version conflicts. Fortunately, there is a tool that lets you do just that, and its name is Conda.

> Conda is an open source package management system and environment management system for installing multiple versions of software packages and their dependencies and switching easily between them.

The small worlds that Conda creates are called "environments". You can create as many environments as you like, and then use each one for a separate bioinformatics project, a course, a bachelor project, or whatever you would like to insulate from everything else. Conda also downloads and installs the packages for you and it makes sure that the software packages you install in each environment are compatible. It even makes sure that packages needed by packages (dependencies) are also installed. Conda is truly awesome.

## Creating an environment for BSF  {.unnumbered}

When you install Anaconda, Conda makes a single base environment for you. It is called "base" and this is why it says "(base)" on your terminal.

Many of you take the course "Biomolecular Structure and Function" (let us call that BSF) alongside this course. In BSF, you need to install programs (e.g. PyMol) that may conflict with the packages you need for Bioinformatics and Programming. So we will create isolated Conda environments for each course to avoid such conflicts. Conda is a program you run from the command line, just like `python` or `cd`. So open your terminal (i.e., the "Terminal" program if you are on a Mac and the "Anaconda Powershell Prompt" program if you are on Windows). You need to two different set of commands depending on what chip set your computer has. If you have a new Mac it may have the new M1 or M2 chips. If you click the top left apple icon and select "About This Mac", it will say "Apple M1" or "Apple M2" if it is.

**If your Mac is an M1/M2 Mac**, you create a conda environment for BSF by copy/pasteing these command lines into the terminal *one at a time* and press return (enter) after pasting each one:

```
CONDA_SUBDIR=osx-64 conda create -y -n BSF
conda activate BSF
conda config --env --set subdir osx-64
conda install -y -c conda-forge -c anaconda -c schrodinger pymol-bundle pyqt
```

**Otherwise**, you create a conda environment for BSF by copy/pasteing these command lines into the terminal *one at a time* and press return (enter) after pasting each one:

```
conda create -y -n BSF
conda activate BSF
conda install -y -c conda-forge -c anaconda -c schrodinger pymol-bundle pyqt
```

Notice how the command prompt changed from "(base)" to "(bioprog)" to show that you are now in the bioprog environment. Looks like nothing changed, but now you have access to terminal commands not available in the base envirionment. You will learn about these later. Try this command:

```
conda deactivate
```

Notice how it now again says "(base)" on your command prompt. That is because you are back in your base environment. Every time you start a new terminal window, you will need to run `conda activate BSF` to activate the BSF environment to be able to access pymol. Try it out:

```
conda activate BSF
```

and press enter. Voila, you are now back in the BSF environment. Notice how the command prompt changed from "(base)" to "(BSF)" to show that you are now in the BSF environment. To run PyMol that you installed in this environment, just type

```
pymol
```

and hit enter.

Now try to close PyMol. Then go back to your terminal and type

```
conda deactivate
```

Notice how it now again says "(base)" on your command prompt. That is because you are back in your base environment. Try to type `pymol` (and hit enter), you terminal will tell you that it could not find anything called `pymol`. This is the way it should be. That is because PyMols is installed in the BSF environment, *not* in the base environment. It illustrates how the base environment is entirely separate from the BSF environment you just made.

## Starting PyMol  {.unnumbered}

From now on, you can start PyMol by typing these commands into the terminal (Anaconda Powershell Prompt on Windows):

```
conda activate BSF
```

(hit enter)

```
pymol
```

(hit enter)

