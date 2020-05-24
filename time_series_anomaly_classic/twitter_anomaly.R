setwd("/Users/hugojosebello/Documents/git-repos/twitter-data-scripts-analysis/")
data <- read.csv("./data/grouped_data_month_mean.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_day <- read.csv("./data/grouped_data_day_mean.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
library(lubridate)
#data_day$normalised_date <- ymd(data_day$normalised_date)

#install.packages("devtools")
#devtools::install_github("twitter/AnomalyDetection")
library(AnomalyDetection)
d = data("raw_data")
d


df = data_day[,c("normalised_date","sentiment")]
df$normalised_date <- as.POSIXct(df$normalised_date)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.05, plot=TRUE)
res$anoms
res$plot
help(AnomalyDetectionTs)


df = data[,c("month_year","sentiment")]
df$month_year <- sub("$", "-01", df$month_year )

df$month_year <- as.POSIXct(df$month_year)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.1, plot=TRUE)
res$anoms
res$plot
help(AnomalyDetectionTs)
