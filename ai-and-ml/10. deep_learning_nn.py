import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

dataset = pd.read_excel("dataset_features.xlsx")

features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels,
    test_size=0.2,
    random_state=42
)

model = Sequential([
    Dense(
        128,
        input_dim=X_train.shape[1],
        activation='relu'
    ),

    Dense(
        64,
        activation='relu'
    ),

    Dense(
        1,
        activation='sigmoid'
    )
])

model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_data=(X_test, y_test)
)

loss, accuracy = model.evaluate(X_test, y_test)

print(f"Test Accuracy: {accuracy * 100:.2f}%")

weights = model.get_weights()

print("Weights of the model after training:")

for i, weight_matrix in enumerate(weights):
    print(
        f"Layer {i+1} weights shape: {weight_matrix.shape}"
    )

first_layer_weights = weights[0]

print(f"First layer weights:\n{first_layer_weights}")

plt.plot(
    history.history['accuracy'],
    label='Training Accuracy'
)

plt.plot(
    history.history['val_accuracy'],
    label='Validation Accuracy'
)

plt.xlabel('Epochs')
plt.ylabel('Accuracy')

plt.legend()

plt.title('Training and Validation Accuracy')

plt.show()
