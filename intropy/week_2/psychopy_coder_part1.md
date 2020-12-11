# The PsychoPy Coder (part 1)
At last, we'll discuss the PsychoPy Coder! In this tutorial, we explain the basics of the Coder interface. In the next (and final) tutorial, we'll discuss the Coder interface in more detail. Like in the previous Builder tutorial, we will explain the concepts by walking you through the process of programming a real experiment. This time, we will create a variant of the classical color-word Stroop task, the *emotion-word Stroop* task, in which participants are presented with images of emotional facial expressions in combination with words describing emotions that are congruent with the images (e.g., an angry expression with the word "angry") or incongruent with the images (e.g., a happy exression with the word "angry").

## The `psychopy` package
When using the Builder interace, you've seen that, "under the hood", PsychoPy converts your Builder experiment to a Python script, which is then executed to run your experiment. If you look at this generated Python script closely, you'll see that most of the code is based on functions and classes from the `psychopy` Python package. Whereas the Builder interface generates such code from your graphical experiment, in the Coder interface you'll write your experiment using functionality from the `psychopy` package directly!

:::{tip}
If you plan on programming your PsychoPy experiment (so *not* use the Builder interface), you technically do not need the entire "standalone" PsychoPy package; installing the `psychopy` Python package would suffice and you could just write your experiments in your favorite editor (like [Visual Studio Code](https://code.visualstudio.com/)). However, as mentioned on the [Getting started](../getting_started/installation.md) page, getting the `psychopy` package to work is not easy, which is why we recommend the "batteries included" standalone version of PsychoPy.
:::

The `psychopy` package contains different modules for different features. For example, the `visual` module contains a class to specify and create a window and a large set of visual components (like text, image, and movie components) and the `event` module contains code to work with "events" such as mouse clicks/movement and keyboard presses. Check out PsychoPy's [reference manual](https://www.psychopy.org/api/api.html) for a complete overview of the package's modules.

As you will see, most of PsychoPy's functionality (like the different *components*) is implemented in custom classes, so your experience with object-oriented programming as discussed in week 1 will be very useful! 

:::{note}
In this tutorial, you'll notice that many of the properties of Builder elements (e.g., the *Experiment settings* and Builder components like *text* and *image* components) have the same name and can take the same values as the attributes of the corresponding classes in the Coder interface! 
:::

## The Coder interface
Now, let's get started by opening the Coder interface. 

:::{admonition,attention} ToDo
Open the Coder interface (*View* &rarr; *Open Coder view*). You may close the *Builder* interface for now.
:::

Like the Builder interface, the Coder interface has several subwindows (panes). The panel on the left represents the *Source assistant*, which lists all files in the current working directory (in the *File Browser* tab) and information about the Python modules in the current working directory specifically (in the *Structure* tab).

:::{admonition,attention} ToDo
By default, PsychoPy's current directory is its installation path. Although this is not strictly necessary for this tutorial, change it to the `tutorials/week_2` directory by clicking on the right arrow (*Jump to another folder*).
:::

At the bottom of the Coder interface in the *Shelf* pane, you'll find a so-called "Python shell". You can think of it as a type of command line (like we discussed in the first Jupyter notebook of week 1), but specifically for Python code. You can only run a single line at once, but it'll show the result immediately.

:::{admonition,attention} ToDo
Try writing some valid Python code in the Python shell (and pressing enter to run it), e.g., `1 + 1`. Note that the Python shell will remember variables if you define them, just like Jupyter notebooks, so you can also run multiple commands like this:

```python
>>> a = 5
>>> b = a ** 2
>>> b - a
```
:::

This Python shell is very useful to debug or try out short code snippets. For example, if you forgot what the function `#!python len` returns, you can for example run the command `#!python len([1, 2])` in the Python shell to find out (spoiler: an integer). 

Finally, the last pane in the middle is PsychoPy's code editor. Here, you can open any plain-text file (not just Python files!) which you can modify and save. In practice, of course, you'll probably mostly work with Python files in this editor. Like most code editors, the Psychopy code editor also does some code formatting and syntax highlighting. One thing you'll notice is that it by default uses two spaces (in contrast to the more conventional four spaces) for indentation.

Right now, there are probably no active files in your Psychopy code editor, so let's create one for our emotion-word Stroop task! 

:::{admonition,attention} ToDo
Create a new Python file (*File* &rarr; *New*) and save it as `emo_stroop.py` in the `tutorials/week_2` directory.
:::

Although you learned in week 1 that Python files should be run in a terminal on the command line (e.g., `python emo_stroop.py`), Python files within the PsychoPy coder are actually run the same way as Builder experiments: by clicking on the big green play (&#9658;) button!

:::{admonition,attention} ToDo
Add some code to your `exp_stroop.py` file, e.g., `#!python print("PsychoPy 4evah")`, and run the file.
:::

After clicking the *Run experiment* button, the *Experiment runner* window should pop up, displaying something like the following:

```
#### Running:/Path/to/your/file/emo_stroop.py ####
PsychoPy 4evah
##### Experiment ended. #####
```

As you can see, the *Experiment runner* shows your print statement; remember this, as it is a nice way to debug your experiments!

## Dialog boxes
Arguably the first step in many experiments is providing the experiment with some information about the current session, such as the participant number, condition the participant is in, etc. In Builder experiments, you can implement this in the *Experiment settings* (under the *Basic* tab). The equivalent functionality in the Coder interface is implemented in the `psychopy.gui` module. 

The `psychopy.gui` module contains different classes to create [dialog boxes](https://en.wikipedia.org/wiki/Dialog_box), but arguably the easiest one to use is the `DlgFromDict` class. This class needs a single mandatory argument upon initialization: a dictionary in which the keys represent the dialog's fields (e.g., "participant_id") and the values represent the default for each field. (If you set a value to an empty string, `''`, there won't be a default value.)

For example, if you'd like a dialog box in which the participant number can be filled in, you can do the following:

```python
exp_info = {'participant_nr': ''}  # no default!
dlg = DlgFromDict(exp_info)
```

Note that it is quite important to create the dictionary before passing it to the `DlgFromDict` class instead of passing it directly, e.g., `#!python DlgFromDict({'participant_nr': ''})`. This is because PsychoPy will modify the dictionary (i.e., the variable `exp_info` in the code snippet above) with the information filled in by the participant/experimenter.

:::{admonition,attention} ToDo
In your experiment, create a dialog box with the fields "participant_nr" and "age", in which the participant number should have the default `99` (for testing purposes) but age should not get a default value. Don't forget to import the `DlgFromDict` class first! Then, run your experiment.
:::

As you can see, when you run the experiment, a dialog box appears! After you filled in the required information, you can click *OK* to start the experiment. Notably, after you fill in the fields of the dialog box (e.g., with participant number `01` and an age of `29`), you can access this information from the original dictionary passed to the `DlgFromDict` class (i.e., `example_info` in the code snippet above). For example, `exp_info['age']` will return the age that the participant filled in (e.g., `29`).

:::{warning}
The type of the values from the dictionary depend on the type of the variables you initialized the dictionary with. For example, if you initialize a particular value with an empty string (i.e., `''`, such as with "participant_nr" in the code snippet above), then the value representing that field will also be a string, even if you fill in a number (such as `1`)!
:::

Let's do an exercise to see whether everything's clear so far.

:::{admonition,attention} ToDo
Given the dialog box configuration from the previous ToDo, include a print statement to your script that will print out the following: "Started the experiment for participant ... with age ...", where the triple dots are replaced by whatever you filled in when running the experiment.
:::

Currently, it doesn't matter whether the user clicked on *OK* or *Cancel* in the dialog box &mdash; in both cases, PsychoPy would have continued with the script. It would be nice to actually quit the experiment when the user pressed *Cancel*. To do so, we can use the attribute `OK` from the dialog box object, which is set to `True` when the user clicks on *OK* and is set to `False` when the user clicks on *Cancel*. To quit the experiment, we can use the function `quit` from the `psychopy.core` module. Then, we can implement something like the following to quit the experiment when the user clicked on *Cancel* instead of *OK* (assuming the dialog box object is named `dlg` and the `quit` function has already been imported):

```python
if not dlg.OK:
    # Maybe add a nice print statement?
    print("User pressed 'Cancel'!")
    quit()
```

We recommend adding this snippet right after initialization of the dialog box in every experiment that actually uses a dialog box! Now, those that want a challenge, try the following (optional) ToDo. 

:::{admonition,attention} ToDo (optional)
Add some code after the `if not dlg.OK` code block that also quits the experiment when the user fills in an invalid participant number (let's say, anything higher than 99) or an invalid age (let's say, below 18). Try running the experiment with different values for these two options to see whether your implementation works as expected!
:::

Note that the `DlgFromDict` in fact can be customized much by using different arguments upon initialization. Check out the [documentation](https://www.psychopy.org/api/gui.html) to learn more. 

Now, so far we haven't really discussed how to actually create proper experiments, so let's start with arguably the most important element of Coder exeriments: the `Window`.

## The `Window`
One of the most important classes from the `psychopy` package is the `Window` class, which defines the window in which you are going to run your experiment. It is quite a complex class, with many different attributes and methods; we'll discuss the most important ones in this tutorial.

You can import the `Window` class from the `visual` module of the `psychopy` package (i.e., `#!python from psychopy.visual import Window`). This, by itself, does nothing; for the experiment window to appear, we need to intialize an object with the `Window` class. There are *a lot* of arguments that can be used upon initialization (for an overview, see the [docs](https://www.psychopy.org/api/visual/window.html)), but all arguments have sensible defaults, so you can initialize a `Window` object as follows:

```python
win = Window()
```

Note that you may use any variable name for your `Window` object, but we recommend naming it `win` like in the code snippet above, as it's short but descriptive.

:::{admonition,attention} ToDo
Initialize a `Window` object as shown in the above code snippet and run your experiment! Don't forget to also import the `Window` class!
:::

When running the current experiment, you should briefly see a gray window pop up. This is the "default" experiment window. We can, of course, change the way it looks by passing it arguments upon initialization! We can, for example, change the size by passing a tuple with the width and height in pixels to the argument `size`. For example, if you'd want a window of (for some reason) 400 (width) by 800 (height) pixels, you'd initialize your `Window` as follows:

```python
win = Window(size=(400, 800))
```

Most of the times, though, you'd probably want to run your experiment in "full-screen" mode. To do so, pass `True` to the argument `fullscr` (i.e., `#!python win = Window(fullscr=True)`). Note that if you specify `fullscr=True` but leave the window's `size` at its default (i.e., `(800, 600)`), you'll see a warning in the *Experiment running* saying "User requested fullscreen with size [800, 600], but screen is actually ... Using actual size". This warning is harmless and can be ignored, but if you want to prevent this warning, you should specify the actual size of your monitor as well (e.g., `size=(1920, 1080)` for an HD monitor).

You can also change the window's background color by passing a list or tuple with three numbers, corresponding to the desired RGB values, to the `color` argument.

:::{admonition,attention} ToDo
Although we don't recommend doing so in a real experiment, try making the window's background color bright blue. Want a more challenging exercise? Try to set the background to bright orange. Hint: note that PsychoPy assumes that RGB values range from -1 (minimum) to 1 (maximum), not from 0 to 255!
:::

Another important argument of the `Window` class is the `monitor`, to which you can pass the name of the monitor, as defined in the monitor center, you want to use for this experiment. For example, if you defined a monitor in the monitor center with the name "laptop", you can pass this configuration to the `Window` class as follows:

```python
win = Window(monitor='laptop')
```

:::{admonition,attention} ToDo (optional/difficult!)
If you don't want to use the monitor center at all (e.g., when you're programming your experiments in an external code editor), you can also programmatically using the `Monitor` class from the `psychopy.monitor` module. Try creating a monitor configuration for your own laptop/desktop monitor. Make sure you set the monitor's size (in pixels), width (in cm), and distance between you to the monitor (in cm). The [documentation of the `monitor` module](https://www.psychopy.org/api/monitors.html) contains all info you need to do this! 
:::

Finally, the last important argument of the `Window` class is the type of *units* that should be used by default for your components (which we'll discuss later), such as "norm" (for normalized units), "deg" (for visual degree angle), and "pix" (for pixels). As said before, there are in fact many more arguments to pass to the `Window` class (see the [documentation](https://www.psychopy.org/api/visual/window.html) for an overview), but we believe that the ones we discussed here are most important to know and that the other arguments all have sensible defaults.

:::{admonition,attention} ToDo
Let's create a `Window` object that we'll use for the rest of our emotion-word Stroop experiment! Make sure it is shown in full-screen mode, uses normalized units, uses the monitor specification of your own laptop/desktop monitor, and has a black background. Run your experiment to see whether it looks like expected! 
:::

Note that you can also change `Window` attributes after creating the object by directly editing the attributes. For example, if you'd want to change the units after initialization to pixels, you can do the following:

```python
win.units = 'pix'
```

## Timing & clocks
When you run the current experiment, you'll only see a black screen for like a second or so before it disappears again. The reason why the window doesn't stay open is because we don't tell it to! It is important to realize that PsychoPy will run the experiment script from top to bottom (like any Python file is run, actually) and will close the window once the script ends. Put differently, you can interpret the script as a chronological chain of events from the top of the script (beginning) to the bottom of the script (end). 

So, if you want to keep the window open for a little longer, we can simply tell PsychoPy so! There are, in fact, different ways to do this, but arguably the easiest way is using the `wait` function from the [`psychopy.core`](https://www.psychopy.org/api/core.html) module. We can pass this function a number corresponding to the amount of time (in seconds) PsychoPy should wait before continuing with the rest of the script.

:::{admonition,attention} ToDo
Import the `wait` function from the `psychopy.core` module and, after initializing the window, use it to make PsychoPy wait 2 seconds. Then, run the experiment.
:::

When you ran the experiment after adding the call to the `wait` function, you may have noticed that the window was active for more than 2 seconds. This because, as we mentioned earlier, it takes a while to close the window. 

Another important timing-related concept in PsychoPy is "clocks". Clocks allow you to precisely keep track of the timing of events, which is especially important in studies that need strict control of stimulus onsets and duration, such as psychophysics and neuroimaging experiments. This functionality in PsychoPy is implemented in, you guessed it, the `Clock` class (from the `psychopy.core` module). The `Clock` class does not require any arguments upon initialization, so you can simply create a `Clock` object as follows:

```python
clock = Clock()
```

The variable name, `clock`, is of course arbitrary; name it whatever you like! Upon initialization, the clock's time is set to 0. If you, at some point, want to know how much time has passed since the clock's initialization, you can call the `getTime` method:

```python
t_since_init = clock.getTime()
print(t_since_init)  # prints time (in sec.)
```

Now, with our knowledge about clocks, let's check whether the `wait` function actually makes PsychoPy wait as long as we tell it. 

:::{admonition,attention} ToDo
Import the `Clock` class and, after creating a `Window` object, initialize it. Then, query the time using `getTime` and store it in a variable (e.g., `t_before_wait`). Aftewards, make PsychoPy wait for 2 seconds (using the `wait` function), and finally, query the time again and store in another variable (e.g., `t_after_wait`). Make your script print the time before `wait` call, after the `wait` call, and the difference between those two times. Then, run the experiment.
:::

If you implemented the ToDo correctly, you should see that the time just after initialization of the clock is very close to zero (e.g., `#!python 7.83892915e-06`) and that both the time after the `wait` call and the difference before and after the `wait` call is approximately `2` seconds &mdash; just like we expected!

Two other important methods of the `Clock` class are `reset`, which sets the clock's time back to zero, and `add`, which &mdash; paradoxically &mdash; subtracts time from the clock. These two features will be discussed in detail in the next tutorial.

## Quitting the experiment
As you've seen so far, when the Python interpreter arrives at the end of your script, the PsychoPy window automatically closes and the Python process finishes. In the context of PsychoPy experiments, however, it is good practice to end the experiment by explicitly closing the window using the window's `close` method *and* then calling the `quit` function from the `core.psychopy` module (as we did before in the section on dialog boxes). Although not strictly necessary, calling the `close` method and the `quit` function perform a bit of bookkeeping that may prevent issues, so we recommend always including this at the very end of your script!

:::{admonition,attention} ToDo
At the end of your script, add the code to close your window and to quit the experiment. While you're at it, remove the calls to the `getTime` methods and the associated `print` statements, such that you only have the imports, code related to the dialog box, window and clock initializations, and the calls to the `close` method and `quit` function left.
:::

This tutorial features some of the most important, but arguably boring, aspects of programming experiments in the PsychoPy Coder, so let's continue with the [next (and final) tutorial](psychopy_coder_part2.md) which discusses creating components and other fun stuff!

:::{tip}
If you want the "solution" to the implementations from the ToDos, check out the file `solutions_coder_part1.py` (from the `solutions/week2` directory) in the PsychoPy editor, which contains the code from most ToDos.
:::