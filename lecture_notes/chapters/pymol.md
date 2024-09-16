# Installation instructions  {.unnumbered}

<!-- TODO: Figure  out whether to tell students from Gregers class to call their environment something different, og whether the environment for both Gregers and Ditlevs classes should both be called "pymol". -->

<!-- TODO: Add note to students that had Gregers class, that they have already installed Anaconda and Pymol, and that they only need to install VScode (if they don't alrady have it). -->


In this course, we use a distribution of Python called *Anaconda*. Anaconda is simply an easy way of installing Python on and PyMol.

## Install Python  {.unnumbered}

To install Anaconda, head to [this](https://www.anaconda.com/download) site. Click the big green Download button.

When the download has completed, you should follow the platform specific instructions. It is important accept the default installation settings.

## Install PyMol  {.unnumbered}

If you are on a Windows machine, find the program called "Anaconda Powershell Prompt". If you are on a Mac, find the program called "Terminal". These are both programs where you can type commands to run other programs. When you open *Anaconda Powershell Prompt* you should see something like @fig:prompt. The OSX Terminal looks like @fig:terminal, possibly with a different background color.

![Screenshot of Anaconda Powershell Prompt](./images/anaconda_prompt.jpg){#fig:prompt}

![Screenshot of Terminal](./images/terminal.png){#fig:terminal}

Now paste this into Anaconda Powershell Prompt (or Terminal).

```
conda create -n BSF -c schrodinger pymol python=3
```

Then hit enter. Now the program works for some time and then writes a long list of packages. These are all the packages and dependencies required by python and PyMol in versions that all fit together. It looks something like this:

```
  readline           pkgs/main/osx-64::readline-7.0-h1de35cc_5
  requests           pkgs/main/osx-64::requests-2.22.0-py37_0
  rigimol            schrodinger/osx-64::rigimol-1.3-2
  setuptools         pkgs/main/osx-64::setuptools-41.0.1-py37_0
  sip                pkgs/main/osx-64::sip-4.19.8-py37h0a44026_0
  six                pkgs/main/osx-64::six-1.12.0-py37_0
  sqlite             pkgs/main/osx-64::sqlite-3.29.0-ha441bb4_0
  tk                 schrodinger/osx-64::tk-8.6.9-x11tk0_2000
  urllib3            pkgs/main/osx-64::urllib3-1.24.2-py37_0
  wheel              pkgs/main/osx-64::wheel-0.33.4-py37_0
  xz                 pkgs/main/osx-64::xz-5.2.4-h1de35cc_4
  zlib               pkgs/main/osx-64::zlib-1.2.11-h1de35cc_3
  zstd               pkgs/main/osx-64::zstd-1.3.7-h5bba6e5_0


Proceed ([y]/n)? 
```

Just hit enter again to Proceed. Once you do that, the program starts to download and install all the packages. It takes a bit of time.

When installation is complete the program writes:

```
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate BSF
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

## Start PyMol  {.unnumbered}

From now on, you can start PyMol by typing these commands in Anaconda Powershell Prompt if you are on windows, or Terminal if you are on Mac:

```
conda activate BSF
```

(hit enter)

```
pymol
```

(hit enter)
