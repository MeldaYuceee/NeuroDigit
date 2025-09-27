from tensorflow.keras import layers, models


def create_model(input_shape=784, hidden_units=128, output_units=10):

    model = models.Sequential()
    model.add(layers.Dense(hidden_units, activation='relu', input_shape=(input_shape,)))
    model.add(layers.Dense(output_units, activation='softmax'))

    return model
