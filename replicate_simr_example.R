setwd("~/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time")
#Create covariates
library(simr)
expectation <- factor(c(0.5,0.65,0.85))
expectation <- c(0.5,0.65,0.85)

dtDelay=c(-300,-233,-167,-100,-33,33,100,167,233,300)
expectation_congruency= factor(c("none","met","unmet"))
time <- 0:2
group <- c("control", "intervention")

dtDelay_full <- rep(dtDelay, 60)
expectation_congruency_full=rep(rep(expectation_congruency, each=200), 1)
class_full <- rep(rep(class_id, each=10), 3)
time_full <- rep(time, each=50)
group_full <- rep(rep(group, each=5), 15)

covars <- data.frame(id=subj_full, class=class_full, treat=group_full, time=factor(time_full))

covars

# y∼treatment+time+treatment×time+(1|class/id)+ϵ

## Intercept and slopes for intervention, time1, time2, intervention:time1, intervention:time2
fixed <- c(5, 0, 0.1, 0.2, 1, 0.9)
## Random intercepts for participants clustered by class
rand <- list(0.5, 0.1)
## residual variance
res <- 2


model <- makeLmer(y ~ treat*time + (1|class/id), fixef=fixed, VarCorr=rand, sigma=res, data=covars)
model

#effect of time
sim_treat <- powerSim(model, nsim=100, test = fcompare(y~time))
sim_treat

#effect of time

sim_time <- powerSim(model, nsim=100, test = fcompare(y~treat))
sim_time


## Change effect Size
model_large <- model
fixef(model_large)['treatintervention:time1'] <- 2

sim_treat_large <- powerSim(model_large, nsim=100, test = fcompare(y~time))
sim_treat_large

#Changing the number of classes used in study

model_ext_class <- extend(model, along="class", n=20)
model_ext_class

sim_treat_subj <- powerSim(model_ext_subj, nsim=100, test = fcompare(y~time))
sim_treat_subj

p_curve_treat <- powerCurve(model_ext_subj, test=fcompare(y~time), within="class+treat+time", breaks=c(5,10,15,20))
plot(p_curve_treat)


# Change number of participants
model_final <- extend(model, along="class", n=8)
model_final <- extend(model_final, within="class+treat+time", n=10)

sim_final <- powerSim(model_final, nsim=100, test = fcompare(y~time))
sim_final


p_curve_treat <- powerCurve(model_final, test=fcompare(y~time), within="class+treat+time", breaks=c(5,10,15,20))
plot(p_curve_treat)

