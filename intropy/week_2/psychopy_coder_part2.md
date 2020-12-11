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
After welcoming our participant, let's add some instructions. Like we did in the Builder experiment, let's also make sure that, after reading the instructions, the participant can continue the experiment by pressing enter ('return'). This gives us an excuse to introduce the topic of working with participant responses!

But first, let's create a `TextStim` with the instructions:

> In this experiment, you will see emotional faces (either happy or angry) with a word above the image (either “happy” or “angry”).
> Importantly, you need to respond to the EXPRESSION of the face and ignore the word. You respond with the arrow keys:
>         
>   HAPPY expression = left<br>
>   ANGRY expression = right
>       
> (Press ‘enter’ to start the experiment!)

:::{admonition,attention} ToDo
Initialize a `TextStim` object with the text above and store it in a variable named `instruct_txt_stim`. Make sure it is left-aligned and has a font size of 0.085 (check the [docs](https://www.psychopy.org/api/visual/textstim.html) to see how to do this).

Tip: you can create multi-line strings easily by enclosing text in triple-quotes, e.g., `""" some multiline text etc etc """`. Then, call its `draw` method, flip the window to make it visible.
:::

Now, just like we added a Keyboard component in the Builder tutorials to interact with keyboard responses, we can use the `Keyboard` class from the `psychopy.hardware.keyboard` module to do the same in the Coder interface! [This class](https://www.psychopy.org/api/hardware/keyboard.html) has a method called `getKeys`, which will return a list `KeyPress` objects with information (as attributes) about the keys pressed since the last time `getKeys` was pressed.

Alright, let's pick that apart a little bit.

:::{admonition,attention} ToDo
Add the correct import statement to the top of your script and then add the following Python code right after your last call to the window's `flip` method:

```python
kb = Keyboard()
while True:
    # getKeys returns a list (here: `keys`)
    keys = kb.getKeys()

    # check if the return key is in the list
    if 'return' in keys:
        # If so, break out of the loop!
        break
```

Then, run the experiment.
:::

As you can see, you can implement the wait-for-keypress routine using a `while` loop in which you keep calling the keyboard's `getKeys` function and breaking out of it when the result of the `getKeys` method (a list) contains the key you want the participant to press.

:::{admonition,attention} ToDo (optional/difficult)
As mentioned before, the `getKeys` method returns a list of `KeyPress` objects. These objects contain several attributes with information about the key press: its name (`.name`, e.g., "return"), the reaction time in seconds relative to the initialization of the `Keyboard` class (`.rt`), the time in seconds the key went down in absolute time (`.tDown`), and the duration of the keypress (`.duration`). 

Within the `if 'return' in key` block, for *each* key that has been pressed in the meantime, print in a single statement the name of the key, it's reaction time, and duration (e.g., "The 'a' key was pressed within 2.156 seconds for a total of 0.255 seconds").
:::

* Stuff about `waitKeys`.
* Multiple components

## Timing revisited

* clock vs. frames
* Check how long it takes to initialize a stimulus
* Stuff about autoDraw

## Logging onsets


## Saving data