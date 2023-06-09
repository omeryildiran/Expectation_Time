setwd("~/Omer_Documents/Omer_Repos/Internship Pascal/Expectation_Shapes_Perceived_Time_final/analysis")

library(ggplot2)
#084661_expectation_shapes_perceived_time_2023-03-09_21h27.15.100 test
#274531_expectation_shapes_perceived_time_2023-03-10_10h12.16.162
# first 084661_expectation_shapes_perceived_time_2023-03-09_21h27.15.100
#df=read.csv("data/274531_expectation_shapes_perceived_time_2023-03-10_10h12.16.162.csv")
#df=read.csv("nicola_pilot_expectation_shapes_perceived_time_2023-03-16_15h38.21.393.csv")
df=read.csv("niho_pilot_base_expectation_shapes_perceived_time_2023-03-16_23h46.19.804.csv")
df=read.csv("omer_pilot2_expectation_shapes_perceived_time_2023-03-17_00h51.58.576.csv")
df=read.csv("omer_pilot1_expectation_shapes_perceived_time_2023-03-17_12h35.14.339.csv")
df=read.csv("omer_pilot_high_exp_expectation_shapes_perceived_time_2023-03-17_12h35.14.339.csv")
df=read.csv("299271_expectation_shapes_perceived_time_2023-03-19_15h42.48.633.csv")
df=read.csv("nicola_base_pilot_expectation_shapes_perceived_time_2023-03-20_15h03.16.305.csv")
as=read.csv(paste("data/",data_Erva_70,sep=""))
rm(as) 
data_nicola_85_1="nicola_85_1_expectation_shapes_perceived_time_2023-03-28_15h04.34.263.csv"
data_Erva_70="erva07_expectation_shapes_perceived_time_2023-03-23_20h55.33.677.csv"
data_omer_80G="omer80G_expectation_shapes_perceived_time_2023-04-03_14h30.36.416.csv" #expected 80 percent
data_omer70="omer70_expectation_shapes_perceived_time_2023-03-27_21h43.36.152.csv"
data_erva_80="erva80G_expectation_shapes_perceived_time_2023-04-07_23h25.04.855.csv"
data_omer_85="omer85_high_exp_expectation_shapes_perceived_time_2023-03-17_12h35.14.339.csv"
data_elaine80="elaine08R_expectation_shapes_perceived_time_2023-04-13_17h14.41.421.csv"
data_paths=c(data_omer_85,data_omer70,data_omer_80G,data_Erva_70,data_erva_80,data_nicola_85_1)
df=read.csv(paste("data/",data_omer_85,sep=""))


### Function for cleaning data
data_cleaner <- function(data) {
  df=read.csv(paste("data/",data,sep=""))
  #df <- read.csv(paste0(data_folder, data))
  df$delayS <- df$delay / 1000
  df$pTemporalError <- df$perceivedTime - df$target.started
  df$pTemporalErrorMs <- df$pTemporalError * 1000
  df$physicalDelay <- df$distractor.started - df$target.started
  df$physicalDelayMs <- df$physicalDelay * 1000
  df_test <- df[df$isTrial == "testSingleStim", ]
  avgError <- mean(df_test$perceivedTime - df_test$target.started)
  df <- df[df$isTrial == "trial" & !is.na(df$pTemporalError), ]
  df$pTemporalErrorAveraged <- df$pTemporalError - avgError
  df = df[, c("delayS","pTemporalError","pTemporalErrorMs","perceivedTime", "isTrial","target_color","stim_color","distractor_color","trial_num","delay","physicalDelayMs","physicalDelay","expectation","congruency","target.started",
              "pTemporalErrorAveraged","participant","rTAfterMotionTreshold","responseStarted")]
  df$trialNum=seq_len(nrow(df))
  df$sqr_distr=df$delayS**2
  df$third_distr=df$delayS**3
  df$quad_distr=df$delayS**4
  df$modeled_time_error=(df$expectation)*df$delayS*exp(-(df$delayS**2))
  return (df)
}


data_paths=c(data_omer_80G,data_erva_80,data_elaine80)
df_pilot=data.frame()
for (i in data_paths){
  tmp=data_cleaner(i)
  df_pilot=rbind(df_pilot,tmp)
  rm(tmp)
}
df_omer_85=data_cleaner(data_omer_85)
df_nicola85=data_cleaner(data_nicola_85_1)
df_omer80=data_cleaner(data_omer_80G)
df_erva80=data_cleaner(data_erva_80)

######
df_nicola85$expectation[df_nicola85$expectation==0.85]=0.8
df_omer_85$expectation[df_omer_85$expectation==0.85]=0.8
df_pilot=rbind(df_nicola85,df_omer_85,)

df_pilot$sqr_distr=df_pilot$delayS**2
df_pilot$third_distr=df_pilot$delayS**3
df_pilot$quad_distr=df_pilot$delayS**4
df_pilot$modeled_time_error=(df_pilot$expectation)*df_pilot$delayS*exp(-(df_pilot$delayS**2))

#####

df_omer=data_cleaner(data_omer_80G)
df_erva80=data_cleaner(data_erva_80)
df_pilot=rbind(df_omer,df_erva80)
df_erva70$id=1
df_omer80=data_cleaner(data_omer70)
df_omer70$id=2
# df=read.csv(data_omer_80G)
# df=read.csv(data_Erva_70)
# df=df[df$isTrial=="trial",]
# df$delayS=df$delay/1000
# df$pTemporalError=df$perceivedTime-df$target.started
# df$pTemporalErrorMS=df$pTemporalError*1000
# df$physicalDelay=df$distractor.started-df$target.started
# df$physicalDelayMS=df$physicalDelay*1000
# df <- df[,!names(df) %in% c("famLoop.thisRepN", "famLoop.thisTrialN", " famLoop.thisN ","famLoop.thisIndex")]
# df$distractor.started
# df$physicalDelay
# df$delay
# df$perceivedTime

summary()
mean(df_erva80$rtAfterMotionTreshold)

ggplot(data=df_pilot,aes(x=rtAfterMotionTreshold,y=perceivedTime),fill=df_pilot$congruency)+
  geom_point()+
  ylim(0,2)+
  xlim(0,2)+
  geom_abline(intercept = 0, slope = 1)+
  coord_fixed()
  


summary(df_pilot)
#df=df[41:nrow(df),]
head(df_trials)


df_met=df[df$congruency=="met",]
df_unmet=df[df$congruency=="unmet",]
median(df_met$rTAfterMotionTreshold)
median(df_unmet$rTAfterMotionTreshold)
summary(df_met)
summary(df_unmet)

t.test(df_met$pTemporalErrorMS,df_unmet$pTemporalErrorMS)



ggplot(data=df,aes(x=physicalDelay,y=pTemporalError))+
  geom_point()+
  #geom_line()+
  geom_smooth(method='lm', formula= y~x)+
  #geom_smooth()+
  #xlim(-0.32,+0.32)+
  #ylim(0,1.9)+
  facet_wrap(~congruency)+
  scale_x_continuous(n.breaks = 15)+
  scale_y_continuous(n.breaks =15)+# limits=c(-1000,1000))+
  geom_hline(yintercept = 0,alpha=0.3) + geom_vline(xintercept = 0,alpha=0.3)



ggplot(data=df, aes(x=perceivedTime,y=target.started))+
  geom_point()+
  geom_smooth(method='lm', formula= y~x)+
  #geom_smooth()+
  facet_wrap(~congruency)



###
df_unmet[,c(2,56)]
## plot met and unmet together
  ggplot(data=df,aes(x=physicalDelay,y=delayS))+
  geom_point()


ggplot(data=df,aes(x=physicalDelayMS,y=pTemporalErrorMS,color=target_color))+
  geom_point()+
  #geom_line()+
  geom_smooth()+
  #xlim(-0.32,+0.32)+
  #ylim(0,1.9)+
  facet_wrap(~congruency)+
  scale_x_continuous(n.breaks = 10)+
  scale_y_continuous(n.breaks =10)+
  geom_hline(yintercept = 0,alpha=0.3) + geom_vline(xintercept = 0,alpha=0.3)


summary(as.factor(df$delay))
max(df$target.started)
min(df$target.started)

min(df$distractor.started)
max(df$distractor.started)

ggplot(data=df,aes(x=df$expected_target_onset))+
  geom_histogram()
  













# plot unmet
ggplot(data=df,aes(x=delayS,y=df$expected_delays_frame,color=target_color))+
  geom_point()+
  geom_line()+
  geom_smooth()+
  xlim(-0.32,+0.32)+
  ylim(-1,+1)+
  facet_wrap(~target_color)



ggplot(data=df,aes(x=physicalDelay,y=delay,color=as.character(congruency)))+
  geom_jitter()+
  geom_line()+
  geom_smooth()+
  xlim(-0.4,+0.4)+
  ylim(-1,+1)

ggplot(data=df,aes(x=physicalDelay,y=pTemporalError))+
  geom_jitter()+
  geom_line()+
  geom_smooth()+
  xlim(-0.4,+0.4)+
  ylim(-1,+1)
## plot met 
