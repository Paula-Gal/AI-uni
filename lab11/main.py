import numpy as np
import os
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

from utils.kmeans import kmeansAlg
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


# functio that reads data from file
def readData(filename):
    import csv
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                data_names = row
            else:
                data.append(row)
            line_count += 1
    return data


# k-means alg for numeric data type - iris dataset
def kmeansIris():
    iris = load_iris()
    print("Iris data: ")
    print(iris)
    data = iris.data[:, :2]
    print("Data: ")
    print(data)
    # apply k means alg
    centers, labels = kmeansAlg(data, 3)
    # plot the data
    plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='plasma')
    plt.show()


# Extragere caracteristici din texte - BAG OF WORDS Tool
def bagOfWords(trainInputs, testInputs):
    vectorizer = CountVectorizer()
    trainF = vectorizer.fit_transform(trainInputs)
    testF = vectorizer.transform(testInputs)
    # get_feature_names => contains the uniques words of the vocabulary
    print("Feature names: ", vectorizer.get_feature_names()[:10])
    print("Features: ", trainF.toarray()[:3][:10])

    return trainF, testF


def tfIdf(trainInputs, testInputs):
    vectorizer = TfidfVectorizer(max_features=50)

    trainFeatures = vectorizer.fit_transform(trainInputs)
    testFeatures = vectorizer.transform(testInputs)

    # features names from the train data
    print('Fetures Names: ', vectorizer.get_feature_names()[:10])
    print('Features: ', trainFeatures.toarray()[:3])

    return trainFeatures, testFeatures


# k means tool
def bagOfWordsCl(labelNames, trainFeat, testFeat, testOutputs):
    classifier = KMeans(n_clusters=2, random_state=0)
    classifier.fit(trainFeat)
    computed = classifier.predict(testFeat)
    computedOutputs = [labelNames[value] for value in computed]

    print("Accuracy BW Method: ", accuracy_score(testOutputs, computedOutputs))


# k means tool
def tfIdClassifier(labelNames, tfTestFeatures, testOutputs, tfTrainFeatures):
    classifier = KMeans(n_clusters=2, random_state=0)
    classifier.fit(tfTrainFeatures)
    computed = classifier.predict(tfTestFeatures)
    computedOutputs = [labelNames[value] for value in computed]

    print("Accuracy TF-IDF Method: ", accuracy_score(testOutputs, computedOutputs))
    print(testOutputs)
    print(computedOutputs)


def run():
    crtDir = os.getcwd()
    fileName = os.path.join(crtDir, 'data', 'reviews_mixed.csv')
    data = readData(fileName)
    inputs = [data[i][0] for i in range(len(data))]
    outputs = [data[i][1] for i in range(len(data))]
    labelNames = list(set(outputs))

    # Impartire date pe train si test
    np.random.seed(7)

    noSamples = len(inputs)
    indexes = [i for i in range(noSamples)]
    trainSample = np.random.choice(indexes, int(0.8 * noSamples), replace=False)
    testSample = [i for i in indexes if i not in trainSample]

    trainInputs = [inputs[i] for i in trainSample]
    trainOutputs = [outputs[i] for i in trainSample]
    testInputs = [inputs[i] for i in testSample]
    testOutputs = [outputs[i] for i in testSample]

    kmeansIris()

    # extragere caracteristici din text
    print("BAG OF WORDS Tool")
    # Bag of words
    trainFeat, testFeat = bagOfWords(trainInputs, testInputs)
    print("BAG OF WORDS train: ")
    print(trainFeat)
    print("BAG OF WORDS test: ")
    print(testFeat)

    # bag of words classifier
    bagOfWordsCl(labelNames, trainFeat, testFeat, testOutputs)

    # TF-IDF method
    print()
    print("TF-IDF:")
    tfTrainFeatures, tfTestFeatures = tfIdf(trainInputs, testInputs)
    print("TF-IDF: ")
    print(tfTrainFeatures)
    print("TF-IDF: ")
    print(tfTestFeatures)

    tfIdClassifier(labelNames, tfTestFeatures, testOutputs, tfTrainFeatures)


run()
