setwd("~/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time/Codes_Functions/simulation")
library(tidyverse)
df=read.csv("predicted results 2.csv")
library(ggplot2)
#install.packages("patchwork")
library(patchwork)

##### Simulation
library(simr)

setwd("~/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time")
#Create covariates
library(simr)
expectation <- factor(c(0.5,0.65,0.85))
expectation <- factor(c("None","Modete","High"))
expectation<- c(0.5,0.65,0.85)
samp_size=5
expectation_full=rep(rep(expectation,each=500),samp_size)
expectation_full=factor(expectation_full)

subj <- factor(1:samp_size)
subj_full=rep(rep(subj,each=1500),1)

dtDelay=c(-300,-233,-167,-100,-33,33,100,167,233,300)
dtDelay_full <- rep(rep(dtDelay, 150),samp_size)
trial_num=c(1:500)
trial_num_full=rep(trial_num,3)
## Create no_expectation conditions
no_expectation=rep("none",500)
## Create Moderate expectation conditions
moderate_expectation_met=rep("met",65)
moderate_expectation_unmet=rep("unmet",35)
moderate_expectation=c(moderate_expectation_unmet,moderate_expectation_met)
moderate_expectation=sample(moderate_expectation)
moderate_expectation=rep(moderate_expectation,5)
## Create high_expectation conditions
high_expectation_met=rep("met",85)
high_expectation_unmet=rep("unmet",15)
high_expectation=c(high_expectation_met,high_expectation_unmet)
high_expectation=sample(high_expectation)
high_expectation=rep(high_expectation,5)


### Full expectation Congruencies
expectation_congruency_full=factor(c(no_expectation,moderate_expectation,high_expectation))
expectation_congruency_full=rep(expectation_congruency_full,samp_size)
length(expectation_congruency_full)
###


df <- data.frame(id=subj_full, delay=dtDelay_full, expectation=expectation_full, congruency=expectation_congruency_full,trial_num=trial_num_full)
summary(df)
df$expectation=as.factor(df$expectation)
df$delay=as.factor(df$delay)
###

#coefficients
## Intercept and slopes for intervention, time1, time2, intervention:time1, intervention:time2
fixed <- c(5, 0, 0.3, -1, 1, -1)
fixed <- c(5, 0, 0.1, 0.2, 1, 0.9)

## Random intercepts for participants clustered by class
rand <- list(0.5, 0.1)

## residual variance
res <- 2
# y ~ delay * expectation
df$delay=as.factor(df$delay)
delay_coeff=0.38
expectation_coeff=-0.4
expectation_coeff85=-0.6
congruencynone=0.01
congruencyunmet=-0.9
congruency_coeff=-0.4
expectation_full_congruencyunmet=-0.7
fixed= c(3.0,delay_coeff,expectation_coeff,expectation_coeff85,congruencyunmet,expectation_full_congruencyunmet,0.08,-0.08)
fixed= c(3.0,delay_coeff,expectation_coeff,expectation_coeff85,congruencyunmet,expectation_full_congruencyunmet)

df$delay=as.factor(df$delay)
model <- makeLmer(y ~ delay+expectation+congruency+expectation*congruency+delay*congruency +(1|id), fixef=fixed, VarCorr=0.1, sigma=100, data=df)# sigma=res,
#model <- makeLmer(y ~ delay+expectation*congruency +(1|id), fixef=fixed, VarCorr=0.1, sigma=0.5, data=df)# sigma=res,
model

#summary(model)
#model <- makeGlmer(y ~ delay+expectation+congruency+expectation*congruency+delay*congruency +(1|id), family="poisson",fixef=fixed, VarCorr=0.1, data=df)# sigma=res,

sim_expectation <- powerSim(model, nsim=100, test = fcompare(y ~ delay+congruency))
sim_expectation
#Predicted results based on hard coded data
#####
p_curve_sim_expectation <- powerCurve(model, test=fcompare(y~congruency), along="id")
plot(p_curve_sim_expectation)


#####
df$Distractor.Target.Delay.D.T.= as.numeric(df$Distractor.Target.Delay.D.T.)
p=ggplot(data=df,aes(x=Distractor.Target.Delay.D.T., y=Perceived.Time.Error,color=Expectation.Congruency..Met.Unmet.))+
  geom_jitter()+
  geom_smooth()+
  scale_x_continuous(labels=as.character(df$Distractor.Target.Delay.D.T.),breaks=df$Distractor.Target.Delay.D.T.)+
  #geom_line()+
  geom_line(y=0,color='black')+
  #geom_hline(yintercept = 0, color="black")+
  #geom_vline(xintercept=0, color="black")+
  facet_wrap(~df$Block.Type+df$Expectation.Congruency..Met.Unmet.)
  #geom_line(x=0,color='black')
  
p=p+  geom_vline(xintercept=0, color="black")
p
p + labs(title = "Predicted Temporal Errors", x="Distractor-Target Delay",y="Perceived time Error")




p+    theme(
  axis.title = element_text( color="red", size=15, face=2),
  #axis.line = element_line(size = 3, colour = "green", linetype=2),
  #axis.text = element_text( angle = 90, color="blue", size=15, face=2)
)

#p+geom_line()
#mean_wt=data.frame(c(-60,75,-60,75,-7)
p + geom_hline(yintercept = )

p

dfNoExp=df[df$Block.Type=="No Expectation",]
dfExpMet65=df[df$Block.Type=="Moderate Expectation " & df$Expectation.Congruency..Met.Unmet.=="Met",]
dfExpMet85=df[df$Block.Type=="High Expectation " & df$Expectation.Congruency..Met.Unmet.=="Met",]
dfExpUnMet65=df[df$Block.Type=="Moderate Expectation " & df$Expectation.Congruency..Met.Unmet.=="Unmet",]
dfExpUnMet85=df[df$Block.Type=="High Expectation " & df$Expectation.Congruency..Met.Unmet.=="Unmet",]

NoExp=ggplot(data=dfNoExp,aes(x=Distractor.Target.Delay.D.T., y=Perceived.Time.Error,color=Expectation.Congruency..Met.Unmet.))+
  geom_jitter()+
  geom_smooth()+
  ylim(-100,+100)+
  scale_x_continuous(labels=as.character(df$Distractor.Target.Delay.D.T.),breaks=df$Distractor.Target.Delay.D.T.)+
  #geom_line()+
  geom_line(y=0,color='black')+
  geom_hline(yintercept = mean(dfNoExp$Perceived.Time.Error), color="blue")+
  geom_vline(xintercept=0, color="black")+
  labs(title = "No Expectation Block", x="Distractor-Target Delay(ms)",y="Perceived time Error(ms)")+
  theme(legend.position="none",plot.title= element_text( color="blue", size=16, face=2),
        axis.title = element_text( color="black", size=13, face=2),
        axis.text=element_text(size=11,face=2))
NoExp

highExp=ggplot(data=dfExpMet85,aes(x=Distractor.Target.Delay.D.T., y=Perceived.Time.Error))+
  geom_jitter(color="aquamarine4")+
  geom_smooth(color="aquamarine4")+
  ylim(-100,+100)+
  scale_x_continuous(labels=as.character(df$Distractor.Target.Delay.D.T.),breaks=df$Distractor.Target.Delay.D.T.)+
  #geom_line()+
  geom_line(y=0,color='black')+
  geom_hline(yintercept = mean(dfExpMet85$Perceived.Time.Error), color="blue")+
  geom_vline(xintercept=0, color="black")+
  labs(title = "High Expectation Block - Expectation Met", x="Distractor-Target Delay(ms)",y="Perceived time Error(ms)")+
  theme(legend.position="none",plot.title= element_text( color="blue", size=16, face=2),
        axis.title = element_text( color="black", size=13, face=2),
        axis.text=element_text(size=11,face=2))
highExp


modExp=ggplot(data=dfExpMet65,aes(x=Distractor.Target.Delay.D.T., y=Perceived.Time.Error))+
  geom_jitter(color="aquamarine3")+
  geom_smooth(color="aquamarine3")+
  ylim(-100,+100)+
  scale_x_continuous(labels=as.character(df$Distractor.Target.Delay.D.T.),breaks=df$Distractor.Target.Delay.D.T.)+
  #geom_line()+
  geom_line(y=0,color='black')+
  geom_hline(yintercept = mean(dfExpMet65$Perceived.Time.Error), color="blue")+
  geom_vline(xintercept=0, color="black")+
  labs(title = "Moderate Expectation Block - Expectation Met", x="Distractor-Target Delay(ms)",y="Perceived time Error(ms)")+
  theme(legend.position="none",plot.title= element_text( color="blue", size=16, face=2),
        axis.title = element_text( color="black", size=13, face=2),
        axis.text=element_text(size=11,face=2))
modExp

modExpUnmet=ggplot(data=dfExpUnMet65,aes(x=Distractor.Target.Delay.D.T., y=Perceived.Time.Error))+
  geom_jitter(color="darkorchid3")+
  geom_smooth(color="darkorchid3")+
  ylim(-100,+100)+
  scale_x_continuous(labels=as.character(df$Distractor.Target.Delay.D.T.),breaks=df$Distractor.Target.Delay.D.T.)+
  #geom_line()+
  geom_line(y=0,color='black')+
  geom_hline(yintercept = mean(dfExpUnMet65$Perceived.Time.Error), color="blue")+
  geom_vline(xintercept=0, color="black")+
  labs(title = "Moderate Expectation Block - Expectation Unmet", x="Distractor-Target Delay(ms)",y="Perceived time Error(ms)")+
  theme(legend.position="none",plot.title= element_text( color="blue", size=16, face=2),
        axis.title = element_text( color="black", size=13, face=2),
        axis.text=element_text(size=11,face=2))
modExpUnmet

highExpUnmet=ggplot(data=dfExpUnMet85,aes(x=Distractor.Target.Delay.D.T., y=Perceived.Time.Error))+
  geom_jitter(color="darkorchid4")+
  geom_smooth(color="darkorchid4")+
  ylim(-100,+100)+
  scale_x_continuous(labels=as.character(df$Distractor.Target.Delay.D.T.),breaks=df$Distractor.Target.Delay.D.T.)+
  #geom_line()+
  geom_line(y=0,color='black')+
  geom_hline(yintercept = mean(dfExpUnMet85$Perceived.Time.Error), color="blue")+
  geom_vline(xintercept=0, color="black")+
  labs(title = "High Expectation Block - Expectation Unmet", x="Distractor-Target Delay(ms)",y="Perceived time Error(ms)")+
  theme(legend.position="none",plot.title= element_text( color="blue", size=16, face=2),
        axis.title = element_text( color="black", size=13, face=2),
        axis.text=element_text(size=11,face=2))
highExpUnmet
  #facet_wrap(~df$Block.Type+df$Expectation.Congruency..Met.Unmet.)
#geom_line(x=0,color='black')


means=aggregate(df$Perceived.Time.Error~df$Expectation.Congruency..Met.Unmet.,FUN=mean)
means


