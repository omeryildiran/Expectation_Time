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

"""
standAlone=True # If you run this code to run whole experiment you need to always state that standAlone is True
## creating mapping of experimental blocks
blockDict={'base':"trial_list_0.5_0.csv",
           'mod':"trials_mod_exp",
           "high":"trial_list_0.85_0.csv",
          'mod2':"trials_mod_exp_2",
          "high2":"trial_list_0.8_red.csv"}#

soundVolume=0.65
# 0 - initiate exp
exec(open("expectation_shapes_perceived_time_0_initiateExp.py").read())
# 1 - Welcome Screen
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
# 2 - Familiarization
rep_fam=20
exec(open("expectation_shapes_perceived_time_phase_2_familiarization.py").read())
# 3 - Test instructions
exec(open("expectation_shapes_perceived_time_phase_3_testInstructions.py").read())
##### Test Phase ###########################################################################################
##### 4 - Test Single stim with feedback 
rep_test=40
exec(open("expectation_shapes_perceived_time_phase_4_test.py").read())
# 4.1 - Test with 1 wo feedback
this_text="Great! now after a couple of clock adaptation you will continue these trials without feedback:"
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
rep_fam=5
exec(open("expectation_shapes_perceived_time_phase_2_familiarization.py").read())
rep_test=40
exec(open("expectation_shapes_perceived_time_phase_4_test_singleStim.py").read())
# 4.2- Double_stim_training
this_text="Now you will do the same task, only this time there you will see two"\
" consequent different colored stimuli."\
" But you will be asked for reporting time of one of them at the end of trial."
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
expBlock="training_double_stim.csv"
rep_trial=4
exec(open("expectation_shapes_perceived_time_phase_6_trial.py").read())
########################################################################################################
# 5 - Trial instructions
exec(open("expectation_shapes_perceived_time_phase_5_trialInstructions.py").read())
# 6 - Trial Phase
block_type="high2"
expBlock=blockDict[block_type]
rep_trial=1
# if block_type in ["mod" ,"mod2"]:     rep_trial=5
# elif block_type in["high", "high2"]: rep_trial=5
# elif block_type=="base" : rep_trial=5
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
