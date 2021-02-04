from sentiment_analysis_spanish import sentiment_analysis
#from subject_classification_spanish import subject_classifier

import os
import pandas as pd

directory = '../data'
output_dir = '../data'


sentiment = sentiment_analysis.SentimentAnalysisSpanish()
#print(sentiment.sentiment("me gusta la tombola es genial"))

#subject_class = subject_classifier.SubjectClassifier()
#subject_class_main_tags = subject_classifier.SubjectClassifier(use_main_tags_only=True)


def sentiment_row(row):
    return sentiment.sentiment(row['text'])

def classify_and_sentiment(df, filename):
    
    df_base = df[["id", "date", "text", "reply_to"]]

    print("calculating sentiment")
    df_sentiment = df_base
    #∫df_sentiment['text'] = df_sentiment['text'].map(lambda x: x.replace("#"," "))
    #df_sentiment = df_sentiment[df_sentiment['reply_to'].isnull()]
    print(df_sentiment.text)

    print("calculating sentiment on each row")

    df_sentiment['sentiment'] = df_sentiment.apply(lambda row: sentiment_row(row), axis=1)

    print("truncating sentiment")

    df_sentiment = df_sentiment[["id", "date", "text","sentiment"]]

    print("saving file")

    df_sentiment.to_csv(output_dir+"/full_tweets_sentiment" +filename, sep=";")

    
if __name__== "__main__":

    #filename = "data-scraper_asociaciones_2016-2020.csv"
    #filename = "data-scraper_ibex_2018-2020.csv"
    #filename = "data-scraper_empresas_peru_2017-2020.csv"
    #filename = "data-scraper_asociaciones_peru-2016-2020.csv"

    #asoc_peru.csv
    #asociaciones_empresariales.csv
    #empresas_peru.csv
    #ibex35.csv

    #filename = "asoc_peru.csv"
    #filename = "asociaciones_empresariales.csv"
    #filename = "empresas_peru.csv"
    #filename = "ibex35.csv"

    for filename in ["empresas_peru.csv", "ibex35.csv"]:
        df = pd.read_csv(directory+"/"+ filename,sep=",")
        df['text'] =  df['text'].astype(str)
        classify_and_sentiment(df, filename)