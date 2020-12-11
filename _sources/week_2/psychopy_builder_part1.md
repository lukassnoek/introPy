# The PsychoPy Builder
In this tutorial, we will discuss and show you how to use the *Builder* interface of PsychoPy. We will explain the basic elements of the Builder interface so that, in the next tutorial, we can focus more on the implementational details by building a new experiment from scratch.

You might think, "Why learn how to use a graphical interface in a programming course?" The reason we first teach you how to use the *Builder* interface is because it allows us to focus on the structure of experiments before elaborating on the underlying code. Another advantage of Builder experiments is that they can be used online! (But this is beyond the scope of this course.)

:::{admonition,attention} ToDo
Read [this page](https://workshops.psychopy.org/3days/10introductions.html) which discusses the respective advantages of the Builder and Coder interface in more detail.
:::

## Builder vs. Coder
As discussed before, the Builder and Coder interfaces can both be used to create experiments. Whereas the Builder allows you create experiments graphically, the Coder allows you to program your experiment directly in Python. It is important to realize, though, that when PsychoPy runs Builder experiments, it actually first generates (or "compiles") the experiment as a Python file (as if you created it using the Coder)! 

:::{admonition,attention} ToDo
Let's see this Builder-to-Coder compilation in action. If you haven't loaded the demo Builder experiment (`intropy_demo.psyexp`), do so now. Then, click the *Compile to script* button (right of the *Edit experiment settings* button). This should open the *Coder* interface with the code equivalent of the demo Builder experiment!
:::

The generated `intropy_demo.py` script contains the code necessary to run the experiment originally specified in the Builder interface (i.e., in the `intropy_demo.psyexp` file). In fact, everytime your run a Builder experiment on your own computer, Psychopy first generates the corresponding Python script, which is then executed to start the experiment. 

Most of the time, you can ignore the script associated with your Builder experiment. It may, however, give you some insight about what is going on "under the hood". Take a look at the generated script; do you see elements from the demo experiment (e.g., the text or images shown during the demo experiment)?

## Elements of the Builder interface
Now, let's take a look at the elements of the Builder interface. Make sure you (still) have the demo experiment active in the Builder. Apart from the list of icons on top of the Builder window, there are several subwindows (or panes): the *Routines* pane, the *Components* pane, and the *Flow* pane. We'll discuss these in turn.

### The routines pane
The [*Routines* pane](https://www.psychopy.org/builder/routines.html
) consist of the different elements of your experiment, where each element gets its own tab. In the demo experiment, for example, there are four routines: *intro*, *show_stimulus*, *gabor*, and *wrap_up*. Each routine may consist of multiple components (e.g., text, images, and sounds). For example, if you click on the *intro* routine tab, the routine pane shows, across different "rows", that this routine consists of three consecutive text components (*hello*, *welcome*, and *wait_key*) and a "keyboard" component (*key_resp*). Moreover, the routine pane also shows you the onset and offsets of the different components. Note that routines do not *have to* contain multiple components; for example, the *show_stimulus* routine only contains a single component (i.e., *stim*). It's up to you how you how you structure your routines!

:::{admonition,attention} ToThink
In the *intro* routine, the *wait_key* and *key_resp* components seem to lack an explicit offset. Considering the demo experiment, do you understand why?
:::

### The components pane
The [*components* pane](https://www.psychopy.org/builder/components.html
) contains, as you might have guessed, the different components you can include in your routines. Some of the most used components are listed under *favorites* (such as *text* and *image* components). The *stimuli* section contains various different stimulus components you might want to use in your experiment, such as [dot stimuli](https://www.psychopy.org/builder/components/dots.html), [gratings](https://www.psychopy.org/builder/components/grating.html), and [sounds](https://www.psychopy.org/builder/components/sound.html). The *responses* section contains several components that facilitate interaction with the participant. For example, the [mouse component](https://www.psychopy.org/builder/components/mouse.html) allows you to record and use mouse movements and clicks and the [rating scale component](https://www.psychopy.org/builder/components/ratingscale.html) creates a rating scale which you can use to collect ratings on, for example, questionnaire items.

By clicking on a particular component, a pop-up appears in which you can set the *properties* of the component, such as the component name, onset and and duration, and several component-specific properties. For example, if you click on a *text* component, you can set the color, font, font size ("letter height"), position, and of course the text itself. 

:::{tip}
In the properties window, if you hover your cursor over the different options, you see a little window with an explanation of that option! Also, the PsychoPy documentation contains detailed information about each component. The easiest way to find the appropriate page is, in my experience, just googling "psychopy component {component name}".
:::

In the properties window, if you click the "OK" button, PsychoPy will add this component to the currently active routine. If you want, you can still change the properties afterwards. We will discuss setting component properties in more detail in the next tutorial!

:::{admonition,attention} ToDo (optional)
Try adding another *text* component with the text "The end!" to the *wrap_up* routine. Make sure it immediately starts after the *goodbye* component and it lasts one second. Run the experiment to see whether it worked!
:::

### The flow pane
Finally, the [*flow* pane](https://www.psychopy.org/builder/flow.html) shows and defines the order of your experiment's routines. In the demo experiment, for example, the flow pane shows that the experiment starts with the *intro* routine, followed by the *show_stimulus* routine, and finally the *gabor* and *wrap_up* routines. The colors of the routines in the flow pane indicate whether the routines has a known and exact duration (green) or not (blue or red). For experiments in which precision of onsets/offsets is not crucial, this is not really important. But in experiments in which you want to be sure your routines' onsets, offsets, and durations are precise (i.e., [non-slip timing](https://www.psychopy.org/general/timing/nonSlipTiming.html) in PsychoPy lingo), such as in neuroimaging experiments, you want to make sure each routine is green.

:::{admonition,attention} ToThink
Do you understand why the *intro* routine is blue instead of green? Hint: the answer to this question is the same as to the previous *ToThink*.
:::

:::{admonition,attention} ToDo (optional)
Try inserting a new routine at the end of the experiment flow (i.e., after the *goodbye* routine). For example, create a new routine called *the_end* (in the top menu: *Experiment* &rarr; *New routine*) with a single text component lasting 1 second. Then, to insert it in the experiment flow, click on *Insert Routine*, select your new routine, and click on the flow line in between *wrap_up* and the arrow head to insert it!
:::

Anothing think you might encounter in the flow pane is "loops", like the *stimulus_loop* in the demo experiment. This functionality allows you to, well, add loops across routines! In the demo experiment, we use this to repeat our *show_stimulus* routine for the three different images. This is, of course, much more efficient than creating three different routines (or, equivalently, a single routine with three image components)! We will discuss loops in more detail in the next tutorial!

Alright, now you should know enough of the Builder functionality to start creating a new experiment, which we'll do in the [next tutorial](psychopy_builder_part2.md).