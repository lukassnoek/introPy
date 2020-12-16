import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait, getTime
from psychopy.event import Mouse
from psychopy.visual import TextStim, Circle, Polygon, ShapeStim, ImageStim
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
win = Window(size=(1920, 1080), fullscr=True, monitor='samsung', waitBlanking=True)

# Also initialize a mouse, for later
# We'll set it to invisible for now
mouse = Mouse(visible=False)

# Initialize a clock
clock = Clock()

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
            print(f"The {key.name} key was pressed within {key.rt:.3f} seconds for a total of {key.duration:.3f} seconds.")
        break

mouse.setVisible(True)
click_txt = TextStim(win, "Click the button to start!", pos=(0, 0.5))
click_txt.draw()

button = Circle(win, fillColor=(1, -1, -1), size=(0.5625*0.25, 0.25))
#button = Polygon(win, fillColor=(1, -1, -1), size=(0.5625*0.25, 0.25), edges=100)

button.draw()
win.flip()

while True:
    if mouse.isPressedIn(button):
        mouse.setVisible(False)
        break

cond = pd.read_excel('emo_conditions.xlsx')
cond = cond.sample(frac=1)

stim_txt = TextStim(win, 'happy')
stim_img = ImageStim(win, image='happy.png')

for i in range(cond.shape[0]):
    emo = cond.loc[i, 'smiley']
    word = cond.loc[i, 'word']
    stim_txt.setText(word)
    stim_img.setImage(emo + '.png')
    stim_txt.draw()
    stim_img.draw()
    
# Start experiment!

win.flip()
t_end = clock.getTime() 
print(t_end-t_start)

# Finish experiment by closing window and quitting
win.close()
quit()  