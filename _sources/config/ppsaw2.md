# Assignment week 2
For this assignment, you have to program a *change detection* task to test participants' visual working memory. This should be programmed in the Coder interface of PsychoPy. This task consists of a set of trials in which the participant briefly sees a stimulus (usually a set of gratings, slanted lines, or shapes), which after a short delay reappears in the exact same configuration or slightly differently (e.g., one of the lines changed orientation). After the stimulus reappears, the participant then has to respond whether the stimulus changed or not. The idea, here, is that the participant needs to keep the stimulus in *visual working memory* to be able to perform the task. Often, the complexity of the stimulus, sometimes called *set size*, (e.g., the number of lines/shapes presented at each trial) is varied in order to manipulate the working memory load. 

Please read this page carefully before starting on your assignment.

```{margin}
For more information about the change detection paradigm, check out the article by [Rouder et al., (2011)](https://link.springer.com/article/10.3758%2Fs13423-011-0055-3)! {cite}`rouder2011measure`
```

In this assignment, you will program a relatively simple version of the change detection task involving random strings of integers (e.g., `286931`). To give you an idea of how the experiment should look like, we created a "demo" Builder version of it, which is included in the materials: `intropy/config/change_detection.psyexp`.

:::{admonition,attention} ToDo
Open the `change_detection.psyexp` file in the PsychoPy Builder interface and run the experiment.
:::

As you can see in the Builder, the experiment consists of the following elements:

* **A dialog box asking for the participant number**

    Make sure it asks for a participant ID (an integer).<br><br>

* **A welcome screen for 2 seconds**

    Use whatever text you like (as long as it's professional).<br><br>

* **An instruction screen (visible until participant pressed 'enter')**

    You may copy the text from the Builder experiment if you want. Make sure it is clear that the participant needs to press the left key when the stimulus was the same, and the right key when the stimulus changed.<br><br>

* **An initial fixation target (1 second)**

    You may use whatever fixation target you like.<br><br>

* **A trial loop consisting of both the trial itself and subsequent feedback**

    Make sure the trial is build up as indicated in the *Trial routine structure* below. Also, make sure the participant can quit the experiment during the trial loop when pressing the "q" key.<br><br>

* **An overview of the participant's performance**

    Make sure it shows the accuracy (proportion of correct trials) and a plot with reaction times. You may format your plot any way you like (lineplot, barplot, etc.).<br><br>

* **Saving the data**

    The data should be saved in the current directory with the filename `sub-xx_events.csv`, where `xx` refers to the submitted participant ID. This file should contain (at least) the following columns: `first_string` (the string presented the first time, e.g., "386291"), `second_string` (the string presented the second time, e.g., "386281"), `condition` (either "change" or "no_change"), `response` (either "left" or "right"), and `reaction_time` (in seconds, e.g., "0.6292389").

## Trial/feedback routine structure
Specifically, the trial + feedback part should be build up as follows:

* Presentation of the stimulus (0.5 seconds);
* A delay showing the fixation target (2 seconds);
* Second presentation of the (identical or changed) stimulus (0.5 seconds)
* Presentation of a fixation target (1.5 seconds)
* Presentation of colored feedback text ("Correct!" in green, "Wrong!" in red, or "Missed!" in white)
* Presentation of a fixation target (1 second)

### Stimulus criteria
In the Builder demo, we used random strings of six digits (0-9) to represent our stimuli, which may or may not contain a *single* changed digit in the second presentation. As such, there are two conditions: "change" and "no_change", if you will. You may define/generate your stimuli in any way you like (e.g., using an external conditions file, hardcoded in the script itself, etc.), but the stimuli have to meet the following criteria:

* There should be *at least* 20 unique stimuli (and thus at least 20 trials);
* Of all stimuli, 50% should belong to the "change" condition (and the other 50% to the "no_change" condition);
* For the stimuli in the "change" condition, each digit from the string should have the same chance of being changed;
* For stimuli in the "change" condition, only a *single* digit should be changed
* The changed digit (e.g., 4) should have an equal chance of being changed to any *other* digit (e.g., 0, 1, 2, 3, 5, 6, 7, 8, 9).

## Advanced version
If you complete the experiment as described thus far, you'll score an 9 (out of 10). For the remaining point, you need to add one "advanced" feature to the experiment: the ability to change the length of the string of digits when running the experiment. To do this, add another field to the dialog box, `nr_of_digits` (with a default of 6), which determines the length of the random strings of digits used in the entire experiment (e.g., when filling in 9, stimuli have 9 digits). The minimum number of digits should be 4 and the maximum should be 12 (otherwise, quit the experiment). In addition to the columns mentioned above, add a column `nr_of_digits` to the data file. Otherwise, the experiment and the criteria for the stimuli remain the same.

We highly recommend that you first try to implement the regular experiment and only then try to implement this advanced feature.

## Grading key
Your assignment will be graded on both qualitative criteria (5 points) and quantitative criteria (25 points), outlined below.

**Note**: this probably goes without saying, but if you hand in the compiled Builder script from the demo experiment, you will fail this assignment.

### Qualitative criteria (5 points)
The qualitative criteria are related to the quality of the code as well as the experiment. 

* **Readability of code (comments where needed, consistently formatted, etc.)**

    If you would give this script to someone who doesn't know PsychoPy, would they understand how it worked?<br><br>

* **Efficiency of code (no redundancy, i.e., repeated code)**<br><br>

    Use (for-) loops where needed. If you repeat code, consider writing a function for it.

* **"User experience"**

    Does the experiment look okay? Is the text readable?

### Quantitative criteria (25 points)
The following elements need to be incorporated as specified and work as expected:

* An dialog box (1 point);
* A welcome screen (1 point);
* Instructions (2 points);
* Trial/feedback routine:
  * Stimuli conform criteria (3 points);
  * Trial routine structure and timing (2 points);
  * Correct feedback text (2 points);
  * Correct feedback color (1 point);
* Overview routine:
  * Accuracy text (2 points);
  * Reaction time plot (2 points);
* Response key and reaction time are stored (3 points);
* Data is saved as a CSV file with proper name (and contains all specified columns; 3 points)
* Advanced `nr_of_digits` feature (3 points)

## Tips & tricks
You can find some tips and tricks for completing this assignment below (feel free to use or ignore as you like)!

* Start with the definition of your stimuli &mdash; this may be the hardest part of the assignment!
* Feel free to copy-paste stuff from the tutorials;
* Google is your friend; use it!
* You may specify your trial conditions any way you like, as long as it meets the criteria defined above;
* It doesn't matter which timing method you use (the `wait` function/clock-based timing/frame-based timing)

## Plagiarism
Although this is an "open-book" assignment, you may not work together on this assignment. In case we find out that students work together on this assignment, this will be reported as plagiarism to the exam committee. 

## Handing in your assignment
Hand in your experiment (a `.py` file) on Canvas: *Modules* &rarr; *Assignment 4 (PsychoPy)*. If you use additional files (e.g., custom Python modules you wrote, a condition file, etc.), create a zip-file with every file necessary for the experiment and upload this on Canvas instead.

The deadline for handing in the assignment is 3 PM. For every 30 minutes you hand in your assignment too late, 1 point (out of 10) will be deducted from your final grade.

<br><center><b>GOOD LUCK!</b> You got this.</center>
