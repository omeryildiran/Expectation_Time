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
    prefs.hardware['audioLib'] = 'PTB'
    prefs.hardware['audioLatencyMode'] = '4'
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
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # --- Setup the Window ---
    win = visual.Window(
        size=[800,800], fullscr=False, screen=0, 
        winType='pyglet', allowStencil=False,
        monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
        blendMode='avg', useFBO=True, 
        units='height')
    win.mouseVisible = False
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
    sizeHand=6#2.5
    sizeHandPix=monitorunittools.deg2pix(degrees=sizeHand,monitor=win.monitor)
    sizeClockCentre=0.5# =fixation point
    sizePlaceholder=3#1
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
### Start Exp
try:
    soundVolume=soundVolume
except NameError:
    soundVolume=0.75

### ----- initiate Components --- 
clockOutDisk = visual.ShapeStim(
    win=win, name='clockOutDisk',units='deg', 
    size=(sizeHand*2, sizeHand*2), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-3.0, interpolate=True)
clockHand = visual.ShapeStim(
    win=win, name='clockHand', vertices=[[0,0],[1,1]],units='deg', 
    size=(sizeHand-0.2, 0.0001),
    ori=1.0, pos=(0, 0), anchor='bottom-center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=False)
audioCue2Start = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='audioCue2Start')
audioCue2Start.setVolume(soundVolume)
audioCue2End = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='audioCue2End')
audioCue2End.setVolume(soundVolume)
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
    pos=(0, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
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

## timing variables of Familiarization
clockDuration=msToFrame(2000)
afterRevolution=msToFrame(200)
# set up handler to look after randomisation of conditions etc
try:
    rep_fam=rep_fam
except NameError:
    rep_fam=3
famLoop = data.TrialHandler(nReps=rep_fam, method='random', 
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
    thisExp.addData("isTrial","fam")
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
    
    #key2pass
    sapce2pass.keys = []
    sapce2pass.rt = []
    _sapce2pass_allKeys = []

    audioCue2Start.setSound('audioCue2Init.wav',secs=0.033, hamming=False)
    audioCue2Start.setVolume(soundVolume, log=False)
    audioCue2End.setSound('audioCue2Init.wav', secs=0.033,hamming=False)
    audioCue2End.setVolume(soundVolume, log=False)
    # keep track of which components have finished
    famComponents = [clockOutDisk, clockHand, audioCue2Start, audioCue2End, centreClock,sapce2pass,continueFam]
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
                thisExp.addData('handMove.started', t)
                frameHand=0
                
        
        if frameHand<round(2*fps):
            oriHand+=oriPerFrame
            #fColor=fColor-0.0085
            #clockHand.setOri(oriHand, log=False)
            frameHand+=1
        elif frameHand==round(2*fps):
             thisExp.addData('handOri',oriHand) 
             thisExp.addData('handMove.ended', t)
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
            win.timeOnFlip(clockOutDisk, 'tStartRefresh')  # time at next scr refresh
            clockOutDisk.setAutoDraw(True)
        if clockOutDisk.status == STARTED:
            if frameN >= (clockOutDisk.frameNStart + clockRotStart+clockDuration):
                # keep track of stop time/frame for later
                clockOutDisk.tStop = t  # not accounting for scr refresh
                clockOutDisk.frameNStop = frameN  # exact frame index
                #clockOutDisk.setAutoDraw(False)
        
        # *clockHand* updates
        if clockHand.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            clockHand.frameNStart = frameN  # exact frame index
            clockHand.tStart = t  # local t and not account for scr refresh
            clockHand.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clockHand, 'tStartRefresh')  # time at next scr refresh
            clockHand.setAutoDraw(True)
        if clockHand.status == STARTED:
            if frameN >= (clockHand.frameNStart + clockRotStart+clockDuration+afterRevolution):
                # keep track of stop time/frame for later
                clockHand.tStop = t  # not accounting for scr refresh
                clockHand.frameNStop = frameN  # exact frame index
                #clockHand.setAutoDraw(False)
        if clockHand.status == STARTED:  # only update if drawing
            clockHand.setOri(oriHand, log=False)
        # start/stop audioCue2Start
        if audioCue2Start.status == NOT_STARTED and frameN >= toneStart:
        #if audioCue2Start.status == NOT_STARTED and  frameN >= clockRotStart+round(2*fps):

            # keep track of start time/frame for later
            audioCue2Start.frameNStart = frameN  # exact frame index
            #audioCue2Start.tStart = t  # local t and not account for scr refresh
            #audioCue2Start.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            audioCue2Start.play()  # sync with win flip
            thisExp.addData('audioCue2Start.started', t)
        # start/stop audioCue2End
        if audioCue2End.status == NOT_STARTED and frameN >= clockRotStart+clockDuration:
            # keep track of start time/frame for later
            audioCue2End.frameNStart = frameN  # exact frame index
            audioCue2End.tStart = t  # local t and not account for scr refresh
            audioCue2End.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('audioCue2End.started', t)
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
            if frameN >= (centreClock.frameNStart + clockRotStart+clockDuration+afterRevolution):
                # keep track of stop time/frame for later
                centreClock.tStop = t  # not accounting for scr refresh
                centreClock.frameNStop = frameN  # exact frame index
                #centreClock.setAutoDraw(False)
        if centreClock.status == STARTED:  # only update if drawing
            centreClock.setFillColor([fColor,fColor,fColor], log=False)
        
        
        # *continueFam* updates
        if frameN >= (centreClock.frameNStart + clockRotStart+clockDuration+afterRevolution):
                        # keep track of start time/frame for later
            continueFam.frameNStart = frameN  # exact frame index
            continueFam.tStart = t  # local t and not account for scr refresh
            continueFam.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continueFam, 'tStartRefresh')  # time at next scr refresh
            continueFam.setAutoDraw(True)

        
        # *sapce2pass* updates
        waitOnFlip = False
        if sapce2pass.status == NOT_STARTED and frameN >= (centreClock.frameNStart + clockRotStart+clockDuration+afterRevolution):
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
            try: 
                if testing:      continueRoutine=False
            except NameError:     pass
        if sapce2pass.status == STARTED and not waitOnFlip:
            theseKeys = sapce2pass.getKeys(keyList=['space'], waitRelease=False)
            _sapce2pass_allKeys.extend(theseKeys)
            if len(_sapce2pass_allKeys):
                sapce2pass.keys = _sapce2pass_allKeys[-1].name  # just the last key pressed
                sapce2pass.rt = _sapce2pass_allKeys[-1].rt
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
    
    # # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'famLoop'
