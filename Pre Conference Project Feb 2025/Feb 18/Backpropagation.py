# Import required libraries
import numpy as np

# Define Activation Function (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Standard Sigmoid Activation

# Define Derivative of Sigmoid (Used in Backpropagation)
def sigmoid_derivative(x):
    return x * (1 - x)  # Derivative of Sigmoid

# Define XOR Input and Expected Output
inputs = np.array([
    [0, 0],  # Expected output: 0
    [0, 1],  # Expected output: 1
    [1, 0],  # Expected output: 1
    [1, 1]   # Expected output: 0
])

expected_output = np.array([[0], [1], [1], [0]])  # XOR Truth Table Output

# Define Neural Network Architecture
input_layer_neurons = inputs.shape[1]  # 2 neurons (input features)
hidden_layer_neurons = 2  # Experimentally chosen
output_layer_neurons = 1  # Binary output

# Initialize Weights and Biases Randomly
np.random.seed(42)  # Ensures reproducibility

hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))

output_weights = np.random.uniform(size=(hidden_layer_neurons, output_layer_neurons))
output_bias = np.random.uniform(size=(1, output_layer_neurons))

# Define Training Parameters
learning_rate = 0.1  # Controls how much weights are updated
epochs = 10000  # Number of training iterations

# Train the Neural Network using Forward and Backpropagation
for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_activation = np.dot(inputs, hidden_weights) + hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    output_layer_activation = np.dot(hidden_layer_output, output_weights) + output_bias
    predicted_output = sigmoid(output_layer_activation)

    # Compute Error
    error = expected_output - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Update Weights & Biases using Gradient Descent
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate

    hidden_weights += inputs.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Print Loss every 1000 epochs
    if epoch % 1000 == 0:
        loss = np.mean(np.square(expected_output - predicted_output))
        print(f'Epoch {epoch}, Loss: {loss}')

# Display Final Predictions
print("\nFinal Predictions after Training:")
print(predicted_output)
