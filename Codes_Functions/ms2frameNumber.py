# ms to frameNumber
#fps=expInfo['frameRate']
#frameDur = 1.0 / round(expInfo['frameRate'])
def s2nFrame(durInS):
	#durInS=0.33
	#fps=expInfo['frameRate']
	fps= 59# lets say it is 60
	preciseFrameDur=1.0/fps # expInfo['frameRate']
	nFrame=round(durInS/preciseFrameDur)
	return(nFrame)

print(s2nFrame(0.033))

   #x_train=latent_data_overall
    #put randomly selected training data instead of whole training
    x_train=x_train_vShort
    
    x_test=latent_data_test

    #factor='type_truncted'
    labels_train = list(trainscenes[factor])
    labels_test=list(testscenes[factor])
    
    #y_train=labels_train
    #put randomly selected training LABELS instead of whole training
    y_train=y_train_vShort