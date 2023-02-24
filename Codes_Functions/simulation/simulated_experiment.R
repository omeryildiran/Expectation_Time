setwd("~/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time")
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

# fixed factor coefficients
delay_coeff=0.38
expectation_coeff=-0.4
expectation_coeff85=-0.6
congruencynone=0.01
congruencyunmet=-0.9
congruency_coeff=-0.4
expectation_full_congruencyunmet=-0.7
fixed= c(3.0,delay_coeff,expectation_coeff,expectation_coeff85,congruencyunmet,expectation_full_congruencyunmet,0.08,-0.08)
fixed= c(3.0,delay_coeff,expectation_coeff,expectation_coeff85,congruencyunmet,expectation_full_congruencyunmet)


model <- makeLmer(y ~ delay+expectation+congruency+expectation*congruency+delay*congruency +(1|id)+(1|trial_num), fixef=fixed, VarCorr=0.1, sigma=100, data=df)# sigma=res,
model
sim_model=powerSim(model, nsim=100)


#Predicted results based on hard coded data
#####
p_curve_sim_expectation <- powerCurve(sim_model, test=fcompare(y~congruency), along="id")
plot(p_curve_sim_expectation)
