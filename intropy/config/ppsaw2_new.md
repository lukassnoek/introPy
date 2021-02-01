# Assignment week 2
For this assignment, you have to program a *change detection* task to test participants' visual working memory. This should be programmed in the Coder interface of PsychoPy. This task consists of a set of trials in which the participant briefly sees a stimulus (usually a set of gratings, slanted lines, or shapes), which after a short delay reappears in the exact same configuration or slightly differently (e.g., one of the lines changed orientation). After the stimulus reappears, the participant then has to respond whether the stimulus changed or not. The idea, here, is that the participant needs to keep the stimulus in *visual working memory* to be able to perform the task. Often, the complexity of the stimulus, sometimes called *set size*, (e.g., the number of lines/shapes presented at each trial) is varied in order to manipulate the working memory load. 

*Please read this page carefully and from top to bottom before starting on your assignment.*

```{margin}
For more information about the change detection paradigm, check out the article by [Rouder et al., (2011)](https://link.springer.com/article/10.3758%2Fs13423-011-0055-3)! {cite}`rouder2011measure`
```

In this assignment, you will program a relatively simple version of the change detection task involving random strings of integers (e.g., `286931`). To give you an idea of how the experiment should look like, we created a "demo" Builder version of it, which is included in the materials. If you didn't download the materials already, please follow the instructions in the *Downloading the material* section on the [installation page](../getting_started/installation.md).

In the unzipped folder (probably called *intropy*), there is another folder called *intropy*, which contains yet another folder called *config*. This folder contains a Builder experiment with the name `change_detection.psyexp` (so the full path is: `intropy/intropy/config/change_detection.psyexp`). In the same folder, there is a CSV file named `cd_conditions.csv`, which contains the trial attributes of the experiment.

:::{admonition,attention} ToDo
Open the `change_detection.psyexp` file in the PsychoPy Builder interface (*File* &rarr; *Open* &rarr; select the `change_detection.psyexp` file) and run the experiment.
:::

Essentially, for this assignment, you'll need to recreate the change detection Builder experiment in the Coder interface. Like the Builder version, your Coder experiment should contain the following elements:

* **A dialog box asking for the participant number**

    Asking for a participant ID (a number).<br><br>

* **A welcome screen for 2 seconds**

    Use whatever text you like (as long as it's professional).<br><br>

* **An instruction screen (visible until participant pressed 'enter')**

    You may copy the text from the Builder experiment if you want. Make sure it is clear that the participant needs to press the left key when the stimulus was the same, and the right key when the stimulus changed.<br><br>

* **An initial fixation target (1 second)**

    You may use whatever fixation target you like.<br><br>

* **A trial loop consisting of both the trial itself and subsequent feedback**

    Make sure the trial is build up as indicated in the *Trial routine structure* below.<br><br>

* **An overview of the participant's performance (5 seconds)**

    Make sure it shows the accuracy (proportion of correct trials) in a `TextStim`.<br><br>

* **Saving the data**

    The data should be saved in the current directory with the filename `sub-xx_events.csv`. This file should contain (at least) the following columns: 
    
    * `first_string` (the string presented the first time, e.g., "386291")
    * `second_string` (the string presented the second time, e.g., "386281")
    * `condition` (either "change" or "no_change")
    * `response` (either "left" or "right")
    * `reaction_time` (in seconds, e.g., "0.6292389").

## Trial/feedback routine structure
Specifically, the trial + feedback part should be build up as follows:

* Presentation of the stimulus (0.5 seconds);
* A delay showing the fixation target (1.5 seconds);
* Second presentation of the (identical or changed) stimulus (0.5 seconds)
* Presentation of a fixation target during which the participant has to respond (1.5 seconds)
* Presentation of colored feedback text ("Correct!" in green, "Wrong!" in red, or "Missed!" in white; 0.5 seconds)
* Presentation of a fixation target (i.e., an inter-stimulus interval; 1 second)

### Stimuli
We already created the stimuli for you, which we stored in the `cd_conditions.csv` file (located in the same directory as the `change_detection.psyexp` file).

:::{admonition,attention} ToDo
Open the `cd_conditions.csv` file in Excel/LibreOffice or a plain-text file editor (e.g., Notepad).
:::

The CSV file contains 20 rows for 20 trials, with the following attributes (column names):

* `first`: the first stimulus (for the first presentation)
* `second`: the second stimulus (for the second presentation)
* `changed`: whether the stimulus is changed (`1`) or not (`0`)
* `correct_resp`: the correct response for this trial (either "left" or "right" arrow key)

We recommend you use this file (after reading it in using Pandas) in your experiment, but you don't have to! It's completely fine to generate the stimuli yourself using your own Python code. (In fact, if you want to complete the *Advanced Feature*, you *have to* create them yourself.) If you do so, please make sure the stimuli (i.e., digits) adhere to the following criteria:

* There should be at least 20 unique stimuli (and thus at least 20 trials);
* Of all stimuli, 50% should belong to the “change” condition (and the other 50% to the “no_change” condition);
* For the stimuli in the “change” condition, each digit from the string should have the same chance of being changed;
* For stimuli in the “change” condition, only a single digit should be changed
* The changed digit (e.g., 4) should have an equal chance of being changed to any other digit (e.g., 0, 1, 2, 3, 5, 6, 7, 8, 9).

## Advanced version
If you complete the experiment as described thus far, you'll score an 9 (out of 10). For the remaining point, you need to add one "advanced" feature to the experiment: the ability to change the length of the string of digits when running the experiment. To do this, add another field to the dialog box, `nr_of_digits` (with a default of 6), which determines the length of the random strings of digits used in the entire experiment (e.g., when filling in 9, stimuli have 9 digits). The minimum number of digits should be 4 and the maximum should be 12 (otherwise, make sure the experiment aborts). 

Depending on the value submitted to the `nr_of_digits` parameter in the dialog box, your experiment should generate the trials "on the fly" (make sure they adhere to the criteria listed in the previous section) and subsequently be presented as outlined previously. This means that you should *not* use an external conditions file (like the `cd_conditions.csv`) if you want to complete this advanced version. Also, in addition to the columns mentioned above, add a column `nr_of_digits` to the data file. 

We highly recommend that you first try to implement the regular experiment and only then try to implement this advanced feature if time permits.

## Grading key
Your assignment will be graded on both qualitative criteria (5 points) and quantitative criteria (25 points), outlined below.

:::{warning}
This probably goes without saying, but if you hand in the compiled Builder script from the demo experiment, you will fail this assignment.
:::

### Qualitative criteria (10 points)
The qualitative criteria are related to the quality of the code as well as the experiment. 

* **Readability of code (comments where needed, consistently formatted, etc.)**

    If you would give this script to someone who doesn't know PsychoPy, would they understand how it worked? (5 points)<br><br>

* **Run without errors**

    Does the code run without errors? (5 points)

### Quantitative criteria (20 points)
The following elements need to be incorporated as specified and work as expected:

* An dialog box (1 point);
* A welcome screen (1 point);
* Instructions (2 points);
* Trial/feedback routine:
  * Trial routine structure and timing (2 points);
  * Correct feedback routine (correct text/color; 3 points);
* Overview routine:
  * Computing accuracy (1 point);
  * Screen with accuracy (1 point);
* Response key and reaction time are stored inside trial loop (3 points);
* Data is saved as a CSV file with proper name (and contains all specified columns; 3 points)
* Advanced `nr_of_digits` feature (3 points)

## Tips & tricks
You can find some tips and tricks for completing this assignment below (feel free to use or ignore as you like)!

* Feel free to copy-paste stuff from the tutorials, *but make sure you are using the correct variable named in your experiment*;
* Google is your friend; use it!;
* It doesn't matter which timing method you use (the `wait` function/clock-based timing/frame-based timing);
* When developing the experiment, set `fullscr=False` during initialization of your `Window` so you can abort it whenever you want; 
* Testing, testing, testing: make sure you test your experiment regularly!

Finally, don't try to implement the entire experiment at once. Instead, implement the features step by step. I would recommend implement the features in the following order:

1. The dialog box
2. The welcome screen
3. The instruction screen
4. Reading in the conditions file (if you use this)
5. The trial loop, containing the first stimulus presentation, the delay, the second stimulus presentation, and the ISI *only*
6. Once the trial loop is working, add the feedback part
7. Once the feedback part is working, try storing the participant response and reaction time in a Pandas `DataFrame` (this may be the same `DataFrame` that contains the trial attributes)
8. Compute accuracy and show it
9. Make sure your `DataFrame` contains everything it needs and save it to disk
10. Work on the *advanced feature* if you still have time (you may want to do this in a separate file to not mess up your current version)

## Plagiarism
Although this is an "open-book" assignment, you may not work together on this assignment. In case we find out that students worked together on this assignment, this will be reported as plagiarism to the exam committee.

## Handing in your assignment
Hand in your experiment (a `.py` file) on Canvas: *Modules* &rarr; *Assignment 4 (PsychoPy)*. **If you use additional files (e.g., custom Python modules you wrote, a conditions Excel/CSV file, etc.), make sure to upload those files as well**.

The deadline for handing in the assignment is 3 PM.

<br><center><b>GOOD LUCK!</b> You got this.</center>
