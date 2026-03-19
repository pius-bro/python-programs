import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Input (X) and Output (y)
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

model = keras.Sequential([
    layers.Dense(units=1, input_shape=[1])
])
model.compile(
    optimizer='sgd',       # Stochastic Gradient Descent
    loss='mean_squared_error'
)
model.fit(X, y, epochs=500)
print(model.predict([10.0]))
