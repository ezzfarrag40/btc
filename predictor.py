import numpy as np
from sklearn.preprocessing import MinMaxScaler
from data import load_data, create_sequences
from model import create_model

# Set the sequence length and number of features
seq_length = 24
num_features = 4

# Load and preprocess the data
data, scaler = load_data()
x, y = create_sequences(data, seq_length)

# Split the data into training and testing sets
train_size = int(len(x) * 0.8)
x_train, y_train = x[:train_size], y[:train_size]
x_test, y_test = x[train_size:], y[train_size:]

# Create and train the model
model = create_model(seq_length, num_features)
model.fit(x_train, y_train, epochs=50, batch_size=64, validation_data=(x_test, y_test))

# Make predictions for the next 24 hours
last_day = data[-seq_length:, :]
prediction = []
for i in range(24):
    seq = np.expand_dims(last_day, axis=0)
    pred = model.predict(seq)
    prediction.append(pred[0][0])
    last_day = np.vstack((last_day[1:], pred))

# Scale the predictions back to the original range
prediction = np.array(prediction).reshape(-1, 1)
prediction = scaler.inverse_transform(prediction)

print(prediction)
