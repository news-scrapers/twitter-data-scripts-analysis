
import os
import pandas as pd

directory = '../data'
output_dir = '../data'



def calculate_trimester (row):
        month_code = str(row['date'])
        year = month_code.split("-")[0]
        month = int(month_code.split("-")[1])
        return year + "-" + str(3*((month-1)//3) +1).rjust(2, '0') +"-01"
    

def group_data(df, filename):
    
    df_grouped = df[["date","sentiment"]]
    df["date"]=df["date"].astype(str)

    #print("adding concat tag probab")
    #df_grouped['main_tags_probabilities'] = df_grouped.apply(lambda row: concat_probas(row), axis=1)
    print("calculating dates")

    df_grouped['date'] = pd.to_datetime(df['date'], errors='coerce')
    df_grouped['normalised_date'] = df_grouped['date'].dt.normalize()

    df_grouped['month_year'] = pd.to_datetime(df_grouped['date']).dt.to_period('M')



    print("grouping by day")
    df_grouped_day = df_grouped.groupby(df_grouped.normalised_date).mean()
    df_grouped_day.to_csv(output_dir+"/grouped_data_day_mean_"+filename, sep=";")

    print("grouping by month")
    df_grouped_month = df_grouped.groupby(df_grouped.month_year).mean()
    print(df_grouped_month)
    #df_grouped_month["month_year"] = df_grouped_month.apply(lambda row: complete_with_day(row), axis=1)
    df_grouped_month.to_csv(output_dir+"/grouped_data_month_mean_" + filename, sep=";")



def classify_and_sentiment_dir():
    
    #filename = "tweets_sentimentdata-scraper_asociaciones_2016-2020.csv"
    #filename = "tweets_sentimentdata-scraper_ibex_2018-2020.csv"
    #filename = "tweets_sentimentdata-scraper_asociaciones_peru-2016-2020.csv"
    #filename = "tweets_sentimentdata-scraper_empresas_peru_2017-2020.csv"

    #filename = "full_tweets_sentiment_ngrams_asoc_peru.csv"
    filename = "full_tweets_sentiment_ngrams_asociaciones_empresariales.csv"
    #filename = "full_tweets_sentiment_ngrams_empresas_peru.csv"
    #filename = "full_tweets_sentiment_ngrams_ibex35.csv"

    for filename in ["full_tweets_sentiment_ngrams_asoc_peru.csv", "full_tweets_sentiment_ngrams_empresas_peru.csv", "full_tweets_sentiment_ngrams_asociaciones_empresariales.csv", "full_tweets_sentiment_ngrams_ibex35.csv"]:
        print(filename)
        df = pd.read_csv(directory+"/" +filename, sep=";", lineterminator='\n')
        print(df.shape)
        df=df.drop_duplicates(subset=['id'])
        df=df.drop_duplicates()
        print(df.shape)

        group_data(df, filename)



    #df = group_data(df)

if __name__== "__main__":
    classify_and_sentiment_dir()