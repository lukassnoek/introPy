#!/usr/bin/env python
# coding: utf-8

# # Introduction to Numpy
# This notebook is about Numpy, Python's core library for numeric computing. Knowing how to use Numpy is *essential* in domains such as machine learning, neuroimaging analysis, and image processing.
# 
# ## Contents
# 1. The *nd*array
# 2. Indexing
# 3. Array math
# 4. Broadcasting
# 
# Let's start by importing numpy, which is commonly done as follows:

# In[1]:


import numpy as np


# ## The *ndarray*
# The most important feature of Numpy is it's core data structure: the numpy *ndarray* (which stands for *n*-*d*imensional array, referring to the fact that the array may be of any dimension: 1D, 2D, 3D, 180D ... *n*D). This is, just like basic lists/dictionaries/integers/tuples, a data structure with its own syntax, operations, and methods, as we will explain below.

# ### Python lists vs. numpy arrays
# Basically, numpy arrays are a lot like Python lists. The major difference, however, is that *numpy arrays may contain only a single data-type*, while Python lists may contain different data-types within the same list.
# 
# Let check this out:

# In[2]:


# Python lists may contain mixed data-types: an integer, a float, a string, a list
python_list = [1, 2.5, "whatever", [3, 4, 5]] 

for value in python_list:
    
    print("%s is a: %s" % (str(value), type(value)))


# Unlike Python lists, numpy only allows entries of the same data-type. This difference between Python lists and numpy arrays is basically the same as R lists (allow multiple data-types) versus R matrices/arrays (only allow one data type), and is also the same as MATLAB cells (allow multiple data-types) versus MATLAB matrices (only allow one data type).
# 
# In fact, if you try to make a numpy array with different data-types, numpy will force the entries into the same data-type (in a smart way), as is shown in the example below:

# In[3]:


# Importantly, you often specify your arrays as Python lists first, and then convert them to numpy
to_convert_to_numpy = [1, 2, 3.5]               # specify python list ...
numpy_array = np.array(to_convert_to_numpy)     # ... and convert ('cast') it to numpy

for entry in numpy_array:
    
    print(entry)
    print('this is a: %s \n' % type(entry))


# As you can see, Numpy converted our original list (to_convert_to_numpy), which contained both integers and floats, to an array with only floats! You might think that such a data structure that only allows one single data type is not ideal. However, the very fact that it only contains a single data-type makes operations on numpy arrays extremely fast. For example, loops over numpy arrays are often way faster than loops over python lists. This is because, internally, Python has to check the data-type of each loop entry before doing something with that entry. Because numpy arrays one allow a single data-type, it only has to check for the entries' data type **once**. If you imagine looping over an array or list of length 100,000, you probably understand that the numpy loop is way faster.
# 
# Let's check out the speed difference between Python list operations and numpy array operations:

# In[4]:


# %timeit is a cool 'feature' that you can use in Notebooks (no need to understand how it works)
# it basically performs a computation that you specify a couple of times and prints how long it took on average
results_python = get_ipython().run_line_magic('timeit', '-o [x * 2 for x in range(0, 100000)] ')


# And now let's do the same with numpy:

# In[5]:


results_numpy = get_ipython().run_line_magic('timeit', '-o np.arange(0, 10000) * 2 ')

ratio = results_python.average / results_numpy.average
print("Numpy is %i times faster than base Python!" % ratio)


# You see that Numpy *much* faster! This really matters when you start doing more complex operations or large arrays!

# ### Creating numpy arrays
# As shown an earlier example, numpy arrays can be created as follows:
# 
# 1. Define a Python list, e.g. `my_list = [0, 1, 2]` 
# 2. Convert the list to a numpy array, e.g. `numpy_array = np.array(my_list)`
# 
# Importantly, a simple Python list will be converted to a 1D numpy array, but a nested Python list will be converted to a 2D (or even higher-dimensional array). Nesting is simply combining different lists, separated by commans, as is shown here:

# In[6]:


my_list = [1, 2, 3]
my_array = np.array(my_list)

print("A 1D (or 'flat') array:")
print(my_array, '\n')

my_nested_list = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

my_2D_array = np.array(my_nested_list)
print("A 2D array:")
print(my_2D_array)


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Create the following 1D array:
# 
# \begin{align}
# \begin{bmatrix}
# 5 & 3 & 2 & 8 & 9
# \end{bmatrix}
# \end{align}
# 
# and store it in a variable named <tt>vec</tt>.
# </div>

# In[7]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
vec = np.array([5, 3, 2, 8, 9])
### END SOLUTION


# In[8]:


""" Tests the above ToDo. """
if 'vec' not in dir():
    raise ValueError("You haven't created the variable 'vec' yet!")
    
if type(vec) != np.ndarray:
    raise ValueError("vec is not a numpy array!")
    
if vec.ndim != 1:
    raise ValueError("vec is not a 1D array!")

if vec.tolist() != [5, 3, 2, 8, 9]:
    raise ValueError("vec does not have the right contents ...")
    
print("Yay!")


# <div class='alert alert-warning'>
#     <b>ToDo</b>:
#     
# Create the following matrix (2D array):
# 
# \begin{align}
# \begin{bmatrix}
# 5 & 2 & 8 \\
# 8 & 2 & 1 \\
# 4 & 4 & 4 \\
# 1 & 2 & 3
# \end{bmatrix}
# \end{align}
# 
# and store it in a variable named <tt>arr_2d</tt>. Hint: start by creating a nested python list (like we did with the <tt>my_nested_list</tt> variable) and then convert it to numpy.
# </div>

# In[9]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
arr_2d = np.array([
    [5, 2, 8],
    [8, 2, 1],
    [4, 4, 4],
    [1, 2, 3]
])
### END SOLUTION


# In[10]:


""" Tests the above ToDo. """
if type(arr_2d) != np.ndarray:
    raise ValueError("arr_2d is not a numpy array!")
    
if arr_2d.shape != (4, 3):
    raise ValueError("arr_2d does not have the right shape!")
    
print("Yes! Well done!")


# <div class='alert alert-warning'>
#     <b>ToDo</b> (optional): Let's try something more difficult! Create a 3D array with dimensions $2 \times 2 \times 2$ with consecutive numbers starting at 1 and store this in a variable named <tt>arr_3d</tt>. So <tt>arr_3d[0, 0, 0]</tt> should evaluate to 1, <tt>arr_3d[0, 0, 1]</tt> should evaluate to 2, <tt>arr_3d[0, 1, 0]</tt> evaluates to 3, etc.
# </div>

# In[11]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
arr_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
### END SOLUTION


# In[12]:


""" Tests the above ToDo. """
if arr_3d.shape != (2, 2, 2):
    raise ValueError("The array does not have the right dimensions!")

if arr_3d[0, 0, 0] != 1:
    raise ValueError("Hmm, something went wrong ...")

if arr_3d[0, 0, 1] != 2:
    raise ValueError("Hmm, something went wrong ...")
    
if arr_3d[1, 1, 1] != 8:
    raise ValueError("Hmm, something went wrong ...")


# As you can imagine, creating numpy arrays from nested lists becomes cumbersome if you want to create (large) arrays with more than 2 dimensions. There are, fortunately, a lot of other ways to create ('initialize') large, high-dimensional numpy arrays. One often-used method is to create an array with zeros using the numpy function `np.zeros`. This function takes one (mandatory) argument, which is a tuple with the dimensions of your desired array:

# In[13]:


my_desired_dimensions = (2, 5) # suppose I want to create a matrix with zeros of size 2 by 5
my_array = np.zeros(my_desired_dimensions)

print(my_array)


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Using the <tt>np.zeros</tt> function, create a five dimensional array of shape $2 \times 3 \times 5 \times 3 \times 7$ and store it in a variable named <tt>array_5d</tt>.
# </div>

# In[14]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
array_5d = np.zeros((2, 3, 5, 3, 7))
### END SOLUTION


# In[15]:


""" Tests the above ToDo. """
from tests import test_create_array_with_zeros
test_create_array_with_zeros(array_5d)


# Using arrays with zeros is often used in what is called 'pre-allocation', in which you create an 'empty' array with only zeros and for example, 'fill' that array in a loop.
# 
# Below, we show you an example in which we pre-allocate an array with 5 zeros, and fill that in a for-loop with the squares of 1 - 5. Try to understand how it works! (You have to do something similar in the next ToDo!)

# In[16]:


my_array = np.zeros(5)

print('Original zeros-array')
print(my_array)

for i in range(5):  # notice the range function here! This loop now iterates over [0, 1, 2, 3, 4]
    number_to_calculate_the_square_of = i + 1
    my_array[i] = number_to_calculate_the_square_of ** 2

print('\nFilled array')
print(my_array)


# <div class='alert alert-warning'>
# <b>ToDo</b>: Write a loop in which you fill each value in the variable <tt>my_array2</tt> with the value 1 divided by the current index plus one. So, suppose the index (usually <tt>i</tt>, like the last example) is 3, then you should fill <tt>my_array2</tt> at index <tt>i</tt> with <tt>1 / (3 + 1)</tt>.
# </div>

# In[17]:


""" Implement the ToDo here. """
my_array2 = np.zeros(8)

### BEGIN SOLUTION
for i in range(8):
    my_array2[i] = 1 / (i + 1)
### END SOLUTION


# In[18]:


""" Tests the above ToDo. """
from tests import test_fill_array_with_complement
test_fill_array_with_complement(my_array2)


# In addition to `np.zeros`, you can create numpy arrays using other functions, like `np.ones` and `random` from the `np.random` module:

# In[19]:


ones = np.ones((5, 10)) # create an array with ones
print(ones, '\n')

rndom = np.random.random((5, 10)) # Create an array filled with random values (0 - 1 uniform)
print(rndom)


# ## Numpy indexing
# Indexing (extracting a single value of an array) and slicing (extracting multiple values - a subset - from an array) of numpy arrays is largely the same as with regular Python lists and data structures from other scientific computing languages such as R and MATLAB. Let's check out a couple of examples of a 1D array:

# In[20]:


my_array = np.arange(10, 21)  # numpy equivalent of list(range(10, 21))
print('Full array:')
print(my_array, '\n') 


# In[21]:


print("Index the first element:")
print(my_array[0])


# In[22]:


print("Index the second-to-last element:")
print(my_array[-2])


# In[23]:


print("Slice from 5 until (not including!) 8")
print(my_array[5:8])


# In[24]:


print("Slice from beginning until 4")
print(my_array[:4])


# Setting values in numpy arrays works the same way as lists:

# In[25]:


my_array = np.arange(10, 21)
my_array[0] = 10000
print(my_array)

my_array[5:7] = 0
print(my_array)


# <div class='alert alert-warning'>
#     <b>ToDo</b> (1 point): In the array <tt>my_array</tt> below, set all odd indices (i.e., the first element, the third element, the fifth element, etc.) to the value <tt>0.0</tt> <em>in a single statement using a slice</em> (i.e., not a for-loop).
# </div>

# In[26]:


""" Implement the ToDo here. """
my_array = np.arange(3, 25)

### BEGIN SOLUTION
my_array[1::2] = 0.0
### END SOLUTION


# In[27]:


''' Tests the above ToDo. '''
from tests import test_set_odd_indices_to_zero
test_set_odd_indices_to_zero(my_array)


# ### Multidimensional indexing
# Often, instead of working on and indexing 1D array, we'll work with multi-dimensional (>1D) arrays. Indexing multi-dimensional arrays is, again, quite similar to other scientific computing languages. 
# 
# Like indexing Python lists, indexing multidimensional numpy arrays is done with square brackets `[]`, in which you can put as many comma-delimited numbers as there are dimensions in your array. 
# 
# For example, suppose you have a 2D array of shape $3 \times 3$ and you want to index the value in the first row and first column. You would do this as follows:

# In[28]:


my_array = np.zeros((3, 3)) # 3 by 3 array with zeros
indexed_value = my_array[0, 0]
print("Value of first row and first column: %.1f" % indexed_value)


# <div class='alert alert-warning'>
# <b>ToDo</b>: Using multidimensional indexing, set the value in the last row and last column of the 2D array <tt>my_array</tt> to <tt>1.0</tt>. In other words, set the value in the lower-right "corner" of the 2D array to 1.0.
# </div>

# In[29]:


""" Implement the ToDo here. """
my_array = np.zeros((3, 3))

print(my_array)

# ToDo: set the value in the lower right corner to 1

### BEGIN SOLUTION
my_array[-1, -1] = 1.0
### END SOLUTION


# In[30]:


""" Tests the ToDo above. """
from tests import test_set_lower_right_value_to_one
test_set_lower_right_value_to_one(my_array)


# In addition to setting specific slices to specific values, you can also extract sub-arrays using slicing/indexing. An important construct here is that you can use a single colon `:` to select all values from a particular dimension. For example, if you want to select all column-values (second dimension) from only the first row (first dimension), do this:
# 
# ```
# some_2d_arr[0, :]
# ```
# 
# We'll show you some examples below:

# In[31]:


my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(my_array, '\n')

all_column_values_from_first_row = my_array[0, :]
print('First row')
print(all_column_values_from_first_row, '\n')

all_row_values_from_first_col = my_array[:, 0]
print('First column')
print(all_row_values_from_first_col)


# So far, we only talked about 2D arrays, which are relatively easy to 'understand'. In neuroimaging, however, we usually work with 3D, 4D, or even higher-dimensional arrays. These arrays are great for organizing data, but they are somewhat unintuitive. This takes some time to get used to!
# 
# To get you used to thinking in more than 2 (or 3) dimensions, consider the following scenario. Suppose that a researcher wants to test the efficacy of a particular medicine against high blood pressure. To do so, she/he measures the (average systolic) blood pressure of a group of twenty subjects every hour for 30 days when they're not on the medication. The same subjects are then again measured for another 30 days, but then when they're on medication.
# 
# After this period of data collection, the researcher has $20\ \mathrm{(subjects)}\ \times\ 24\ \mathrm{(hours)}\ \times\ 30\ \mathrm{(days)}\ \times\ 2\ \mathrm{(conditions: off/on)} = 28800$ measurements! We can then organize the data in a 4D array, in which each factor (subjects/hours/days/conditions) represents a separate dimension (also called "axis") of our array!\*
# 
# ---
# \* Note that this type of data is perhaps best represented in a "table-like" structure, such as a Dataframe in R or a Pandas DataFrame, the Python-equivalent of R's dataframe). But you can ignore that for the sake of this example.

# So, let's generate some random data (from a normal distribution to generate 'realistic' blood pressure data) that could represent this blood pressure dataset:

# In[32]:


np.random.seed(42)  # this is not important for now
bp_data = np.random.normal(loc=100, scale=5, size=(20, 24, 30, 2))


# (Note that we're not printing the `bp_data` variable here, because it's way too much to visualize/interpret at once anyway!)
# 
# Now, suppose I would want to extract the blood pressure of subject 5 at 09.00 (AM) in the morning at day 21 when he/she was *not* on medication. In that case, I would do:

# In[33]:


# Note that I count midnight as the first measurement
this_particular_datapoint = bp_data[4, 8, 20, 0]
print("Blood pressure of participant 5 at 09.00 (AM) on day 21 in "
      "the no-medication (off) condition is %.3f" % this_particular_datapoint)

# Also, remember that Python is zero-based, so e.g. participant 5 is indexed by index 4!


# Try to remember this: *in multidimensional arrays, each dimension (axis) represents a different "attribute" of your data (e.g. subjects, time, condition, etc.)*. This concept is very important to understand in, for example, functional MRI analysis (which revolves around 4D data: 3 spatial dimensions and 1 time dimension)!

# <div class='alert alert-warning'>
# <b>ToDo</b>: Consider the blood-pressure dataset again. In the code-cell below, extract from all participants all data from day 18 in the medication ("on") condition. You'll have to use slices with the single <tt>:</tt>! Store the results of your index-operation in the variable <tt>day_18_condition_on</tt>.
# </div>

# In[34]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
day_18_condition_on = bp_data[:, :, 17, 1]
### END SOLUTION


# In[35]:


""" Tests the above ToDo. """
from tests import test_bloodpressure_index
test_bloodpressure_index(day_18_condition_on)


# Multidimensional indexing using slices (especially the single colon `:` slice, i.e., selecting everything) is very common in scientific programming such as neuroimaging analyses. There is, however, yet another way of (multidimensional) indexing called "boolean indexing". 
# 
# In this type of indexing, you index an array with a boolean array (i.e. array with True and False values) of the same shape. Basically, when you're indexing the array `my_array` with boolean array `bool_array`, you're saying: "give me all values in `my_array` that are `True` at the same location in `bool_array`!"
# 
# Let's look at an example:

# In[36]:


my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print("The original array:\n")
print(my_array, '\n')

bool_array = np.array([[True, False, True],
                       [False, True, False],
                       [True, False, True]])

print("The boolean array:\n")
print(bool_array, '\n')

print('Result of indexing my_array with bool_array:\n')
print(my_array[bool_array])


# Usually, you do not write out the boolean array in full (as we did above), but you base it on the data itself to "filter" it according to some criterion formalized as a logical statement (i.e., using the boolean operators >, <, ==, or !=). For example, suppose I want to extract only the values above 6 from the `my_array` variable in the above example. 
# 
# To do so, I could do the following:

# In[37]:


my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print("The original array:\n")
print(my_array, '\n')

bool_array = my_array > 6

print("The boolean array:\n")
print(bool_array, '\n')

print('Result of indexing my_array with bool_array:\n')
print(my_array[bool_array])


# Easy, right? Now try it yourself in the next ToDo!

# <div class='alert alert-warning'>
# <b>ToDo</b>: Use a boolean index to extract all values whose square (i.e. $x^2$) is larger than 4 from the array (<tt>my_array</tt>) below. Store the results in a variable with the name <tt>square_is_larger_than_4</tt>.
# </div>

# In[38]:


""" Implement the ToDo here. """
my_array = np.array([[0, 1, -1, -2],
                     [2, -5, 1, 4],
                     [10, -2, -4, 20]])

# Make a new boolean array below (name it whatever you want) ...

# And use it to index my_array and store it in a variable `square_is_larger_than_4`.

### BEGIN SOLUTION
square_is_larger_than_4 = my_array[my_array ** 2 > 4]
### END SOLUTION


# In[39]:


""" Tests the above ToDo. """
from tests import test_boolean_indexing
test_boolean_indexing(square_is_larger_than_4)


# Again, it's very important to understand how to (effectively) index multidimensional numpy arrays using slices and boolean indexing, as we'll use it a lot in this course!

# ## Data-types
# Every numpy array is a grid of values of the same type. Numpy provides a large set of numeric datatypes that you can use to construct arrays. Numpy guesses the datatype when you create an array, but functions that construct arrays usually also include an optional argument to explicitly specify the datatype.
# 
# Here are a couple of examples:

# In[40]:


x1 = np.array([1, 2])  # Let numpy choose the datatype (here: int)
x2 = np.array([1.0, 2.0])  # Let numpy choose the datatype (here: float)
x3 = np.array([1, 2], dtype=np.float64)  # Force a particular datatype (input: int, but converted to 64bit float)
x4 = np.array([-1, 0, 1, 2], dtype=bool)  # Convert ints to booleans! 0 -> False, everthing else -> True 

print('%r (%s)' % (x1, type(x1[0])))
print('%r (%s)' % (x2, type(x2[0])))
print('%r (%s)' % (x3, type(x3[0])))
print('%r (%s)' % (x4, type(x4[0])))


# Note that, after creating the array, you can still change the datatype by using the numpy method `astype()`!

# In[41]:


x = np.array([1, 2, 3, 4])
print(type(x[0]))

# Now convert it to floasts!
x = x.astype(float)  # or astype(np.float)
print(type(x[0]))


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Below, we've defined a boolean array named <tt>bool_array</tt>. Convert it to an array with integers and store it in a new array called <tt>bool2int_array</tt>. Check out the values of the new array!
# </div>

# In[42]:


""" Implement the ToDo here. """
bool_array = np.array([True, True, False, False, True])
### BEGIN SOLUTION
bool2int_array = bool_array.astype(int)
print(bool2int_array)
### END SOLUTION


# In[43]:


""" Tests the above ToDo (not for points). """
np.testing.assert_array_equal(bool2int_array, np.array([1, 1, 0, 0, 1]))
print("Well done!")


# ## Methods vs. functions
# In the previous notebooks, you've learned that, in addition to functions, 'methods' exist that are like functions of an object. You've seen examples of list methods, e.g. `my_list.append(1)`, and string methods, e.g. `my_string.replace('a', 'b')`.
# 
# Like lists and strings, numpy arrays have a lot of convenient methods that you can call (like the `astype` method we saw earlier). Again, this is just like a function, but then applied to itself. Often, numpy provides both a function and method for simple operations. 
# 
# Let's look at an example: 

# In[44]:


my_array = np.arange(10)  # creates a numpy array from 0 until (excluding!) 10
print(my_array, '\n')

mean_array = np.mean(my_array)
print('The mean of the array is: %f' % mean_array)

mean_array2 = my_array.mean() 
print('The mean of the array (computed by its corresponding method) is: %f' % mean_array2)

print('Is the results from the numpy function the same as '
      'the corresponding method? Answer: %s' % str(mean_array == mean_array2))


# If there is both a function and a method for the operation you want to apply to the array, it really doesn't matter what you choose! Let's look at some more (often used) methods of numpy ndarrays:

# In[45]:


my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

std_my_array = my_array.std()  # same as np.std(array)
print("Standard deviation of my_array: %.3f" % std_my_array, '\n')

transpose_my_array = my_array.T  # same as np.transpose(array)
print("Transpose of my_array:\n%r" % transpose_my_array, '\n')

min_my_array = my_array.min()  # same as np.min(array)
print("Minimum of my_array: %i" % my_array.min(), '\n')

max_my_array = my_array.max()  # same as np.max(array)
print("Maximum of my_array: %i" % max_my_array, '\n')

sum_my_array = my_array.sum()  # same as np.sum(array)
print("Sum of my_array: %i" % sum_my_array, '\n')


# Importantly, a method may or may not take arguments (input).
# If no arguments are given, it just looks like "object.method()", i.e. two enclosing brackets with nothing in between.
# However, a method may take one or more arguments (like the my_list.append(1) method)! 
# This argument may be named or unnamed - doesn't matter. An example:

# In[46]:


my_array2 = np.random.random((3, 3))
print('Original array:')
print(my_array2, '\n')

print('Use the round() method with the argument 3:')
print(my_array2.round(3), '\n')

print('Use the round() method with the named argument 5:')
print(my_array2.round(decimals=5), '\n')


# In addition to the methods listed above, you'll probably see the following methods a lot in the code of others.
# 
# Reshaping arrays:

# In[47]:


my_array = np.arange(10)
print(my_array.reshape((5, 2))) # reshape to desired shape


# Ravel ("flatten") an array:

# In[48]:


temporary = my_array.reshape((5, 2))
print("Initial shape: %s" % (temporary.shape,))
print(temporary.ravel()) # unroll multi-dimensional array to single 1D array
print("Shape after ravel(): %s" % (temporary.ravel().shape,))


# In[49]:


# .dot() does matrix multiplication (dot product: https://en.wikipedia.org/wiki/Dot_product)
# This linear algebra operation is used very often in neuroimaging research 
# (which depends heavily on the General Linear Model!)
array1 = np.array([0, 1, 2, 3])
array2 = np.array([4, 5, 6, 7])

dot_product = array1.dot(array2)
print(dot_product)


# <div class='alert alert-warning'>
# <b>ToDo</b> (1 point): Let's practice writing functions some more. Complete the function below, named <tt>calculate_range</tt>. This function takes  a single input-argument &mdash; a 1D numpy array &mdash; and subsequently calculates the <a href="https://en.wikipedia.org/wiki/Range_(statistics)">range</a> of the array. The range is the difference between the maximum and minimum of any given array (vector) $x$:
# 
# \begin{align}
# \mathrm{range}(x) = \max(x) - \min(x)
# \end{align}
# 
# You may use the corresponding numpy min/max methods or functions in your custom function, doesn't matter. Don't forget to explicitly return the value of the range! 
# 
# Note: this custom function that implements the *mathematical* formula for a vector's range is completely unrelated to the <em>Python function</em> <tt>range</tt> that is often used in for-loops! 
# </div>

# In[50]:


""" Implement the ToDo here by completing the function. """
def calculate_range(arr):
    ''' Calculate the range of an array.
    
    Parameters
    ----------
    arr : a 1D numpy array
    
    Returns
    -------
    The range of the input arr
    '''
    
    ### BEGIN SOLUTION
    return arr.max() - arr.min()
    ### END SOLUTION


# In[51]:


""" Tests the above ToDo. """

outp = calculate_range(np.array([0, 1, 2, 3]))
if outp is None:
    raise ValueError("Didn't get any output! Did you explicitly return the range?")

assert(outp == 3)
assert(calculate_range(np.array([-1, 0, 1, 2])) == 3)
assert(calculate_range(np.array([0, 0, 0, 0])) == 0)

print("Great job!")


# Alright, by now, if you see a variable followed by a word ending with enclosed brackets, e.g. `my_array.mean()`, you'll know that it's a method! But sometimes you might see something similar, but **without** the brackets, such as `my_array.size`. As you know, this `.size` is called an **attribute** of the variable `my_array`. The attribute may be of any data-type, like a string, integer, tuple, an array itself. Let's look at a numpy-specific example:

# In[52]:


my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(my_array, '\n')
print('The size (number of element) in the array is:')
print(my_array.size, '\n')
print('The .size attribute is of data-type: %s' % type(my_array.size))


# Again, you might not use attributes a lot during this course, but you'll definitely see them around in the code of the tutorials. Below, some of the common ndarray attributes are listed:

# In[53]:


my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print('Size (number of elements) of array:')
print(my_array.size, '\n') # returns an integer

print('Shape of array:')
print(my_array.shape, '\n') # this is a tuple!

print('Number of dimensions:')
print(my_array.ndim) # this is an integer


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Let's try another one. Complete the function below, named <tt>compute_one_sample_ttest</tt>. This function takes two input arguments:
# 
# - arr : a 1D numpy array
# - h0 : a scalar value (single number) that represents the value representing the null-hypothesis
# 
# The function should compute the one-sample t-test, which tests whether the mean of an array is significantly different from a given value representing the null-hypothesis. Formally, for any given array $x$ and null-hypothesis $h_{0}$:
# 
# \begin{align}
# t = \frac{\bar{x} - h_{0}}{s\ / \sqrt{N}}
# \end{align}
# 
# Here: $\bar{x}$ represents the mean of $x$, $s$ represents the standard deviation of $x$, and $N$ represents the length ('size') of x. So, in slightly less mathematical notation:
# 
# \begin{align}
# t = \frac{\mathrm{mean}(x) - h_{0}}{\mathrm{std}(x)\ / \sqrt{\mathrm{length}(x) - 1}}
# \end{align}
# 
# Make sure to return the t-value! 
# 
# **Hint 1**: to compute $N$, you can use the `.size` attribute of an array ... <br>
# **Hint 2**: use the function `np.sqrt(some_number)` to calculate the square root ...
# </div>

# In[54]:


""" Implement the ToDo here. """
def compute_one_sample_ttest(arr, h0):
    ''' Computes the one-sample t-test for any array and h0. 
    
    Parameters
    ----------
    arr : a 1D numpy array
    h0 : an int or float
    
    Returns
    -------
    A single value representing the t-value
    '''
    
    ### BEGIN SOLUTION
    t_val = (arr.mean() - h0) / (arr.std() / np.sqrt(arr.size - 1))
    return t_val
    ### END SOLUTION


# In[55]:


""" Tests the ToDo above. """
from tests import test_tvalue_computation

arr = np.random.randn(100)
outp = compute_one_sample_ttest(arr , 0)

if outp is None:
    raise ValueError("Your function didn't return anything! Did you forget the return statement?")

print("Going to do 3 tests ...")
test_tvalue_computation(arr, 0, outp)

outp = compute_one_sample_ttest(arr, 5) 
test_tvalue_computation(arr, 5, outp)

outp = compute_one_sample_ttest(arr, -3) 
test_tvalue_computation(arr, -3, outp)


# ## Numpy: array math
# Now you know all the numpy basics necessary to do neuroimaging analysis! As you'll see in the last section (Working with nifti-images), we'll work with 3D (structural MRI images) or 4D (functional MRI images) numpy arrays a lot. Given that you know how the basics about numpy in general and numpy ndarrays in particular, we can utilize some of numpy's best features: (very fast) array math.
# 
# Basic mathematical functions operate elementwise on arrays, which means that the operation (e.g. addition) is applied onto each element in the array. So, let's initialize a 1D array with ten zeros and let's add 1 to it:

# In[56]:


x = np.zeros(10)
print(x, '\n')
x += 1 # remember: this the same as x = x + 1
print(x)


# Additionally, you can also sum two arrays together in an elementwise manner by simply writing: `array_1 + array_2`, given that these two (or more) arrays are of the same shape! Let's look at an example:

# In[57]:


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print("x: \n%r" % x, '\n')
print("y: \n%r" % y, '\n')
print("x+y: \n%r" % (x + y), '\n')


# Often, there exist function-equivalents of the mathematical operators. For example, `x + y` is the same as `np.add(x, y)`. However, it is recommended to use the operators wherever possible to improve readability of your code. See below for an example:

# In[58]:


print(x + y, '\n')
print(np.add(x, y))


# Next to addition, we can also do elementwise subtraction, multiplication, divison, square root, and exponentiation:

# In[59]:


# Elementwise difference; both produce the array
print(x - y, '\n')
print(np.subtract(x, y))  # function-equivalent of above 


# In[60]:


# Elementwise product; both produce the array
print(x * y, '\n')
print(np.multiply(x, y))


# In[61]:


# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y, '\n')
print(np.divide(x, y))


# In[62]:


# Elementwise square root; there is no operator-equivalent!
print(np.sqrt(x))


# In[63]:


# Elementwise exponentiation
print(x ** y, '\n')
print(np.power(x, y))


# <div class='alert alert-warning'>
# <b>ToDo</b>: Do an elementwise product between the two variables defined below (<tt>arr_A</tt> and <tt>arr_B</tt>) and subsequently add 5 to each element; store the result in a new variable called <tt>result_product_and_sum</tt>.
# </div>

# In[64]:


""" Implement the ToDo here. """
arr_A = np.arange(10).reshape((5, 2))
arr_B = np.arange(10, 20).reshape((5, 2))

### BEGIN SOLUTION
result_product_and_sum = (arr_A * arr_B) + 5
### END SOLUTION


# In[65]:


""" Tests the above ToDo. """
from tests import test_array_product_and_sum
test_array_product_and_sum(result_product_and_sum)    


# Note that unlike Matlab, `*` is elementwise multiplication, not matrix multiplication. We instead use the dot function (or method!) to  compute matrix operations like inner products of vectors, multiplication of a vector by a matrix, and multiplication of two matrices.
# 
# These matrix operations are quite important in this course, because they are used a lot in neuroimaging methods (such as the General Linear Model, the topic of next week!). You're not expected to fully understand these matrix operations, but you'll see them several times in this course, so make sure you're familiar with its implementation in Python/Numpy.
# 
# An example of the inner product ("dot product") of two vectors in both the function-format and the method-format:

# In[66]:


v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))


# Additionally, in Python 3.6 (and above), you can use the `@` character as an operator for matrix multiplication of numpy arrays!

# In[67]:


print(v @ w)


# Probably the most used functions in numpy are the sum() and mean() fuctions (or equivalent methods!). A nice feature is that they can operate on the entire array (this is the default) or they can be applied per dimension (or, in numpy lingo, per "axis").
# 
# Applying functions along axes is very common in scientific computing! Let's look at an example in which we apply the `sum` function/method across rows and columns:

# In[68]:


x = np.array([[1, 2],[3, 4], [5, 6]])

print('Original array:')
print(x, '\n')

print('Sum over ALL elements of x:')
print(np.sum(x), '\n')

print('Sum across rows of x:')
print(np.sum(x, axis=0), '\n')

print('Sum across columns of x:')
print(x.sum(axis=1)) # this is the method form! Is exactly the same as np.sum(x, axis=1) 


# Importantly, application of functions across axes is much quicker (and more concise) than writing for-loops! Let's look at the speed difference between a for-loop (implemented as a list comprehension) and the numpy-style application of the `sum` function across axes:

# In[69]:


arr = np.random.random((1000, 100))
loop_style = get_ipython().run_line_magic('timeit', '-o [arr[i, :].sum() for i in range(arr.shape[0])]')
axis_style = get_ipython().run_line_magic('timeit', '-o arr.sum(axis=1)')
print("Using the axis-argument is %.3f times faster than a for-loop!" % (loop_style.average / axis_style.average))


# This application of functions on entire arrays (in an elementwise manner, like `arr_1 + arr_2`) and application of functions across a certain axis (like `np.sum(arr_1, axis=1)`) is often called **vectorization**. This is an incredibly useful concept and something that is used in many data analysis tools! Make sure you understand this. 
# 
# Let's practice this a bit.

# <div class='alert alert-warning'>
# <b>ToDo</b>: Remember the "range" function from before? Below, we started writing a function, called <tt>calculate_range_vectorized</tt>, that calculates, for any 2D array, the range of each column (i.e. calculates range <em>across rows</em> for each column) in a vectorized manner (so without any for loops!).<br><br>
# Complete the function, and make sure to return the result, which should be a 1D vector which values represents the ranges for all columns. So, if the input array would be of shape <tt>(100, 10)</tt>, then the shape of your returned array should be <tt>(10,)</tt>.
# </div>

# In[70]:


""" Implement the ToDo here (by completing the function below). """
def compute_range_vectorized(arr):
    ''' Compute the range across rows for each column in a 2D array. 
    
    Parameters
    ----------
    arr : a 2D numpy array
    
    Returns
    -------
    A 1D vector with the ranges for each column
    '''
    
    ### BEGIN SOLUTION
    return arr.max(axis=0) - arr.min(axis=0)
    ### END SOLUTION


# In[71]:


""" Tests the above ToDo. """
from tests import test_compute_range_vectorized

np.random.seed(42)
test_arr = np.random.random((100, 10))
outp = compute_range_vectorized(test_arr)

if outp is None:
    raise ValueError("Output is None! Did you forget the Return statement in your function?")

test_compute_range_vectorized(test_arr, outp)


# ## Broadcasting
# Broadcasting is a powerful mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.
# 
# For example, suppose that we want to add a vector to each row of a matrix. We could do it like this:

# In[72]:


# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print('x array is of shape: %r' % (x.shape,))
print(x, '\n')

v = np.array([1, 0, 1])
print('v vector is of shape: %r (different shape than x!)' % (v.shape,))
print(v, '\n')

y = np.zeros(x.shape)   # Create an empty (zeros) matrix with the same shape as x
print('Shape of (pre-allocated) y-matrix: %r' % (y.shape,))

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(x.shape[0]): # see how the shape attributes comes in handy in creating loops?
    y[i, :] = x[i, :] + v

print('The result of adding v to each row of x, as stored in y:')
print(y)


# This works; however when the matrix `x` is very large, computing an explicit for-loop in Python could be slow. Note that adding the vector v to each row of the matrix `x` is equivalent to forming a matrix `vv` by stacking multiple copies of `v` vertically, like this `[[1 0 1], [1 0 1], [1 0 1], [1 0 1]]`, and subsequently elementwise addition of `x + vv`:

# In[73]:


vv = np.tile(v, (4, 1)) # i.e. expand vector 'v' 4 times along the row dimension (similar to MATLAB's repmat function)
y = x + vv  # Add x and vv elementwise
print(y)


# Numpy **broadcasting** allows us to perform this computation without actually creating multiple copies of v. Consider this version, using broadcasting:

# In[74]:


# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v  # Add v to each row of x using broadcasting
print(y)


# The line `y = x + v` works even though `x` has shape `(4, 3)` and `v` has shape `(3,)` due to broadcasting; this line works as if v actually had shape `(4, 3)`, where each row was a copy of `v`, and the sum was performed elementwise.
# 
# This broadcasting function is really useful, as it prevents us from writing unnessary and by definition slower explicit for-loops. Additionally, it's way easier to read and write than explicit for-loops (which need pre-allocation). Functions that support broadcasting are known as universal functions. You can find the list of all universal functions in the [documentation](http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs).
# 
# Here are some applications of broadcasting using different functions:

# In[75]:


x = np.array([[1, 2],[3, 4], [5, 6]], dtype=np.float)
x_sum = x.sum(axis=0)

print(x / x_sum, '\n')

x_mean = x.mean(axis=0)
print(x / x_mean)


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Below, we started writing a function called <tt>standardize_columns</tt>, which takes a single input-argument &mdash; a 2D numpy array &mdash; and should subsequently <em>standardize</em> each column such that each column has a mean of zero and a standard deviation of 1. In other words, standardization subtracts the mean (across rows) of each column from the values in that column, and then divides those value with the standard deviation of that column. Formally, for each column $j$ in any 2D array, standardization entails:
# 
# \begin{align}
# x_{j}\ \mathrm{standardized} = \frac{(x_{j} - \bar{x_{j}})}{\mathrm{std}(x_{j})}
# \end{align}
# 
# Standardization, which is also oftend called "z-transformation", is often done in statistics. So, in the function below, make sure that it is able to standardize each column in any 2D array. Make sure to use vectorized array computations (i.e, the <tt>np.mean</tt> and <tt>np.std</tt> functions/methods across rows) and broadcasting, so no for-loops! 
# 
# </div>

# In[76]:


""" Implement the ToDo here (by completing the function below). """
def standardize_columns(arr):
    ''' Standardize each column of a 2D input-array. 
    
    Parameters
    ----------
    arr : a 2D numpy array
    
    Returns
    -------
    The input-array with standardized columns (should have the same shape as the input-array!)
    '''
    
    ### BEGIN SOLUTION
    return (arr - arr.mean(axis=0)) / arr.std(axis=0)
    ### END SOLUTION


# In[77]:


""" Tests the above ToDo. """

test_arr = np.random.normal(5, 2, size=(100, 10))
outp = standardize_columns(test_arr)

if outp is None:
    raise ValueError("The output from your function is None; did you forget the Return statement?")

try:
    np.testing.assert_array_almost_equal(outp.mean(axis=0), np.zeros(test_arr.shape[1]))
except AssertionError as e:
    print("The mean of the columns of your standardized array are not 0!")
    raise(e)

try:
    np.testing.assert_array_almost_equal(outp.std(axis=0), np.ones(test_arr.shape[1]))
except AssertionError as e:
    print("The std of the columns of your standardized array are not 1!")
    raise(e)
    
print("A-MA-ZING!")


# Now, you know the most important numpy concepts and functionality that is necessary to start using it. Surely, there is a lot more to the numpy package that what we've covered here, but that's for another time 😃
