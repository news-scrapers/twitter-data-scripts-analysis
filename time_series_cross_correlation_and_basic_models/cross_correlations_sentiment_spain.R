setwd("/Users/hugojosebello/Documents/git-repos/twitter-data-scripts-analysis/")
data_asoc_month <- read.csv("./data/grouped_data_month_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_asoc_day <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_ibex_day <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_ibex_month <- read.csv("./data/grouped_data_month_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
data_precios_ibex <- read.csv("./data/ibex_historico.csv",  header=TRUE, sep=",", stringsAsFactors = TRUE)
data_ecoicop   <- read.csv("./data/ecoicop.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
library(lubridate)
library(ggplot2)

data_asoc_month$month_year <- sub("$", "-01", data_asoc_month$month_year )
data_ibex_month$month_year <- sub("$", "-01", data_ibex_month$month_year )

data_ecoicop$date <- ymd(data_ecoicop$date)
data_ibex_month$month_year <- ymd(data_ibex_month$month_year)
data_asoc_month$month_year <- ymd(data_asoc_month$month_year)

data_ibex_month$sentiment_diff <- append(diff(data_ibex_month$sentiment), 0, after = 0)
data_asoc_month$sentiment_diff <- append(diff(data_asoc_month$sentiment), 0, after = 0)
data_ibex_day$sentiment_diff <- append(diff(data_ibex_day$sentiment), 0, after = 0)
data_asoc_day$sentiment_diff <- append(diff(data_asoc_day$sentiment), 0, after = 0)
data_precios_ibex$Close_diff <- append(diff(data_precios_ibex$Close), 0, after = 0)

#graphs
ggplot(data_ecoicop, aes(date, indice_general)) + geom_line() + xlab("") + ylab("indice_general")
ggplot(data_ibex_month, aes(month_year, sentiment_diff)) + geom_line() + xlab("") + ylab("sentiment ibex diff")
ggplot(data_asoc_month, aes(month_year, sentiment_diff)) + geom_line() + xlab("") + ylab("sentiment asociaciones diff")
ggplot(data_ibex_month, aes(month_year, sentiment)) + geom_line() + xlab("") + ylab("")
ggplot(data_ibex_month, aes(month_year, favorites)) + geom_line() + xlab("") + ylab("")

#graphs_mix


ts.plot(diff(data_ecoicop$indice_general),  main = "" )

ccf(data_ibex_month$sentiment_diff,data_ecoicop$indice_general)
ccf(data_asoc_month$sentiment_diff,data_ecoicop$indice_general)

#!! data_asoc_month leads with lag 1 over data_ibex_month 
ccf(data_ibex_month$sentiment_diff,data_asoc_month$sentiment_diff)



data_asoc
acf(diff(data_asoc_day$sentiment))

acf(data_asoc_day$sentiment)
acf(data_ibex_day$sentiment)

ccf(data_ibex_day$sentiment, data_precios_ibex$Close,lag.max = 50)
ccf(data_ibex_day$sentiment_truncated, data_precios_ibex$Close,lag.max = 50)
ccf(data_ibex_day$sentiment_diff, data_precios_ibex$Close_diff,lag.max = 200)

#!! data precios ibex lead sentiment
ccf(data_asoc_day$sentiment_diff, data_precios_ibex$Close_diff,lag.max = 50)



hist(data_asoc_day$sentiment)
plot(data_asoc$sentiment)
plot(diff(data_asoc$sentiment))


