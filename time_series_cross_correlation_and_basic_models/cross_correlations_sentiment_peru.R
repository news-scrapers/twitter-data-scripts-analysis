setwd("/Users/hugojosebello/Documents/git-repos/twitter-data-scripts-analysis/")
data_asoc_month <- read.csv("./data/grouped_data_month_mean_tweets_sentimentdata-scraper_asociaciones_peru-2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_asoc_day <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_peru-2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)

library(lubridate)
library(ggplot2)

data_asoc_month$month_year <- sub("$", "-01", data_asoc_month$month_year )

data_asoc_month$month_year <- ymd(data_asoc_month$month_year)
data_asoc_day$normalised_date <- ymd(data_asoc_day$normalised_date)

data_asoc_month$sentiment_diff <- append(diff(data_asoc_month$sentiment), 0, after = 0)
data_asoc_day$sentiment_diff <- append(diff(data_asoc_day$sentiment), 0, after = 0)

#graphs
ggplot(data_asoc_month, aes(month_year, sentiment_diff)) + geom_line() + xlab("") + ylab("sentiment asociaciones diff")
ggplot(data_asoc_month, aes(month_year, sentiment)) + geom_line() + xlab("") + ylab("sentiment asociaciones diff")
ggplot(data_asoc_day, aes(normalised_date, sentiment)) + geom_line() + xlab("") + ylab("sentiment asociaciones diff")

#graphs_mix



ts_asoc_day = ts(data_asoc_day$sentiment, frequency = 30)
decompose_ts_asoc_day = decompose(ts_asoc_day, "additive")
plot(decompose_ts_asoc_day)

ts.plot(diff(data_ecoicop$indice_general),  main = "" )

ccf(data_ibex_month$sentiment_diff,data_ecoicop$indice_general)
ccf(data_asoc_month$sentiment_diff,data_ecoicop$indice_general)

#!! data_asoc_month leads with lag 1 over data_ibex_month 
ccf(data_ibex_month$sentiment_diff,data_asoc_month$sentiment_diff)




