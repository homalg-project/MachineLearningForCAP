import numpy as np
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam, SGD
from sklearn.model_selection import train_test_split

with open("data/training_examples.txt", "r") as f:
    f = f.read()

data = np.array(eval(f))

# create the data
X = data[:, :2]
y = data[:, 2:]

# Convert the labels to class indices
y = np.argmax(y, axis=1)

# Convert the labels to categorical format
y = to_categorical(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential()

# Add an Input layer
model.add(Input(shape=(2,)))

# Add hidden layers
model.add(Dense(5, activation='relu'))
model.add(Dense(5, activation='relu'))

# Add output layer
model.add(Dense(4, activation='softmax'))

# Build the model with the input shape to initialize the weights
model.build()

# Summary of the model
model.summary()

# Specify the optimizer
#optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07)
optimizer = SGD(learning_rate=0.01)

model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# View the initial weights
initial_weights = model.get_weights()
for i, weight in enumerate(initial_weights):
    print(f'Initial weights for layer {i+1}: {weight}')

# View the parameters of the Adam optimizer
print(f'Learning rate: {optimizer.learning_rate.numpy()}')
#print(f'Beta_1: {optimizer.beta_1}')
#print(f'Beta_2: {optimizer.beta_2}')
#print(f'Epsilon: {optimizer.epsilon}')

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=1)

# Evaluate the model. Accuracy should less or more than 83%
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Accuracy: {accuracy}')
