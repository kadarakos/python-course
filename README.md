# Python Programming for the Humanities

For this course, we will make use of IPython notebooks. Follow the instructions below to install all the software required for this course. (Many thanks to Folgert Karsdorp for his kind help in providing the installation instructions and launching scripts!)

## Instruction for developers

We are going to use the method from the caffe guys, I think
it's not that overdone: https://github.com/sguada/caffe-public
The only difference we are going to make is that we are only
going to have a master branch and no dev.

First get your own copy of the repo. 
Fork this repository and clone your own fork

```
git clone https://github.com/yourusername/python-course.git
```

If you would like to make your edits first make sure that everything is
up to date, then create a branch where you add some feature
lets call it "feature".

```
git checkout master
git pull upstream master
git checkout -b feature
# do your work, make commits
```

When you are done with your feature prepare your merge by rebasing first.

```
# make sure master is fresh
git checkout master
git pull upstream master
# rebase your branch on the tip of master
git checkout master
git rebase master
```

Push your branch to pull request it into master 

```
git push origin feature
# ...make pull request to dev...
```

Now make a pull request! Please write informative messages in the
pull requestion so we know what changes have been made.

Make sure you check out these links for more information:

https://help.github.com/articles/fork-a-repo/
https://help.github.com/articles/creating-a-pull-request/
https://help.github.com/articles/checking-out-pull-requests-locally/



## Installation instructions

First we will install Python, the programming language which we will use throughout this course. We will make use of the free Anaconda distribution, which has all the packages we need built in. Important: we will use Python 3.4 in this course, but first you will have to install Python 2.7, so follow **exactly** the instructions below:

- Go to http://continuum.io/downloads
- Download the Graphical Installer for Python 2.7 (not for Python 3.4 yet!) which corresponds to your operating system (Mac OSX, Windows or Linux)
- Run the Graphical installer (if you run into problems, check out: http://docs.continuum.io/anaconda/install.html)

Now we will update our version of Anaconda for Python 3.4 via the command-line. First, open a command line (the scary black screen in which you can type commands for your computer):
- Under Mac OS X, navigate to /Applications/Utilities and double-click "Terminal"
- Under Windows, click "Start button Picture" > "All Programs" > "Accessories" > "Command Prompt"
- Under Linux: press the key combination Ctrl+Alt+T

Issue the following two commands in the command line: enter each command (and hit enter after each command):

On Windows:
- conda create -n py34 python=3.4 anaconda
- source py34

Other platforms:
- conda create -n py34 python=3.4 anaconda
- source activate py34

Download the course folder for this course, by navigating to https://github.com/mikekestemont/python-course and click "Download ZIP". Save and extract this ZIP folder to a convenient location, such as your Desktop. You should now be able to launch the interactive IPython notebooks in your browser. Open the unzipped folder and:

- Under Windows: double-click "start-windows.bat"
- Under Mac OSX: double-click "start-osx.command"
- Under Linux: double-click "start-unix.sh"

After double-clicking this file once, this should open your browser (preferably Google Chrome or Firefox) on a page http://127.0.0.1:8888/ (or something similar) which says `IP[y]: Notebook'. (Note that this might take a while on slower machines, so don't panic if this page doesn't show up immediately.) If for some reason, the notebook is opened by Internet Explorer, copy the URL and paste that in either Google Chrome or Firefox. If none of this worked, send me an email (firstname.lastname@uantwerp.be), but in the meanwhile you can still use the static versions of each chapter, listed below.

## Static Notebooks

[Chapter 1 - Variables](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%201%20-%20Variables.ipynb)

[Chapter 2 - Collections](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%202%20-%20Collections.ipynb)

[Chapter 3 - Conditions](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%203%20-%20Conditions.ipynb)

[Chapter 4 - Loops](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%204%20-%20Loops.ipynb)

[Chapter 5 - Functions and Files](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%205%20-%20Functions%20and%20Files.ipynb)

[Chapter 6 - Regular Expressions](http://nbviewer.ipython.org/github/mikekestemont/python-course/blob/master/Chapter%206%20-%20Regular%20Expressions.ipynb)

[Chapter 7 - More on Loops](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%207%20-%20More%20on%20Loops.ipynb)

[Chapter 8 - The Pattern Package (advanced)](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%208%20-%20The%20Pattern%20Package.ipynb)