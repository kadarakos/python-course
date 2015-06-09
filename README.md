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




## Static Notebooks

[Chapter 1 - Variables](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%201%20-%20Variables.ipynb)

[Chapter 2 - Collections](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%202%20-%20Collections.ipynb)

[Chapter 3 - Conditions](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%203%20-%20Conditions.ipynb)

[Chapter 4 - Loops](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%204%20-%20Loops.ipynb)

[Chapter 5 - Functions and Files](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%205%20-%20Functions%20and%20Files.ipynb)

[Chapter 6 - Regular Expressions](http://nbviewer.ipython.org/github/mikekestemont/python-course/blob/master/Chapter%206%20-%20Regular%20Expressions.ipynb)

[Chapter 7 - More on Loops](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%207%20-%20More%20on%20Loops.ipynb)

[Chapter 8 - The Pattern Package (advanced)](http://nbviewer.ipython.org/urls/raw.github.com/mikekestemont/python-course/master/Chapter%208%20-%20The%20Pattern%20Package.ipynb)