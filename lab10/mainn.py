import os
import cv2
import numpy as np
from keras import Sequential
from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
from keras.losses import SparseCategoricalCrossentropy
from keras_preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt


def getImages(dataDir, labels):
    data = []
    for label in labels:
        path = os.path.join(dataDir, label)
        classNum = labels.index(label)
        for img in os.listdir(path):
            try:
                convImg = cv2.imread(os.path.join(path, img))[..., ::-1]
                resized = cv2.resize(convImg, (300, 300))
                data.append([resized, classNum])
            except Exception as ex:
                print(ex)
    return np.array(data)


def data_normalisation(x_train, y_train, x_validation, y_validation):
    x_train = np.array(x_train) / 255
    x_validation = np.array(x_validation) / 255

    x_train.reshape(-1, 300, 300, 1)
    x_validation.reshape(-1, 300, 300, 1)

    y_train = np.array(y_train)
    y_validation = np.array(y_validation)

    return x_train, y_train, x_validation, y_validation

def run_sepia_CNN():
    labels = ['filter', 'nonFilter']

    trainInputs = getImages('img\\training', labels)
    validationInputs = getImages('img\\test', labels)

    outputs = []
    for element in trainInputs:
        outputs.append(element[1])

    # print(outputs)

    plt.hist(outputs, rwidth=0.8)
    plt.xticks(np.arange(len(labels)), labels)
    plt.show()

    x_train = []
    y_train = []
    x_validation = []
    y_validation = []

    for feature, label in trainInputs:
        x_train.append(feature)
        y_train.append(label)

    for feature, label in validationInputs:
        x_validation.append(feature)
        y_validation.append(label)

    # apply data normalisation

    x_train, y_train, x_validation, y_validation = data_normalisation(x_train, y_train, x_validation, y_validation)

    datagen = ImageDataGenerator(
        featurewise_center=False,  # input mean to 0 over de dataset
        samplewise_center=False,
        featurewise_std_normalization=False,
        samplewise_std_normalization=False,  # divide each input by its std
        zca_whitening=False,
        rotation_range=30,  # randomly rotate images in the range
        zoom_range=0.2,  # randomly zoom images
        width_shift_range=0.1,  # randomly shift horizontally
        height_shift_range=0.1,  # randomly shift vertically
        horizontal_flip=True,  # randomly flip
        vertical_flip=False  # randomly flip
    )

    datagen.fit(x_train)

    # define a CNN model with 3 convolutional layers followed by max - pooling
    # layers. Dropout layer added after the 3rd max - pool operation
    # (to avoid over-fitting)
    model = Sequential()
    model.add(Conv2D(32, 3, padding="same", activation="relu", input_shape=(300, 300, 3)))
    model.add(MaxPool2D())

    model.add(Conv2D(32, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())

    model.add(Conv2D(64, 3, padding="same", activation="relu"))
    model.add(MaxPool2D())
    model.add(Dropout(0.4))

    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dense(2, activation="softmax"))

    model.summary()
    from keras.optimizers import adam_v2
    optimizer = adam_v2.Adam(learning_rate=0.00001)

    model.compile(optimizer=optimizer, loss=SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    training = model.fit(x_train, y_train, epochs=100, validation_data=(x_validation, y_validation))

    accuracy = training.history['accuracy'][len(training.history['accuracy']) - 1]
    print("accuracy:", accuracy)

run_sepia_CNN()