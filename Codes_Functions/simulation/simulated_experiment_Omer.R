setwd("~/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time")
library(ggplot2)
##### Simulation
library(simr)
library(simr)
### Create Covarietes
samp_size=5 ### SAMPLE size
expectation<- c(0.5,0.65,0.85)
expectation_full=rep(rep(expectation,each=500),samp_size)
#expectation_full=factor(expectation_full)
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
df$expectation[df$expectation==0.65 & df$congruency=="unmet"]=0.35
df$expectation[df$expectation==0.85 & df$congruency=="unmet"]=0.15
colors=c("red","green")
noexp_color=sample(colors,replace=TRUE)
df$color="green"
df$color[df$expectation=="0.35" & df$congruency=="unmet"]="red"
df$color[df$expectation=="0.15" & df$congruency=="unmet"]="red"
df$color[df$expectation=="0.65" & df$congruency=="met"]="green"
df$color[df$expectation=="0.85" & df$congruency=="met"]="green"
df$color[df$expectation==0.50]=noexp_color
df$color=as.factor(df$color)
summary(df)

###
#coefficients
## Intercept and slopes for intervention, time1, time2, intervention:time1, intervention:time2
fixed <- c(5, 0, 0.38, -1, 1, -1)
## Random intercepts for participants clustered by class
rand <- list(0.1)
## residual variance
res <- 2
# fixed factor coefficients
delay_coeff=0.38
fixed <- c(5, 0.38, -2, 0.2)


model <- makeLmer(y ~ delay*expectation +(1|id), fixef=fixed, VarCorr=0.1, sigma=100, data=df)# sigma=res,
model

#Predicted results based on hard coded data
#####
p_curve_sim_expectation <- powerCurve(model, test=fcompare(y~ delay*expectation +(1|id)), along="id")
plot(p_curve_sim_expectation)
