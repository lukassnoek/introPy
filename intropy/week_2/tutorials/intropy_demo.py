#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.9),
    on Mon Nov 30 17:47:26 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.9'
expName = 'intropy_demo'  # from the Builder filename that created this script
expInfo = {'participant': '01'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/sub-%s_%s' % (expInfo['participant'], expInfo['expName'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/lukas/education/introPy/tutorials/week_2/intropy_demo.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
hello = visual.TextStim(win=win, name='hello',
    text='Hello, dear Python aficionado.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcome = visual.TextStim(win=win, name='welcome',
    text='Welcome to this super basic Psychopy Builder demo.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
wait_key = visual.TextStim(win=win, name='wait_key',
    text='What about some images?\n\nTo see some images, press ‘enter’.',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "show_stimuli"
show_stimuliClock = core.Clock()
stim = visual.ImageStim(
    win=win,
    name='stim', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)

# Initialize components for Routine "gabor"
gaborClock = core.Clock()
gabor_txt = visual.TextStim(win=win, name='gabor_txt',
    text='And what about a fancy “gabor wavelet”?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
gabor_stim = visual.GratingStim(
    win=win, name='gabor_stim',
    tex='sin', mask='gauss',
    ori=0, pos=(0, 0), size=(0.5, 0.5), sf=10, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,blendmode='avg',
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "wrap_up"
wrap_upClock = core.Clock()
txt1 = visual.TextStim(win=win, name='txt1',
    text='There’s so much more you can do with Psychopy …',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
txt2 = visual.TextStim(win=win, name='txt2',
    text='But let’s stop here …',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
txt3 = visual.TextStim(win=win, name='txt3',
    text='Goodbye!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [hello, welcome, wait_key, key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *hello* updates
    if hello.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        hello.frameNStart = frameN  # exact frame index
        hello.tStart = t  # local t and not account for scr refresh
        hello.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(hello, 'tStartRefresh')  # time at next scr refresh
        hello.setAutoDraw(True)
    if hello.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > hello.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            hello.tStop = t  # not accounting for scr refresh
            hello.frameNStop = frameN  # exact frame index
            win.timeOnFlip(hello, 'tStopRefresh')  # time at next scr refresh
            hello.setAutoDraw(False)
    
    # *welcome* updates
    if welcome.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        welcome.frameNStart = frameN  # exact frame index
        welcome.tStart = t  # local t and not account for scr refresh
        welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcome, 'tStartRefresh')  # time at next scr refresh
        welcome.setAutoDraw(True)
    if welcome.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > welcome.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            welcome.tStop = t  # not accounting for scr refresh
            welcome.frameNStop = frameN  # exact frame index
            win.timeOnFlip(welcome, 'tStopRefresh')  # time at next scr refresh
            welcome.setAutoDraw(False)
    
    # *wait_key* updates
    if wait_key.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        wait_key.frameNStart = frameN  # exact frame index
        wait_key.tStart = t  # local t and not account for scr refresh
        wait_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_key, 'tStartRefresh')  # time at next scr refresh
        wait_key.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('hello.started', hello.tStartRefresh)
thisExp.addData('hello.stopped', hello.tStopRefresh)
thisExp.addData('welcome.started', welcome.tStartRefresh)
thisExp.addData('welcome.stopped', welcome.tStopRefresh)
thisExp.addData('wait_key.started', wait_key.tStartRefresh)
thisExp.addData('wait_key.stopped', wait_key.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
stimuli = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli.csv'),
    seed=None, name='stimuli')
thisExp.addLoop(stimuli)  # add the loop to the experiment
thisStimulus = stimuli.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
if thisStimulus != None:
    for paramName in thisStimulus:
        exec('{} = thisStimulus[paramName]'.format(paramName))

for thisStimulus in stimuli:
    currentLoop = stimuli
    # abbreviate parameter names if possible (e.g. rgb = thisStimulus.rgb)
    if thisStimulus != None:
        for paramName in thisStimulus:
            exec('{} = thisStimulus[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "show_stimuli"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    stim.setImage(image)
    # keep track of which components have finished
    show_stimuliComponents = [stim]
    for thisComponent in show_stimuliComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    show_stimuliClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "show_stimuli"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = show_stimuliClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=show_stimuliClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim* updates
        if stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim.frameNStart = frameN  # exact frame index
            stim.tStart = t  # local t and not account for scr refresh
            stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
            stim.setAutoDraw(True)
        if stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                stim.tStop = t  # not accounting for scr refresh
                stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim, 'tStopRefresh')  # time at next scr refresh
                stim.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in show_stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "show_stimuli"-------
    for thisComponent in show_stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    stimuli.addData('stim.started', stim.tStartRefresh)
    stimuli.addData('stim.stopped', stim.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'stimuli'


# ------Prepare to start Routine "gabor"-------
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
gaborComponents = [gabor_txt, gabor_stim]
for thisComponent in gaborComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gaborClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "gabor"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = gaborClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gaborClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gabor_txt* updates
    if gabor_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gabor_txt.frameNStart = frameN  # exact frame index
        gabor_txt.tStart = t  # local t and not account for scr refresh
        gabor_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gabor_txt, 'tStartRefresh')  # time at next scr refresh
        gabor_txt.setAutoDraw(True)
    if gabor_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gabor_txt.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            gabor_txt.tStop = t  # not accounting for scr refresh
            gabor_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gabor_txt, 'tStopRefresh')  # time at next scr refresh
            gabor_txt.setAutoDraw(False)
    
    # *gabor_stim* updates
    if gabor_stim.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        gabor_stim.frameNStart = frameN  # exact frame index
        gabor_stim.tStart = t  # local t and not account for scr refresh
        gabor_stim.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gabor_stim, 'tStartRefresh')  # time at next scr refresh
        gabor_stim.setAutoDraw(True)
    if gabor_stim.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gabor_stim.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            gabor_stim.tStop = t  # not accounting for scr refresh
            gabor_stim.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gabor_stim, 'tStopRefresh')  # time at next scr refresh
            gabor_stim.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gaborComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "gabor"-------
for thisComponent in gaborComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gabor_txt.started', gabor_txt.tStartRefresh)
thisExp.addData('gabor_txt.stopped', gabor_txt.tStopRefresh)
thisExp.addData('gabor_stim.started', gabor_stim.tStartRefresh)
thisExp.addData('gabor_stim.stopped', gabor_stim.tStopRefresh)

# ------Prepare to start Routine "wrap_up"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
wrap_upComponents = [txt1, txt2, txt3]
for thisComponent in wrap_upComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
wrap_upClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wrap_up"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = wrap_upClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=wrap_upClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt1* updates
    if txt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt1.frameNStart = frameN  # exact frame index
        txt1.tStart = t  # local t and not account for scr refresh
        txt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt1, 'tStartRefresh')  # time at next scr refresh
        txt1.setAutoDraw(True)
    if txt1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt1.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            txt1.tStop = t  # not accounting for scr refresh
            txt1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt1, 'tStopRefresh')  # time at next scr refresh
            txt1.setAutoDraw(False)
    
    # *txt2* updates
    if txt2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        txt2.frameNStart = frameN  # exact frame index
        txt2.tStart = t  # local t and not account for scr refresh
        txt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt2, 'tStartRefresh')  # time at next scr refresh
        txt2.setAutoDraw(True)
    if txt2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            txt2.tStop = t  # not accounting for scr refresh
            txt2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt2, 'tStopRefresh')  # time at next scr refresh
            txt2.setAutoDraw(False)
    
    # *txt3* updates
    if txt3.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        txt3.frameNStart = frameN  # exact frame index
        txt3.tStart = t  # local t and not account for scr refresh
        txt3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt3, 'tStartRefresh')  # time at next scr refresh
        txt3.setAutoDraw(True)
    if txt3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txt3.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            txt3.tStop = t  # not accounting for scr refresh
            txt3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txt3, 'tStopRefresh')  # time at next scr refresh
            txt3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wrap_upComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wrap_up"-------
for thisComponent in wrap_upComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt1.started', txt1.tStartRefresh)
thisExp.addData('txt1.stopped', txt1.tStopRefresh)
thisExp.addData('txt2.started', txt2.tStartRefresh)
thisExp.addData('txt2.stopped', txt2.tStopRefresh)
thisExp.addData('txt3.started', txt3.tStartRefresh)
thisExp.addData('txt3.stopped', txt3.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
