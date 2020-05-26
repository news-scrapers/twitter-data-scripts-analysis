setwd("/Users/hugojosebello/Documents/git-repos/twitter-data-scripts-analysis/")
data_asoc <- read.csv("./data/grouped_data_month_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_asoc_day <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_ibex_day <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_ibex <- read.csv("./data/grouped_data_month_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
library(lubridate)
#data_day$normalised_date <- ymd(data_day$normalised_date)

#install.packages("devtools")
#devtools::install_github("twitter/AnomalyDetection")
library(AnomalyDetection)
d = data("raw_data")
d


df = data_asoc_day[,c("normalised_date","sentiment_truncated")]
df$normalised_date <- as.POSIXct(df$normalised_date)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.05, plot=TRUE)
res$anoms
res$plot

df = data_asoc_day[,c("normalised_date","sentiment")]
df$normalised_date <- as.POSIXct(df$normalised_date)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.05, plot=TRUE)
res$anoms
res$plot

df = data_ibex_day[,c("normalised_date","sentiment_truncated")]
df$normalised_date <- as.POSIXct(df$normalised_date)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.05, plot=TRUE)
res$anoms
res$plot

df = data_ibex_day[,c("normalised_date","sentiment")]
df$normalised_date <- as.POSIXct(df$normalised_date)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.1, plot=TRUE)
res$anoms
res$plot

df = data_asoc[,c("month_year","sentiment")]
df$month_year <- sub("$", "-01", df$month_year )

df$month_year <- as.POSIXct(df$month_year)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.1, plot=TRUE)
res$anoms
res$plot
help(AnomalyDetectionTs)


df = data_ibex[,c("month_year","sentiment")]
df$month_year <- sub("$", "-01", df$month_year )

df$month_year <- as.POSIXct(df$month_year)
res = AnomalyDetectionTs(df, max_anoms=0.03, direction='both',alpha=0.1, plot=TRUE)
res$anoms
res$plot
help(AnomalyDetectionTs)


