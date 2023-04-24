## ---- Run initiator code itself if its not in initiator directory ----
#This code will help debugging when only working with phases of experiment

try: 
    if standAlone == True:
        pass
except NameError:
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
        size=[800,800], fullscr=True, screen=0, 
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
    # # ----- Variables and Parameters ----- 
    fColor=1
    sizeHand=5#2.5
    sizeHandPix=monitorunittools.deg2pix(degrees=sizeHand,monitor=win.monitor)
    sizeClockCentre=0.5# =fixation point
    sizePlaceholder=2#1
    diskSize=sizePlaceholder
    pointer_size=monitorunittools.deg2pix(degrees=sizeClockCentre,monitor=win.monitor)/win.size[1]
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
    toneStart=msToFrame(500)
    clockRotStart=toneStart

    # Create some handy timers
    globalClock = core.Clock()  # to track the time since experiment started
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

### End initiator run
## Start EXP
standAlone=True
# --- Initialize components for Routine "welcomeScr" ---
welcomeTxt = visual.TextStim(win=win, name='welcomeTxt',
    text="Here comes the actual experiment trials. If you dont feel confident enough you can press 'left' key to redo the test trials\n"\
    "In this phase, you will see two disks on the screen, one red and one green."\
    "Only one of these disks will be the target stimulus, which will be shown at the response phase. "\
    "You will be asked to report the onset time of the target disk only by clicking on the clock circle. "\
    "Please click on the circle to indicate the perceived onset time of the target disk."\
    "Get Ready and press 'space' to start!",
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
skipWelcome = keyboard.Keyboard()

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
againTest=True
while againTest==True:
    againTest=False

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
            try: 
                if testing:      continueRoutine=False
            except NameError:     pass
        

        if skipWelcome.status == STARTED and not waitOnFlip:
            theseKeys = skipWelcome.getKeys(keyList=['space','left'], waitRelease=False)
            _skipWelcome_allKeys.extend(theseKeys)
            if len(_skipWelcome_allKeys):
                skipWelcome.keys = _skipWelcome_allKeys[-1].name  # just the last key pressed
                skipWelcome.rt = _skipWelcome_allKeys[-1].rt
                if skipWelcome.keys=='left':
                    continueRoutine = False
                    againTest=True
                else:
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

    for thisComponent in welcomeScrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if againTest==True:
        rep_test=5
        exec(open("expectation_shapes_perceived_time_phase_4_test.py").read())
        exec(open("expectation_shapes_perceived_time_phase_5_trialInstructions.py").read())
    # --- Ending Routine "welcomeScr" ---
    # the Routine "welcomeScr" was not non-slip safe, so reset the non-slip ti mer
    routineTimer.reset()
