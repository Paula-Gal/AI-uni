
import warnings

import re

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

from utils.GeneticAlg import GeneticAlg

warnings.simplefilter('ignore')


def readGraph(file):
    G = nx.Graph()
    G = nx.read_gml(file, label='id')
    pos = nx.spring_layout(G)
    # image 8x8 inches
    plt.figure(figsize=(8, 8))
    nx.draw_networkx(G, pos, node_size=60, cmap=plt.cm.RdYlBu, node_color='green')
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show()
    mat = nx.adjacency_matrix(G).todense()
    invalid = re.compile('[^0-9]')
    matx = []
    for i in range(0, len(mat)):
        a = str(mat[i])
        cleaned = [int(i) for i in a if not invalid.search(i)]
        matx.append(cleaned)
    degrees = []
    edgesNo = 0
    for i in range(len(matx)):
        d = 0
        for j in range(len(matx)):
            if matx[i][j] == 1:
                d += 1
            if j > i:
                edgesNo = edgesNo + matx[i][j]
            degrees.append(d)
    param = {'noNodes': len(matx),
             'mat': matx,
             'edgesNo': edgesNo,
             'degrees': degrees}
    return param, G


def run(file):
    param, G = readGraph(file)
    # nr de generatii -> cat de mare sa fie populatia
    param['populationSize'] = 300
    # Etapa 1. Initializare (generez populatia)
    geneticAlg = GeneticAlg(param)
    geneticAlg.initialisation()
    # calculare fitness pentru fiecare cromozom din populatie
    geneticAlg.evaluation()
    for i in range(0, 301):
        print('Generatia ' + str(i))
        geneticAlg.oneGenerationElitism()
        A = np.matrix(param["mat"])
        G = nx.from_numpy_matrix(A)
        # graph layout
        pos = nx.spring_layout(G)  # compute graph layout
        plt.figure(figsize=(8, 8))  # image is 8 x 8 inches
        nx.draw_networkx_nodes(G, pos, node_size=60, cmap=plt.cm.RdYlBu, node_color=geneticAlg.bestChromosome().rep)
        nx.draw_networkx_edges(G, pos, alpha=0.3)
        print(geneticAlg.bestChromosome().rep)
    print(geneticAlg.bestChromosome().fitness)


fileKarate = "real//karate//karate.gml"
fileFootball = "real//football//football.gml"
fileKrebs = "real//krebs//krebs.gml"
fileDolphins = "real//dolphins//dolphins.gml"

fileLesmis = "other//lesmis//lesmis.gml"
filePrimarySchool = "other//primaryschool//primaryschool.gml"

simple = "other//simple//simple.gml"

run(fileKarate)
