from sklearn.preprocessing import MultiLabelBinarizer
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Dense, LSTM, SimpleRNN, Activation, Embedding, MaxPooling1D, Flatten, GlobalMaxPool1D, Dropout, Conv1D
from keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from matplotlib import pyplot
from sklearn.model_selection import train_test_split

from keras.preprocessing.sequence import pad_sequences

import pandas as pd
import numpy as np
import pickle
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

def test_window_functions():
    future_steps = 2
    past_steps = 3
    arr = [1,2,3,4,5,6,7,8,9,10][:-future_steps]
    arr2 = [11, 12, 13, 14,15, 16,17,18,19, 20][:-future_steps]
    Y = [111,112, 113, 114,115, 116,117,118,119, 120]


    #Y = np.array([211,212, 213, 214,215, 216,217,218,219, 220])

    X = create_window_data_arrays([arr, arr2], past_steps)
    Y = create_window_data_array_with_shift(Y,future_steps,past_steps +future_steps)
    print(X)
    print(Y)
    print(X.shape)
    print(Y.shape)

def create_model_and_train(train_X, train_y, test_X, test_y, output_size):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(output_size))

    model.compile(loss='mae', optimizer='adam',metrics=['accuracy'])
    # fit network
    history = model.fit(train_X, train_y, epochs=100, batch_size=20, validation_data=(test_X, test_y), verbose=2, shuffle=False)
    # plot history
    print(history)
    pyplot.plot(history.history['loss'], label='train')
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    pyplot.show()
    return model

def save_model(model):
        print("saving model")
        # serialize model to JSON
        model_json = model.to_json()
        with open("../data/model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        model.save_weights("../data/model.h5")
        print("Saved model to disk")

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
    df_total = df_total.dropna()

    
    num_steps = 20
    future_steps = 2

    X_sent_asoc = df_total["sentiment_asociacones"].values[:-future_steps]
    X_sent_ibex = df_total["sentiment_ibex"].values[:-future_steps]
    X_ibex_prices = df_total["Close"].values[:-future_steps]
    X_ibex_prices_next = df_total["Close"].values

    X = np.array(create_window_data_arrays([X_sent_asoc, X_sent_ibex, X_ibex_prices], num_steps))
    Y = create_window_data_array_with_shift(X_ibex_prices_next,future_steps, num_steps +future_steps)
    print(X.shape, Y.shape)

    train_X, test_X, train_y, test_y = train_test_split(
    X, Y, test_size=0.10, random_state=1000)
   
    print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

    test_window_functions()

    model = create_model_and_train(train_X, train_y, test_X, test_y, future_steps)
    save_model(model)


    val_sent_asoc = df_total["sentiment_asociacones"].values[-num_steps-future_steps:-future_steps]
    val_sent_ibex = df_total["sentiment_ibex"].values[-num_steps-future_steps:-future_steps]
    val_ibex_prices = df_total["Close"].values[-num_steps-future_steps:-future_steps]
    X_val=[]
    for i in range (0,num_steps):
        new = np.array([val_sent_asoc[i], val_sent_ibex[i],val_ibex_prices[i]])
        X_val.append(new)
    X_val= np.array(X_val)
    print(X_val.shape)

    yhat = model.predict(np.array([X_val]), verbose=0)
    # we only want the vector forecast

    print(df_total.tail(future_steps+1))
    print(X_val)
    print(yhat)
    #yhat = yhat[0]