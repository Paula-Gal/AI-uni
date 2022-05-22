import numpy as np


# Unsupervised Machine Learning Algorithm Used for Solving Classification Problems
# k means Algorithm
# X[x,y]
def kmeansAlg(dataInput, noClusters, randomSeed=2):
    # Step 1. Impartirea random in noClusters
    # selectare random 3 puncte distincte
    clusters = np.random.RandomState(randomSeed)
    # number of training data
    tr = dataInput.shape[0]
    # generate 3 random points for centers
    i = clusters.permutation(tr)[:noClusters]
    # centers = [[4.6 3.4] [4.6 3.1] [5.7 2.5]]
    centers = dataInput[i]
    while True:
        # aici pun distanta minima
        labels = []
        # for each sample from dataset
        for data in dataInput:
            distance = []
            for i in range(len(centers)):
                # calculare distanta fata de fiecare centroid
                dis = computeDistance(data, centers[i])
                distance.append(dis)
            labels.append(np.argmin(distance))
        labels = np.asarray(labels)

        # recalc centroizilor - media pt fiecare cluster
        newCenters = np.array([dataInput[labels == i].mean(axis=0) for i in range(noClusters)])
        if np.all(centers == newCenters):
            break
        # update the old centroid
        centers = newCenters

    return centers, labels


# compute the euclidian distance
def computeDistance(x1, x2):
    dist = (sum((x1 - x2) ** 2)) ** 0.5
    return dist
