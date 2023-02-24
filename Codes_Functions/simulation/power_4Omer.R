
library(simr)
library(performance)
library(psycho)
library(lme4)
library(plotrix)
library(MPDiR)
require(tidyverse)

# clear all
rm(list = ls())
setwd("~/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time/Codes_Functions/simulation")

load('sims_power_exp1_4Omer')

sd(data.point$temp_error)
summary(data.point)
df=data.point

# params 
nsim = 100
# n observers for powerCurve
nobs_sim = c(8,10,20,30)

# do lmer
fit.for.power = lmer(temp_error ~ distractor + sqr_distr + third_distr + (1  |subject), data = data.point)
# check object
summary(fit.for.power)

# change coefficients for power 
new_d1 = fixef(fit.for.power)[2]/2
new_d2 = fixef(fit.for.power)[3]/2
new_d3 = fixef(fit.for.power)[4]/2

# add coeffs
fixef(fit.for.power)["distractor"] <- new_d1
fixef(fit.for.power)["sqr_distr"] <- new_d2
fixef(fit.for.power)["third_distr"] <- new_d3

# check updated object
summary(fit.for.power)

# do sim 
#sim_power  = powerSim(fit.for.power,test = fixed("distractor"), nsim=nsim)
sim_power  = powerSim(fit.for.power, test = fcompare(. ~  sqr_distr + third_distr + (1 |subject)), nsim=nsim)
sim_power
summary(sim_power)


# extend n 
fit.for.power_change_n =  extend(fit.for.power, along = 'subject', n=max(nobs_sim))
# check n
nrow(getData(fit.for.power)) 
nrow(getData(fit.for.power_change_n)) 


#sim_power_var_n <- powerCurve(fit.for.power_change_n, test = fixed("distractor"), sim = fit.for.power_change_n, along="subject", breaks=nobs_sim, nsim = nsim)
sim_power_var_n <- powerCurve(fit.for.power_change_n, test = fcompare(. ~  sqr_distr + third_distr + (1 |subject)), sim = fit.for.power_change_n, along="subject", breaks=nobs_sim, nsim = nsim)
print(sim_power_var_n)
plot(sim_power_var_n)

# saving sims
#save.image('sims_power_exp1')


