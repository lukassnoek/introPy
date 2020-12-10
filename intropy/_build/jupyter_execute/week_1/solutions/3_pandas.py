#!/usr/bin/env python
# coding: utf-8

# # Introduction to Pandas
# Pandas is a Python package that contains functionality for data analysis and manipulatoin. It is used mostly for "table-like" data, i.e., data that can be organized in 2D tables with observations organized across rows and variables across columns. With Pandas, you can do most of the data processing routines you might know from R. (R contains more extensive statistics-related functionality, though.)
# 
# ## Contents
# 1. Dataframes
# 2. Indexing
# 3. Dataframe operations
# 4. Aggregation (optional)

# ## Dataframes
# Alright, let's get started. The Pandas package isis usually imported as follows:

# In[1]:


import pandas as pd


# Although Pandas contains several functions for processing data, the package is very object-oriented. Specifically, most of its functionality is implemented in the `DataFrame` class, which is similar to R's `dataframe` (or [tibble](https://tibble.tidyverse.org/)). 
# 
# Now, you can actually create a `DataFrame` object using different methods. You can create it from scratch (in Python) or you can load it from an external file, like a CSV (comma-separated value) file or an Excel file. The latter is probably the most often used, so let's take a look at that. We created some data from a (very small) hypothetical working memory experiment, which we saved in a CSV file (where each column is separated by commas, hence the name). To load in this data, we will use the function `pd.read_csv`:

# In[2]:


df = pd.read_csv('example_data.csv')
df.index = [0, 1, 2, 3]  # you may ignore this line


# To view its contents, we can just enter `df` as the last line in a code cell (so without `print`) and run the cell. This way, Jupyter notebooks will actually render the dataframes nicely:

# In[3]:


df


# <div class='alert alert-warning'>
#     <b>ToDo</b>: The <tt>pd.read_csv</tt> is in fact a very flexible function and has a lot of arguments to tweak it according to your needs. Check out its <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html">documentation</a> to get an overview of its arguments! For example, try to load the same data (from <tt>example_data.csv</tt>), but include only the "age" and "wm_score" columns, and store this 2-column dataframe in a variable named <tt>df_todo</tt>.
# </div>

# In[4]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
df_todo = pd.read_csv('example_data.csv', usecols=['age', 'wm_score'])
### END SOLUTION


# In[5]:


""" Tests the above ToDo. """
if df_todo.columns.tolist() != ['age', 'wm_score']:
    raise ValueError('Something went wrong ... :-(')
else:
    print("Well done!")


# As mentioned, Pandas dataframes assume that its rows represent different observations (here: participants) and its columns represent different variables (here: participant ID, age, condition, and working memory score). Apart from the dataframe's values (e.g., "sub-01", "sub-02" and 25, 21), the dataframe also contains column names (here: "participant_id", "age", "condition", "wm_score") and row names (0, 1, 2, 3). The row names are usually referred to as the dataframe's *index*. The column names can be accessed using the `columns` attribute:

# In[6]:


# Actually, this is a specific object called an Index, but
# you can forget about that for now
df.columns


# ... and the row index can be accessed using the `index` attribute:

# In[7]:


# Again, it is a specific object, which you may ignore for now
df.index


# <div class='alert alert-success'>
#     <b>Note</b>: there is no reason that the column names should be strings and the index should be integers. It completely valid to use, for example, integers as column names and strings as index values!
# </div>

# ### Creating dataframes from scratch
# In some situations, you may want to create a `DataFrame` object from scratch. Although there are different ways to do this, arguably the easiest way is to pass a dictionary to the `DataFrame` class:

# In[8]:


data = {'var1': [1, 2, 3], 'var2': ['a', 'b',  'c']}
some_df = pd.DataFrame(data)
some_df


# As you can see, the `DataFrame` class automatically infers the column names from the dictionary keys and creates a default integer index starting at 0.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: You can also specify the index explicitly by passing a list to the <tt>index</tt> parameter (see also the <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html">documentation</a>). Using the variable <tt>data</tt> again, create a new dataframe (called <tt>df_todo</tt>) but use "x", "y", "z" for the index. 
# </div>

# In[9]:


""" Implement your ToDo here. """
df_todo = pd.DataFrame(data, index=['x', 'y', 'z'])


# In[10]:


""" Tests the above ToDo. """
if df_todo.index.tolist() != ['x', 'y', 'z']:
    raise ValueError("Something went wrong ...")
    
print("Yes! Well done!")


# ## Indexing
# One important operation you need to now is how to select (or "extract") particular rows and/or columns. There are, in fact, multiple ways to do this, but we recommend sticking with `loc` and `iloc`. 
# 
# ### Indexing with `loc`
# The `loc` indexer selects rows and/or columns based on their name (similar to indexing a dictionary). You always need to supply the `loc` indexer both your row selection and your column selection. In general, it should be used as follows:
# 
# ```python
# df_subset = df.loc[row_selection, column_selection]
# ```
# 
# where `row_selection` and `column_selection` may be either a single row/column name or a list of row/column names. For example, if you'd want to select the first two rows and the "age" and "wm_score" columns, you could do the following:

# In[11]:


df_subset = df.loc[[0, 1], ['age', 'wm_score']]
df_subset


# Note that other indexing methods also exist, like indexing columns directly (e.g., `df['age']`), or indexing columns by accessing them as attributes (e.g., `df.age`). We strongly suggest always using `loc` (and `iloc`), though, for consistency (also because this method is the most versatile).

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Select the second and fourth row and the "participant_id" and "condition" columns from the dataframe (<tt>df</tt>) and store the result in a new variable named <tt>df_todo</tt>.
# </div>

# In[12]:


""" Implement your ToDo here. """
### BEGIN SOLUTION
df_todo = df.loc[[1, 3], ['participant_id', 'condition']]
### END SOLUTION


# In[13]:


""" Tests the above ToDo. """
if df_todo['participant_id'].tolist() != ['sub-02', 'sub-04']:
    raise ValueError("Something went wrong ...")

if df_todo['condition'].tolist() != ['B', 'B']:
    raise ValueError("Something went wrong ...")
    
print("Well done!")


# Note that you can also select *all* rows or columns at once using the colon (`:`). For example, if you'd want to select all rows from the "age" and "wm_score" columns, you can do the following:

# In[14]:


df.loc[:, ['age', 'wm_score']]


# ### Intermezzo: Series vs. Dataframes
# Before continuing with position-based indexing using `iloc`, we need to quickly discuss pandas `Series` objects. `Series` are basically single-column (or single-row) dataframes. For example, if we'd select a single column from our example dataframe, we'd have a `Series` object:

# In[15]:


srs = df.loc[:, 'age']  # note the absence of the list
srs


# In[16]:


type(srs)


# As such, you can think of `DataFrame` objects as a collection of `Series` objects. As opposed to `DataFrame` object, `Series` object does not have column names (but its original column name can be accessed through the `name` attribute), but it *does* have an index:

# In[17]:


srs.index


# We won't discuss `Series` in this notebook, as in practice you'll mostly work with `DataFrame` objects (but we wanted to show it to you in case you encounter them).

# <div class='alert alert-success'>
#     <b>Tip</b>: Want to select a single column/row, but still want pandas to return a dataframe? Make sure you use a list to index the single column/row!<br><br>That is, use:<br><tt>df.loc[:, ['age']]</tt><br>and not:<br><tt>df.loc[:, 'age']</tt>).
# </div>

# ### Indexing with `iloc`

# Instead of selecting subsets from dataframes based on their column names and row names (index) using `loc`, you can also do so using the "integer-location" of the subsets using `iloc`. This method of indexing follows the same rules as indexing lists. For example, you can simply select specific columns, e.g., the first and fourth column:

# In[18]:


df.iloc[:, [0, 3]]


# But you can also use negative indices (counting from the end) or using slices:

# In[19]:


# Take the first and last row and every second column starting at 1
# i.e., all odd columns
df.iloc[[0, -1], 1::2]


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Using a row and column slice, select the first three rows and the last three columns of the <tt>df</tt> dataframe and store it a new variable named <tt>df_todo</tt>.
# </div>

# In[20]:


""" Implement your ToDo here. """
### BEGIN SOLUTION
df_todo = df.iloc[:3, 1:]
### END SOLUTION


# In[21]:


""" Tests the above ToDo. """
if df_todo.index.tolist() != [0, 1, 2]:
    raise ValueError("Row index is incorrect!")
    
if df_todo.columns.tolist() != ['age', 'condition', 'wm_score']:
    raise ValueError("Column index is incorrect!")


# ### Boolean indexing
# A last, slightly trickier, indexing method is *boolean indexing*. This method is often used to select a specific subset of rows from a dataframe. It essentially boils down to creating a `Series` object with boolean values (i.e., `True` and `False` values) and using that in combination with `loc`. 
# 
# For example, suppose that you want to select all participants (i.e., rows) who are older than 21. First, you need to create a boolean series:

# In[22]:


b_idx = df.loc[:, 'age'] > 21
b_idx


# ... and then, you can use it together with `loc`:

# In[23]:


df.loc[b_idx, :]


# You can, of course, also do this within a single line of code:

# In[24]:


df.loc[df.loc[:, 'age'] > 21, :]


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Using boolean indexing, select all participants in condition A and store it in new variable named <tt>conA_pp</tt>.
# </div>

# In[25]:


""" Implement your ToDo here. """
### BEGIN SOLUTION
conA_pp = df.loc[df.loc[:, 'condition'] == 'A', :]
### END SOLUTION


# In[26]:


""" Tests the above ToDo. """
if len(conA_pp.columns) != 4:
    raise ValueError("Make sure you only filter the rows, not the columns!")
    
if conA_pp.index.tolist() != [0, 2]:
    raise ValueError("Hmm, the indexing operation didn't go as expected ...")
    
print("WELL DONE!")


# ## Adding and removing rows and columns
# When working with dataframes, at some point you'll may want to add columns and/or rows. You can actually use the `loc` and `iloc` indexers for this as well. For example, if you would like to add a new column named "nationality" to the dataframe, you can do the following:

# In[27]:


# Note: no list this time
df.loc[:, 'nationality'] = ['Dutch', 'British', 'Dutch', 'German']
df


# In the above cell we basically used `loc` to assign a list of values to a new column named "nationality". Importantly, this list should have the same number of values as the number of rows of the dataframe.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: In the same way as shown above, you can add rows to the dataframe. You got some new data from "sub-05" (a 23 year old French participant who was part of condition B and had a working memory score of 51). Add this to the existing dataframe (<tt>df</tt>) in the code cell below. Make sure not to overwrite the existing data by choosing a new index value (e.g., 4).
# </div>

# In[28]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
df.loc[4, :] = ['sub-05', 23, 'B', 51, 'French']
### END SOLUTION


# In[29]:


""" Tests the above ToDo. """
if df.iloc[-1, :].loc['participant_id'] != 'sub-05':
    raise ValueError("Hmm, the participant_id of the new row does not seem to be correct ...")
    
if df.iloc[-1, :].loc['age'] != 23:
    raise ValueError("Hmm, the age of the new row does not seem to be correct ...")

if df.iloc[-1, :].loc['condition'] != 'B':
    raise ValueError("Hmm, the condition of the new row does not seem to be correct ...")

if df.iloc[-1, :].loc['wm_score'] != 51:
    raise ValueError("Hmm, the wm_score of the new row does not seem to be correct ...")

if df.iloc[-1, :].loc['nationality'] != 'French':
    raise ValueError("Hmm, the nationality of the new row does not seem to be correct ...")

print("CORRECT!")


# To delete a row or column, you can use the `drop` method (see the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html) for more details). You can drop both columns (using the argument `columns`) and rows (using the argument `rows`) at the same time. For example, if I'd want to drop data fram "sub-05" and the entire "nationality" column, we could do the following:

# In[30]:


df.drop(columns='nationality', index=4)


# Note that the dataframe is not automatically updated! If we want to *replace* the original dataframe, we need to assign the result of the `drop` call to the original variable name (`df`):

# In[31]:


df = df.drop(columns='nationality', index=4)


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Try running the above cell again. You'll get an error! Do you understand why?
# </div>

# ## Dataframe operations
# `DataFrame` (and `Series`) objects have a lot of methods that implement common computational and statistical operations. Often, these methods return a new `DataFrame` or `Series` object with the result from the operation. For example, a useful method is `describe`, which returns a set of descriptive statistics for all numeric columns (i.e., it will automatically skip non-numeric columns):

# In[32]:


df.describe()


# Separate operations, like computing the mean, are also available:

# In[33]:


# Note that it returns a Series, because it consists
# of a single column (with two values)
df.mean()


# <div class='alert alert-warning'>
#     <b>ToDo</b>: Compute the standard deviation of the "age" column only using the appropriate dataframe method (google this!) and store single value in a new variable named <tt>age_sd</tt>.
# </div>

# In[34]:


""" Implement the ToDo here. """
### BEGIN SOLUTION
age_sd = df.loc[:, 'age'].std()
### END SOLUTION


# In[35]:


""" Tests the above ToDo. """
if round(age_sd, 3) != 2.872:
    raise ValueError("Something went wrong ...")

print("Well done!")


# ## Aggregation (advanced / optional)
# In the context of data analysis and statistics, you may want to perform operations separately for different subsets of the data. For example, you may want to compute the mean age separately for the different conditions. You may know this aggregation operation as creating a "pivot table". With pandas `DataFrame` objects, this can be easily done using the `groupby` method in combination with a particular operation. 
# 
# In the `groupby` method, you define by which factor you want to group your data (e.g., "condition") and you may subsequently "chain" it with another method (e.g, `mean`):

# In[36]:


means = df.groupby('condition').mean()
means


# Note that the group factor becomes the index in the resulting dataframe! Again, the mean operation is only performed for the numeric columns. To explain all of the functionality of the `groupby` method probably needs a completely separate tutorial, so let's just finish with a relatively more difficult (and optional) ToDo.

# <div class='alert alert-warning'>
#     <b>ToDo</b>: Below, we simulate a dataset with reaction time data (in ms.) across four groups ('A', 'B', 'C', 'D') of 25 participants each. Suppose that we want to, for each group separately, a one-sided t-test of reaction time (against a population mean of 300 ms.). Create a dataframe with 3 columns ("mean", "std", and "t_value") and 4 rows ('A', 'B', 'C', 'D', representing the groups), where the "t_value" column should contain t-values corresponding to the groups.
# </div>

# In[37]:


import numpy as np
np.random.seed(42)

data = np.random.normal(300, 70, 100)
cond = ['A', 'B', 'C', 'D'] * 25
df_final = pd.DataFrame({'rt': data, 'condition': cond})
df_final

### BEGIN SOLUTION
# Not necessarily the most elegant solution!
df_stats = df_final.groupby("condition").mean()
df_stats.columns = ['mean']
df_stats['std'] = df_final.groupby("condition").std()
df_stats['t_value'] = (df_stats.loc[:, 'mean'] - 300) / df_stats.loc[:, 'std'].pow(1. / 2)
df_stats
### END SOLUTION


# In[38]:


""" Tests the above ToDo. """
if df_stats.columns.tolist() != ['mean', 'std', 't_value']:
    raise ValueError("The dataframe does not contain the right columns!")
    
if df_stats.index.tolist() != ['A', 'B', 'C', 'D']:
    raise ValueError("The dataframe does not contain the right index!")

if df_stats.loc[:, 't_value'].round(3).tolist() != [-1.477, -1.713, -1.073, 0.374]:
    raise ValueError("T-values are not yet correct!")

print("YOU'RE AMAZING!")

