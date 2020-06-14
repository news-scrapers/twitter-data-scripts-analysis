from sentiment_analysis_spanish import sentiment_analysis
from subject_classification_spanish import subject_classifier

import os
import pandas as pd

directory = '../data'
output_dir = '../data'


sentiment = sentiment_analysis.SentimentAnalysisSpanish()
#print(sentiment.sentiment("me gusta la tombola es genial"))

subject_class = subject_classifier.SubjectClassifier()
subject_class_main_tags = subject_classifier.SubjectClassifier(use_main_tags_only=True)


def subjects_join(row):
    return "--".join(list(subject_class.classify(row['text']).keys()))

def subjects_probability_join(row):
    classification_list = subject_class.obtain_raw_probabilities(row['text'])[0]
    return "--".join(str(e) for e in classification_list)

def main_tags_probability_join(row):
    classification_list = subject_class_main_tags.obtain_raw_probabilities(row['text'])[0]
    return "--".join(str(e) for e in classification_list)


def main_tags(row):
    return subject_class_main_tags.classify(row['text'])

def sentiment_row(row):
    return sentiment.sentiment(row['text'])

def sentiment_truncated(row):
    sent = row['sentiment']
    if sent < 0.001:
        return 0
    elif sent > 0.5:
        return 1
    else:
        return 0.5

def classify_and_sentiment(df, filename):
    
    df_base = df[["id", "date", "text", "favorites", "to", "retweets","replies"]]

    print("calculating sentiment")
    df_sentiment = df_base
    #∫df_sentiment['text'] = df_sentiment['text'].map(lambda x: x.replace("#"," "))
    df_sentiment = df_sentiment[df_sentiment['to'].isnull()]
    print(df_sentiment)
    df_sentiment['sentiment'] = df_sentiment.apply(lambda row: sentiment_row(row), axis=1)
    df_sentiment['sentiment_truncated'] = df_sentiment.apply(lambda row: sentiment_truncated(row), axis=1)
    df_sentiment = df_sentiment[["id", "date", "text","sentiment", "sentiment_truncated", "favorites", "retweets","replies"]]
    df_sentiment.to_csv(output_dir+"/tweets_sentiment" +filename, sep=";")
"""
    print("calculating main tags classification")
    df_subjects = df_base
    df_subjects['subjects_probabilities_array'] = df_subjects.apply(lambda row: subjects_probability_join(row), axis=1)
    
    print("calculating main_tags")
    df_subjects['main_tags'] = df_subjects.apply(lambda row: main_tags_probability_join(row), axis=1)
    df_subjects['subjects'] = df_subjects.apply(lambda row: subjects_join(row), axis=1)

    df_subjects = df_subjects[["id", "date","text", "main_tags","subjects", 'subjects_probabilities_array']]
    df_subjects.to_csv(output_dir+"/tweets_subjects_" + filename, sep=";")
"""
    
if __name__== "__main__":

    #filename = "data-scraper_asociaciones_2016-2020.csv"
    #filename = "data-scraper_ibex_2018-2020.csv"
    filename = "data-scraper_empresas_peru_2017-2020.csv"
    #filename = "data-scraper_asociaciones_peru-2016-2020.csv"
    df = pd.read_csv(directory+"/"+ filename,sep=";")
    df['text'] =  df['text'].astype(str)
    classify_and_sentiment(df, filename)