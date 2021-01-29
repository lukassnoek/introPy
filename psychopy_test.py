""" A simple test to see whether the (non-standalone) install 
of PsychoPy was successful. """

from psychopy.core import quit
from psychopy.visual import Window, TextStim
from psychopy.hardware.keyboard import Keyboard

win = Window()
kb = Keyboard()
txt = TextStim(win, "Testing PsychoPy!\n\nIf you see this, it probably works just fine :-)\n\nPress enter to quit.")
txt.draw()
win.flip()

while 'return' not in kb.getKeys():
    kb.getKeys()

quit()