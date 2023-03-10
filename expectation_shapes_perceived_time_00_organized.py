standAlone=True
# 0 - initiate exp
exec(open("expectation_shapes_perceived_time_0_initiateExp.py").read())
# 1 - Welcome Screen
exec(open("expectation_shapes_perceived_time_phase_1_welcome.py").read())
# 2 - Familiarization
rep_fam=2
exec(open("expectation_shapes_perceived_time_phase_2_familiarization.py").read())
# 3 - Test instructions
exec(open("expectation_shapes_perceived_time_phase_3_testInstructions.py").read())
# 4 - Test phase
rep_test=2
exec(open("expectation_shapes_perceived_time_phase_4_test.py").read())
# 5 - Trial instructions
exec(open("expectation_shapes_perceived_time_phase_5_trialInstructions.py").read())
# 6 - Trial Phase
rep_trial=2
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
