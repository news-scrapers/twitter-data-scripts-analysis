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


#graphs
plot(diff(data_ibex_month$sentiment))
ggplot(data_ecoicop, aes(date, indice_general)) + geom_line() + xlab("") + ylab("")
ggplot(data_ibex_month, aes(month_year, sentiment)) + geom_line() + xlab("") + ylab("")


acf(diff(data_asoc_day$sentiment))

acf(data_asoc_day$sentiment)
acf(data_ibex_day$sentiment)

ccf(data_ibex_day$sentiment, data_precios_ibex$Close)
ccf(data_asoc_day$sentiment, data_precios_ibex$Close)



hist(data_asoc_day$sentiment)
plot(data_asoc$sentiment)
plot(diff(data_asoc$sentiment))


