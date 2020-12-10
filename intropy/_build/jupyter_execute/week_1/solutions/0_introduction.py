#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# In this notebook, we will introduce you to the basics of programming in Python. We will explain how to work with Jupyter notebooks, contrast "interactive programming" with "scripting", and introduce you to the concept of object-oriented programming. Importantly, we believe that programming is best learned by *doing it*, so this notebook will feature a lot of (ungraded) exercises. Because students often differ in how much experience they have with programming, the exercises are often relatively easy. However, to challenge those more familiar with programming, we also include (optional!) more difficult exercises. The concepts discussed in these exercises will not be featured on the exam and/or graded assignments.
# 
# ## Contents
# 1. Jupyter notebooks
# 2. Interative vs. script mode
# 3. Object-oriented programming
# 
# **Estimated time to complete**: 1-3 hours

# ## Jupyter notebooks
# So, what are Jupyter notebooks, actually? Basically, using Jupyter notebooks is like using the web-browser as a kind of editor from which you can run Python code, similar to the MATLAB interactive editor or RStudio. Just like any editor, code in Jupyter notebooks is interpreted and executed by Python on your computer (or on a remote server) and their results are returned to the notebook for display.
# 
# The cool thing about these notebooks is that they allow you to mix code "cells" (see below) and text "cells" (such as this one). The (printed) output from code blocks are displayed right below the code blocks themselves. 
# 
# Jupyter notebooks have two **modes**: edit mode and command mode.
# 
# - *Command mode* is indicated by a grey cell border with a blue left margin (as is the case now!): When you are in command mode, you are able to edit the notebook as a whole, but not type into individual cells. Most importantly, in command mode, the keyboard is mapped to a set of shortcuts that let you perform notebook and cell actions efficiently (some shortcuts in command mode will be discussed later!). Enter command mode by pressing **Esc** or using the mouse to click outside a cell’s editor area; <br><br>
# - *Edit mode* is indicated by a green cell border and a prompt showing in the editor area: When a cell is in edit mode, you can type into the cell, like a normal text editor. Enter edit mode by pressing Enter or using the mouse to double-click on a cell’s editor area.
# 
# When you're reading and scrolling through the tutorials, you'll be in the command mode mostly. But once you have to program (or write) stuff yourself, you have to switch to edit mode. But we'll get to that. First, we'll explain something about the two types of cells: code cells and text cells.

# ### Code cells
# 
# Code cells are the place to write your Python code, similar to MATLAB 'code sections' (which are usually deliniated by %%). Importantly, unlike the interactive editors in RStudio and MATLAB, a code cell in Jupyter notebooks can only be run all at once. This means you cannot run it line-by-line, but you have to run the entire cell!
# 
# #### Running cells
# Let's look at an example. Below, you see a code-cell with two print-statements. To run the cell, select it (i.e., the cell should have a green or blue frame around it; doesn't matter whether you're in edit or command mode), and click on the "&#9654; `Run`" icon or press `ctr+Enter`). Try it with the cell below!

# In[1]:


print("I'm printing Python code")
print(3 + 3)


# Note that you cannot run the two print statements separately! (Unless you put them in two separate cells.) Also, in the above cell, we're explicitly printing the results of the code. By default, code cells always print the *last* line (if it's not a variable assignment), even if you don't explicitly call `print`:

# In[2]:


first_line = "This is not printed"
last_line = "But this is!"
last_line


# In your own code, if you want to see the results of your code, we recommend always using `print` statements!

# #### Stop running/execution of cells
# Sometimes, you might want to quit the execution of a code-cell because it's taking too long (or worse, you created an infinite loop!). To do so, click the stop icon &#9632; in the top menu!

# #### Restarting the kernel
# Sometimes, you accidentally 'crash' the notebook, for example when creating an infinite loop or when loading in too much data. You know your notebook 'crashed' when stopping the cell (&#9632;) does not work and your cell continues its execution, as evident by the `In [*]:` prompt next to the cell. In those cases, you need to completely restart the notebook, or in programming lingo: you need to "restart the kernel". To do so, click `Kernel` and `Restart`.
# 
# Importantly, when you restart the kernel, it will keep all text/code that you've written, but it will **not** remember all the variables that you defined before restarting the kernel, including the imports. So if you restart the kernel, you will have to re-import everything (e.g. run `import numpy as np` again).

# #### Inserting cells
# As you can see in the code cell above, you can only run the entire cell (i.e. both `print` statements). Sometimes, of course, you'd like to organise code across multiple cells. To do this, you can simply add new blocks (cells) by selecting "Insert &rarr; Insert Cell Below" on the toolbar (or use the shortcut by pressing the "B" key when you're in command mode; "B" refers to "**b**elow"). This will insert a new code cell below the cell you have currently highlighted (the currently highlighted cell has a blue box around it). 

# <div class='alert alert-warning' style="padding-bottom:10px">
#     <b>ToDo</b>: Try inserting a cell below and write some code, e.g., <tt>print(10 * 10)</tt>.
# </div>

# #### Inline plotting
# Another cool feature of Jupyter notebooks is that you can display figures in the same notebook! You simply define some plots in a code cell and it'll output the plot below it. 
# 
# Check it out by executing (click the "play" button or `ctr+Enter`) the next cell.

# In[3]:


# We'll get to what the code means later in the tutorial
import matplotlib.pyplot as plt # The plotting package 'Matplotlib' is discussed in section 3!

# Now, let's plot something
plt.plot(range(10))
plt.show()


# We'll discuss plotting in detail in a future tutorial!

# ### Text ("markdown") cells
# Next to code cells, jupyter notebooks allow you to write text in so-called "markdown cells" (the cell this text is written in is, obviously, also a markdown cell). Markdown cells accept plain text and can be formatted by special markdown-syntax. A couple of examples:
# 
# \# One hash creates a large header <br>
# \#\# Two hashes creates a slightly smaller header (this goes up to four hashes)
# 
# **Bold text** can be created by enclosing text in \*\*double asterisks\*\* and italicized text can be created by enclosing text in \*single asterisks\*. You can even include URLs and insert images from the web; check this [link](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for a cheatsheet with markdown syntax and options! All the special markdown-syntax and options will be converted to readable text *after running the text cell* (again, by pressing the "play" icon in the toolbar or by `ctr+Enter`).
# 
# To insert a text (markdown) cell, insert a new cell ("Insert &rarr; Insert Cell Below" or "B" in command mode). Then, *while highlighting the new cell*, press "Cell &rarr; Cell Type &rarr; Markdown" on the toolbar on top of the notebook (or, while in command mode, press the "m" key; "m" refers to "markdown"). You should see the prompt (the **`In [ ]`** thingie) disappear. Voilà, now it's a text cell!

# <div class="alert alert-warning">
# <b>ToDo</b>: Try it out yourself! Insert a new markdown cell and try to write the following (without peeking at this cell!):
# 
# **OMG**, this is the most awesome Python tutorial *ever*.
# </div>

# ### Changing cell type
# Sometimes you might accidentally change the cell type from "code" to "markdown". To change it back, you can click "Cell" &rarr; "Cell Type" &rarr; "Code" or "Markdown" (or use the shortcuts, in command mode, "m" for markdown or "y" for code). 

# <div class="alert alert-warning">
# <b>ToDo</b>: Try it out yourself! Change the code cell, which contains markdown, into a markdown cell!
# </div>

# In[4]:


This is a code cell, but it contains markdown, **oh no**!


# ### Getting help
# Throughout this course, you'll encounter situations in which you have to use functions that you'd like to get some more information on, e.g. which inputs it expects. To get help on any python function you'd like to use, you can simply write the function-name appended with a "?" and run the cell. This will open a window below with the "docstring" (explanation of the function). Take for example the built-in function **`len()`**. To get some more information, simply type `len?` in a code cell and run the cell.

# <div class="alert alert-warning">
#     <b>ToDo</b>: Try it out yourself: create a code cell below, type <tt>len?</tt> and check the output!
# </div>

# If this method (i.e. appending with "?") does not give you enough information, try to google (or just whatever search engine) the name of the function together with 'python' and, if you know from which package the function comes, the name of that package. For instance, for len() you could google: ['python len()'](http://lmgtfy.com/?q=python+len), or later when you'll use the numpy package, and you'd like to know how the `numpy.arange` function works you could google: "python numpy arange".

# <div class="alert alert-success">
#     <b>Tip</b>: Google is your friend! Googling things is an integral aspect of programming. If you're stuck, try to figure it out yourself by trying to find the solution online. At first, this might seem frustrating, but in the long run, it will make you a better programmer.
# </div>

# ### Saving your work & closing/shutting down the notebook
# You're running and actively editing the notebook in a browser, but remember that it's still just a file located on your account on your laptop (or server). Therefore, for your work to persist, you need to save the notebook once in a while (and definitely before closing the notebook). To save, simply press the floppy-disk image in the top-left (or do `ctr+s` while in command mode).
# 
# If you saved your notebook and want to close it, click "File" &rarr; "Close and halt". This will stop your notebook from running and close it.

# ### Executing order and overwriting variables
# Jupyter notebooks are meant to be run from top to bottom. You can, of course, go back and work on a previous section. But beware: variables from later sections (i.e., more towards the bottom of the notebook) might overwrite previously defined ones! For example, suppose that we define a particular variable `y` to be 5 (note that assignment in Python is done using the `=` operator):

# In[5]:


y = 5


# In[6]:


print("Is y equal to 5?", (y == 5))


# Now, in a later part we might again define a variable `y`, but this time we define it to be 6.

# In[7]:


y = 6


# If we would rerun (i.e., "go back") to the cell with the print statement (try this!), suddenly, it will print:
# 
# ```
# Is y equal to 5? False
# ```
# 
# This is why the order of executing the cells matter! The notebooks are designed to be run from top to bottom. So, if you encounter situations where you get errors because your variable suddenly seemed to have changed (where it used to work just fine), it might be due to variables being overwritten by code in later sections.
# 
# If this happens, we recommend clearing and restarting your kernel (the thing that executes your code) by Kernel &rarr; Restart & Clear Output (in the toolbar on top), and rerun all your cells from top to bottom.

# ### Exercises (ToDo/ToThink)
# We believe that the best way to learn how to do neuroimaging analysis is by *actually programming* the analyses yourself. You have already seen some of these (ungraded) exercises, which we call "ToDos" (formatted as <font color='orange'>orange</font> boxes): short programming exercises, which you get immediate feedback for using "tests" (more on this later). We highly recommend doing/answering the ToDos/ToThinks, because they are designed to improve your understanding of the material!
# 
# Sometimes, you also encounter <font color='green'>Tips and Tricks</font>, which may contain advice, more information on a specific topic, or links to relevant websites or material. 
# 
# For example, a "ToDo" would look something like this:

# <div class="alert alert-warning">
#     <b>ToDo</b>: In the code-cell below, set the variable <tt>x</tt> to 5 (without quotes!) and remove the <tt>raise NotImplementedError</tt> statement.
# </div>

# In[8]:


""" Implement the ToDo here. """

x = 'not yet 5'
### BEGIN SOLUTION
x = 5
### END SOLUTION


# Each answer-cell will contain the statement `raise NotImplementedError`. When implementing your ToDo, *you always have to remove this statement*, otherwise it will give an error when you run it.
# 
# Then, *after* each code-cell corresponding to the ToDo, there are one or more code cell(s) with "tests" written by us. These tests provide you with feedback about whether you implemented the "ToDo" correctly ("Well done!"), or, if it give an error or the wrong answer, will give you some hints on how to get it right. You can keep trying these ToDo exercises until your implementation passes the test cell(s)! If you don't see any errors when running the test-cells, you did the ToDo correctly!
# 
# The tests associated with the ToDo exercises are usually implemented as a set of `assert` statements (or `np.testing.assert_*`, which 'assert' whether a specific statement is true. If it evaluates to `False`, then that means you've made an error and it will "crash" by raising a specific error (with optional hints on how to proceed). For example, for the above `ToDo`, we simply evaluated the statement `assert(x == 5)` to check whether you set `x` to 5 correctly, as is shown in the cell below:

# In[9]:


""" Checks whether the above ToDo is correct. """
try:
    assert(x == 5)
except AssertionError as e:
    print("x does not evaluate to 5! Did you replace 'not yet 5' with 5?")
    raise(e)
else:
    print("Well done!")


# In contrast to ToDos, you don't get any immediate feedback on <font color='blue'>ToThinks</font> (because this cannot be automated). These ToThinks are designed to make you reflect on the study material.
# 
# Now, let's try another ToDo. Note that it is followed by two test-cells, which test different aspects of your implementation.

# <div class="alert alert-warning">
#     <b>ToDo</b>: In the code-cell below, set the variable <tt>y</tt> to <tt>x * 2</tt>, so you have to replace <tt>None</tt> with <tt>x * 2</tt> (yes, this is as easy as it sounds). Don't forget to remove the <tt>raise NotImplementedError</tt>.
# </div>

# In[10]:


""" Implement the ToDo here. """
x = 2
y = None
### BEGIN SOLUTION
y = x * 2
### END SOLUTION


# In[11]:


""" This tests the above ToDo. """
try:
    assert(y == x * 2)
except AssertionError as e:
    print("y does not evaluate to x * 2 (i.e., 4)! Did you replace y with x * 2?")
    raise(e)
else:
    print("Correct!")


# In[12]:


""" This tests the above ToDo as well. """
try:
    assert(isinstance(y, int))
except AssertionError as e:
    print("y doesn't seem to be an integer (it is of type %s; make sure it is!" % type(y))
    raise(e)
else:
    print("Epic!")


# ToThink exercises need a written answer in the associated markdown cell. A typical 'ToThink' may look like this:  

# <div class='alert alert-info'>
# <b>ToThink</b> (1 point): What's your name? Please write it in the text-cell below.
# </div>

# Lukas Snoek

# Make sure you actually write your name in the cell above! (You'll have to double-click the text-cell to go into 'edit mode' and replace 'YOUR ANSWER HERE' with your name, and render the cell again by running it.)

# ## Interactive vs. script mode
# Some programming languages, including Python, can be used *interactively*. Here, interactive means that subsets of code from a single file can be run one by one. Jupyter notebooks enable this way of programming by allowing users to split code across multiple cells (as you've seen in the previous section). Importantly, because all variables defined will be kept in memory until you close the notebook (i.e., when you stop the Python process), you can inspect the result of each step in your code. 
# 
# To peek at all variables defined thus far, we can use the `%whos` "magic command":

# In[13]:


get_ipython().run_line_magic('whos', '')


# Note that [magic commands](https://ipython.readthedocs.io/en/stable/interactive/magics.html) are Jupyter notebook-specific functionality, so it won't work in environments other than Jupyter notebooks! 
# 
# Interactive programming is common in languages such as R and Matlab, whose popular editors (like RStudio and the default Matlab editor) by design encourage users to run their scripts line by line. This way of programming is great for teaching, as it allows for explanation of concepts in a step by step fashion. Similarly, interactive programming is great when troubleshooting ("debugging") your code, exploring your data, or trying out different data visualizations.
# 
# However, this way of programming is not necessarily always the best way to write, organize, and run your code. For example, if you want to reuse your code across multiple projects or applications, you'd have to copy your code from one notebook to the other. Also, notebooks tend to become large and messy when the scope and complexity of projects increase. Fortunately, you can also store your code in regular Python files, i.e., any plain text file with the extension `.py`. These are analogous to R scripts (`.R`) and Matlab scripts (`.m`). Writing Python code in Python files is actually the way most people use Python!
# 
# Like Jupyter notebooks, Python files accept any valid Python code. We included an example script, `example_script.py`, in the current directory. 

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Locate the <tt>example_script.py</tt> file in the file browser on the left side of the Jupyterlab interface. Click on it to open it and inspect its contents.
# </div>

# As you can see, this file contains a couple of comments (prefixed by `#`) and two lines of code: one defining a variable (`message`) pointing to a string (`"Hi, welcome to introPy!"`) and one printing the variable. Now, you might ask yourself, "how should these files by run?". Usually, Python files are run (or "executed") in a *terminal*. A terminal, or sometimes called a *command line*, is a tool to perform tasks on a computer without a graphical interface. Instead of a graphical interface, you type commands in the terminal to tell it what to do. Although each operating system has its own type of terminal (and way to open it), Jupyterlab also comes with its own terminal implementation. 

# <div class='alert alert-warning'>
#     <b>ToDo</b> Open a terminal in Jupyterlab by clicking on <em>File</em> &rarr; <em>New</em> &rarr; <em>Terminal</em> in the upper left corner.
# </div>

# This should open a new tab in Jupyterlab with a terminal. In the terminal, you can enter different commands. For example, to print something (like the Python `print` function), you can run the following command:
# 
# ```bash
# echo "Hey! I'm running stuff in the terminal. #lit"
# ```

# <div class='alert alert-warning'>
#     <b>ToDo</b> Run the command above in the terminal!
# </div>

# In the above example, `echo` is a built-in command on most Linux and Mac systems. In addition to built-in commands, you can also enter Python commands to run Python files! To do so, your command should look something like:
# 
# ```
# python path/to/your/python_file.py
# ```

# The path to your Python file should be specified relative to your location in the terminal. By default in this course, Jupyterlab terminals are openened at the root of the directory with course materials. So, to run the `example_file.py` file, we cannot enter `python example_file.py`, but we should instead enter the full path to the file:
# 
# ```
# python tutorials/week_1/example_file.py
# ```

# <div class='alert alert-success'>
#     <b>Note</b>: While Mac and Linux systems use forward slashes (/) as a "separator" symbol, Windows uses backslashes (\). So, on Windows, you'd need to run <tt>python tutorials\week_1\example_file.py</tt>.
# </div>

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Run the file <tt>example_file.py</tt> in your terminal!
# </div>

# Importantly, when running Python files, it is run *as a whole*; unlike R and Matlab scripts, Python files cannot be run line by line!
# 
# As you can see, this non-interactive way of programming &mdash; which we'll call "script mode" for a lack of a better term &mdash; is quite different from interactive programming in Jupyter notebooks. Unlike in Jupyter notebooks, script mode strictly separates the process of writing code and running code. In this course, you will write code in both "interactive mode" (mostly week 1) and in "script mode" (mostly week 2).

# ### Scripts vs. modules
# One last concept related to script mode we want to discuss is the distinction between Python "scripts" and Python "modules". In short, any Python file (i.e., a file with the extension `.py`) can be either a *script* or a *module*, and whether it is one or the other depends on how you use the file. In short, scripts are Python files that contain code that actually *does* something (e.g., compute the average of a series of numbers, clean up a messy excel file, etc.) while modules only contain code that *define* things.
# 
# In the course materials, we have included a very simple script (`example_script.py`) and a simple module (`example_module.py`). The script computes the average of two (predefined) numbers (i.e., it *does* something). The module file only *defines* a function (`average`). Indeed, if you'd run the script, several things will be done (i.e., the average of `a` and `b` will be computed and the result will be printed), but if you'd run the module, nothing will happen.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Run both files separately and confirm for yourself that nothing happens when running the module file.
# </div>

# It is important to realize that this distinction between scripts and modules is a *conceptual* difference, not a *technical* one. Python doesn't care whether you think a file is a script or a module &mdash; it just sees and runs a `.py` file. Why would *you* care, then? Well, because it allows you to organize your code in a sensible and efficient manner, where modules may define operations that may be used across different scripts. In the example script and module discussed previously, we actually did something similar by "importing" functionality from the module in the script file! (Imports will be discussed at length in the next notebook.)
# 
# To give a more practical example, in my own research projects I often have a single `analysis.py` *script* which I run when I want to (re)run my analysis. This script uses functionality from different modules, such as `preprocessing.py` and `visualization.py`. This way, the analysis script stays relatively short and readable, abstracting away from the different operations defined in the modules.
# 
# Again, this distinction between scripts and modules is only conceptual. Nothing is stopping you from writing all your code in one single file! For example, the `average` function definition from the `example_module.py` module could also have been directly included in the `example_script.py` script; nothing wrong with that. But understanding the difference between these two types of files and organizing your code accordingly will undoubtely lead to cleaner, better readable code in the long run, especially for large projects!

# ## Object-oriented programming
# Before you are going to delve more into actual programming in the next notebook, we need to discuss one more concept: object-oriented programming. Here, we will discuss the essentials of what you need to know for this course. 
# 
# Object-oriented programming (OOP) is a particular programming paradigm. In such paradigms, "objects" are things that may contain data (called *attributes*) and functionality (called *methods*). Python is such an object-oriented programming language, as opposed to for example R and Matlab (although both feature some OOP functionality). Now, you may ask, "what are these *objects*, then?"
# 
# The answer is **everything**.
# 
# Everything in Python is an object. Every variable you define is pointing to a particular object in memory. For example, consider the following variable definition:

# In[14]:


x = 'hello'


# Here, `x` is an object! If we define a particular function (which will be explained in detail in the next notebook) ...

# In[15]:


def some_function(arg):
    return arg + 1


# ... then `some_function` is also an object!

# Importantly, each object is of a certain *class*. An object's class defines which *attributes* and which *methods* an object has. To find out an object's class, you can use the function `type`:

# In[16]:


type(x)


# So, it appears that the class of `x` is `str`, which stands for "string"!

# <div class='alert alert-warning'>
#     <b>ToDo</b>: find out the class of the function <tt>some_function</tt>
# </div>

# In[17]:


# Find out the class of `some_function` below!


# To further explain the relation between objects and classes, consider the following analogy. One way to think about the relationship between an object and a class is as the relationship between a building and it's (architectural) plan.
# 
# In other words, just like a building plan outlines how a building should be constructed, the class specifies how an object should be created. In programmer lingo, an object is always an *instance* of a class. Classes in Python define, basically, the attributes (i.e., things that an object *is* or *has*) and the methods (i.e., what each object *can do*). Importantly, all built-in data types in Python (like strings, integers, and lists) are in fact classes! In addition to built-in classes, you can also define your own custom classes! We will see an example of a custom class shortly.
# 
# Both attributes and methods can be accessed by the object appended with a period (.) and the name of the attribute/method. The *only* difference between attributes and methods is that methods are followed by round brackets, (), with optional arguments. For example, to access the `__class__` attribute of the string variable `x`, we would run the following:

# In[18]:


x.__class__


# As you can see, this attribute of `x` returns the name of its class. (Note that you could achieve the same by running `type(x)`!) Think of attributes as things that describe properties of objects.
# 
# As mentioned before, *methods* represent things that objects can *do*. For example, all string objects (like `x`) have the method `capitalize`, which can be run as follows:

# In[19]:


x.capitalize()


# As you can see, this method *does* something, i.e., it capitalizes the first character of the string! Note the round brackets in the previous line of code! This shows us that `capitalize` is in fact a method, and not an attribute.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: In the cell below, try out the string method <tt>isdigit</tt> using the object <tt>x</tt>. Do you understand what it does?
# </div>

# In[20]:


# Try out the `isdigit` method below!


# In the previous two examples (`capitalize` and `isdigit`), the methods do not take any inputs (or "arguments"). Some methods, however, need inputs. For example, the `replace` method of string objects takes two arguments: the first with the substring that should be replaced and the second with the substring that should replace the first one. An example:

# In[21]:


x.replace('h', 'c')


# As you can see in the example above, methods are very much like *functions* in the sense that they (may) take some inputs and (may) return something. Importantly, often (but not always, as we'll see in a minute) the results from the method operation are not automatically stored! So, if you want to store the result of a method call, assign the result to a (new) variable!

# In[22]:


x_h2c = x.replace('h', 'c')
print("The variable x_h2c contains:", x_h2c)


# Importantly, the `x_h2c` variable is now a new object, again from the string class!

# In[23]:


type(x_h2c)


# This is highlighting the fact about Python we mentioned earlier: *everything is an object!*

# <div class='alert alert-warning'>
#     <b>ToDo</b>: In the code cell below, using the variable <tt>x</tt>, call the method <tt>islower</tt> and save the result in a new variable <tt>is_x_lowercase</tt>.
# </div>

# In[24]:


# Implement the ToDo here
### BEGIN SOLUTION
is_x_lowercase = x.islower()
### END SOLUTION


# In[25]:


""" This cell tests your implementation above. """
# Test if variable is defined
if 'is_x_lowercase' not in locals():
    raise ValueError("Couldn't find the variable 'is_x_lowercase'; did you spell it correctly?")
else:
    # Test if the right method has been called
    if type(is_x_lowercase) != bool:
        raise ValueError("Hmmm, the output type is not what I expected (a boolean); did you "
                         "call the right method (islower)?")
    else:  # probably correct implementation then
        print("Yay! Well done.")


# Alright, although you now know how to access and use attributes and methods of *existing* objects, you might wonder how you can *create* objects. Creating objects actually looks a lot like calling a function (or method!): 
# 
# * you call a particular "class" (`Someclass` in the image below) ...
# * ... with, optionally, one or more arguments (`arg1`, `arg2` in the image below) ...
# * ... which you assign to a new variable (`my_var` in the image below)
# 
# The new variable then represents the new object!

# ![obj_class_diff](https://docs.google.com/drawings/d/e/2PACX-1vRs-GPEf1hZ229q01Zv4Nwwspi4dxXr900qUxFBPHeeI70yXE0uLKgrvxjk9LVL1bHp78ZIZGWCnOT4/pub?w=893&h=284)

# Most object are initialized in this way. To showcase this, we created a custom class, `Person`, which we defined in the `utils.py` file. We import the class below:

# In[26]:


from utils import Person


# Here, `Person` is like the `Someclass` element in the image above. Often, the class documentation tells us if the class should be initialized with any variables, and if so, which ones. One neat trick to peek at the code documentation of a particular class/function in Jupyter notebooks is to run the class/function appended with a question mark:

# In[27]:


get_ipython().run_line_magic('pinfo', 'Person')


# As you can see, the `Person` class needs two variables upon initialization: a name (a string) and an age (an integer or a float). Now, let's initialize a `Person` object and store it in a variable named `random_person`:

# In[28]:


random_person = Person('Lukas', 29)


# Now, the `random_person` represents an object (from the class `Person`) with its own attributes and methods! Often, the names of the input arguments (here, "name" and "age") are also bound to the object as attributes:

# In[29]:


print(random_person.name)
print(random_person.age)


# To find out which (other) attributes and methods a particular object has, you can either look at the source code (i.e., looking at the `utils.py` file in this case) or using the following Jupyter trick: in a code cell, type the name of the object followed by a period (.) and press TAB. This will create a pop-up with a list of the possible attributes (called "instances" in Jupyterlab) and methods (called simply "functions" in Jupyterlab).

# <div class='alert alert-warning'>
#     <b>ToDo</b>: In the cell below, use the Jupyter notebook trick just discussed to check out the attributes and methods of the <tt>random_person</tt> object.
# </div>

# In[30]:


# Use the Jupyter notebook trick here!


# As you've seen, the `random_person` object has three methods: `introduce`, `is_older_than_30`, and `increase_age`. The `introduce` method is a simple method that only prints something:

# In[31]:


random_person.introduce()


# Other methods, like the `is_older_than_30` method, actually also return something:

# In[32]:


older_than_30 = random_person.is_older_than_30()
print(f"Is {random_person.name} older than 30?", older_than_30)  # thank God


# Finally, some methods may not return anything but instead modify its own attributes! For example, the `increase_age` method takes a single input (an integer) that will increase the age attribute of the `Person` object by that number! For example:

# In[33]:


random_person.increase_age(1)
print(f"{random_person.name} is now this old:", random_person.age)  # oh no!


# As you can see, no need to save the result from `increase_age` in a new variable, because it is saved "internally" in the `age` attribute!

# <div class='alert alert-danger'>
#     <b>Warning!</b> If you save the "result" from a method call in a new variable even though that method doesn't return something, Python won't crash but save the result as <tt>None</tt>! So if you ever notice that one of your variables is <tt>None</tt>, this might have happened!
# </div>

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Lukas doesn't like to be 30 years old. Can you make him 29 again? Watch out: if you run the command <tt>increase_age</tt> multiple times, the <tt>age</tt> attribute will also be modified multiple times!
# </div>

# In[34]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
random_person.increase_age(-1)
### END SOLUTION


# In[35]:


""" Tests the ToDo implementation above. """
if random_person.age != 29:
    raise ValueError(f"Oh no, {random_person.name} is not 29 but {random_person.age}!")
else:
    print("Yes! Well done. I feel younger already.")


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Create a new <tt>Person</tt> object with your own name and age and save it in a variable named <tt>my_self</tt>. Then, introduce yourself (using the <tt>introduce</tt> method) and pretend its your birthday and increase your age by 1 (using the <tt>increase_age</tt> method).
# </div>

# In[36]:


""" Implement your ToDo here. """
### BEGIN SOLUTION
my_self = Person("Lukas", 29)
my_self.introduce()
my_self.increase_age(1)
### END SOLUTION


# In[37]:


""" Tests the above ToDo. """
if not 'my_self' in locals():
    raise ValueError("Oh no! I couldn't find the variable 'my_self'! Did you spell it correctly?")
else:
    if type(my_self.age) not in (int, float):
        raise ValueError("Oh no! Did you enter a valid number for age upon initialization?")
    else:
        print(f"Great work, {my_self.name}! You're on a roll!")


# Now, some of you may wonder about those built-in classes like strings, integers, and lists &mdash; objects from those classes seem to be initialized differently than we discussed! This is true! This is because some classes are used so often, Python introduced a shorter sytax (sometimes called "[syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)") to initialize objects from such classes. For example, as we have seen, string objects can be initialized by just wrapping characters in quotes:

# In[38]:


this_is_a_string = "a random sequence of characters in quotes"  # single quotes are fine too


# A more elaborate, but equivalent, way to initialize strings also exists, however:

# In[39]:


this_is_another_string = str("another random sequence of characters")


# The initialization process underlying `this_is_a_string` and `this_is_another_string` is equivalent! The same applies to integers:

# In[40]:


# Integers can be initialized using "syntactic sugar":
my_integer = 5

# ... or this way:
my_integer = int(5)


# ... and lists:

# In[41]:


# The "syntactic sugar" way:
my_list = [0, 1, 2]

# ... or this way:
my_list = list([1, 2, 3])


# All this is to show that *everything* in Python is an object! Objects may be initialized from built-in classes (like strings, integers, and lists) or from custom classes (like the `Person` class). We want you to understand that all objects may have certain attributes (which describe properties of the object) and methods (which represent things an object can *do*). You will encounter this idea a lot when we start working with the different data visualization (Matplotlib) and analysis (Pandas, Numpy) packages. Also, Psychopy features a lot of object-oriented programming.
# 
# For those that want a challenge can continue with the **optional** next section about creating custom classes yourself! If not, please continue with the next notebook: `1_python_basics.ipynb`.

# ### Custom classes (optional)
# In the previous section, you have seen how to instantiate objects from (custom) classes. In this (optional) section, you will learn how to *write* your own classes! This won't cover everything of object-oriented programming, but it will teach you enough to get started. Although it is not strictly necessary, familiarity with functions helps a lot to understand this section. 
# 
# Now, suppose that you are running an experiment for your MSc thesis. Each participant in your study performs a simple reaction time task. Half of the subjects are given a cup of coffee beforehand (condition: caffeine) while the other half are given a cup of water beforehand (condition: water). You think it would be nice to create a custom class that stores some information about a participant and their results. We will call this class `Participant`. In what follows, we will create the class step by step.
# 
# To create a custom class in Python, you use the keyword `class` followed by the name of your class, which is customarily capitalized:

# In[42]:


class Participant:
    pass


# Here, we leave the "body" of the class empty and just use the filler keyword `pass` (without `pass`, the cell would raise an error). 

# #### The `__init__` method
# The next step is to define the class *constructor*, which is a method which outlines what needs to happen upon initialization. To create a method, you just need to define a function inside the class. Functions in Python are defined using the keyword `def`, followed by the name of the function, its (optional) arguments, and the function body (we will discuss functions in detail in the next notebook). The name of the constructor method is `__init__` (short for "initialize") and takes at least one argument, which is customarily named `self` (which we'll explain in a bit):

# In[43]:


class Participant:
    """ Usually, right underneath the class name, some documentation about the class is added
    across a multiline string using triple quotes. For example, we might add 'A class to represent
    participants in our study'. """
    def __init__(self):
        pass


# Note that any code within the class definition is indented with four spaces (or a single tab; both are okay)! This tells Python which code belongs (and doesn't belong) to the class definition. Right now, the `__init__` method doesn't do anything, but it does allow us to create an object with the class `Participant` by calling `Participant()` (note the round brackets):

# In[44]:


participant_1 = Participant()


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Let's make the <tt>__init__</tt> method actually do something! In the class definition below, add a print statement within the <tt>__init__</tt> function which prints out "Constructing a Participant object!". Make sure to add another indent (four spaces or a tab) for your print statement (just like the <tt>pass</tt> keyword in the <tt>__init__</tt> method above).
# </div>

# In[45]:


""" Implement your ToDo here. """

class Participant:
    """ Usually, right underneath the class name, some documentation about the class is added
    across a multiline string using triple quotes. For example, we might add 'A class to represent
    participants in our study'. """
    def __init__(self):
        ### BEGIN SOLUTION
        print("Constructing a Participant object!")
        ### END SOLUTION


# In[46]:


""" Tests the above ToDo. """
import inspect
testp = Participant()
if not any('print(' in l for l in inspect.getsourcelines(testp.__init__)[0]):
    raise ValueError("Could not find a print statement in the __init__ method!")
else:
    print("Awesome! You're doing great.")


# As you can see in the test cell, whenver a `Participant` object is initialized, the `__init__` method is triggered (under the hood)! You can do anything you like in the `__init__` method, but usually this method is used to "bind" attributes to it**self**, such as arguments given to the `__init__` method. For example, let's add a single argument (in addition to `self`) to the constructor, a subject number (an integer):

# In[47]:


""" Implement your ToDo here. """

class Participant:
    """ A class to represent participants in our study. """
    def __init__(self, sub_nr):
        self.sub_nr = sub_nr


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Below, initialize a new <tt>Participant</tt> object with a particular participant number (e.g., `1`). Then, try to access that attribute (<tt>sub_nr</tt>) from your new object! What happens if you don't supply a participant number when calling <tt>Participant</tt>?
# </div>

# In[48]:


""" Implement your ToDo here (no test cell). """
### BEGIN SOLUTION
participant_x = Participant(1)
print(participant_x.sub_nr)
### END SOLUTION


# As you can see, whenever you construct a new `Participant` object (and thus implicitly call the `__init__` method) the `self` argument is actually ignored. The `self` argument in classes function as a sort of placeholder (or template) in the class that will be "filled in" by the specific object once it is initialized. In other words, anything that is referenced by `self` in the *class definition* is referenced by the object name after initialization. This concept will become more clear when we'll discuss other class methods later.
# 
# 

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Below, rewrite the <tt>__init__</tt> method to accept (apart from <tt>self</tt>) two arguments: <tt>sub_nr</tt> <em>and</em> <tt>condition</tt>, a string (which should be either a "caffeine" or "water"). Then, make sure the value of the <tt>condition</tt> argument is bound to <tt>self</tt> such that the object will have a <tt>condition</tt> attribute. Bonus for those with more programming experience: raise a <tt>ValueError</tt> whenever the condition is something else than "caffeine" and "water".
# </div>

# In[49]:


""" Implement your ToDo here. """
class Participant:
    """ A class to represent participants in our study. """
    ### BEGIN SOLUTION
    def __init__(self, sub_nr, condition):
        self.sub_nr = sub_nr
        self.condition = condition
        
        if self.condition not in ['caffeine', 'water']:
            raise ValueError("Please choose 'condition' from ['caffeine', 'water']!")
    ### END SOLUTION


# In[50]:


""" Tests the above ToDo. """
try:
    testp = Participant(1, 'water')
except Exception as e:
    print("Something went wrong during initialization ... Is your syntax correct?")
    raise(e)
else:
    if not hasattr(testp, 'condition'):
        raise ValueError("Your class does not have an attribute called 'condition'!")
    else:
        print("Yeah! Well done!")


# In[51]:


""" Tests bonus part. If you haven't done this, you may ignore this. """
try:
    testp = Participant(1, 'tea')
except ValueError:
    # Yes! It's raising an error, great!
    print("Well done!")
else:
    raise ValueError("It should raise an error, but it isn't doing so ... ")


# #### Other methods
# The `__init__` method is almost always included in custom Python classes. But you can of course add more custom methods (like the `introduce` method in the previously discussed `Person` class)! For example, suppose that you want to know whether the participant number is larger than 10. I know, not a very realistic use case, but we'll keep it simple. Just like the `__init__` method, you can add a method by defining a function inside the class definition:

# In[52]:


class Participant:
    """ A class to represent participants in our study. """
    def __init__(self, sub_nr, condition):
        self.sub_nr = sub_nr
        self.condition = condition
    
    def larger_than_10(self):
        """ Checks if sub_nr is larger than 10. """
        if self.sub_nr > 10:
            ans = 'yes'
        else:
            ans = 'no'

        return ans


# As you can see, like the `__init__` method, the `larger_than_10` method also takes `self` as input. This way, the object can access attributes of it**self**. This happens in the `larger_than_10` method when it accesses the `sub_nr` attribute through `self.sub_nr`! Without `self` as the first argument, this would not have been possible. Let's check out whether it works:

# In[53]:


participant_15 = Participant(15, 'water')
answer = participant_15.larger_than_10()
print(answer)


# One last thing that is important to know is that you can also create attributes outside the `__init__` method! For example, we could store the result of the `larger_than_10` call as an attribute by "binding" it to `self` inside the method: 

# In[54]:


class Participant:
    """ A class to represent participants in our study. """
    def __init__(self, sub_nr, condition):
        self.sub_nr = sub_nr
        self.condition = condition
        self.ltt = None  # to be filled in later
    
    def larger_than_10(self):
        """ Checks if sub_nr is larger than 10. """
        if self.sub_nr > 10:
            ans = 'yes'
        else:
            ans = 'no'
        
        # Here, we bind `ans` to `self`! Note that we can call the attribute
        # whatever we want! Here, we use `ltt` (Larger Than Ten)
        self.ltt = ans
        
        return ans


# Note that, if you expect attributes to be created after initialization (i.e., outside the `__init__` method), it is good practice to pre-set this attribute to `None` inside the `__init__` function (as we did above as well). Now, let's see whether it works as expected:

# In[55]:


participant_x = Participant(10, 'caffeine')

# After initialization, `ltt` is still None
print(participant_x.ltt)

# But after calling `larger_than_10`, it is correctly set!
participant_x.larger_than_10()
print(participant_x.ltt)


# Now, let's try a slightly harder ToDo!

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Create a new method, <tt>add_data</tt>, that takes as a list of numbers as a single (apart from <tt>self</tt>) input argument named <tt>data</tt> and checks whether its length is larger than 4. You can use the built-in function <tt>len</tt> for this. If the list of numbers is larger than 4, add it as an attribute named <tt>data</tt>. If it isn't, do not add it as an attribute. Make sure to pre-set the <tt>data</tt> attribute! 
# </div>

# In[56]:


""" Implement your ToDo here. """
class Participant:
    """ A class to represent participants in our study. """
    
    def __init__(self, sub_nr, condition):
        ### BEGIN SOLUTION
        self.sub_nr = sub_nr
        self.condition = condition
        self.data = None
        
    def add_data(self, data):

        if len(data) > 4:
            self.data = data
    ### END SOLUTION


# In[57]:


""" Tests the ToDo above. """
testp = Participant(1, 'water')
if not hasattr(testp, 'data'):
    raise ValueError("It looks like you didn't pre-set the data attribute!")
else:
    if testp.data is not None:
        raise ValueError("Make sure to pre-set the data attribute with None!")
    
testp.add_data([1, 2, 3])
if testp.data is not None:
    raise ValueError("The data attribute should not be updated when the length of the list is smaller than 5!")

testp.add_data([1, 2, 3, 4, 5, 6])
if testp.data is None:
    raise ValueError("The data attribute has not been updated ...")

print("EPIC! This wasn't easy, but everything works as expected!")


# Okay then, let's finish with an even harder ToDo for those that already have some experience with Python. Its solution features quite some more advanced concepts that will be discussed in the upcoming notebooks, so no worries if you can't figure this out!

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Modify the <tt>add_data</tt> method such that it <em>only</em> stores data when the input is a list of exactly 10 numbers. Whenever the data (of length 10) is added for the first time, store it as an attribute with the name <tt>data</tt> as before. However, whenever the <tt>add_data</tt> method is called when the <tt>data</tt> attribute already contains a list of 10 numbers, add the 10 new numbers to the corresponding existing numbers: the first number from the new list should be added to the first number from the existing list in the <tt>data</tt> attribute, etc. etc. Also, add a new method called <tt>average_data</tt> that computes the average of each number in the <tt>data</tt> attribute and stores this list of numbers in a new attribute called <tt>current_average</tt>.
# <br><br>
# A couple of hints:
# <ul>
#     <li>Make sure to pre-set all attributes upon initialization!</li>
#     <li>Do not cheat by using external packages such as Numpy ;-) </li>
# </ul>
# </div>

# In[58]:


""" Implement your ToDo here. """
class Participant:
    """ A class to represent participants in our study. """

    ### BEGIN SOLUTION
    def __init__(self, sub_nr, condition):
        self.sub_nr = sub_nr
        self.condition = condition
        self.data = None
        self.current_average = None
        self.counter = 0
        
    def add_data(self, data):

        if len(data) == 10:
            if self.data is None:
                self.data = copy(data)
            else:
                i = 0
                for d in data:
                    self.data[i] += d
                    i += 1

            self.counter += 1

    def average_data(self):
        """ Note: this implementation is not completely correct! Because it won't
        average the numbers correctly whenever this method is called for more than once!
        Technically, a running average should be used. """
        self.current_average = []
        i = 0
        for d in self.data:
            av = d / self.counter
            self.current_average.append(av)
    ### END SOLUTION


# In[59]:


""" Tests the above ToDo (part 1). """
from copy import copy

testp = Participant(1, 'water')
testp.add_data([1, 2, 3])  # should not add it because != length 10
if testp.data is not None:
    raise ValueError("It should only store data with the list contains exactly 10 numbers!")

inp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testp.add_data(copy(inp1))
if not isinstance(getattr(testp, 'data'), list):
    raise ValueError("Hmm, the data was not stored although it was exactly of length 10!")
    
# Let's add some numbers
inp2 = [2, 1, 5, 8, 9, 10, 3, 3, 1, 2]
testp.add_data(inp2)
for i, (x, y) in enumerate(zip(inp1, inp2)):
    if (x + y) != testp.data[i]:
        raise ValueError("Hmm, the number in position {i+1} is not added correctly ...")
        
print("YES! Well done so far! Let's see how the next test cell goes ...")


# In[60]:


""" Tests the above ToDo (part 2). """
testp = Participant(1, 'water')
testp.add_data(inp1)
testp.add_data(inp2)
testp.average_data()

av = [(i1 + i2) / 2 for i1, i2 in zip(inp1, inp2)]
if all(testp.current_average[i] == av[i] for i in range(10)):
    print("OMG. You're amazing!")


# If you're done with this notebook, please continue with the next one, `1_python_basics.ipynb` (but treat yourself to a nice cup of tea or coffee, first &mdash; you deserved it).
