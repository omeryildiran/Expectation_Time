#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --- Import packages ---
import psychopy
from psychopy import locale_setup
from psychopy import prefs
#prefs.hardware['audioLib'] = 'PTB'
#prefs.hardware['audioLatencyMode'] = '4'
#from pysoundcard import Stream
#from scipy.io.wavfile import read as wavread

from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

from psychopy.tools import monitorunittools
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard
from math import atan as arctan

def coord2time(x,y):
	if x>=0 and y>0: 		time=(250*(arctan(x/y)/arctan(1))) # Take cotangent by dividing x/y
	elif x>0 and y<=0:		time=500+(250*(abs(arctan(y/x)/arctan(1)))) # Take tangent
	elif x<=0 and y<0:		time=1000+(250*((arctan(x/y))/arctan(1))) # Take cotangent
	elif x<0 and y>=0:		time=1500+(250*(abs(arctan(y/x)/arctan(1))))# Take tangent
	else:		time=None
	return time


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'expectation_shapes_perceived_time'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\omeru\\Documents\\Omer_Repos\\Internship Pascal\\Expectation_Shapes_Perceived_Time\\expectation_shapes_perceived_time.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.0001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1020,720], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "welcomeScr" ---
welcomeTxt = visual.TextStim(win=win, name='welcomeTxt',
    text="Welcome to the experiemnt,\nPress 'Space' to start familiarizing with trial time intervals.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
skipWelcome = keyboard.Keyboard()

# --- Initialize components for Routine "fam" ---
# Run 'Begin Experiment' code from sizeVariables
# TODO:  Give the sizes Size
fColor=1
sizeHand=2.5
sizeHandPix=monitorunittools.deg2pix(degrees=sizeHand,monitor=win.monitor)
sizeClockCentre=0.5# =fixation point
sizePlaceholder=1
diskSize=sizePlaceholder
pointer_size=monitorunittools.deg2pix(degrees=0.3,monitor=win.monitor)/win.size[1]
# Run 'Begin Experiment' code from secToFrame
expInfo['frameRate'] = win.getActualFrameRate()
fps=expInfo['frameRate']
# Ms to Frame number converter
def msToFrame(durInMs):
    presentationFrames = round(durInMs/(1000/expInfo['frameRate']))
    return presentationFrames

# Second to Frame number converter
def s2nFrame(durInS):
    #durInS=0.33
    #fps= 59.9# lets say it is 60
    preciseFrameDur=1.0/round(fps) # expInfo['frameRate']
    nFrame=round(durInS/preciseFrameDur)
    return(nFrame)
# Run 'Begin Experiment' code from handRoate
import math
fps=expInfo['frameRate'] #gives frame-per-second fps
fpsR=round(fps)
durFam=2.0#in s
numFramePer2Sec=round(fps*2)
frameReq=numFramePer2Sec
#frameReq=durFam/frameDur
oriPerFrame=360/frameReq

#oriPerFrame=(360/fps)/2
toneStart=round(fps/4)
clockRotStart=toneStart+2

clockOutDisk = visual.ShapeStim(
    win=win, name='clockOutDisk',units='deg', 
    size=(sizeHand*2, sizeHand*2), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-3.0, interpolate=True)
clockHand = visual.ShapeStim(
    win=win, name='clockHand', vertices=[[0,0],[1,1]],units='deg', 
    size=(sizeHand, 0.0001),
    ori=1.0, pos=(0, 0), anchor='bottom-center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
audioCue2Start = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='audioCue2Start')
audioCue2Start.setVolume(1.0)
audioCue2End = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='audioCue2End')
audioCue2End.setVolume(1.0)
centreClock = visual.ShapeStim(
    win=win, name='centreClock',units='deg', 
    size=(sizeClockCentre,sizeClockCentre), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-7.0, interpolate=False)

# --- Initialize components for Routine "key2pass" ---
continueFam = visual.TextStim(win=win, name='continueFam',
    text="Press 'Space' to continue familiarizing with timig-interval",
    font='Open Sans',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sapce2pass = keyboard.Keyboard()

clockOutDisk_2 = visual.ShapeStim(
    win=win, name='clockOutDisk_2',units='deg', 
    size=(sizeHand*2, sizeHand*2), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
clockHand_2 = visual.ShapeStim(
    win=win, name='clockHand_2', vertices=[[0,0],[1,1]],units='deg', 
    size=(sizeHand, 0.0001),
    ori=1.0, pos=(0, 0), anchor='bottom-center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=False)
centreClock_2 = visual.ShapeStim(
    win=win, name='centreClock_2',units='deg', 
    size=(sizeClockCentre,sizeClockCentre), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)

# --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from pickTargetCol
stimColors=['red','blue']
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
# Run 'Begin Experiment' code from code
x_coord = np.random.uniform(-1,1)
y_coord = np.random.uniform(-1,1)

#key
key_resp = keyboard.Keyboard()
#circle showing mouse point
responsePointer = visual.ShapeStim(
    win=win, name='responsePointer',
    size=(pointer_size, pointer_size), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)

# Create some handy timers
# Run 'Begin Experiment' code from timingVars
diskRadius=1
durS1=msToFrame(33)
durS2=msToFrame(33)
audCueStart = sound.Sound('A', secs=0.033, stereo=True, hamming=False,
    name='audioCueStart')
audCueStart.setVolume(1.0)
outerDisk = visual.ShapeStim(
    win=win, name='outerDisk',units='deg', 
    size=(sizeHand*2, sizeHand*2), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=3.5,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-3.0, interpolate=False)
distractor = visual.ShapeStim(
    win=win, name='distractor',units='deg', 
    size=(diskSize,diskSize), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
target = visual.ShapeStim(
    win=win, name='target',units='deg', 
    size=(diskSize,diskSize), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=False)
cueForRep = visual.ShapeStim(
    win=win, name='cueForRep',units='deg', 
    size=(diskSize,diskSize), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=False)

placeholder = visual.ShapeStim(
    win=win, name='placeholder',units='deg', 
    size=(diskSize,diskSize), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.5,     colorSpace='rgb',  lineColor=[fColor,fColor,fColor], fillColor=None,
    opacity=None, depth=-6.0, interpolate=False)
audCueEnd = sound.Sound('A', secs=0.033, stereo=True, hamming=False,
    name='audCueEnd')
audCueEnd.setVolume(1.0)
sapce2pass_2 = keyboard.Keyboard()
fixationPoint = visual.ShapeStim(
    win=win, name='fixationPoint', vertices='cross',units='deg', 
    size=(0.25, 0.25),
    ori=45.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
# Run 'Begin Experiment' code from fixOpacitiy
fixation_opacity=1

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "welcomeScr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
skipWelcome.keys = []
skipWelcome.rt = []
_skipWelcome_allKeys = []
# keep track of which components have finished
welcomeScrComponents = [welcomeTxt, skipWelcome]
for thisComponent in welcomeScrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "welcomeScr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeTxt* updates
    if welcomeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeTxt.frameNStart = frameN  # exact frame index
        welcomeTxt.tStart = t  # local t and not account for scr refresh
        welcomeTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeTxt, 'tStartRefresh')  # time at next scr refresh
        welcomeTxt.setAutoDraw(True)
    
    # *skipWelcome* updates
    waitOnFlip = False
    if skipWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        skipWelcome.frameNStart = frameN  # exact frame index
        skipWelcome.tStart = t  # local t and not account for scr refresh
        skipWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skipWelcome, 'tStartRefresh')  # time at next scr refresh
        skipWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skipWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skipWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skipWelcome.status == STARTED and not waitOnFlip:
        theseKeys = skipWelcome.getKeys(keyList=['space'], waitRelease=False)
        _skipWelcome_allKeys.extend(theseKeys)
        if len(_skipWelcome_allKeys):
            skipWelcome.keys = _skipWelcome_allKeys[-1].name  # just the last key pressed
            skipWelcome.rt = _skipWelcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeScrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "welcomeScr" ---
for thisComponent in welcomeScrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcomeScr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
famLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='famLoop')
thisExp.addLoop(famLoop)  # add the loop to the experiment
thisFamLoop = famLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFamLoop.rgb)
if thisFamLoop != None:
    for paramName in thisFamLoop:
        exec('{} = thisFamLoop[paramName]'.format(paramName))

for thisFamLoop in famLoop:
    currentLoop = famLoop
    # abbreviate parameter names if possible (e.g. rgb = thisFamLoop.rgb)
    if thisFamLoop != None:
        for paramName in thisFamLoop:
            exec('{} = thisFamLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fam" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from handRoate
    oriHand=-90
    frameHand=999
    counterForStart=0
    fColor=1
    #oriPerFrame=360/frameReq
    #oriPerFrame=360/(2*fps)
    
    audioCue2Start.setSound('A',secs=0.033, hamming=False)
    audioCue2Start.setVolume(1.0, log=False)
    audioCue2End.setSound('A', secs=0.033, hamming=False)
    audioCue2End.setVolume(1.0, log=False)
    # keep track of which components have finished
    famComponents = [clockOutDisk, clockHand, audioCue2Start, audioCue2End, centreClock]
    for thisComponent in famComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "fam" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from handRoate
        if counterForStart==clockRotStart:
            if clockHand.status == STARTED:
            #if frameHand<(1000+fps) and frameHand>999:
            #    frameHand+=1
            #if frameHand==1000:
                thisExp.addData('handMove.started', tThisFlipGlobal)
                frameHand=0
                
        
        if frameHand<round(2*fps):
            oriHand+=oriPerFrame
            #fColor=fColor-0.0085
            #clockHand.setOri(oriHand, log=False)
            frameHand+=1
        elif frameHand==round(2*fps):
             thisExp.addData('handOri',oriHand) 
             thisExp.addData('handMove.ended', tThisFlipGlobal)
             frameHand=999
            #oriHand=-90
            #clockHand.setOri(45, log=False)
        
        #elif frameHand==round(2*fps):
            #clockHand.setOri(270, log=False)
        #    frameHand=1999
        
        counterForStart=counterForStart+1
        
        
        # *clockOutDisk* updates
        if clockOutDisk.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            clockOutDisk.frameNStart = frameN  # exact frame index
            clockOutDisk.tStart = t  # local t and not account for scr refresh
            clockOutDisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clockOutDisk, 'tStartRefresh')  # time at next scr refresh
            clockOutDisk.setAutoDraw(True)
        if clockOutDisk.status == STARTED:
            if frameN >= (clockOutDisk.frameNStart + round(clockRotStart+fpsR*2.5)):
                # keep track of stop time/frame for later
                clockOutDisk.tStop = t  # not accounting for scr refresh
                clockOutDisk.frameNStop = frameN  # exact frame index
                clockOutDisk.setAutoDraw(False)
        
        # *clockHand* updates
        if clockHand.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            clockHand.frameNStart = frameN  # exact frame index
            clockHand.tStart = t  # local t and not account for scr refresh
            clockHand.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clockHand, 'tStartRefresh')  # time at next scr refresh
            clockHand.setAutoDraw(True)
        if clockHand.status == STARTED:
            if frameN >= (clockHand.frameNStart + round(clockRotStart+fpsR*2.5)):
                # keep track of stop time/frame for later
                clockHand.tStop = t  # not accounting for scr refresh
                clockHand.frameNStop = frameN  # exact frame index
                clockHand.setAutoDraw(False)
        if clockHand.status == STARTED:  # only update if drawing
            clockHand.setOri(oriHand, log=False)
        # start/stop audioCue2Start
        if audioCue2Start.status == NOT_STARTED and frameN >= toneStart:
            # keep track of start time/frame for later
            audioCue2Start.frameNStart = frameN  # exact frame index
            audioCue2Start.tStart = t  # local t and not account for scr refresh
            audioCue2Start.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('audioCue2Start.started', tThisFlipGlobal)
            audioCue2Start.play(when=win)  # sync with win flip
        # start/stop audioCue2End
        if audioCue2End.status == NOT_STARTED and frameN >= clockRotStart+round(2*fps):
            # keep track of start time/frame for later
            audioCue2End.frameNStart = frameN  # exact frame index
            audioCue2End.tStart = t  # local t and not account for scr refresh
            audioCue2End.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('audioCue2End.started', tThisFlipGlobal)
            audioCue2End.play(when=win)  # sync with win flip
        
        # *centreClock* updates
        if centreClock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            centreClock.frameNStart = frameN  # exact frame index
            centreClock.tStart = t  # local t and not account for scr refresh
            centreClock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(centreClock, 'tStartRefresh')  # time at next scr refresh
            centreClock.setAutoDraw(True)
        if centreClock.status == STARTED:
            if frameN >= (centreClock.frameNStart + round(clockRotStart+fpsR*2.5)):
                # keep track of stop time/frame for later
                centreClock.tStop = t  # not accounting for scr refresh
                centreClock.frameNStop = frameN  # exact frame index
                centreClock.setAutoDraw(False)
        if centreClock.status == STARTED:  # only update if drawing
            centreClock.setFillColor([fColor,fColor,fColor], log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in famComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fam" ---
    for thisComponent in famComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    audioCue2Start.stop()  # ensure sound has stopped at end of routine
    audioCue2End.stop()  # ensure sound has stopped at end of routine
    # the Routine "fam" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "key2pass" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    sapce2pass.keys = []
    sapce2pass.rt = []
    _sapce2pass_allKeys = []
    # keep track of which components have finished
    key2passComponents = [continueFam, sapce2pass, clockOutDisk_2, clockHand_2, centreClock_2]
    for thisComponent in key2passComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "key2pass" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *continueFam* updates
        if continueFam.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            continueFam.frameNStart = frameN  # exact frame index
            continueFam.tStart = t  # local t and not account for scr refresh
            continueFam.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continueFam, 'tStartRefresh')  # time at next scr refresh
            continueFam.setAutoDraw(True)
        
        # *sapce2pass* updates
        waitOnFlip = False
        if sapce2pass.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sapce2pass.frameNStart = frameN  # exact frame index
            sapce2pass.tStart = t  # local t and not account for scr refresh
            sapce2pass.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sapce2pass, 'tStartRefresh')  # time at next scr refresh
            sapce2pass.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sapce2pass.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sapce2pass.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sapce2pass.status == STARTED and not waitOnFlip:
            theseKeys = sapce2pass.getKeys(keyList=['space'], waitRelease=False)
            _sapce2pass_allKeys.extend(theseKeys)
            if len(_sapce2pass_allKeys):
                sapce2pass.keys = _sapce2pass_allKeys[-1].name  # just the last key pressed
                sapce2pass.rt = _sapce2pass_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *clockOutDisk_2* updates
        if clockOutDisk_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            clockOutDisk_2.frameNStart = frameN  # exact frame index
            clockOutDisk_2.tStart = t  # local t and not account for scr refresh
            clockOutDisk_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clockOutDisk_2, 'tStartRefresh')  # time at next scr refresh
            clockOutDisk_2.setAutoDraw(True)
        
        # *clockHand_2* updates
        if clockHand_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            clockHand_2.frameNStart = frameN  # exact frame index
            clockHand_2.tStart = t  # local t and not account for scr refresh
            clockHand_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clockHand_2, 'tStartRefresh')  # time at next scr refresh
            clockHand_2.setAutoDraw(True)
        if clockHand_2.status == STARTED:  # only update if drawing
            clockHand_2.setOri(-90.0, log=False)
        
        # *centreClock_2* updates
        if centreClock_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            centreClock_2.frameNStart = frameN  # exact frame index
            centreClock_2.tStart = t  # local t and not account for scr refresh
            centreClock_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(centreClock_2, 'tStartRefresh')  # time at next scr refresh
            centreClock_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in key2passComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "key2pass" ---
    for thisComponent in key2passComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "key2pass" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'famLoop'

## ---- Prepare to start routine Trial ---
# set up handler to look after randomisation of conditions etc
trialss = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('high_exp_trials.csv'),
    seed=None, name='trialss')
thisExp.addLoop(trialss)  # add the loop to the experiment
thisTrials = trialss.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials.rgb)
if thisTrials != None:
    for paramName in thisTrials:
        exec('{} = thisTrials[paramName]'.format(paramName))

for thisTrials in trialss:
    currentLoop = trialss
    # abbreviate parameter names if possible (e.g. rgb = thisTrials.rgb)
    if thisTrials != None:
        for paramName in thisTrials:
            exec('{} = thisTrials[paramName]'.format(paramName))

    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    routineForceEnded = False
    # setup some python lists for storing info about the mouse

    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    mouse.clicked_position = []

    gotValidClick = False  # until a click is received
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # update component parameters for each repeat
    # Run 'Begin Routine' code from pickTargetCol
    #shuffle(stimColors)
    targetColor=stimColors[0]
    distractorColor=stimColors[1]    
    # Run 'Begin Routine' code from timingVars
    durS1=msToFrame(33)
    durS2=msToFrame(33)
    fColor=1
    ### Timing of objects
    preTrialIntervalMs=500
    preTrialInterval=msToFrame(preTrialIntervalMs)
    initIntervalMs=np.random.uniform(150,1550)
    onsetS1Ms=initIntervalMs+preTrialIntervalMs
    initInterval=msToFrame(initIntervalMs)+preTrialInterval
    #midInterval =[-0.300 , -0.233, -0.167, -0.100 , -0.033, 0.033, 0.100 ,0.167, 0.233, 0.300]
    #midInterval =[300 , 233, 167, 100 , 33, 33, 100 ,167, 233, 300]
    #shuffle(midInterval)

    #midInterval=msToFrame(midInterval[0])
    midInterval=msToFrame(delay)
    onsetS1=initInterval
    onsetS2=onsetS1+midInterval
    lastInterval=msToFrame(2000)-(onsetS2+33)
    cueForRepOnset=msToFrame(2000)
    # #response
    x_coord = np.random.uniform(-1,1)
    y_coord = np.random.uniform(-1,1)
    # random     #initial Position pointer location
    x_coord_init = np.random.uniform(-1,1)
    y_coord_init = np.random.uniform(-1,1)
    x_coord_initPX=win.size[1]*x_coord_init
    y_coord_initPX=win.size[1]*y_coord_init
    hypoPx_init=math.sqrt(x_coord_initPX**2+y_coord_initPX**2)
    x_coord_onCircle=(((x_coord_initPX/hypoPx_init)*sizeHandPix)/win.size[1])
    y_coord_onCircle=(((y_coord_initPX/hypoPx_init)*sizeHandPix)/win.size[1])    
    responsePointer.setPos((x_coord_onCircle,y_coord_onCircle),log=False)

    audioCue2Start.setSound('A', secs=0.033, hamming=False)
    audioCue2Start.setVolume(1.0, log=False)
    distractor.setFillColor(distractor_color)
    distractor.setLineColor(distractor_color)
    # stim_color: color of stimuli in csv file trialList
    target.setFillColor(stim_color)
    target.setLineColor(stim_color)
    cueForRep.setFillColor(stim_color)
    cueForRep.setLineColor(stim_color)
    audCueEnd.setSound('A', secs=0.033, hamming=False)
    audCueEnd.setVolume(1.0, log=False)
    audCueStart.setSound('A', secs=0.033, hamming=False)
    audCueStart.setVolume(1.0, log=False)
    sapce2pass_2.keys = []
    sapce2pass_2.rt = []
    _sapce2pass_2_allKeys = []
    # Run 'Begin Routine' code from fixOpacitiy
    fixation_opacity=1
    i=0
    # keep track of which components have finished
    trialComponents = [audCueStart, outerDisk, distractor, target, placeholder, audCueEnd, sapce2pass_2, fixationPoint,responsePointer,cueForRep,mouse]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    preTrialInterval=msToFrame(preTrialIntervalMs)
    t = 0        
    # --- Run Routine "trial" ---
    while continueRoutine:
        # get current time
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop audCueStart
        t = routineTimer.getTime()   
        # *fixationPoint* updates
        if fixationPoint.status == NOT_STARTED and frameN>=0:
            # keep track of start time/frame for later
            fixationPoint.frameNStart = frameN  # exact frame index
            fixationPoint.tStart = t  # local t and not account for scr refresh
            #fixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
            #win.timeOnFlip(fixationPoint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('fixationPoint.started',t)
            fixationPoint.setAutoDraw(True)
        if fixationPoint.status == STARTED:
            if frameN >= (fixationPoint.frameNStart + preTrialInterval):
                # keep track of stop time/frame for later
                fixationPoint.tStop = t  # not accounting for scr refresh
                fixationPoint.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('fixationPoint.stopped',t)
                fixationPoint.setAutoDraw(False)
        if fixationPoint.status == STARTED:  # only update if drawing
            fixationPoint.setOpacity(fixation_opacity, log=False)
        # Run 'Each Frame' code from fixOpacitiy
        opacityDecrement=(1/preTrialInterval)
        if i>(round(preTrialInterval/2)):
            fixation_opacity=fixation_opacity-opacityDecrement
        i+=1

        # AudCueStart update in Trial Routine
        if audCueStart.status == NOT_STARTED and frameN >= preTrialInterval:
            # keep track of start time/frame for later
            #audCueStart.frameNStart = frameN  # exact frame index
            #audCueStart.tStart = t  # local t and not account for scr refresh
            audCueStart.play()  # start the sound (it finishes automatically)
            thisExp.addData('audCueStart.started', t)
            audCueStart.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
        if audCueStart.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > audCueStart.tStartRefresh + 0.033-frameTolerance:
                # keep track of stop time/frame for later
                audCueStart.tStop = t  # not accounting for scr refresh
                audCueStart.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('audCueStart.stopped', t)
                audCueStart.stop()
        
        # *outerDisk* updates
        if outerDisk.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            outerDisk.frameNStart = frameN  # exact frame index
            outerDisk.tStart = t  # local t and not account for scr refresh
            outerDisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outerDisk, 'tStartRefresh')  # time at next scr refresh
            outerDisk.setAutoDraw(True)
        
        # *distractor* updates
        if distractor.status == NOT_STARTED and frameN >= onsetS2:
            # keep track of start time/frame for later
            distractor.frameNStart = frameN  # exact frame index
            distractor.tStart = t  # local t and not account for scr refresh
            distractor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(distractor, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('distractor.started',t)
            distractor.setAutoDraw(True)
        if distractor.status == STARTED:
            if frameN >= (distractor.frameNStart + durS2):
                # keep track of stop time/frame for later
                distractor.tStop = t  # not accounting for scr refresh
                distractor.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData( 'distractor.stopped',t)
                distractor.setAutoDraw(False)
        
        # *target* updates
        if target.status == NOT_STARTED and frameN >= onsetS1:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('target.started',t)
            target.setAutoDraw(True)
        if target.status == STARTED:
            if frameN >= (target.frameNStart + durS1):
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('target.stopped',t)
                target.setAutoDraw(False)
        
        # *placeholder* updates
        if placeholder.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            placeholder.frameNStart = frameN  # exact frame index
            placeholder.tStart = t  # local t and not account for scr refresh
            placeholder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(placeholder, 'tStartRefresh')  # time at next scr refresh
            placeholder.setAutoDraw(True)
        # if placeholder.status == STARTED:  # only update if drawing
        #     fColor=fColor-0.0085
        #     placeholder.setFillColor([fColor,fColor,fColor], log=False)

            #break
        #    if frameN>= msToFrame(2500)+preTrialInterval:
        #        placeholder.setAutoDraw(False)
                #placeholder.setFillColor('', log=False)
        # start/stop audCueEnd
        if audCueEnd.status == NOT_STARTED and frameN >= msToFrame(2000)+preTrialInterval:
            # keep track of start time/frame for later
            audCueEnd.frameNStart = frameN  # exact frame index
            audCueEnd.tStart = t  # local t and not account for scr refresh
            audCueEnd.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('audCueEnd.started', t)
            audCueEnd.play()  # start the sound (it finishes automatically)
        if audCueEnd.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > audCueEnd.tStartRefresh + 0.033-frameTolerance:
                # keep track of stop time/frame for later
                audCueEnd.tStop = t  # not accounting for scr refresh
                audCueEnd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('audCueEnd.stopped', t)
                audCueEnd.stop()
        
        # *sapce2pass_2* updates
        if sapce2pass_2.status == NOT_STARTED and t >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            sapce2pass_2.frameNStart = frameN  # exact frame index
            sapce2pass_2.tStart = t  # local t and not account for scr refresh
            sapce2pass_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sapce2pass_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('sapce2pass_2.started', t)
            sapce2pass_2.status = STARTED
            # keyboard checking is just starting
            sapce2pass_2.clock.reset()  # now t=0
            sapce2pass_2.clearEvents(eventType='keyboard')
        if sapce2pass_2.status == STARTED:
            theseKeys = sapce2pass_2.getKeys(keyList=['space'], waitRelease=False)
            _sapce2pass_2_allKeys.extend(theseKeys)
            if len(_sapce2pass_2_allKeys):
                sapce2pass_2.keys = _sapce2pass_2_allKeys[-1].name  # just the last key pressed
                sapce2pass_2.rt = _sapce2pass_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
     
        

        # *mouse* updates
        #mouse_has_been_pressed = False
        if mouse.status == NOT_STARTED and frameN >= msToFrame(2500):
            # keep track of start time/frame for later
            mouse.setPos(newPos=(0,0))
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            #released=mouse.getPressed()

        #buttons=[]
        if mouse.status == STARTED:  # only update if started and not finished!
            #Get mouse position
            x, y = mouse.getPos()
            mouse.x.append(x)
            mouse.y.append(y)
            x_coord=mouse.getPos()[0]
            y_coord=mouse.getPos()[1]
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                released=mouse.getPressed()
                if sum(released) ==0:
                #if len(buttons) > 1:  # state changed to a new click
                    mouse_has_been_pressed = True
                    continueRoutine=False
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False

                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
    

        # *responsePointer* updates
        respX_px=win.size[1]*x_coord   # Coordinate of response X in Pixel 
        respY_px=win.size[1]*y_coord   # Coordinate of response Y in Pixel
        hypoPx=math.sqrt(respX_px**2+respY_px**2)
        if responsePointer.status == NOT_STARTED and frameN >= msToFrame(2500)+preTrialInterval:
            # keep track of start time/frame for later
            responsePointer.frameNStart = frameN  # exact frame index
            responsePointer.tStart = t  # local t and not account for scr refresh
            responsePointer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responsePointer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('responsePointer.started',t)
            responsePointer.setAutoDraw(True)
        if responsePointer.status == STARTED:  # only update if drawing
            if mouse.x[0]!=x or mouse.y[0]!=y:
                x_coord_onCircle=(((respX_px/hypoPx)*sizeHandPix)/win.size[1])
                y_coord_onCircle=(((respY_px/hypoPx)*sizeHandPix)/win.size[1])              
                responsePointer.setPos((x_coord_onCircle,y_coord_onCircle),log=False)
                perceivedTime=coord2time(x_coord_onCircle,y_coord_onCircle)
                pTemporalError=perceivedTime-initIntervalMs
            #else: 
                # x_coord_onCircle=(((x_coord_initPX/hypoPx_init)*sizeHandPix)/win.size[1])
                # y_coord_onCircle=(((y_coord_initPX/hypoPx_init)*sizeHandPix)/win.size[1])    
                # responsePointer.setPos((x_coord_onCircle,y_coord_onCircle),log=False)

            if continueRoutine == False:
                responsePointer.tStop= t  # local t and not account for scr refresh
                responsePointer.frameNstop=frameN
                thisExp.addData("responsePointer.stopped",t)
                perceivedTime=coord2time(x_coord_onCircle,y_coord_onCircle)
                pTemporalError=perceivedTime-initIntervalMs
                thisExp.addData("perceivedTime",perceivedTime)
                thisExp.addData("pTemporalError",pTemporalError)
                responsePointer.setAutoDraw(False)

        # Updates for PostCue 
        if cueForRep.status == NOT_STARTED and frameN >= msToFrame(2500)+preTrialInterval:
            cueForRep.setAutoDraw(True)
        if cueForRep.status == STARTED:
            if continueRoutine == False:
                cueForRep.setAutoDraw(False)
                         
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    audCueStart.stop()  # ensure sound has stopped at end of routine
    audCueEnd.stop()  # ensure sound has stopped at end of routine
    # check responses
    if sapce2pass_2.keys in ['', [], None]:  # No response was made
        sapce2pass_2.keys = None
    trialss.addData('sapce2pass_2.keys',sapce2pass_2.keys)
    if sapce2pass_2.keys != None:  # we had a response
        trialss.addData('sapce2pass_2.rt', sapce2pass_2.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    thisExp.addData('x_coord', x_coord)
    thisExp.addData('y_coord', y_coord)
    
# completed 5.0 repeats of 'trialss'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
