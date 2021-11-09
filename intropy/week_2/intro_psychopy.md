# Introduction to PsychoPy (tutorial)
PsychoPy is currently the most used and complete Python package to create experiments. Before we will explain how to use it, please read the [overview](https://www.psychopy.org/about/overview.html) on the PsychoPy website.

Now, let's familiarize ourselves with PsychoPy. Let's start by opening PsychoPy! After opening, you'll see a "Tip of the Day" pop-up; you may ignore that for now and close it.

:::{warning}
On Mac, PsychoPy might not open right after starting it. In that case, clicking on the icon again seems to work.
:::

## Subwindows
Psychopy by default opens three subwindows: the *PsychoPy Builder*, the *PsychoPy Coder*, and the *Experiment runner*. The *Builder* is the graphical interface of PsychoPy, which you can use to create experiments without any code, whereas the *Coder* interface provides an editor in which you can program experiments using Python code (as provided by the PsychoPy package). The *Experiment runner* is a tool to create complex *sets* of experiments/tasks (e.g., a battery of different tasks or questionnaires). It also provides a "log" of whatever is happening in your experiment when you run it. In this tutorial, we will only discuss some general PsychoPy features, for which the *Builder* interface suffices, so you may close the *Coder* interface and the *Experiment runner* for now. 

To read more about the different interfaces, read the [Getting started](https://www.psychopy.org/gettingStarted.html) page on the PsychoPy website.

:::{note}
In this course's PsychoPy tutorials, we'll often refer to the PsychoPy documentation. This is not because we're too lazy to explain it ourselves. We do this because looking up and reading code/package documentation is an essential programming skill! Even experienced programmers (like your teachers) have to look up things in the documentation *all the time*.
:::

## Running an experiment
To get an idea what a PsychoPy experiment may look like, let's run a demo! We created a super simple demo that showcases some of the functionality of PsychoPy, which can be found in the materials: `tutorials/week_2/intropy_demo.psyexp`. In the next tutorial, we are going to discuss this in more detail. For now, run the demo by doing the following:

* Open the `intropy_demo.psyexp` file (File &rarr; Open);
* Then, click the large green "play" button (&#9658;) to start the experiment;
* This will open the *Experiment runner* and, after a couple of seconds, a new window;

:::{warning}
Currently, running experiments when PsychoPy is full screen doesn't (always) work... So make sure it's *not* full screen when you run the demo (or any experiment, really).
:::

After the experiment has finished, the experiment window closes automatically. In the *Experiment runner*, you see some information about the experiment (but nothing super interesting). Mac users may see some text mentioning "ApplePersistenceIgnoreState"; this is a harmless warning (not an error) and can be ignored. You may close the *Experiment runner* for now.

:::{tip}
Want to quit an experiment before it has finished? Press the escape key! In most experiments, this will abort the experiment.
:::

## Global preferences
PsychoPy as a lot of global settings, which you can view and change if you want. You can open the *PsychoPy Preferences* window by clicking on *PsychoPy* in the top-most menu bar and then on *Preferences*. Any changes you make here should be applied to future sessions. For now, no need to change any global preferences. 

## Experiment settings (Builder only)
When you are using the *Builder* interface, you can set several global settings in the *Experimental settings* window. To open this window, click on the gear icon (<span>&#9881;</span>). In the various tabs, you can edit the experiment's settings. For example, under the "Basic" tab, you can edit the "info dialog": a pop-up that asks the participant for some information. Which information is asked can be changed at the "Experimental info" line.

:::{admonition,attention} ToDo
Enable the info dialog by clicking the checkbox next to "Show info dialog" and add a new field, "age", to the info dialog (without a default value). Then, run the demo experiment again (press the escape key to quit). Just before the experiment window opens, you should see the info dialog pop-up! 
:::

Under the "Data" tab, there are various options to fine-tune how you want your experimental data to be saved. Next to "Data filename", you can specify the filename of the datafiles that will be saved. By default, a new directory, `data`, is created in which the files will be saved. In our demo experiment, we furthermore specified that the filename should be `sub-%s_%s'`, in which the format specifiers (`%s`) are replaced by the participant identifier (`expInfo['participant']`) and experiment name (`expInfo['expName']`). Here, `expInfo`, refers to a Python variable (a dictionary) that represents the info dialog pop-up (plus some additional information). This way, you can customize your output filenames according to the information provided by the participant!

:::{admonition,attention} ToDo (optional)
Assuming you added the "age" field to the info dialog earlier, try to add the participant's age to the output filename such that if, for example, participant 01 who is 29 years old does the experiment, the output filename will be `sub-01_age-29_intropy_demo` (+ extension). If you're feeling adventurous, try using F-strings instead of format specifiers!
:::

In addition to the mandatory "psydat" file (which we personally never used), you can also have Psychopy save an extensive log file and CSV files. We recommend always saving the log and the "trial-by-trial" CSV files.

Under the "Audio" tab, you can specify which soundlibrary Psychopy should use. Currently, Psychopy advises to use the Psychtoolbox (ptb) soundlibrary. The "Online" tab contains various settings to export your experiment to a format that can be used online (only applicable to *Builder* experiments), but this is beyond the scope of this course. 

Finally, the "Screen" tab contains several important settings that specify the experiment window. The "Screen" option (default: 1), for example, specifies on which screen the experiment should run in case of multiple monitor set-ups. You can also choose to run the experiment full screen (the default) or whether to specify a particular window size (in pixels) and the background color used in the window ("Color") and the colorspace used through the experiment ("Color space"). The standard background color is `[0, 0, 0]` in RGB space, where the first value specifies the amount of **R**ed, the second value the amount of **G**reen, and the third value the amount of **B**lue. These values can range from -1 (minimum amount) to 1 (maximum amount). The color `[0, 0, 0]` specifies gray (as you've seen in the demo). You can read more about PsychoPy's color spaces [here](https://psychopy.org/general/colours.html). Another important setting is the "Units" that Psychopy should use. 

:::{admonition,attention} ToDo
Please read the excellent explanation of the different settings for the "Units" on the [PsychoPy website](https://www.psychopy.org/general/units.html). To see the effect of a different unit for size, change "Units" from "height" to, e.g., "pixels" and run the demo experiment again.
:::

Another important setting is the *Monitor*. Here, you need to fill in the name of the specific monitor configuration you want to use in your experiment. How to create a monitor configuration is explained in the next section!

## Monitors
Another important element of each experiment, both in the *Coder* and *Builder* interface, is the monitor that it is displayed on. In Psychopy's [*Monitor Center*](https://www.psychopy.org/general/monitors.html), you can specify several properties of the monitor(s) that you intend to use for your experiment. Although it is not strictly necessary to specify a monitor for your experiment (if you don't, PsychoPy will use a default configuration), it is a prerequisite for some "Units" settings (such as *degree visual angle*)! If possible, we recommend always specifying a monitor.

To open the *Monitor Center*, click on the monitor icon ( &#xf108; ). You should see the default monitor `testMonitor`, which is, as the notes say, a "default (not very useful) monitor." To create a new monitor, click *New* and give your new monitor a name (e.g., "laptop"). Then, you can specify several properties of your monitor. For example, you can specify the number of pixels of your monitor (e.g., 1920×1080 for a full HD screen), which is important if you use the "pixel" setting under "Units". You can also set the screen distance, i.e., how far participants are seated from the monitor (important when stimuli are specified in [degrees visual angle](https://en.wikipedia.org/wiki/Visual_angle)) and the screen width.

Note that it is also possible to run a calibration procedure in the monitor center and to add the procedure's results to your monitor configuration. Such a calibration procedure makes sure your monitor displays colors as specified in your experiment. This procedure, however, needs specialized equipment (a photometer), which you most likely do not have at home, so you may ignore this for now.

:::{admonition,attention} ToDo
Create a new monitor specific to your own laptop/desktop monitor. Fill in your current screen distance, screen size, and screen width. When you're done, click *Save*. Set in the *Experiment settings* the "Units" to "deg" (visual degree angle) and run the demo experiment. Then, change the screen distance to 200 cm and run the demo experiment again. You should see that the size of the stimuli appears smaller on the screen.
:::

Alright, by now you know your way around PsychoPy, so you're ready to start with the [Builder interface](psychopy_builder_part1.md)!
