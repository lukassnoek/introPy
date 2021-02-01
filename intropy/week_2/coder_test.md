# Test your Coder skills!
By now, you know the basics of creating experiments in the PsychoPy Coder! If you want to test your Coder skills, you can try to recreate the Lexical Decision Task like you did with the Builder before!

To refresh your memory, run the Lexical Decision task by clicking on the button below.

<a href="https://run.pavlovia.org/demos/lexical-decision-task/html/" class="btn btn-primary" style="color:white;">Start the Lexical Decision Task
</a>

Try to include the following:

* A dialog box asked for the participant ID and age of the participant
  * Note: you don't have to recreate the "Field marked with an asterisk (*) are required" text
* A welcome screen with text
* An instruction screen, which continues upon a button press by the participant
* A loop with trials including a fixation target, the stimulus, and feedback (text showing "correct", "incorrect", or "missed")
  * Create the stimuli (real words, fake words) yourself
  * Make sure that the trial conditions (real word, fake word) are presented randomly
  * Make sure the responses (left/right) and reaction time per trial are stored in a Pandas DataFrame
* A "goodbye" screen, thanking the participant for their contribution
* Make sure to save the Pandas DataFrame to disk using a sensible filename
  * Include the participant ID in the filename
  * Make sure the file contains, per trial, the condition (real/fake), response (right, left), and reaction time (in seconds)