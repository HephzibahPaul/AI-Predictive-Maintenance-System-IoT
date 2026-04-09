import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from lstm_preprocessing import create_sequences

data = pd.read_csv("data/time_series_data.csv")

features = data[['temperature','vibration','current','failure']].values

scaler = MinMaxScaler()
features = scaler.fit_transform(features)

X, y = create_sequences(features)

split = int(0.8*len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

model = Sequential()
model.add(LSTM(50, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10)

loss, acc = model.evaluate(X_test, y_test)
print("Accuracy:", acc)

model.save("models/lstm_model.keras")