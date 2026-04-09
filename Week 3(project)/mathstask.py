import numpy as np

# data
# Study hours (X) and result (y)
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([0, 0, 0, 1, 1, 1])

#standardization
# Pattern Recognition and Machine Learning – Christopher Bishop (Feature Scaling)
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X = (X - X_mean) / X_std

#sigmoid function
# from MOODLE 
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# model function
def model(X, w, b):
    return sigmoid(np.dot(X, w) + b)

# loss function
# Deep Learning – Ian Goodfellow, Yoshua Bengio, Aaron Courville
def loss(y, y_pred):
    return -np.mean(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))

# training (gradient descent)
#Pattern Recognition and Machine Learning – Christopher Bishop
w = np.zeros((1,1))
b = 0
lr = 0.1

for i in range(1000):
    y_pred = model(X, w, b)

    dw = np.dot(X.T, (y_pred - y.reshape(-1,1))) / len(y)
    db = np.mean(y_pred - y.reshape(-1,1))

    w -= lr * dw
    b -= lr * db

    if i % 100 == 0:
        print(f"Iteration {i}, Loss: {loss(y.reshape(-1,1), y_pred)}")

# prediction function
# Hands-On Machine Learning – Aurélien Géron
def predict(X_new):
    X_new = (X_new - X_mean) / X_std
    probs = model(X_new, w, b)
    return (probs > 0.5).astype(int)

# testing
test_data = np.array([[2], [4], [6]])
predictions = predict(test_data)

print("\nTest Results:")
for i in range(len(test_data)):
    print(f"Study Hours: {test_data[i][0]} -> Prediction: {predictions[i][0]}")