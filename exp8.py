# Experiment 8
# Activation Functions

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x):
    return np.where(x > 0, x, 0.01 * x)

x_values = np.linspace(-10, 10, 100)

plt.figure(figsize=(10, 6))

plt.plot(x_values, sigmoid(x_values), label="Sigmoid")
plt.plot(x_values, tanh(x_values), label="Tanh")
plt.plot(x_values, relu(x_values), label="ReLU")
plt.plot(x_values, leaky_relu(x_values), label="Leaky ReLU")

plt.title("Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.grid(True)

plt.show()

print("Activation functions plotted successfully.")

