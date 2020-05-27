from sklearn.preprocessing import MultiLabelBinarizer
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, MaxPooling1D, Flatten, GlobalMaxPool1D, Dropout, Conv1D
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint

from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences

import pandas as pd
import numpy as np
import pickle


def create_window_data(array,window_size):
    windows = []
    for i in range(window_size,len(array)):
        newItem = []
        for j in reversed(range(0,window_size)):
            newItem.append(array[i-j])
        windows.append(newItem)
    return windows

def create_window_data_two_arrays(array1, array2,window_size):
    windows = []
    for i in range(window_size,len(array1)):
        newItem = []
        for j in reversed(range(0,window_size)):
            newItem.append(array1[i-j])

        for j in reversed(range(0,window_size)):
            newItem.append(array2[i-j])
        windows.append(newItem)
    return windows

def create_window_data_arrays(arrays,window_size):
    windows = []
    for i in range(window_size,len(arrays[0])):
        newItem = []
        for array in arrays:
            for j in reversed(range(0,window_size)):
                newItem.append(array[i-j])
        windows.append(newItem)
    return windows



if __name__== "__main__":
    filename_asoc = "../data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv"
    filename_ibex ="../data/grouped_data_day_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv"
    filename_ibex_prices ="../data/ibex_historico.csv"


    df_asoc = pd.read_csv(filename_asoc, sep=";")
    df_ibex = pd.read_csv(filename_ibex, sep=";")
    df_ibex_prices = pd.read_csv(filename_ibex_prices, sep=",")

    df_x = pd.merge(left=df_asoc, right=df_ibex, left_on='normalised_date', right_on='normalised_date')
    df_total = pd.merge(left=df_x, right=df_ibex_prices, left_on='normalised_date', right_on='Date')
    df_total = df_total.rename(columns={"sentiment_x": "sentiment_asociacones", "sentiment_y": "sentiment_ibex"})
    
    
    X_sent_asoc = df_total["sentiment_asociacones"].values
    X_sent_ibex = df_total["sentiment_ibex"].values


    arr = [1,2,3,4,5,6,7,8,9,10]
    arr2 = [11, 12, 13, 14,15, 16,17,18,19, 20]
    print(create_window_data_arrays([arr,arr2, arr], 3))


    