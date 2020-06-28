setwd("/Users/hugojosebello/Documents/git-repos/twitter-data-scripts-analysis/")

asoc_es <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
asoc_es$sentiment = append(0,diff(asoc_es$sentiment))

empresas_es <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
empresas_es$sentiment = append(0,diff(empresas_es$sentiment))


asoc_pe <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_peru-2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
asoc_pe$sentiment = append(0,diff(asoc_pe$sentiment))


empresas_pe <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_empresas_peru_2017-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
empresas_pe$sentiment = append(0,diff(empresas_pe$sentiment))


library(lubridate)

asoc_es$normalised_date <- ymd(asoc_es$normalised_date)
empresas_es$normalised_date <- ymd(empresas_es$normalised_date)
asoc_pe$normalised_date <- ymd(asoc_pe$normalised_date)
empresas_pe$normalised_date <- ymd(empresas_pe$normalised_date)
empresas_es<-empresas_es[empresas_es$normalised_date >= "2017-07-01",]
empresas_pe<-empresas_pe[empresas_pe$normalised_date >= "2017-07-01",]
asoc_pe<-asoc_pe[asoc_pe$normalised_date >= "2017-07-01",]
asoc_es<-asoc_es[asoc_es$normalised_date >= "2017-07-01",]

empresas_es


library(ggplot2)


ggplot(asoc_es, aes(normalised_date, sentiment)) + geom_line() + xlab("") + ylab("variation of average daily sentiment\n main business associations Spain")

ggplot(asoc_pe, aes(normalised_date, sentiment)) + geom_line() + xlab("") + ylab("variation of average daily sentiment\n main business associations Peru")


ggplot(empresas_es, aes(normalised_date, sentiment)) + geom_line() + xlab("") + ylab("variation of average daily sentiment\n main companies Spain")


ggplot(empresas_pe, aes(normalised_date, sentiment)) + geom_line() + xlab("") + ylab("variation of average daily sentiment\n main companies Peru")

