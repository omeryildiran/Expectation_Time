
standAlone=True # If you run this code to run whole experiment you need to always state that standAlone is True
## creating mapping of experimental blocks
blockDict={'base':"trial_list_0.5_0.csv",
           'mod':"trials_mod_exp",
           "high":"trial_list_0.7_0.csv",
          'mod2':"trials_mod_exp_2",
          "high2":"trial_list_0.7_1.csv"}#


# 0 - initiate exp
exec(open("expectation_shapes_perceived_time_0_initiateExp.py").read())
# 1 - Welcome Screen
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
# 2 - Familiarization
rep_fam=5
exec(open("expectation_shapes_perceived_time_phase_2_familiarization.py").read())
# 3 - Test instructions
exec(open("expectation_shapes_perceived_time_phase_3_testInstructions.py").read())
##### Test Phase ###########################################################################################
##### 4 - Test Single stim with feedback 
rep_test=20
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
"consequent different colored stimuli"\
"But you will be asked for reporting color of one of them at the end of trial."
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
expBlock="training_double_stim.csv"
rep_trial=4
exec(open("expectation_shapes_perceived_time_phase_6_trial.py").read())
########################################################################################################
# 5 - Trial instructions
exec(open("expectation_shapes_perceived_time_phase_5_trialInstructions.py").read())
# 6 - Trial Phase
block_type="base"
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
