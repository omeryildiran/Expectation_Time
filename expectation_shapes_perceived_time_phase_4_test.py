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
    frameTolerance = 0.001  # how close to onset before 'same' frame

    # Start Code - component code to be run after the window creation

    # --- Setup the Window ---
    win = visual.Window(
        size=[800,800], fullscr=True, screen=0, 
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
from time2coord import time2coord

try:
    soundVolume=soundVolume
    rep_test=rep_test

except NameError:
    soundVolume=0.65
    rep_test=10

## --- Start Trial Routine --- 
# # --- Initialize components for Routine "trial" ---
# Run 'Begin Experiment' code from pickTargetCol
stimColors=['green','red']
mouse = event.Mouse(win=win,visible=False)
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
## FeedbackPointer
feedbackPointer = visual.ShapeStim(
    win=win, name='feedbackPointer',
    size=(pointer_size, pointer_size), vertices='circle',
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-4.0, interpolate=True)

# Create some handy timers
# Run 'Begin Experiment' code from timingVars

diskRadius=1
durS1=msToFrame(33)
durS2=msToFrame(33)
audCueStart = sound.Sound('audioCue2Init.wav', secs=0.033, stereo=True, hamming=False,
    name='audioCueStart')
audCueStart.setVolume(soundVolume)
outerDisk = visual.ShapeStim(
    win=win, name='outerDisk',units='deg', 
    size=(sizeHand*2, sizeHand*2), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=6,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-3.0, interpolate=False)

target = visual.ShapeStim(
    win=win, name='target',units='deg', 
    size=(diskSize,diskSize), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=False)
cueForRep = visual.ShapeStim(
    win=win, name='cueForRep',units='deg', 
    size=(diskSize,diskSize), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=False)

placeholder = visual.ShapeStim(
    win=win, name='placeholder',units='deg', 
    size=(diskSize+0.1,diskSize+0.1), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=None,
    opacity=None, depth=-4.0, interpolate=False)
audCueEnd = sound.Sound('audioCue2Init.wav', secs=0.033, stereo=True, hamming=False,
    name='audCueEnd')
audCueEnd.setVolume(soundVolume)
sapce2pass_2 = keyboard.Keyboard()
fixationPoint = visual.ShapeStim(
    win=win, name='fixationPoint', vertices='circle', 
    size=(pointer_size, pointer_size),
    ori=45.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
fixation_opacity=1

# Time of stimuli presentation
stimuliOnsetTimes=np.random.uniform(150,1850,rep_test)
### --- Components added

## ---- Prepare to start routine Trial ---
# set up handler to look after randomisation of conditions etc

trialss = data.TrialHandler(nReps=rep_test, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trialss')
thisExp.addLoop(trialss)  # add the loop to the experiment
thisTrials = trialss.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials.rgb)
if thisTrials != None:
    for paramName in thisTrials:
        exec('{} = thisTrials[paramName]'.format(paramName))

test_trialN=-1 #trial number
for thisTrials in trialss:
    test_trialN+=1#trial number increment
    win.setMouseVisible(False)
    currentLoop = trialss
    # abbreviate parameter names if possible (e.g. rgb = thisTrials.rgb)
    if thisTrials != None:
        for paramName in thisTrials:
            exec('{} = thisTrials[paramName]'.format(paramName))
    thisExp.addData("isTrial","test")
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
    shuffle(stimColors)
    targetColor=stimColors[0]

    # Run 'Begin Routine' code from timingVars
    durS1=msToFrame(33)
    durS2=msToFrame(33)
    fColor=1
    ### Timing of objects
    preTrialIntervalMs=1000
    preTrialIntervalFrame=msToFrame(preTrialIntervalMs)
    initIntervalMs=stimuliOnsetTimes[test_trialN] #np.random.uniform(150,1850) # Target onset relative to start of trial
    onsetS1Ms=initIntervalMs
    initInterval=msToFrame(initIntervalMs)

    #midInterval =[-0.300 , -0.233, -0.167, -0.100 , -0.033, 0.033, 0.100 ,0.167, 0.233, 0.300]
    midInterval =[-300 , -233, -167, -100 , -33, 33, 100 ,167, 233, 300]
    shuffle(midInterval)

    #midInterval=msToFrame(midInterval[0])
    onsetS1FrameN=msToFrame(onsetS1Ms)#initInterval
    onsetS2FrameN=msToFrame(onsetS1Ms+midInterval[0])#onsetS1FrameN+midInterval
    lastInterval=msToFrame(2000)-(onsetS2FrameN+33)
    totalTrialDurationFrame=msToFrame(2000)
    apreTrialIntervalMs=300 # the time after trial has finished
    apreTrialIntervalFrame=msToFrame(apreTrialIntervalMs)
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

    # stim_color: color of stimuli in csv file trialList
    target.setFillColor(targetColor)
    target.setLineColor(targetColor)
    cueForRep.setFillColor(targetColor)
    cueForRep.setLineColor(targetColor)
    audCueEnd.setSound('audioCue2Init.wav', secs=0.033, hamming=False)
    audCueEnd.setVolume(soundVolume, log=False)
    audCueStart.setSound('audioCue2Init.wav', secs=0.033, hamming=False)
    audCueStart.setVolume(soundVolume, log=False)
    sapce2pass_2.keys = []
    sapce2pass_2.rt = []
    _sapce2pass_2_allKeys = []
    feedbackPointer.setFillColor(targetColor)
    feedbackPointer.setLineColor(targetColor)
    # Run 'Begin Routine' code from fixOpacitiy
    fixation_opacity=1
    i=0
    # keep track of which components have finished
    trialComponents = [audCueStart, outerDisk, target, placeholder, audCueEnd, sapce2pass_2, fixationPoint,responsePointer,cueForRep,mouse, feedbackPointer]
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
    preTrialIntervalFrame=msToFrame(preTrialIntervalMs)       
    t = 0 
    mouse_has_been_released=False
    responseTimeNotStarted=True
    win.setMouseVisible(False)
    fixationEnded=False
    audCue1Started=False
    audCue2Started=False
    ### --- Save some variables to csv
    thisExp.addData("target_color", targetColor)
    thisExp.addData("expected_target_onset",onsetS1Ms/1000)
    thisExp.addData("expected_target_onset_in_frames",onsetS1FrameN*frameDur)

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
            fixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationPoint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('fixationPoint.started',t)
            fixationPoint.setAutoDraw(True)
        if fixationPoint.status == STARTED:
        #Code for changing fixation opacity
            #fixationPoint.setOpacity(fixation_opacity, log=False)
            # if frameN>fixationPoint.frameNStart+msToFrame(800):
            #     fColor=fColor-(1/msToFrame(200))
            #     fixationPoint.setFillColor([fColor,fColor,fColor], log=False)
            #     fixationPoint.setLineColor([fColor,fColor,fColor], log=False)
            #if frameN >= (preTrialIntervalFrame):
            if tThisFlip >= 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixationPoint.tStop = t  # not accounting for scr refresh
                fixationPoint.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('fixationPoint.stopped',t)
                routineTimer.reset()
                frameN=0
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                t=routineTimer.getTime()   
                fixationPoint.setAutoDraw(False)
                fixationEnded=True
                fColor=1
                # fixationPoint.setFillColor([fColor,fColor,fColor], log=False)
                # fixationPoint.setLineColor([fColor,fColor,fColor], log=False)
        # fixOpacitiy to decrease
        # opacityDecrement=(1/(preTrialIntervalFrame/2))
        # if i>(round(preTrialIntervalFrame/2)):
        #     fixation_opacity=fixation_opacity-opacityDecrement
        # i+=1

        if audCueStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance and fixationEnded==True:
            # keep track of start time/frame for later
            audCueStart.tStart = t  # local t and not account for scr refresh
            audCueStart.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('audCueStart.started', round(t,5))
            audCueStart.play()  # start the sound (it finishes automatically)
            audCue1Started=True
        #if audCueStart.status == STARTED:
        if audCue1Started== True:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > audCueStart.tStartRefresh + 0.033-frameTolerance:
                # add timestamp to datafile
                audCueStart.stop()
                thisExp.addData('audCueStart.stopped', round(t,5))
                audCue1Started=False

        #audCueStart.stream.status.active !=1.0
        # *placeholder* updates
        if placeholder.status == NOT_STARTED and  tThisFlip >= 0.0-frameTolerance and fixationEnded==True:
            # keep track of start time/frame for later
            placeholder.tStart = t  # local t and not account for scr refresh
            placeholder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(placeholder, 'tStartRefresh')  # time at next scr refresh
            thisExp.addData("placeholder.started",round(t,5))
            placeholder.setAutoDraw(True)
            placeholder.status = STARTED

        #    if frameN>= msToFrame(2500)+preTrialIntervalFrame:
        #        placeholder.setAutoDraw(False)

        if placeholder.status == STARTED: 
            if cueForRep.autoDraw==True or target.autoDraw == True:
                placeholder.setAutoDraw(False)
                placeholder.status=STARTED
            elif frameN>= totalTrialDurationFrame:
                placeholder.setAutoDraw(False)
                fixationPoint.setAutoDraw(True)
                fixationPoint.status=NOT_STARTED
                placeholder.status=STARTED
            else:
                placeholder.setAutoDraw(True)


        # *outerDisk* updates
        if outerDisk.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            outerDisk.frameNStart = frameN  # exact frame index
            outerDisk.tStart = t  # local t and not account for scr refresh
            outerDisk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outerDisk, 'tStartRefresh')  # time at next scr refresh
            outerDisk.setAutoDraw(True)
    
        # *target* updates
        if target.status == NOT_STARTED and frameN >= onsetS1FrameN and fixationEnded==True:
            # keep track of start time/frame for later
            thisExp.addData('target.started',t)
            target.setAutoDraw(True)
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile

        if target.status == STARTED:
            if frameN >= (target.frameNStart + durS1):
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile     
                thisExp.addData('target.stopped',t)
                target.setAutoDraw(False)



        if audCueEnd.status == NOT_STARTED and t >= 2.0 and fixationEnded==True:
            # keep track of start time/frame for later
            audCueEnd.frameNStart = frameN  # exact frame index
            audCueEnd.tStart = t  # local t and not account for scr refresh
            audCueEnd.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('audCueEnd.started', t)       
            audCueEnd.play()  # start the sound (it finishes automatically)
            audCue2Started=True
        #if audCueEnd.status == STARTED:
        if audCue2Started== True:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > audCueEnd.tStartRefresh + 0.033-frameTolerance:
                # add timestamp to datafile
                audCueEnd.stop()
                thisExp.addData('audCueEnd.stopped', round(t,5))
                audCue2Started=False
        
        # *sapce2pass_2* updates
        if sapce2pass_2.status == NOT_STARTED and frameN >= totalTrialDurationFrame+apreTrialIntervalFrame:
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
            #if True:
                sapce2pass_2.keys = _sapce2pass_2_allKeys[-1].name  # just the last key pressed
                sapce2pass_2.rt = _sapce2pass_2_allKeys[-1].rt
                continueRoutine = False # a response ends the routine
                     
        

        # *mouse* updates
        if mouse.status == NOT_STARTED and frameN >= totalTrialDurationFrame+apreTrialIntervalFrame:
            # keep track of start time/frame for later
            win.setMouseVisible(True)
            mouse.setPos(newPos=(0,0))
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED and mouse_has_been_released==False:  # only update if started and not finished!
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
                if sum(released)==0:
                    if monitorunittools.pix2deg(pixels=hypoPx,monitor=win.monitor )>(diskSize/2):
                        mouse_has_been_released = True
                        x_coord=mouse.getPos()[0]
                        y_coord=mouse.getPos()[1]
                        gotValidClick = False
                        buttons = mouse.getPressed()
                        mouse.time.append(mouse.mouseClock.getTime())
    

        # *responsePointer* updates
        respX_px=win.size[1]*x_coord   # Coordinate of response X in Pixel 
        respY_px=win.size[1]*y_coord   # Coordinate of response Y in Pixel
        hypoPx=math.sqrt(respX_px**2+respY_px**2)
        if responsePointer.status == NOT_STARTED and frameN >=totalTrialDurationFrame+apreTrialIntervalFrame:
            # keep track of start time/frame for later
            responsePointer.frameNStart = frameN  # exact frame index
            responsePointer.tStart = t  # local t and not account for scr refresh
            responsePointer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responsePointer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            responsePointer.status = STARTED
            thisExp.addData('responsePointer.started',round(t,5))
        if responsePointer.status == STARTED:  # only update if drawing
            if monitorunittools.pix2deg(pixels=hypoPx,monitor=win.monitor )>(diskSize/2):
                responsePointer.setAutoDraw(True)
                if responseTimeNotStarted==True:
                    thisExp.addData("responseStarted",t)
                    thisExp.addData("rtAfterMotionTreshold",t-responsePointer.tStart)
                    responseTimeNotStarted=False
                if mouse.x[0]!=x or mouse.y[0]!=y:
                    x_coord_onCircle=(((respX_px/hypoPx)*sizeHandPix)/win.size[1])
                    y_coord_onCircle=(((respY_px/hypoPx)*sizeHandPix)/win.size[1])              
                    responsePointer.setPos((x_coord_onCircle,y_coord_onCircle),log=False)
                    
                    if mouse_has_been_released == True:
                        responsePointer.tStop= t  # local t and not account for scr refresh
                        responsePointer.frameNstop=frameN
                        thisExp.addData("responsePointer.stopped",t)
                        thisExp.addData("rTAfterMotionTreshold",t-responsePointer.tStart)

                        perceivedTime=round(coord2time(x_coord_onCircle,y_coord_onCircle)/1000,5)
                        thisExp.addData("perceivedTime",perceivedTime)
                        #responsePointer.setAutoDraw(False)
                        thisExp.addData('resp_x_coord', x_coord_onCircle)
                        thisExp.addData('resp_y_coord', y_coord_onCircle)
                    
        #### ------- Updates for PostCue ------
        if cueForRep.status == NOT_STARTED and frameN >= totalTrialDurationFrame+apreTrialIntervalFrame:
            fixationPoint.setAutoDraw(False )
            cueForRep.setAutoDraw(True)
            thisExp.addData('cueForRep.started', t)

        if cueForRep.status == STARTED:
            if continueRoutine == False:
                cueForRep.setAutoDraw(False)

        ###### ----*feedbackPointer* updates
        x_time,y_time=time2coord(initIntervalMs)
        x_time_px=win.size[1]*x_time   # Coordinate of response X in Pixel 
        y_time_px=win.size[1]*y_time   # Coordinate of response Y in Pixel
        hypoPx=math.sqrt(x_time_px**2+y_time_px**2)
        if  mouse_has_been_released==True:
            # keep track of start time/frame for later
            feedbackPointer.frameNStart = frameN  # exact frame index
            feedbackPointer.tStart = t  # local t and not account for scr refresh
            feedbackPointer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackPointer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            feedbackPointer.setAutoDraw(True)
        if feedbackPointer.status == STARTED:  # only update if drawing
            #if mouse.x[0]!=x or mouse.y[0]!=y:
            x_time_onCircle=(((x_time_px/hypoPx)*sizeHandPix)/win.size[1])
            y_time_onCircle=(((y_time_px/hypoPx)*sizeHandPix)/win.size[1])              
            feedbackPointer.setPos((x_time_onCircle,y_time_onCircle),log=False)
            if continueRoutine == False:
                feedbackPointer.tStop= t  # local t and not account for scr refresh
                feedbackPointer.frameNstop=frameN
                thisExp.addData("feedbackPointer.stopped",t)
                feedbackPointer.setAutoDraw(False)
                thisExp.addData('actualTime_x_coord', x_time_onCircle)
                thisExp.addData('actualTime_y_coord', y_time_onCircle)


        
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

