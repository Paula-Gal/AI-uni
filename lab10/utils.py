# incarc datele si redimensionez imaginea
from PIL import Image
from sklearn import neural_network
import numpy as np
from sklearn.preprocessing import StandardScaler


def load():
    imagini = []
    dateInput = []
    read = open("file")
    with read as data:
        lines = data.read()
    lines = lines.splitlines()

    # pun imaginile din fisier in vector
    for line in lines:
        imagini.append(np.array(Image.open("r\\" + line).resize((300, 300))).flatten())

    # parcurg ca fiecare poza sa aiba o singura lista
    storeImage(imagini, dateInput)
    return dateInput


# fiecare imagine sa aiba o singura lista
def storeImage(inputs, dateInput):
    for x in inputs:
        row = []
        for elem in x:
            row.append(elem)
        dateInput.append(row)


# function that normalise the data
def normalisation(xTrain, yTrain, xValidation, yValidation):
    xTrain = np.array(xTrain) / 255
    xValidation = np.array(xValidation) / 255

    xTrain.reshape(-1, 300, 300, 1)
    xValidation.reshape(-1, 300, 300, 1)

    yTrain = np.array(yTrain)
    yValidation = np.array(yValidation)

    return xTrain, yTrain, xValidation, yValidation
