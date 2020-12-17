# The PsychoPy Coder, part 2 (tutorial)
In the previous tutorial, we discussed most of the "administrative" stuff that needs to happen in any PsychoPy experiment. In this tutorial, we'll discuss how to actually add components to the experiment, interact with user responses, and work with the experiment data.

## Components
Like in the Builder, *components* are the "bread and butter" in the Coder interface as well. In the coder, however, these components are implemented in different classes from the `psychopy` package. For example, to add a text component, you can use the `TextStim` class from the `psychopy.visual` module and to add a sound component, you can use the `Sound` component from the `psychopy.sound` module. 

Basically, every component from the Builder has an equivalent in the `psychopy` package. Moreover, each component has the same properties in the Builder as in the Coder. For example, the *color* and *font* properties from text components in the Builder are also available in the Coder interface as arguments (and attributes) of the corresponding component class. For example, to set the font of a text stim to Calibri and the text color to blue, initialize a `TextStim` object with `font='Calibri'` and `color=(-1, -1, 1)`.

Importantly, all visual stimulus classes (like `TextStim`, but not `Sound`) additionally need one (mandatory) argument: a `Window` object! This allows to `TextStim` to interact with the window. So, let's recap: to initialize a component in the Coder interface, we need to (1) import the corresponding class and (2) initialize it with a `Window` object (in case of visual components) and optionally other arguments that modify the component's behavior or display. 

Now, suppose you would like to welcome my participant by showing a short welcome message &mdash; "Welcome to this experiment!". To do so, you'd need a `TextStim` which would need to be initialized as follows:

```python
from psychopy.visual import TextStim

# We assume `win` already exists
welcome_txt_stim = TextStim(win, text="Welcome to this experiment!")
```

:::{admonition,attention} ToDo
Paste the code snippet above into your script, after initializing the window and clock. Note: it's convention to put all import statements together at the top of your script, so make sure the `from psychopy.visual import TextStim` part is on top of your script as well. Then, run the experiment.
:::

## Drawin' & flippin'
When running your experiment after including the welcome text component, however, the PsychoPy window does not show the text! This is because you first need to *draw* the stimulus! This can be done by calling the `draw` method that is included in each (visual) component class.

:::{admonition,attention} ToDo
After initialization of the text component, call the `draw` method (without arguments) of the `welcome_txt_stim` variable. Then, run your experiment.
:::

Argh, still no sign of the welcome text in the window! This is because your monitor contains [two buffers](https://en.wikipedia.org/wiki/Multiple_buffering), a "front buffer" (which is visible) and a "back buffer" (which isn't), and components are always drawn on the back buffer! To make the drawn components visible, we need to flip the back buffer to the front, which can be done by calling the `flip` method of the `Window` object. By splitting the operation of showing stimuli into two operations (drawing and flipping the back buffer), you can precisely control when you want your stimuli to appear (i.e., when calling `flip`). 

:::{admonition,attention} ToDo
Right after the call to the `draw` method of the text component (`welcome_txt_stim`), add a call to the `flip` method (without arguments) of the window (`win`). Then, run the experiment again.
:::

Finally, you should see the welcome text on the window, albeit quite briefly! Again, it is only shown briefly because PsychoPy will simply follow the script and immediatly go to the next lines (which presumably are those that close the window and quit the experiment). There are several ways in which you can specify how long a component is visible, which differ in how precisely they can determine the duration. One of the easiest ways is to add a call to the `wait` function after the window flip.

:::{admonition,attention} ToDo
Using the `wait` function, make PsychoPy wait for 2 seconds after flipping the window. Then, run the experiment again.
:::

Now you should see that the welcome text is visible for 2 seconds (actually, a bit longer because of the time it takes to shut down the experiment). In one of the next sections, we will discuss other (and more precise) methods to manipulate the duration of stimuli.

Note that after flipping the window such that the back buffer is moved to the front buffer, the back buffer is completely cleared. This means that when you'd flip the window *again* (without drawing any stuff in the meantime), the front buffer would contain an empty window!

:::{admonition,attention} ToDo
After the call to the `wait` function, flip the window again, and add another call to the `wait` function for two seconds (otherwise you won't see the effect of the second flip). Then, run the experiment again.
:::

By flipping the window again, the welcome text disappeared and was replaced by an empty window (because the front buffer was replaced by an empty back buffer). This underlines an important concept: *every time you flip the window, you start with an empty back buffer* (and you need to draw your stimuli again, if you want to show them again on the next flip).

## Responses
After welcoming our participant, let's add some instructions. Like we did in the Builder experiment, let's also make sure that, after reading the instructions, the participant can continue the experiment by pressing enter ("return"). This gives us an excuse to introduce the topic of working with participant responses!

But first, let's create a `TextStim` with the instructions:

> In this experiment, you will see emotional faces (either happy or angry) with a word above the image (either “happy” or “angry”).
> Importantly, you need to respond to the EXPRESSION of the face and ignore the word. You respond with the arrow keys:
>         
>   HAPPY expression = left<br>
>   ANGRY expression = right
>       
> (Press ‘enter’ to start the experiment!)

:::{admonition,attention} ToDo
Initialize a `TextStim` object with the text above and store it in a variable named `instruct_txt_stim`. Make sure it is left-aligned and has a font size of 0.085 (check the [docs](https://www.psychopy.org/api/visual/textstim.html) to see how to do this). Then, draw the `TextStim` and flip the window to make it visible!

Tip: you can create multi-line strings easily by enclosing text in triple-quotes, e.g., `""" some multiline text etc etc """` (more info [here](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string)). Then, call its `draw` method, flip the window to make it visible.
:::

### Keyboard responses
Now, just like we added a Keyboard component in the Builder tutorials to interact with keyboard responses, we can use the `Keyboard` class from the `psychopy.hardware.keyboard` module to do the same in the Coder interface! [This class](https://www.psychopy.org/api/hardware/keyboard.html) has a method called `getKeys`, which will return a list `KeyPress` objects with information (as attributes) about the keys pressed since the last time `getKeys` was pressed.

To implement the "wait-for-key-to-continue" routine, we can keep querying the `getKeys` method until we detect a "return" key, after which we continue the experiment.

:::::{admonition,attention} ToDo
Let's try to implement this! Import the `Keyboard` class at the top of your script and initialize a `Keyboard` object. Then, after drawing the instruction text (and the window flip), write some code that continually queries the `getKeys` function until it detects a "return" keypress and only then continues the script. Hint: a `while` loop (with a "break") would be useful here!

When you're done, run the experiment!

````{dropdown} Click here to show the solution (but try it yourself first!)

```python
kb = Keyboard()  # initialize keyboard obj
while True:
    # getKeys returns a list (here: `keys`)
    keys = kb.getKeys()

    # check if the return key is in the list
    if 'return' in keys:
        # If so, break out of the loop!
        break
```
````

:::::

If you want to learn a little more about keyboard interaction, try the next (optional and more difficult) ToDo!

:::{admonition,attention} ToDo (optional/difficult)
As mentioned before, the `getKeys` method returns a list of `KeyPress` objects. These objects contain several attributes with information about the key press: its name (`.name`, e.g., "return"), the reaction time in seconds relative to the initialization of the `Keyboard` class (`.rt`), the time in seconds the key went down in absolute time (`.tDown`), and the duration of the keypress (`.duration`). 

For each detected key press, print in a single statement the name of the key, its reaction time, and duration (e.g., "The 'a' key was pressed within 2.156 seconds for a total of 0.255 seconds"). Using [F-strings](https://realpython.com/python-f-strings/) would we nice here!
:::

### Mouse responses (optional)
Instead of interacting through the keyboard, you can interact with mouse responses of the participant. Whether you have participants respond with keyboard presses or with the mouse is of course up to you (and depends on your experiment)! For the sake of explaining how to implement interaction with mouse responses, let's add another screen to our experiments with a big, red button, which the participant has to click (with the mouse) in order to start the experiment.

Just like with keyboard responses, the `psychopy` package contains a class, `Mouse` (from `psychopy.event`), which implements interaction with the mouse. As can been seen in [the documentation](https://www.psychopy.org/api/event.html), a `Mouse` object can be initialized with several optional arguments (`visible`, `newPos`, and `win`) and contains various methods to query information about the mouse position (`getPos`) and mouse clicks/presses (`getPressed`). You can even set the position of the mouse (`setPos`) and make the mouse (temporarily) (in)visible (`setVisible`)!

:::{warning}
In the [documentation of the `psychopy.event` module](https://www.psychopy.org/api/event.html), you can also see several functions for keyboard interaction, such as `waitKeys` and `getKeys`, which overlap in functionality with the previously discussed `keyboard` class. [It is recommended](https://discourse.psychopy.org/t/3-ways-to-get-keyboard-input-which-is-best/11184) to use the `keyboard` class instead of the functions from the `event` module!
:::

Alright, let's start with our implementation. First, we need to import the `Mouse` class and initialize a `Mouse` object.

:::{admonition,attention} ToDo
Import the `Mouse` class at the top of your script and then initialize a `Mouse` object. Importantly, as indicated in the documentation, initialization should be done *after* initializing your `Window` object. Using the `visible` argument when initializing the `Mouse` object, make sure the mouse is initially invisible (check the [docs](https://www.psychopy.org/api/event.html)).
:::

We also need to create a big, red button for the participant to click! To create shapes using the `psychopy` package, you can use the [`ShapeStim`](https://www.psychopy.org/api/visual/shapestim.html#psychopy.visual.ShapeStim) class. This is a very broad class that allows you to create arbitrary shapes, like lines and polygons, by specifying the [vertices](https://en.wikipedia.org/wiki/Vertex_(geometry)) of the shape. Specifying the vertices of a circle is quite time intensive, so you can use the more "specialized" `Polygon` or `Circle` classes instead. 

:::{note}
Technically, the `Circle` class is a [subclass](https://pybit.es/python-subclasses.html) of the `Polygon` class, and the `Polygon` class is itself a subclass of the `ShapeStim` class. Being a subclass of another class means that the subclass "inherits" all methods from its "parent class" (but possibly with different default arguments). The subclass itself may, of course, contain additional or different methods and attributes.
:::

:::::{admonition,attention} ToDo
Add a big red button to the experiment using the `Polygon` or `Circle` class (up to you), store it in a variable named `button`, and draw it. As the `Polygon` and `Circle` classes are subclasses of the `ShapeStim` class, check out the [ShapeStim documentation](https://www.psychopy.org/api/visual/shapestim.html#psychopy.visual.ShapeStim) to see which arguments those classes take.

````{dropdown} Click here to show the solution (but try it yourself first!)

```python
from psychopy.visual import Circle  # or Polygon

# You may need to adjust the size if you have a rectangular screen (which is common)
# to get a circle instead of an oval
button = Circle(win, size=(0.25, 0.25), fillColor=(1, -1, -1))

# Alternatively:
# button = Polygon(edges=100, size=(0.25, 0.25), fillColor=(1, -1, -1))
button.draw()
```
````

:::::

Showing the participant the red button by itself may be a bit confusing, so let's add a `TextStim` with the text `"Click the red button to start the experiment"`!

:::{admonition,attention} ToDo
Add a `TextStim` as outlined above. Make sure it doesn't overlap with the red button! Draw it and flip the window. Then, run the experiment to see whether it works. 
:::

At this moment, the only thing we need to implement is a routine that halts the experiment until the participant clicked on the button using their mouse. [As described in the documention](https://www.psychopy.org/api/event.html), the `Mouse` class contains a very useful method, `isPressedIn`, which takes a `ShapeStim` (or a `ShapeStim` subclass) as input and returns a boolean (`True` or `False`) referring to whether the mouse is currently clicking in the area of the shape.

:::::{admonition,attention} ToDo
Add code that halts the experiment until the participant clicked the red button. Again, a while loop may be useful in this routine! Also, make sure the mouse disappears after the participant clickerd the button (check out the [docs](https://www.psychopy.org/api/event.html) to see how to do this). 

````{dropdown} Click here to show the solution (but try it yourself first!)
```python
while True:
    if mouse.isPressedIn(button):
        mouse.setVisible(False)
        break
```
````

When you're done, run the experiment to see whether it works!
:::::

## Timing revisited
Alright, now it's time for the most important part of our experiments: the trial loop! Just like the color-word Stroop experiment we implemented in the Builder, we'd like to create a set of trials in our emotion-word Stroop experiment. This also provides us with a nice opportunity to talk about duration and timing again!

Often, you'd like to make sure your trials/stimuli are presented for a specific duration. This is often especially important for perception and psychophysics studies or neuroimaging studies in which you track stimulus processing at high temporal resolution (e.g., EEG/MEG and eyetracking studies). 

So far, we only showed you how to use the `wait` function to control stimulus duration. There are, however, two other and more precise methods, which we'll call *clock-based* timing and *frame-based* timing. We'll discuss these two methods in turn. But first, let's create a stimulus. As we're creating an emotion-word Stroop task, we'll need an image with a emotional facial expression and an emotion word. 

To create an image, you can use the [`ImageStim`](https://www.psychopy.org/api/visual/imagestim.html) class from the `psychopy.visual` module. Apart from the mandatory argument `win` (the current window), it also needs an `image` (a path to the image file). In the `tutorials/week_2` directory, we included two images: `angry.png` and `happy.png`. Note that these images are smileys, because it's really hard to find proper facial expression stimuli without copyright ...

:::::{admonition,attention} ToDo
Import the `ImageStim` class, initialize an `ImageStim` object with the `angry.png` file (store this is in a variable with the name `stim_img`), and draw it. Also create a `TextStim` with the word "happy" placed above the smiley (store this is in a variable with the name `stim_txt`) and draw it. Then, flip the window and run the experiment to see whether it works as expected.

````{dropdown} Click here to show the solution (but try it yourself first!)
```python
stim_img = ImageStim(win, image='angry.png')
stim_img.draw()
stim_txt = TextStim(win, text='happy', pos=(0, 0.5))
stim_txt.draw()
win.flip()
```
````
:::::

Now, suppose we want to show the image/text for a specific duration, let's say 500 milliseconds, after which it disappears and the participant has to make a response for the experiment to continue. (Note that this is different from the way we implemented the color-word Stroop experiment in the Builder tutorials.) One way to specify the duration is using a clock!

### Clock-based timing
In the previous tutorial, we defined a "clock" (using the `psychopy.core.Clock` class) to do some trivial timing checks, but they can be used in much more useful ways, like controlling the duration of stimuli. To showcase this, let's create a new "trial clock" just after we flipped the window, which visualized the emotion-word trial:

```python
trial_clock = Clock()
```

Now, using a while loop in combination with continuously calling the `getTime` method, we can keep showing the stimulus until the clock has passed 500 milliseconds.

:::::{admonition,attention} ToDo
Try implementing the aforementioned while loop such that the image/text of the trial is visible for 300 milliseconds and disappears afterwards. Hint: if you don't want to execute anything inside the while loop, you can use the keyword `pass`. This is necessary, because a loop in Python can't ever be completely "empty". Also, make sure the image/text actually disappears after

````{dropdown} Click here to show the solution (but try it yourself first!)
```python
trial_clock = Clock()
while trial_clock.getTime() < 0.3:
    pass

# We need to flip the window to actually make the stimuli disappear!
win.flip()
```
````

:::::

Note that there is no need for our stimuli to be redrawn and our window to be flipped every iteration of the while loop! This is only necessary when you want to update your stimuli in the meantime (or when using the frame-based timing method, as discussed next).

### Frame-based timing (optional)
Although the clock-based method is reasonably accurate, it implicitly assumes that stimulus duration is *continuous*, while in reality it is discrete because it can only be drawn a specific number of screen refreshes! In other words, the *exact* duration of visual stimuli is some multiple of the number of screen refreshes. For example, if you have a 60 Hz screen (which refreshes every 1/60 seconds), a stimulus can be shown for 0.0167 seconds (1/60), 0.0333 seconds (2/60), 0.0500 seconds (3/60), etc. But it cannot be shown for, let's say, *exactly* 110 milliseconds. 

::::{admonition,attention} ToThink
Suppose you want to show a stimulus for 120 milliseconds on a monitor with a refresh rate of 60 Hz. What is the duration closest to 120 milliseconds you can achieve?

```{dropdown} Click here to see the answer (but try to come up with the answer yourself first)!
Dividing 120 milliseconds (0.120 seconds) by the refresh rate (1/60) you do not get a whole (integer) number, 7.2, meaning that 7 frames/flips is the best we can do, which results in 7 * (1/60) = 0.1167 seconds.
```
::::

So, if you *really* care about the duration of your stimuli (e.g., in subliminal perception studies), you should specify the duration of your stimuli as a multiple of your refresh rate. Then, to implement this in your PsychoPy script, you can simply draw your stimuli and flip your window as often as the number of frames you want to show your stimuli. For example, if you want to show your stimulus for 60 frames (i.e., 1 
second on a 60 Hz monitor), you simply do the drawing + flipping process 60 times!

:::::{admonition,attention} ToDo
Remove the your clock-based timing implementation (i.e., the while loop from the previous ToDo) and instead program a frame-based timing implementation instead (the duration should be 300 ms again). Hint: a for loop could be quite useful here!

````{dropdown} Click here to show the solution (but try it yourself first!)
```python
# 18 frames on a 60Hz monitor is 300 ms
for frame in range(18):
    # Draw stims again
    stim_img.draw()
    stim_txt.draw()
    # Flip window to make visible
    win.flip()

# We need to flip the window to actually make the stimuli disappear!
win.flip()
```
````
:::::

:::{tip}
Instead of re-drawing your stimuli every iteration of the loop across frames, you can also set the attribute `autoDraw` of visual components to `True`. This will automatically draw those stimuli upon flipping the window, until you set this attribute to `False` again!
:::

:::{tip}
For timing precision, it is very important that no other (CPU-heavy) programs are running while you're running your experiment! So make sure that, when you conduct actual experiments, you shut down all non-essential programs before starting your experiment.
:::

## Trial loops
So far, we only presented a single trial with a emotion word ("happy") and a(n angry) smiley. Like the color-word Stroop in the Builder tutorial, we'd like to present the participant multiple trials in which the two factors &mdash; emotion of the smiley (happy/angry) and the emotion word ("happy"/"angry") &mdash; vary.

So how do we define the different conditions? One way would be two create two lists, one with emotion words and one with the emotion for the smileys, and to choose a random value of each list in each iteration of the trial loop. In such a simple experiment, however, we would recommend to pre-specify the conditions in a CSV or Excel file &mdash just like we did in the Builder tutorial.

:::{admonition,attention} ToDo
Create a CSV or Excel file with two columns (named `smiley` and `word`) and twenty rows (excluding column names) with either "happy" or "angry" such that there are five trials of each possible emotion-word combination (just like you did in the Builder tutorial). Save it in the same directory as your Python script with the same `emo_conditions.xlsx` (or `emo_conditions.csv`). (If you want to see the "solution", check out the `emo_conditions.xlsx` file in the `solutions/week_1` directory of the course materials).
:::

To load in the data, we can use our *pandas* skills! In case of a CSV file, we can use the `read_csv` function and in case of an Excel file, we can use the `read_excel` function.

:::{admonition,attention} ToDo
Read in your `emo_conditions.{csv,xlsx}` file and store the resulting `DataFrame` object in a variable named `cond_df` ("conditions dataframe").
:::

We could start writing our trial loop by now, but this would present the trials just like we defined in the conditions file. Often, you'd want to present the trials in a (semi-)random order. To do so, we can simply shuffle the dataframe, which can be easily done using the [`sample` method](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) of `DataFrames` using a fraction (`frac`) of 1:

```python
cond_df = cond_df.sample(frac=1)
```

This method randomly samples all rows (because `frac=1`) from the dataframe, which is the same as shuffling it. The next step is to start writing a our trial loop! Because we have a fixed number of trials, we can use a for loop across the rows of our dataframe. The `iterrows` method of dataframes generates, row by row, the index and the row itself (as a `Series` object), so it's perfect for our purposes:

```python
for idx, row in cond_df.iterrows():
    # Extract current word and smiley
    curr_word = row['word']
    curr_smil = row['smiley']
```

Then, after extracting the smiley and word conditions, we can initialize a `TextStim` with the current word and an `ImageStim` with the current smiley, draw them, flip the window and wait for as long as we want to show the stimulus, and repeat this process until our trial loop has finished!

:::::{admonition,attention} ToDo
Try finishing the loop in the previous code snippet as indicated above. For now, assume a duration 500 milliseconds. Run the experiment when you're done!

````{dropdown} Click here to show the solution (but try it yourself first!)
```python
for idx, row in cond_df.iterrows():
    # Extract current word and smiley
    curr_word = row['word']
    curr_smil = row['smiley']

    # Create and draw text/img
    stim_txt = TextStim(win, curr_word, pos=(0, 0.7))
    stim_txt.draw()
    stim_img = ImageStim(win, curr_smil + '.png')
    stim_img.draw()

    # Show
    win.flip()
    
    # Wait a bit
    wait(0.5)
```
````
:::::

At this point, the stimuli are following each other instantly! It would be nice to have a, let's say, 1.5 second interstimulus interval (ISI) between each trial showing a fixation target.

:::::{admonition,attention} ToDo
Add code to the loop to show a simple plus sign (+) as a fixation target during the ISI.

````{dropdown} Click here to show the solution (but try it yourself first!)
```python
# No need to define the fix inside the loop, because it doesn't change!
fix = TextStim(win, '+')
for idx, row in cond_df.iterrows():
    # Extract current word and smiley
    curr_word = row['word']
    curr_smil = row['smiley']

    # Create and draw text/img
    stim_txt = TextStim(win, curr_word, pos=(0, 0.7))
    stim_txt.draw()
    stim_img = ImageStim(win, curr_smil + '.png')
    stim_img.draw()

    # Show
    win.flip()
    
    # Wait a bit
    wait(0.5)

    fix.draw()
    win.flip()
    wait(1.5)
```
````
:::::

Voilà, that's all you need for the trial loop! [Something about responses]

## Logging onsets (optional)


## Keeping track of and saving data
