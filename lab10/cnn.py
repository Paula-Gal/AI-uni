import os

from keras.optimizers import adam_v2
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Dropout
import tensorflow as tf
import cv2
import numpy as np

# Clasificare (antrenare si testare) imagini cu si fara filtru cu o CNN (cod propriu sau tool) – 250 puncte
from utils import normalisation

outputName = ['filter', 'nonFilter']


# upload images from file
# return a list of pixels
def getImages(director):
    imagini = []
    for label in outputName:
        path = os.path.join(director, label)
        classNum = outputName.index(label)
        for img in os.listdir(path):
            try:
                # load the image from the file
                imageR = cv2.imread(os.path.join(path, img))[..., ::-1]
                print("Read image: ", imageR)
                # resize the image 300 x 300
                resized = cv2.resize(imageR, (300, 300))
                imagini.append([resized, classNum])
            except Exception as ex:
                print(ex)
    return np.array(imagini)


# read images from folder
trainInputs = getImages('img\\training')
validationInputs = getImages('img\\test')


# Convolutional Neural Network
def CNN():
    outputs = []
    for element in trainInputs:
        outputs.append(element[1])

    plt.hist(outputs, rwidth=0.8)
    plt.xticks(np.arange(len(outputName)), outputName)
    plt.show()

    train1 = []
    train2 = []
    valid1 = []
    valid2 = []

    for feature, label in trainInputs:
        train1.append(feature)
        train2.append(label)

    for feature, label in validationInputs:
        valid1.append(feature)
        valid2.append(label)

    train1, train2, valid1, valid2 = normalisation(train1, train2, valid1, valid2)

    # define a CNN model with 3 convolutional layers followed by max - pooling layers.
    # a sequential model is appropiate for a plain stack of layers where each layer has exactly one input tensor and one output tensor

    model = Sequential()  # from keras

    # The first hidden layer is a convolutional layer Convolution2D
    # add convolutional layers (hidden layers)
    # first parameter: filters (apply filters to extract features)
    # padding:"same" results in padding with zeros evenly to the left/right or up/down of the input.
    model.add(Conv2D(32, 3, padding="same", activation="relu", input_shape=(300, 300, 3)))
    # Max pooling layer => is responsible for reducing the spatial size of the Convolved Feature
    model.add(MaxPool2D())
    # + 1 conv layer
    model.add(Conv2D(32, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())
    # + 1 conv layer
    model.add(Conv2D(64, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())

    # # + 1 conv layer
    # model.add(Conv2D(64, 3, padding="same", activation="relu"))
    # model.add(MaxPool2D())
    # regularization layer
    model.add(Dropout(0.4))

    # fully connected layer
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dense(2, activation="softmax"))

    model.summary()
    print("Model: ")
    print(model)

    # An optimizer alternative to SGD.
    opt = adam_v2.Adam(learning_rate=0.00001)
    # Use the training data to train the model
    # model.compile(optimizer='sgd', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])
    model.compile(optimizer=opt, loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

    # fit the model
    training = model.fit(train1, train2, epochs=10, validation_data=(valid1, valid2))

    # test the model
    error = model.evaluate(valid1, valid2, verbose=0)
    print('The mean square root (MSE) for the test data is: {}'.format(error))

    # compute and print the accuracy
    acc = training.history['accuracy'][len(training.history['accuracy']) - 1]
    print("CNN Accuracy:", acc)


CNN()
