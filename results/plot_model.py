from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, MaxPooling1D, Flatten, GlobalMaxPool1D, Dropout, Conv1D
from keras.utils.vis_utils import plot_model

model = Sequential()
model.add(Embedding(1000, 20, input_length=300))
model.add(Dropout(0.1))
model.add(Conv1D(20, 5, activation='relu'))
model.add(Conv1D(20, 5, activation='relu'))
model.add(MaxPooling1D(5))
model.add(Conv1D(20, 5, activation='relu'))
model.add(Conv1D(20, 5, activation='relu'))
model.add(GlobalMaxPool1D())
model.add(Dense(1, activation='sigmoid'))
plot_model(model, to_file='model_plot.png', expand_nested=False, show_shapes=False,rankdir="LR", show_layer_names=False)

