import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait, getTime
from psychopy.event import Mouse
from psychopy.visual import TextStim, Circle, Polygon, ShapeStim, ImageStim
from psychopy.hardware.keyboard import Keyboard

### DIALOG BOX ROUTINE ###
exp_info = {'participant_nr': 99, 'age': '29'}
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

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1920, 1080), fullscr=False, monitor='samsung')

# Also initialize a mouse, for later
# We'll set it to invisible for now
mouse = Mouse(visible=False)

# Initialize a (global) clock
clock = Clock()

mouse.setVisible(True)
x = [-.95, .95, .95, -.95]
y = [.95, .95, -.95, -.95]
for i in range(4):
    mouse.setPos((x[i],y[i]))
    wait(2)
quit()

### WELCOME ROUTINE ###
# Create a welcome screen and show for 2 seconds
welcome_txt_stim = TextStim(win, text="Welcome to this experiment!", color=(1, 0, -1), font='Calibri')
welcome_txt_stim.draw()
win.flip()
wait(2)

### INSTRUCTION ROUTINE ###
instruct_txt = """ 
In this experiment, you will see emotional faces (either happy or angry) with a word above the image (either “happy” or “angry”).

Importantly, you need to respond to the EXPRESSION of the face and ignore the word. You respond with the arrow keys:
    
    HAPPY expression = left
    ANGRY expression = right
    
(Press ‘enter’ to start the experiment!)
 """

# Show instructions and wait until response (return)
instruct_txt = TextStim(win, instruct_txt, alignText='left', height=0.085)
instruct_txt.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        # The for loop was optional
        for key in keys:
            print(f"The {key.name} key was pressed within {key.rt:.3f} seconds for a total of {key.duration:.3f} seconds.")
        break  # break out of the loop!

### CLICK-BUTTON-TO-START ROUTINE ###
# Make mouse visible for click-button-to-start screen
mouse.setVisible(True)

# Create text + button
click_txt = TextStim(win, "Click the button to start!", pos=(0, 0.5))
click_txt.draw()
        
button = Circle(win, fillColor=(1, -1, -1), size=(0.5625*0.25, 0.25))
# Alternative using Polygon
#button = Polygon(win, fillColor=(1, -1, -1), size=(0.5625*0.25, 0.25), edges=100)

button.draw()
win.flip()

while True:
    if mouse.isPressedIn(button):
        mouse.setVisible(False)
        break

### TRIAL LOOP ROUTINE ###
# Read in conditions file
cond_df = pd.read_excel('emo_conditions.xlsx')
cond_df = cond_df.sample(frac=1)

# Create fixation target (a plus sign)
fix = TextStim(win, '+')
trial_clock = Clock()

# Show initial fixation
fix.draw()
win.flip()
wait(1)

for idx, row in cond_df.iterrows():
    # Extract current word and smiley
    curr_word = row['word']
    curr_smil = row['smiley']

    # Create and draw text/img
    stim_txt = TextStim(win, curr_word, pos=(0, 0.3))
    stim_img = ImageStim(win, curr_smil + '.png', )
    stim_img.size *= 0.5

    trial_clock.reset()
    kb.clock.reset()
    while trial_clock.getTime() < 2:
        # Draw stuff
        
        if trial_clock.getTime() < 0.5:
            stim_txt.draw()
            stim_img.draw()
        else:
            fix.draw()
            
        win.flip()
        
        # Get responses
        resp = kb.getKeys()
        if resp:
            
            if 'q' in resp:
                quit()

            cond_df.loc[idx, 'rt'] = resp[-1].rt
            cond_df.loc[idx, 'resp'] = resp[-1].name
            if resp[-1].name == 'left' and curr_smil == 'happy':
               cond_df.loc[idx, 'correct'] = 1
            elif resp[-1].name ==  'right' and curr_smil == 'angry':
                cond_df.loc[idx, 'correct'] = 1
            else:
                cond_df.loc[idx, 'correct'] = 0
        
effect = cond_df.groupby('congruence').mean()
rt_con = effect.loc['congruent', 'rt']
rt_incon = effect.loc['incongruent', 'rt']
acc = cond_df['correct'].mean()

txt = f"""
Your reaction times are as follows:

    Congruent: {rt_con:.3f}
    Incongruent: {rt_incon:.3f}

Overall accuracy: {acc:.3f}
"""
result = TextStim(win, txt)
result.draw()
win.flip()
wait(5)

cond_df.to_csv(f"sub-{exp_info['participant_id']}_results.csv")

# Finish experiment by closing window and quitting
win.close()
quit()  