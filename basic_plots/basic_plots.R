setwd("/Users/hugojosebello/Documents/git-repos/twitter-data-scripts-analysis/")

asoc_es <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
asoc_es$sentiment_diff = append(0,diff(asoc_es$sentiment))

empresas_es <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
empresas_es$sentiment_diff = append(0,diff(empresas_es$sentiment))


asoc_pe <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_peru-2016-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
asoc_pe$sentiment_diff = append(0,diff(asoc_pe$sentiment))


empresas_pe <- read.csv("./data/grouped_data_day_mean_tweets_sentimentdata-scraper_empresas_peru_2017-2020.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
empresas_pe$sentiment_diff = append(0,diff(empresas_pe$sentiment))


stocks_peru <- read.csv("./data/pe_bvl_mean_day.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)
stocks_spain <- read.csv("./data/es_mse_mean_day.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE)


data_es <- read.csv("./data/df_total_es.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE) 
data_pe <- read.csv("./data/df_total_pe.csv",  header=TRUE, sep=";", stringsAsFactors = TRUE) 


library(lubridate)

stocks_peru$date <- as.Date(stocks_peru$date , format = "%m/%d/%y")
stocks_peru$date <- ymd(stocks_peru$date)

stocks_spain$date <- as.Date(stocks_spain$date , format = "%m/%d/%y")
stocks_spain$date <- ymd(stocks_spain$date)

#install.packages("gtools")
library(gtools)
a <- bind_rows(empresas_es, asoc_es)
a <- merge(empresas_es, asoc_es, by.x="normalised_date", by.y="date")

asoc_es$normalised_date <- ymd(asoc_es$normalised_date)
data_pe$normalised_date <- ymd(data_pe$normalised_date)
data_es$normalised_date <- ymd(data_es$normalised_date)
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


ccf(data_es$sentiment_asociacones, data_es$madrid_change)
ccf(data_es$sentiment_ibex, data_es$madrid_change)

ccf(data_pe$sentiment_asociacones, data_pe$peru_change)
ccf(data_pe$sentiment_empresas, data_es$peru_change)



data_pe<-data_pe[data_pe$normalised_date <= "2020-01-01",]
data_es<-data_es[data_es$normalised_date <= "2020-01-01",]

ccf(data_es$sentiment_asociacones, data_es$madrid_change)
ccf(data_es$sentiment_ibex, data_es$madrid_change)

ccf(data_pe$sentiment_asociacones, data_pe$peru_change)
ccf(data_pe$sentiment_empresas, data_pe$peru_change)



require(smooth)

ts_asoc_es = ts(asoc_es$sentiment, frequency = 7)
decompose_ts_asoc_es = decompose(ts_asoc_es, "additive")
plot(decompose_ts_asoc_es)

ts_asoc_pe = ts(asoc_pe$sentiment, frequency = 7)
decompose_ts_asoc_pe = decompose(ts_asoc_pe, "additive")
plot(decompose_ts_asoc_pe)


ts_empresas_es = ts(empresas_es$sentiment, frequency = 7)
decompose_ts_empresas_es = decompose(ts_empresas_es, "additive")
plot(decompose_ts_empresas_es)

ts_empresas_pe = ts(empresas_pe$sentiment, frequency = 7)
decompose_ts_empresas_pe = decompose(ts_empresas_pe, "additive")

plot(decompose_ts_empresas_pe)
plot(decompose_ts_asoc_es$trend)


ccf(decompose_ts_asoc_es$trend, data_es$madrid_change)


