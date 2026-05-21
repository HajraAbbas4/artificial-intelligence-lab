# Experiment 9
# Backpropagation Strategy in Artificial Neural Network

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

outputs = np.array([
    [0],
    [1],
    [1],
    [0]
])

np.random.seed(1)

weights_input_hidden = np.random.uniform(size=(2, 2))
weights_hidden_output = np.random.uniform(size=(2, 1))

learning_rate = 0.5

for epoch in range(10000):
    hidden_input = np.dot(inputs, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    predicted_output = sigmoid(final_input)

    error = outputs - predicted_output
    output_delta = error * sigmoid_derivative(predicted_output)

    hidden_error = output_delta.dot(weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    weights_hidden_output += hidden_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate

print("Predicted Output after Training:")
print(predicted_output)


