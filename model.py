from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def create_model(seq_length, num_features):
    model = Sequential()
    model.add(LSTM(50, input_shape=(seq_length, num_features)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model
