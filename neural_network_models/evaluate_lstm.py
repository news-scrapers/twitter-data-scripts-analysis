from sklearn.preprocessing import MultiLabelBinarizer
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, LSTM, SimpleRNN, Activation, Embedding, MaxPooling1D, Flatten, GlobalMaxPool1D, Dropout, Conv1D
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from keras.models import model_from_json

from keras.preprocessing.sequence import pad_sequences

import pandas as pd
import numpy as np
import pickle
from matplotlib import pyplot

#https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/


def create_window_data_arrays(arrays,window_size):
    windows = []
    for i in range(window_size,len(arrays[0])):
        newItem = []
        for j in reversed(range(0,window_size)):
            combined_item = []
            for array in arrays:
                combined_item.append(array[i-j])
            newItem.append(combined_item)
        windows.append(np.array(newItem))
    return np.array(windows)

def create_window_data_array_with_shift(array,window_size, shift):
    windows = []
    #we iterate the series
    for i in range(shift,len(array)):
        newItem = []
        for j in reversed(range(0,window_size)):
            newItem.append(array[i-j])
        windows.append(np.array(newItem))
    return np.array(windows)

def read_model():
   
    return model


if __name__== "__main__":
    filename_asoc = "../data/grouped_data_day_mean_tweets_sentimentdata-scraper_asociaciones_2016-2020.csv"
    filename_ibex ="../data/grouped_data_day_mean_tweets_sentimentdata-scraper_ibex_2018-2020.csv"
    filename_ibex_prices ="../data/ibex_historico.csv"
    filename_model = "../data/model_lstm.h5"
    filename_model_json = "../data/model_lstm.json"


    df_asoc = pd.read_csv(filename_asoc, sep=";")
    df_ibex = pd.read_csv(filename_ibex, sep=";")
    df_ibex_prices = pd.read_csv(filename_ibex_prices, sep=",")

    df_x = pd.merge(left=df_asoc, right=df_ibex, left_on='normalised_date', right_on='normalised_date')
    df_total = pd.merge(left=df_x, right=df_ibex_prices, left_on='normalised_date', right_on='Date')
    df_total = df_total.rename(columns={"sentiment_x": "sentiment_asociacones", "sentiment_y": "sentiment_ibex"})
    df_total = df_total.dropna()

    
    num_steps = 7
    future_steps = 1
    X_sent_asoc = df_total["sentiment_asociacones"].values[:-future_steps]
    X_sent_ibex = df_total["sentiment_ibex"].values[:-future_steps]
    X_ibex_prices = df_total["Close"].values[:-future_steps]
    X_ibex_prices_next = df_total["Close"].values

    X = np.array(create_window_data_arrays([X_sent_asoc, X_sent_ibex, X_ibex_prices], num_steps))
    
    json_model_keras = open(filename_model_json, 'r')
    loaded_model_json = json_model_keras.read()
    json_model_keras.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights(filename_model)

    # evaluate loaded model on test data
    loaded_model.compile(optimizer='adam', loss='mse',  metrics=['mae','accuracy'])

    predictions = []
    for elem in X:
        prediction = loaded_model.predict(np.array([elem]))
        predictions.append([prediction[0][0]])
    print(predictions)

    

    
    #yhat = yhat[0]