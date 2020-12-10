#!/usr/bin/env python
# coding: utf-8

# # Python basics
# This notebook will provide short tutorial on basic Python concepts and syntax. We will go over the Python package system and imports, data types, functions, conditionals, and loops.
# 
# ## Contents
# 1. The Python ecosystem, imports, and whitespace
# 2. Basic data types
# 3. Functions and methods
# 4. Conditionals
# 5. Loops
# 
# **Estimated time to complete**: 2-4 hours

# ## The Python ecosystem
# Python is a multipurpose programming language, meaning it can be used for almost anything. While the "standard library" of Python (i.e., the functionality that is shipped with any Python installation) contains the bare minimum for any programming language, Python's versatility comes from a massive community of developers that created many different "third-party" packages for almost any purpose you can think of (e.g., visualization, machine learning, game programming, etc.).
# 
# For example:
# * the [scipy](https://www.scipy.org/) package provides functionality for scientific computing (e.g. statistics, signal processing);
# * the [numpy](http://www.numpy.org/) package provides data structures and functionality for (very fast) numeric computing (e.g. multidimensional numeric array computations, some linear algebra);
# * the [pandas](https://pandas.pydata.org/) package provides functionality to work with "tables";
# * the [matplotlib](http://matplotlib.org/) package provides plotting functions;
# * and various specialied neuroimaging packages provide functionality to work and analyze (f)MRI (e.g. [nibabel](http://nipy.org/nibabel/) and [nipype](http://nipy.org/nipype)) and MEG/EEG (e.g. [MNE](http://www.martinos.org/mne/stable/index.html)).
# 
# Basically, there are packages for everything you can think of! In this course, we will mostly use basic Python in combination with the scientific computing packages (*pandas*, *numpy*, and *matplotlib*).

# ## Import statements
# As explained above, Python ships with some default functionality. This means that it's already available upon starting a notebook (or any other Python environment) and doesn't need to be imported. An example is the function `len()`.

# In[1]:


my_list = [1, 2, 3]
print(len(my_list))


# However, non-built-in packages &mdash; such as `numpy` &mdash; need to be explicitly imported to access their functionality. After importing, their functions are accessible as: `{package}.{function}`.
# 
# For example:

# In[2]:


import numpy

# Now you can access the numpy function `add()` as numpy.add()
print(numpy.add(5, 3)) 


# However, writing `numpy` in front of every function you access from it becomes annoying very quickly. Therefore, we usually abbreviate the package name by two or three characters, which can be achieved through:
# 
# ```
# import {package} as {abbreviation}
# ```
# 
# For example, people usually abbreviate the numpy import as follows:

# In[3]:


import numpy as np

# Now you can access numpy functions such as 'add()' as:
print(np.add(5, 3))


# Often (but not always), Python packages consist of subpackages. These subpackages are often used to group similar functions/code together. For example, the `numpy` package has the subpackage (also called "module") `random`, which contains functions that allow you to generate random data from different distributions.
# 
# In the previous cell, we imported the *entire* `numpy` package by running `import numpy as np`. However, sometimes you might only need a particular subpackage ("module"), like the subpackage `random` from `numpy`. To import *only* the `random` subpackage, you can do the following:

# In[4]:


import numpy.random


# Now, you can use functions from the `numpy.random` class! Technically, even subpackages may contain their own subpackages. Importing subpackages from subpackages works the same way:
# 
# ```python
# import mainpackage.somesubpackage.anothersubpackage.yetanothersubpackage
# ```

# Throughout the tutorials, you'll see different packages (e.g. `nibabel` and `scipy`) being imported using abbreviations (e.g., `import nibabel as nib`). 
# 
# Also, you don't need to import an *entire* package, but you can also import a specific function or class. This is done as follows:
# 
# ```python
# from {package} import {function1}, {function2}, {etc}
# ```
# 
# An example:

# In[5]:


from numpy import add, subtract

# Now I can simply call add() and subtract()
print(add(5, 3))


# Note that some packages have a hierarchical structure with subpackages (also called modules). For example, scipy has a subpackage `ndimage` (with functions for n-dimensional arrays). To import *only* this subpackage, do the following:

# In[6]:


from scipy import ndimage
# Now you can call functions from the ndimage subpackage,
# e.g. gaussian_filter

print(ndimage.gaussian_filter([10, 5, 4], 2))


# Note that you can mix and match all of these operations to customize the import to your own liking (see cell below for such a fancy import). In this course, we'll usually just import entire packages (e.g. `import numpy as np`) or specific functions/subpackages (e.g. `from scipy import stats`). 
# 
# Another thing you can do with imports is renaming the function/module you're importing. This follows the following syntax:
# 
# ```python
# from {package} import {some function/module} as {new name}
# ```
# 
# See the cell below for an example:

# In[7]:


# a fancy import
from scipy.stats import binom_test as omg_binomial_testing_so_cool

print(omg_binomial_testing_so_cool(0.5, 10))


# <div class="alert alert-warning">
#     <b>ToDo</b>: Import the function <tt>randn</tt> (which generates random numbers from a standard normal distribution) from the numpy subpackage <tt>random</tt> and rename it <tt>random_normal_generator</tt>.
# </div>

# In[8]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
from numpy.random import randn as random_normal_generator
### END SOLUTION


# In[9]:


""" Tests the above ToDo. """
try:
    assert('random_normal_generator' in dir())
except AssertionError as e:
    print("I couldn't find the function 'random_normal_generator'; did you spell it correctly?")
    raise(e)
else:
    print("Great! Well done!")


# In[10]:


""" Another test for the above ToDo. """
try:
    assert(random_normal_generator.__name__ == 'randn')
except AssertionError as e:
    print("Your 'random_normal_generator' function does not point to the 'randn' numpy.random subpackage!")
    raise(e)
else:
    print("Correct!")


# <div class="alert alert-success">
# <b>Wildcard imports.</b> Python allows also "wildcard" imports, like: <tt>from numpy import *</tt>, which says: import <em>everything</em> from the <tt>numpy</tt> package. This is often discouraged, because the beauty of having explicit imports (unlike MATLAB) is that you known where your functions come from (e.g., is it a base Python function or a numpy function?). 
# </div>

# ## Whitespace for indentation
# In most programming languages, code blocks (e.g., if-else blocks, or for-loops) are delineated by dedicated symbols (often curly brackets, `{}`). For example, an if-else block in R may be written like this:
# 
# ```R
# if (x > 0) {
#    y = x + 5
# } else {
#    y = x - 5
# }
# ```
# 
# While in languages like R and MATLAB whitespace/indentation is used for readability, it is not necessary! The above if-else statement in R can also be written as:
# 
# ```R
# if (x > 0) { y = x + 5 } else { y = x - 5 }
# ```
# 
# However, in Python, whitespace and indentation is important! In Python, indendation &mdash; instead of curly braces &mdash; delineates code blocks, and if code is incorrectly indented, Python will give an error! Identation can be done using spaces or tabs; both are fine ([but programmers often have a very strong opinion on using on or the other](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go)), as long as it is consistent. Most style guides recommend either four spaces or a single tab.
# 
# Importantly, if a code block (e.g., an if-else statement) in Python is indented incorrectly, Python will throw an `IdentationError`, as show below:

# In[11]:


x = 0
if x < 0:
y = x + 5
else:
y = x - 5


# <div class="alert alert-warning">
# <b>ToDo</b>: Fix the code block above by identing it correctly. (No test cell.)
# </div>

# ## Basic data types
# Base (i.e., built-in) Python has mostly the same data types as you might know from MATLAB or R, such as numbers (integers/floats), strings, and lists (cells in MATLAB; lists in R). Also, Python has to data types that might be unknown to MATLAB/R users, such as "dictionaries" and "tuples", which are explained later. 

# ### Numbers
# Numbers are represented either as integers ("whole" numbers) or floats (numbers with decimals, basically).

# In[12]:


x = 3
print('x is of type', type(x))  # use type(variable) to find out of what data-type something is!

y = 3.1415
print('y is of type', type(y))


# Let's try to apply arithmetic to x as defined above with some basic operations:

# In[13]:


print(x + 1)   # Addition;
print(x - 1)   # Subtraction;
print(x / 2)   # Division;
print(x * 2)   # Multiplication;
print(x ** 2)  # Exponentiation;


# The above commands apply operations to x, but do not *change* x itself. To permanently change x, you have to store the results of the operation (e.g. `x + 1`) into a variable (e.g. `x2 = x + 1`), as shown in the cell below:

# In[14]:


x = 3
x_new = x + 2

# If you simply want to update an existing variable, you can do this in two ways:
x = x + 1

# ... or:
x += 1

print(x)  

x *= 2 # This is the same as: x = x * 2
print(x) 


# <div class="alert alert-warning">
#     <b>ToDo</b>: In the cell below, make a new variable, <tt>y</tt>, which should contain <tt>x</tt> minus 5, of which the result is subsequently raised to the 4th power. 
# </div>

# In[15]:


""" Implement the ToDo here. """
x = 8
### BEGIN SOLUTION
y = (x - 5) ** 4
### END SOLUTION


# In[16]:


''' Tests the above ToDo.'''

# Check if there exists a variable 'y'
try:
    assert('y' in dir())
except AssertionError as e:
    print("The variable 'y' doesn't seem to exist! Did you name it correctly?")
    raise(e)
else:
    print("Well done! 1 out of tests 2 passed")

# Check if it has the correct number
try:
    assert(y == 81)
except AssertionError as e:
    print("The variable y does not seem to equal x minus 5, raised to the power 4.")
    raise(e)
else:
    print("Well done! 2 out of tests 2 passed")


# <div class='alert alert-success'>
#     <b>Tip!</b>
#     When you're working on your ToDo, it's often informative to print (intermediate) output/variables of your solution (in a new code cell for example). This might give insight into (potentially) failing tests! 
# </div>

# ### Booleans
# Python implements all of the usual operators for comparisons. Similar to what you might know from other languages, `==` tests equivalence, `!=` for not equivalent, and `<` and `>` for larger/smaller than. The result of those comparisons are a datatype called a "boolean", representing truth values. Booleans can take on the value `True` or `False`.
# 
# Check out some examples below:

# In[17]:


a = 3
b = 5
is_a_equal_to_b = (a == b)

print(is_a_equal_to_b)
print('the ouput is of type', type(is_a_equal_to_b)) 


# Some more examples of Boolean operators:

# In[18]:


bool_1 = 3 > 5 # False, because 3 is not greater than 5
bool_2 = (5 == 5) # True, because, well, 5 is 5
print(bool_1)
print(bool_2)


# However, for some Boolean logic, python doesn't use operators (such as && for "and" and | for "or") but uses special (regular English) *words*: 

# In[19]:


# note: bool_1 is False, bool_2 is True
print(bool_1 and bool_2)  # Logical AND, both have to be True
print(bool_1 or bool_2)   # Logical OR, either one of them has to be True
print(not bool_1)         # Logical NOT, the inverse of bool_1
print(bool_1 != bool_2)   # Logical XOR, yields True when bool_1 and bool_2 are not equal


# (Although, technically, the keyword `and` and `&`, and `or` and `|` can be used interchangeably.)

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Mess around with booleans in the cell below. Try some more complex things, like: <tt>not ((3 > 5) and not (5 > 2))</tt>. Do you understand why the result is the way it is? Try to follow the logic in the sequence of statements (no test cell).
# </div>

# In[20]:


# Do your ToDo here:


# ### Strings
# Strings in Python are largely the same as in other languages.

# In[21]:


h = 'hello'   # String literals can use single quotes
w = "world"   # or double quotes; it does not matter.

print(h)
print(len(h))  # see how many characters in this string


# A very nice feature of Python strings is that they are easy to concatenate: just use '+'!

# In[22]:


hw = h + ', ' + w + '!' # String concatenation
print(hw)


# You can also create and combine strings with what is called 'string formatting'. This is accomplished by inserting a placeholder in a string, that you can fill with variables. Confusingly, there are many approaches to string formatting. Arguably, the most used one is the "old style" string formatting, of which an example is given below:

# In[23]:


# Here, we have a string with a placeholder '%s' (the 's' refers to 'string' placeholder)
my_string = 'My favorite programming language is: %s'
print('Before formatting:')
print(my_string)

# Now, to 'fill' the placeholder, do the following:
my_fav_language = 'Python'
my_string = 'My favorite programming language is: %s' % my_fav_language

print('\nAfter formatting:')
print(my_string)


# You can also use specific placeholders for different data types:

# In[24]:


week_no = 1  # integer
string1 = 'This is week %i of the Python mini course' % week_no # the %i expects an integer!
print(string1)

score = 99.50 # float
string2 = 'I will get a %f on my quiz this week!' % score
print(string2)

# You can also combine different types in a string:
string3 = 'In week %i of the course, %s will get a %f (or higher) on my quiz!' % (week_no, "I", 95.00)
print(string3)


# <div class='alert alert-warning'>
# <b>ToDo</b>: Modify the variable <tt>to_print</tt> defined below, such that printing it (i.e., running <tt>print(to_print)</tt>) will print: "I love Python 4ever". So you'll have to "fill" the "%" placeholders using string formatting. That is, you have to put a <tt>%</tt> sign after the <tt>to_print</tt> variable and "fill" it with the correct inputs.
# </div>

# In[25]:


""" Implement the ToDo here. """
to_print = "I love %s %iever"

### BEGIN SOLUTION
to_print = "I love %s %iever" % ('Python', 4)
print(to_print)
### END SOLUTION


# In[26]:


""" Tests the above ToDo. """
try:
    assert(to_print == 'I love Python 4ever')
except AssertionError as e:
    print("This string is not formatted correctly!")
    raise(e)
else:
    print("Well done!")


# As mentioned, there are several different approaches to string formatting. We particularly like the "string interpolation" (F-string) approach, in which you can directly "insert" variables into strings:
#     
# ```python
# year = 2020
# string = f"At the time of writing, we're living in the year {year}"
# ```
#     
# To use this method, you have to preprend your string with the letter <tt>f</tt>!

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Using the variables below and the F-string method, create the following string (and print it): "There are five notebooks this week; OMG, way too many."
# </div>

# In[27]:


""" Implement the ToDo here. (no test cell)"""
n_notebooks = 5
oh_my_god = "OMG"
many_or_few = "many"

### BEGIN SOLUTION
print(f"There are {n_notebooks} notebooks this week; {oh_my_god}, way too {many_or_few}.")
### END SOLUTION


# ### Lists
# A list is the Python equivalent of an "array", but can be resized and can contain elements of different types. It is similar to a list in R and a cell in MATLAB. Note that indices in python start with 0! This means that the 3rd element of the list below is accessed through `[2]`.
# 
# Let's check out some lists and how to index them!

# In[28]:


# Note that list may contain numbers ...
list1 = [3, 1, 2]

# ... or strings
list2 = ['hello', 'world']

# ... or, actually, anything at all! List lists themselves
list3 = ['hello', [3, 1, 2], 'world', 5.3, -999]


# Whatever the contents of a list, they are indexed the same way: using square brackets with an integer, e.g. `[0]`:

# In[29]:


print('The first element of list1 is: %i' % list1[0])
print('The second element of list2 is: %s' % list2[1])
print('The last element of list3 is: %i' % list3[-1])
print('The second-to-last element of list3 is: %f' % list3[-2])


# Note that you can also use negative indices! Negative indices start indexing from the end of the list, so `[-1]` indexes the last element, `[-2]` indexes the second-to-last element, etc.
# 
# We cannot only 'extract' element from lists using indexing, but we can also replace them! This works as follows:

# In[30]:


some_list = [1, 2, 3, ['A', 'B', 'C']]

# Let's set the first element of some_list to 100:
some_list[0] = 100
print(some_list)

# Note that indexing a list within a list is done with sequential square brackets,
# so if we want to index the element 'A' in some_list, we do:
some_list[-1][0] = 'ANOTHER STRING'
print(some_list)


# <div class='alert alert-warning'>
# <b>ToDo</b>: In the cell below, replace the element 'TO_REPLACE_1' with 'REPLACED' and the element 'TO_REPLACE_2' also with 'REPLACED' in the list <tt>todo_list</tt>.
# </div>

# In[31]:


""" Implement your ToDo here. """
todo_list = [1, 'B', 'TO_REPLACE_1', [5, 3, 1038, 'C'], [1, 3, 5, [9, 3, 1, 'TO_REPLACE_2']]]
### BEGIN SOLUTION
todo_list[2] = 'REPLACED'
todo_list[-1][-1][-1] = 'REPLACED'
### END SOLUTION


# *Note*: the code-cell below as usual tests your ToDo, but we haven't written out the tests in the cell itself. Instead, we wrote the tests in a separate Python module, which we import here. (We do this, because writing out the tests here would give you the answer rightaway!)

# In[32]:


""" Tests the above ToDo with a custom function. """
from tests import test_list_indexing
test_list_indexing(todo_list)


# In addition to accessing list elements one at a time, Python provides concise syntax to access specific parts of a list (sublists); this is known as *slicing*. 
# 
# Let's look at some slice operations:

# In[33]:


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)         # Our original list


# In[34]:


# Get a slice form index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:4])


# In[35]:


# Get a slice from index 2 to the end; prints "[2, 3, 4, 5, 6, 7, 8, 9]"
print(nums[2:])  


# In[36]:


# Get a slice from the start to index 3 (exclusive); prints "[0, 1, 2]"
print(nums[:3])     


# In[37]:


# Slice indices can be negative; prints ["0, 1, 2, 3, 4, 5, 6, 7, 8]",
# so everything up to (but not including) the last element
print(nums[:-1])    


# Importantly, slices are "end exclusive", which means that if you slice from `0` to `5`, you get the indices `0, 1, 2, 3, 4`! While this may seem confusing at first, you'll get used to it. To appreciate the use of "end exclusive indexing", do the next ToDo.

# <div class='alert alert-warning'>
# <b>ToDo</b>: Slice the list below, <tt>to_be_split</tt>, into two separate lists: one called <tt>first_half</tt> with the first half of the list values, and one called <tt>second_half</tt>, with the second half of the list values.
# </div>

# In[38]:


""" Implement your ToDo here. """
to_be_split = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
### BEGIN SOLUTION
mid = len(to_be_split) // 2
first_half = to_be_split[:mid]
second_half = to_be_split[mid:]
# or just:
# to_be_split[:8]
# to_be_split[8:]
### END SOLUTION


# In[39]:


""" Tests the above ToDo. """
assert(first_half == [10, 11, 12, 13, 14, 15, 16, 17])
assert(second_half == [18, 19, 20, 21, 22, 23, 24, 25])
print("Well done!")


# Apart from the syntax `[from:to]`, you can also specify a "stride" (sort of step-size) of your slice using the syntax `[from:to:stride]`:

# In[40]:


# Return values in steps of 2
print(nums[::2])    

# Returns values in steps of 3, but starting from the second element
print(nums[1::3])   


# With 'normal' indexing of lists, you can only index a subsequently set/replace one element at the time. With slices, however, you can set multiple elements at the same time:

# In[41]:


nums[2:4] = [100, 200] # Assign a new sublist to a slice
print(nums)         # Prints "[0, 1, 100, 200, 4, 5, 6, 7, 8, 9]"


# **Pro-tip**: instead of creating sequential lists like this:
# 
# ```python
# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ```
# 
# ... we can also create a list using the syntax: 
# 
# ```python
# num = list(range(starting_point, exclusive_end_point))
# ```
# 
# For example, to create a list from 5 to 15, you can do the following:
# 
# ```python
# num = list(range(5, 16))
# ```
# 
# We'll use this construction (`list(range(x, y))`, or without the `list`) quite often in this course!

# <div class='alert alert-warning'>
#     <b>ToDo</b>: From the list (<tt>my_list</tt>) below, extract the numbers 2, 3, 4, 5, and 6 using a slice and store it in a new variable named <tt>my_new_list</tt>!
# </div>

# In[42]:


""" Implement the ToDo here. """
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
### BEGIN SOLUTION
my_new_list = my_list[1:6]
### END SOLUTION


# In[43]:


from tests import test_slicing_1
available_vars = dir()
if 'my_new_list' not in available_vars:
    raise ValueError("You did not store the results in a new variable called 'my_new_list'!")
    
test_slicing_1(my_new_list)


# <div class='alert alert-warning'>
#     <b>ToDo</b>: From the list below (<tt>my_list_2</tt>), extract the values <tt>[5, 7, 9, 11]</tt> using a slice (i.e., in a single operation!) and store it in a new variable named <tt>my_new_list_2</tt>.
# </div>

# In[44]:


""" Implement the ToDo here. """
my_list_2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
### BEGIN SOLUTION
my_new_list_2 = my_list_2[2:6]
### END SOLUTION


# In[45]:


''' Tests the above ToDo '''
from tests import test_slicing_2
available_vars = dir()

if 'my_new_list_2' not in available_vars:
    raise ValueError("You didn't define the variable 'my_new_list_2'!")

test_slicing_2(my_new_list_2)


# *Note*: you can index *strings* the same way as you index lists! Try to see it this way: a string is, quite literally, a *string* ("list") of characters. So, to get the first letter of some string s (e.g, 'this is a string'), you simply write: `s[0]`. To get first 5 characters, you write `s[:5]`, etc etc. Remember this!

# In[46]:


# Check out string slicing/indexing below
s = 'python programming'
print(s[0:9:2])


# ### Dictionaries
# Dictionaries might be new for those who are used to MATLAB or R. Basically, a dictionary is an *unordered* list in which list entries have a name (which is also referred to as a "key"). To get a value from a dictionary, you have to use the "key" as index instead of using an integer (although, strictly speaking, keys can also be integers ... but that's not important for now).
# 
# Let's check out such a dictionary and how to index it. We build a dictionary using the following syntax: 
# 
# ```python
# {some_key: value, another_key: another_value, etc: etc}`
# ```
# 
# The keys can be anything! Strings, integers, lists ... doesn't matter! Mostly, though, strings are used as keys. So, let's look at an example:

# In[47]:


my_dict = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data


# To index a dictionary, we'll use square brackets `[]` again, just like with lists. But now, we can index using the key!

# In[48]:


indexed_value = my_dict['cat']
print(indexed_value)


# Adding new key-value pairs to dictionaries is easy! Just index it with a new key, and assign the value to it:

# In[49]:


my_dict['fish'] = 'wet'     # Set an entry in a dictionary
print(my_dict['fish'])      # Prints "wet"


# Like a list, an entry in a dictionary can be of any data type:

# In[50]:


my_dict['rabbit'] = ['omg', 'so', 'cute']
print(my_dict['rabbit'])


# If you try to 'index' a dictionary with a key that doesn't exist, it raises a "KeyError", which means you're trying to index something that doesn't exist:

# In[51]:


print(my_dict['monkey'])


# <div class='alert alert-warning'>
#     <b>ToDo</b>: In the code cell below, add a new key to the dictionary <tt>my_dict</tt> named <tt>"rat"</tt> and with the value <tt>"nasty"</tt>.
# </div>

# In[52]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
my_dict['rat'] = 'nasty'
### END SOLUTION


# In[53]:


""" Tests the above ToDo. """
try:
    assert('rat' in my_dict)
except AssertionError as e:
    print("There exists no key 'rat' in my_dict!")
    raise(e)

try:
    assert(my_dict['rat'] == 'nasty')
except AssertionError as e:
    print("The value of key 'rat' is '%s' and NOT 'nasty'" % my_dict['rat'])

print('Well done!')


# <div class='alert alert-warning'>
# <b>ToDo</b>: Values of dictionaries can be any type of object, even dictionaries themselves! So, add a new key to the dictionary <tt>my_dict</tt> named <tt>"another_dict"</tt> with the value of <em>another</em> dictionary with the keys <tt>"a"</tt> and <tt>"b"</tt> and the corresponding values <tt>1</tt> and <tt>2</tt>. Also, try to figure out how to index the value <tt>1</tt> from the 'nested' dictionary (this is not graded, but try it nonetheless!).
# </div>

# In[54]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
my_dict['another_dict'] = {'a': 1, 'b': 2}
### END SOLUTION


# In[55]:


""" Tests the above ToDo. """
try:
    assert('another_dict' in my_dict)
except AssertionError as e:
    print("There exists no key 'another_dict' in my_dict!")
    raise(e)

try:
    assert(my_dict['another_dict']['a'] == 1)
    assert(my_dict['another_dict']['b'] == 2)
except AssertionError as e:
    print("The key 'another_dictionary' should contain a dictionary with keys 'a' and 'b', corresponding"
          "to values 1 and 2, respectively.")
    raise(e)

print('Well done!')


# ### Tuples
# Tuples are very much like lists, but the main difference is that they are immutable. In other words, after creating them, they cannot be modified (their values cannot be replaced/altered):

# In[56]:


# A list can be modified ...
my_list = [1, 2, 3]
my_list[0] = 0
print(my_list)


# In[57]:


# ... but a tuple cannot (and will give an error!)
my_tuple = (1, 2, 3)
print(my_tuple[0]) # you can print parts of tuple ...
my_tuple[0] = 0   # but you cannot modify it!


# You probably won't use tuples a lot, but you might come across them when using and writing functions, as multiple outputs from functions are stored in tuples (see below; but more about that in the next section!).

# In[58]:


def my_epic_function(integer):
    """ Returns the input and the input times 2."""
    return integer, integer * 2

outputs = my_epic_function(10)
print(outputs)
print(type(outputs))


# ## Functions (and methods)
# Like any programming language, Python allows you to create your own custom functions. Writing your own functions is useful when, for example, you want to do a particular computation/task many times. Then, if you need to change the computation or task, you only have to change the function instead of manually editing your code every time you do the computation/task. If you're familiar with other programming languages, you'll see that the syntax of Python functions is quite similar to what you're used to.
# 
# A function definition in Python starts with the keyword `def`, followed by the function name and round brackets with the arguments to the function, and finally the contents of the function, like so (note the indentation with four spaces/tab!):
# 
# ```python
# def my_awesome_function(arg_1, arg_2):
#     print("Argument 1: %s" % arg_1)
#     print("Argument 2: %s" % arg_2)
# ```
# 
# This dummy-function above prints some stuff, but does not *return* something. Similar to R (but unlike MATLAB), you have to explicitly state what you want to *return* from the function by the `return` statement. 
# 
# So, suppose you have a function that adds 2 to any number. Let's define it as follows (you have to run the cell to let Python know you've defined this function):

# In[59]:


def add_2_to_a_number(some_number):
    new_number = some_number + 2


# Here, we omitted a `return` statement to return the value of `new_number`. This is a problem, because in Python (like most languages) you cannot 'peek' inside the function after using it! You can only access whatever is returned. 
# 
# So, in the function defined above, we cannot access the value of `new_number`, because we didn't return it (so it will give an error):

# In[60]:


# This will give an error!
add_2_to_a_number(5)
print(new_number)


# So, to access the *value* of `new_number` (that is, *not* `new_number` itself, but its associated value), we need to return it:

# In[61]:


def add_2_to_a_number_fixed(some_number):
    new_number = some_number + 2
    return new_number


# In[62]:


value_contained_in_new_number = add_2_to_a_number_fixed(5)
print("Results of function 'add_2_to_a_number' with argument '5': %i" % value_contained_in_new_number)


# Importantly, you can name the variable to which you assign the return value *anyway you like*. This doesn't have to be `new_number`! Like above, we named it `value_contained_in_new_number`, but it really doesn't matter.

# <div class='alert alert-warning'>
# <b>ToDo</b>: In the code cell below, we've started writing a function named <tt>extract_last_element</tt> that takes one input-argument &mdash; a list &mdash; and returns the last element of the list. Some parts of the function are missing, though, which you need to write! When you're done, run the test-cell below it to check if it's right! 
# </div>

# In[63]:


""" Implement the ToDo here. """
def extract_last_element(input_list):
    
    ### BEGIN SOLUTION
    last_element = input_list[-1]
    return last_element
    ### END SOLUTION


# In[64]:


try:
    assert(extract_last_element(input_list=[0, 1, 2]) == 2)
except AssertionError as e:
    print("Your function fails for input [0, 1, 2]")
    raise(e)

try:
    assert(extract_last_element(input_list=[0]) == 0)
except AssertionError as e:
    print("Your function fails for input [0]")
    raise(e)

try:
    assert(extract_last_element(input_list=['string1', 'string2', 'string3']) == 'string3')
except AssertionError as e:
    print("Your function fails for input ['string1', 'string2', 'string3']")
    raise(e)

print("GREAT! All seems to be correct :-)")


# Alright, that was probably relatively easy. Let's do a slightly harder one.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Write a completely new function named <tt>get_values_from_odd_indices</tt> (so you have to write the <tt>def ...</tt> part!) that takes one input-argument &mdash; a list &mdash; and returns all values from the odd indices of that list. So, suppose you have the following list: [2, 100, 25, 48, 92, -5, 12]. Your function should return: [100, 48, -5]. That is, the values from odd indices (here: 1, 3, 5; we exclude index zero!) Hint: slices might be useful here!
# </div>

# In[65]:


""" Implement your function here. """
### BEGIN SOLUTION
def get_values_from_odd_indices(in_list):
    return in_list[1::2]
### END SOLUTION


# In[66]:


""" Tests the ToDo above. """
try:
    assert('get_values_from_odd_indices' in dir())
    assert(callable(get_values_from_odd_indices))
except AssertionError as e:
    print("Your function 'get_values_from_odd_indices' does not seem to exist!")

try:
    out = get_values_from_odd_indices([0, 1, 2])
    if out is None:
        msg = "ERROR: did you forget the Return statement?"
        raise ValueError(msg)
except ValueError as e:
    raise(e)
    
print("Well done (also run the next cell with tests)!")


# In[67]:


""" Some other tests for the ToDo above. """
inp = [0, 1, 2]
outp = get_values_from_odd_indices(inp)
ans = [1]
try:
    assert(outp == ans)
except AssertionError as e:
    print("Your function returned '%r' but I expected '%r'" % (outp, ans))
    raise(e)

inp = [5, 7, 9, 11, 13, 15, 18, 20, 21]
outp = get_values_from_odd_indices(inp)
ans = [7, 11, 15, 20]
try:
    assert(outp == ans)
except AssertionError as e:
    print("Your function returned '%r' but I expected '%r'" % (outp, ans))
    raise(e)

print("Well done!")


# **Important**: it is possible to return *multiple things* from a function. The function, then, returns these things as a tuple, which can subsequently be "unpacked". Let's check out an example using a custom function called `minmax_of_list` which returns both the minimum and maximum of a list:

# In[68]:


def minmax_of_list(some_list):
    ''' Returns both the minimum and maximum of a list.
    
    Parameters
    ----------
    some_list : list
        A list with numbers (int/float) only
    
    Returns
    -------
    min_value : a float or int
        The minimum of a list
    max_value : a float or int
        The maximum of a list
    '''
    min_value = min(some_list)
    max_value = max(some_list)
    
    return min_value, max_value


# As you can see, returning multiple things is a simple as adding more variables after the `return` statement, separated by commas. If we now call the function with a particular list, it gives us back a tuple of size 2 (one value for the minimum, one value for the maximum):

# In[69]:


output_from_function = minmax_of_list([0, 1, 2, 3])
print(output_from_function)
print(type(output_from_function))


# We can now "unpack" the tuple (i.e., extract the separate values) in several ways. One way is to simply index the values:

# In[70]:


output_from_function = minmax_of_list([0, 1, 2, 3])
minimum = output_from_function[0]
print("Minimum: %i" % minimum)

maximum = output_from_function[1]
print("Maximum: %i" % maximum)


# Alternatively, we can already "extract" one value, let's say the maximum (index 1 of the tuple) right after calling the function, so we can skip dealing with the tuple altogether:

# In[71]:


maximum = minmax_of_list([0, 1, 2, 3])[1]  # The [1] extracts the maximum from the output of the function immediately!
print("Maximum: %i" % maximum)


# Keep this feature of returning multiple things and tuple unpacking in mind for the rest of the course (you'll definitely encounter it more often!).

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Write a function called <tt>get_length_first_and_last_value</tt> which takes a list as single input argument, and returns the length of the list (the first output), the first value of the list (the second output), and the last value of the list (the third output). So, e.g., for the list <tt>[0, 1, 2, 3, 4]</tt>, the function should return <tt>(5, 0, 4)</tt> (a tuple of length 3, with the three outputs). Note that it should work for lists of arbitrary lengths and value types!
# </div>

# In[72]:


""" Implement the function here. """
### BEGIN SOLUTION
def get_length_first_and_last_value(lst):
    return len(lst), lst[0], lst[-1]
### END SOLUTION


# In[73]:


""" Tests the above ToDo. """
try:
    assert('get_length_first_and_last_value' in dir())
    assert(callable(get_length_first_and_last_value))
except AssertionError as e:
    print("Your function 'get_length_first_and_last_value' does not seem to exist!")

out = get_length_first_and_last_value([0, 1, 2])
if out is None:
    msg = "ERROR: did you forget the Return statement?"
    raise ValueError(msg)
    
if len(out) != 3:
    msg = "ERROR: you returned %i things; this should be 3!" % len(out)
    raise ValueError(msg)

assert(out == (3, 0, 2))
assert(get_length_first_and_last_value([2, 3, 4, 5, 6, 7]) == (6, 2, 7))
assert(get_length_first_and_last_value([0]) == (1, 0, 0))
assert(get_length_first_and_last_value(['a', 'b']) == (2, 'a', 'b'))

print("Well done!")


# ### Methods (again)
# However, in Python, functions are not the only things that allow you to 'do' things with data. As you've seen in the previous notebook, there are also methods! Different types of objects in Python, such as stings and lists, have their own set of methods. For example, the function you defined above (`extract_last_element()`) also exists as a method each list has, called `pop()`! (This is a builtin, standard, method that each list in Python has.) See for yourself in the block below.

# In[74]:


my_list = [0, 5, 10, 15] 
print(my_list.pop())

# You can also just do the following (i.e. no need to define a variable first!):
print([0, 5, 10, 15].pop())

# ... which is the same as:
print(extract_last_element([0, 5, 10, 15]))


# Not only lists, but also other data-types (such as strings, dictionaries, and, as we'll see later, numpy arrays) have their own methods.
# 
# We'll show you a couple of (often-used) examples of methods in built-in data types:

# In[75]:


# For lists, we have .append()
x = [0, 10, 15]
x.append(20) # Add a new element to the end of the list using the append() method!
print(x)


# Some often-used methods for dictionaries:

# In[76]:


my_dict = {'a': 0, 'b': 1, 'c': 2}

# The .values() method returns all the values of the dictionary 
print(list(my_dict.values()))

# And the .keys() method returns all the keys of the dictionary
print(list(my_dict.keys()))


# Some often-used methods for strings:

# In[77]:


my_string = 'Python is fun!'

# The .upper() method returns the string in uppercase!
print(my_string.upper())

# The .count(substring) method returns the number of times a substring occurs in a string
print(my_string.count('n'))

# The .replace(old, new) method replaces substrings
print(my_string.replace('fun', 'awesome'))

# The .split(separator) splits a string into subparts (returned as a list)
print(my_string.split(' '))  # split by whitespace


# ### Default arguments in functions/methods
# Importantly, and unlike most (scientific) programming languages, Python supports the use of 'default' arguments in functions. Basically, if you don't specify an optional argument, it uses the default:

# In[78]:


def exponentiate_number(number, power=2):
    return number ** power

print(exponentiate_number(2)) # now it uses the default!
print(exponentiate_number(2, 10)) # now it "overwrites" the default and uses power=10
print(exponentiate_number(number=2, power=10)) # also note that you can 'name' arguments 


# ## Conditionals (if-statements)
# Conditionals, or "if-statements", are quite straightforward. There are used in combination with booleans (`True` and `False` values) to run code conditionally. An example:
# An example:

# In[79]:


x = 5

if x > 0:
    print('x is larger than 0')
elif x < 0:
    print('x is smaller than 0')
else:
    print('x must be exactly 0!')


# If-statements contain at least an `if` keyword, but optionally also one or more `elif` ("else if") statements and an optional `else` statement. We'll practice this (in a `ToDo`) after the section on Loops.

# ## Loops
# Loops in Python (for- and while-loops) are largely similar to MATLAB and R loops, with some minor differences in  their syntax:

# In[80]:


animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)


# Basically, each data type that is also an "iterable" (something that you can iterate over) can be used in loops, including lists, dictionaries, and tuples.

# In[81]:


# An example of looping over a list
my_list = [1, 2, 3]
for x in my_list:
    print(x)


# MATLAB users might be used to looping over indices instead of the actual list values, like the following:
# 
# ```Matlab
# for i=1:100
#     disp(some_list(i));
# end
# ```
# 
# In Python, however, you loop (by default) over the contents of a list:
# 
# ```Python
# for entry in some_list:
#     print(entry)
# ```
#     
# If you want to access for the value *and* the index, you can use the built-in `enumerate` function:

# In[82]:


my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    
    print('Loop iteration number (index) = %i, value = %s' % (index, value))

# Don't forget that Python indexing starts at zero!


# Apart from lists, you can also loop over tuples:

# In[83]:


# Looping over a tuple (exactly the same as looping over a list)
my_tuple = (1, 2, 3)
for x in my_tuple:
    print(x)


# ... and dictionaries:

# In[84]:


# Iterating over a dictionary can be done in a couple of ways!
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Looping over the keys ONLY
for key in my_dict:
    print(key)


# In[85]:


# Looping over both the keys and the entries
for key, entry in my_dict.items():
    print(key, entry)


# <div class='alert alert-warning'>
# <b>ToDo</b>: Complete the function below &mdash; named `extract_values_smaller_than_0` &mdash; that takes a single list with numbers as input and returns a new list with <em>only the values smaller than 0</em> from the input-list. For example, suppose our input-list is: [2, -5.3, 1.8, 0.0, -205.1, 6029]. Then, the function should return: [-5.3, -205.1].<br><br>Hint: use an if-statement in combination with the <tt>.append()</tt> method of the empty list we initialized below (<tt>list_to_return</tt>) to fill the <tt>list_to_return</tt> variable in a for-loop. In other words, the function should contain an if-statement in a for-loop (in which you need to use the <tt>.append()</tt> method).
# </div>

# In[86]:


""" Implement the ToDo here. """
# Complete the function below (make sure to remove raise NotImplementedError!)
def extract_values_smaller_than_0(input_list):
    
    # We initialize an empty list here (which you need to fill using a for-loop)
    list_to_return = []
    
    ### BEGIN SOLUTION
    for value in input_list:
        
        if value < 0:
            list_to_return.append(value)
    ### END SOLUTION
    
    return list_to_return


# In[87]:


""" Tests the ToDo above. """
inp = [-5, 2, 3, -8]
outp = extract_values_smaller_than_0(inp)
ans = [-5, -8]
try:
    assert(outp == ans)
except AssertionError as e:
    print("Your function  with input '%r' returned '%r', but I expected '%r'" % (inp, outp, ans))
    raise(e)
    
inp = [0, 2, -3]
outp = extract_values_smaller_than_0(inp)
ans = [-3]
try:
    assert(outp == ans)
except AssertionError as e:
    print("Your function  with input '%r' returned '%r', but I expected '%r'" % (inp, outp, ans))
    raise(e)

inp = [0, 0, 0]
outp = extract_values_smaller_than_0(inp)
ans = []
try:
    assert(outp == ans)
except AssertionError as e:
    print("Your function  with input '%r' returned '%r', but I expected '%r'" % (inp, outp, ans))
    raise(e)

print("EPIC! Well done!")


# ### Advanced loops: list comprehensions (optional)
# Sometimes, writing (and reading!) for-loops can be confusing and lead to "ugly" code. Wouldn't it be nice to represent (small) for-loops on a single line? Python has a way to do this: using what is called `list comprehensions`. It does exactly the same thing as a for-loop: it takes a list, iterates over its entries (and does something with each entry), and (optionally) returns a (modified) list. 
# 
# Let's look at an arbitrary example of a for-loop over a list:

# In[88]:


nums = [0, 1, 2, 3, 4]

# Also, check out the way 'enumerate' is used here!
for index, x in enumerate(nums):
    nums[index] = x ** 2

print(nums)


# You can make this code simpler using a list comprehension:

# In[89]:


nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]  # importantly, a list comprehension always returns a (modified) list!
print(squares)


# Also, list comprehensions may contain if-statements!

# In[90]:


string_nums = ['one', 'two', 'three']
starts_with_t = ['yes' if s[0] == 't' else 'no' for s in string_nums]
print(starts_with_t)


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Write a list comprehension that adds the string <tt>'_check'</tt> to each value in the list <tt>my_list</tt> below, except if the value is 'B'. (This is an optional ToDo to practice list comprehensions.) Note that (in this particular use of list-comprehensions) you always need <em>both</em> a "if .." part <em>and</em> an "else ..." part! So, can you think of a way to add nothing to a string (i.e., the "else ...", when the element is not 'B', part of this list comprehension)? (No test cell.)
# </div>

# In[91]:


""" Implement the ToDo below (no test cell). """
my_list = ['A', 'B', 'C', 'D']


# List comprehensions are somewhat of a more advanced Python concept, so if you don't feel comfortable using them (correctly) in your future assignments, use regular for-loops by all means!

# ### A challenging exercise (optional)
# For those that a challenge, try the following.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Write a function ...
# </div>
