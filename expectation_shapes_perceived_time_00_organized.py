""" Coded by Omer Yildiran in January 2023.

    For the research of "Expectation and Perceived Time Among Other Events" Omer Yildiran, Pascal Mamassian, 2023

    In the Lab of Dr. Pascal Mamassian at the Ecole Normale Superieure in Paris (ENS-PSL), Laboratoire de Systeme Perceptifs (LSP)
    This code is the main code for the experiment. It is organized in phases and blocks.
    The experiment is divided into 3 phases: Familiarization, Test and Trial.
    The familiarization phase is divided into 2 blocks: Single_stim and Double_stim.
    The test phase is divided into 2 blocks: Single_stim and Double_stim.
    qThe trial phase is divided into 4 blocks: base, mod, high and high2.
    The base block is the baseline condition, in which the participant is asked to report the time of the one of the stimulus, and the probability of each stimulus to be asked is equal.
    The high block is the high condition, in which the participant is asked to report the time of the one of the stimulus, but the probability 
    of reporting (the stimulus in question at the end) the time of the cetain stimulus is higher.
    This code and all the custom functions are written in Python and PsychoPy, with also the help of PsychoPy Builder.
    The code is subject to change and update and under creative commons license.
    You can use modify and share this code as long as you give credit to the original author.

    #### Experiment Instructions ####
    In this study, you will be given a series of trials. In each trial, you will see a clock's circle and two different colored disk. The disk will be presented in one of two colors: red or green. 
    After end of the trial, you will be asked to report the time of one of the disks by clicking appropriate position on the clock's circle.
    The color of the disk you will be asked to report will be indicated by cue which is exactly same as the target disk's color and size.
    The cue will be presented at the end of the trial.
    In the baseline condition, the probability of reporting the time of the disk is equal for each color.
    In the expectation condition, the probability of reporting the time of the disk is higher for one of the colors.
    The experiment is consisted of 3 phases: Familiarization, Test and Trial.
    In the familiarization phase, there will be a clock lasting for a specific amount of time and the hand of clock will be rotating from 12'o clock position to 12'o clock position.
    In the test phase, you will solve the trials but this time you will be given feedback about your performance.
    In the trial phase, you will solve the trials without feedback.
    There will be 500 trials and you will be given breaks in every 25 trial.
"""
testing=False 
standAlone=True # If you run this code to run whole experiment you need to always state that standAlone is True
## creating mapping of experimental blocks
blockDict={'base1':"trial_list_0.5_green.csv",
            'base2':"trial_list_0.5_red.csv",
           'mod':"trials_mod_exp",
           "high1":"trial_list_0.8_green.csv",
          'mod2':"trials_mod_exp_2",
          "high2":"trial_list_0.8_red.csv"}#

block_type="high2"
#block_type="mod2"
firstOrder=True #
if firstOrder:
    initFam=20
    singleStimWithFeedback=20
    secondFam=5
    singleStimNoFeedback=40 
    doubleStim=2
else:
    initFam=5
    singleStimWithFeedback=5
    secondFam=0
    singleStimNoFeedback=0
    doubleStim=1


soundVolume=0.65
############################################################################################################


# 0 - initiate exp
exec(open("expectation_shapes_perceived_time_0_initiateExp.py").read())
# 1 - Welcome Screen
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
# 2 - Familiarization
rep_fam=initFam
exec(open("expectation_shapes_perceived_time_phase_2_familiarization.py").read())
# 3 - Test instructions
exec(open("expectation_shapes_perceived_time_phase_3_testInstructions.py").read())
##### Test Phase ###########################################################################################
##### 4 - Test Single stim with feedback 
rep_test=singleStimWithFeedback
exec(open("expectation_shapes_perceived_time_phase_4_test.py").read())
# 4.1 - Test with 1 wo feedback
this_text="Great! now after a couple of clock adaptation you will continue these trials without feedback:"
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
rep_fam=secondFam
exec(open("expectation_shapes_perceived_time_phase_2_familiarization.py").read())
rep_test=singleStimNoFeedback
exec(open("expectation_shapes_perceived_time_phase_4_test_singleStim.py").read())
# 4.2- Double_stim_training
this_text="Now you will do the same task, only this time there you will see two"\
" consequent different colored stimuli."\
" But you will be asked for reporting time of one of them at the end of trial."
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
expBlock="training_double_stim.csv"
rep_trial=doubleStim
exec(open("expectation_shapes_perceived_time_phase_6_trial.py").read())
########################################################################################################

# 5 - Trial instructions
exec(open("expectation_shapes_perceived_time_phase_5_trialInstructions.py").read())


# 6 - Trial Phase
#block_type="high2"
expBlock=blockDict[block_type]
rep_trial=1
exec(open("expectation_shapes_perceived_time_phase_6_trial.py").read())

# 7 - End of Exp
exec(open("expectation_shapes_perceived_time_phase_7_endOfExperiment.py").read())
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
