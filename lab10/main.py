from sklearn import neural_network
import numpy as np
from sklearn.preprocessing import StandardScaler
from utils import load


def training(classifier, trainInputs, trainOutputs):
    # step4: training the classifier
    # identify (by training) the classification model
    classifier.fit(trainInputs, trainOutputs)


def classification(classifier, testInputs):
    # step5: testing (predict the labels for new inputs)
    # makes predictions for test data 
    computedTestOutputs = classifier.predict(testInputs)

    return computedTestOutputs


# calculam accuratea, precizia si recallul
def evalMultiClass(realLabels, computedLabels, labelNames):
    from sklearn.metrics import confusion_matrix

    confMatrix = confusion_matrix(realLabels, computedLabels)
    acc = sum([confMatrix[i][i] for i in range(len(labelNames))]) / len(realLabels)
    precision = {}
    recall = {}
    for i in range(len(labelNames)):
        precision[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[j][i] for j in range(len(labelNames))])
        recall[labelNames[i]] = confMatrix[i][i] / sum([confMatrix[i][j] for j in range(len(labelNames))])
    # return acc, precision, recall, confMatrix
    return acc, precision, recall


def normalisation(trainData, testData):
    scaler = StandardScaler()
    if not isinstance(trainData[0], list):
        # encode each sample into a list
        trainData = [[d] for d in trainData]
        testData = [[d] for d in testData]

        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data

        # decode from list to raw values
        normalisedTrainData = [el[0] for el in normalisedTrainData]
        normalisedTestData = [el[0] for el in normalisedTestData]
    else:
        scaler.fit(trainData)  # fit only on training data
        normalisedTrainData = scaler.transform(trainData)  # apply same transformation to train data
        normalisedTestData = scaler.transform(testData)  # apply same transformation to test data
    return normalisedTrainData, normalisedTestData


# aici le apelez pe toate

outputName = ["filter", "nonFilt"]

outputs = []
outputs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

inputs = load()

# split the data
indexes = [i for i in range(len(inputs))]
trainSample = np.random.choice(indexes, int(0.8 * len(inputs)), replace=False)
testSample = [i for i in indexes if not i in trainSample]

trainInputs = [inputs[i] for i in trainSample]
trainOutputs = [outputs[i] for i in trainSample]
testInputs = [inputs[i] for i in testSample]
testOutputs = [outputs[i] for i in testSample]

# normalise the data
trainInputsNormalised, testInputsNormalised = normalisation(trainInputs, testInputs)

# invatare model
# non-liniar classifier and softmax approach for multi-class 
classifier = neural_network.MLPClassifier(hidden_layer_sizes=(5,), activation='relu', max_iter=100, solver='sgd',
                                          verbose=10, random_state=1, learning_rate_init=0.001)

# step4: training the classifier
# identify (by training) the classification model
training(classifier, trainInputsNormalised, trainOutputs)

# step5: testing (predict the labels for new inputs)
# makes predictions for test data 
predictedLabels = classification(classifier, testInputsNormalised)

# aici se calculeaza accuratea, precisia si recallul
# acc, prec, recall, cm = evalMultiClass(np.array(testOutputs), predictedLabels, outputName)
acc, prec, recall = evalMultiClass(np.array(testOutputs), predictedLabels, outputName)

# accuracy represents the overall performance of classification model:
# precision indicates how accurate the positive predictions are
# recall indicates the coverage of actual positive sample


print("Predicted labels: ", predictedLabels)
print("Test labels: ", testOutputs)

print('acc: ', acc)
print('precision: ', prec)
print('recall: ', recall)
