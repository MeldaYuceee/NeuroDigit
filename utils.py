import numpy as np
import matplotlib.pyplot as plt

def preprocess_data(x, y):

    x = x / 255.0
    x = x.reshape(-1, 28*28)
    return x, y

def plot_predictions(x_test, predictions, n=10):

    plt.figure(figsize=(10,4))
    for i in range(n):
        plt.subplot(2, 5, i+1)
        plt.imshow(x_test[i].reshape(28,28), cmap='gray')
        plt.title(f"Pred: {np.argmax(predictions[i])}")
        plt.axis('off')
    plt.show()
