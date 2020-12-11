from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait, getTime
from psychopy.visual import TextStim
from psychopy.hardware.keyboard import Keyboard

"""
# Create dialog box
exp_info = {'participant_nr': 99, 'age': ''}
dlg = DlgFromDict(exp_info)

# If pressed Cancel, abort!
if not dlg.OK:
    quit()
else:
    # Quit when either the participant nr or age is not filled in
    if not exp_info['participant_nr'] or not exp_info['age']:
        quit()
        
    # Also quit in case of invalid participant nr or age
    if exp_info['participant_nr'] > 99 or int(exp_info['age']) < 18:
        quit()
    else:  # let's star the experiment!
        print(f"Started experiment for participant {exp_info['participant_nr']} "
                 f"with age {exp_info['age']}.")
"""
# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1920, 1080), fullscr=True, monitor='samsung')

# Initialize a clock
timer = Clock()

# We assume `win` already exists
welcome_txt_stim = TextStim(win, text="Welcome to this experiment!")
welcome_txt_stim.draw()
win.flip()
wait(2)

# instructions
instruct_txt = """ 
In this experiment, you will see emotional faces (either happy or angry) with a word above the image (either “happy” or “angry”).

Importantly, you need to respond to the EXPRESSION of the face and ignore the word. You respond with the arrow keys:
    
    HAPPY expression = left
    ANGRY expression = right
    
(Press ‘enter’ to start the experiment!)
 """

instruct_txt = TextStim(win, instruct_txt, alignText='left', height=0.085)
instruct_txt.draw()
win.flip()

kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        for key in keys:
            print(f"The {key.name} key was pressed within {key.rt} seconds for a total of {key.duration} seconds.")
        break

# Finish experiment by closing window and quitting
win.close()
quit()