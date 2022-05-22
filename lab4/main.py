
import warnings

import re

import networkx as nx
import numpy
import numpy as np
from matplotlib import pyplot as plt

from utils.Chromosome import Chromosome
from utils.GeneticAlg import GeneticAlg

warnings.simplefilter('ignore')

# Să se identifice cel mai scurt drum care pleacă dintr-un nod, vizitează toate nodurile (fiecare nod este vizitat o singură dată)
# și revine în locația de start folosind un algoritm evolutiv.

# Cerinte optionale
# In cazul existentei mai multor solutii, precizati toate solutiile. Analizati diversitatea populatiei de potentiale solutii.
# Cum impacteaza metoda de rezolvare si solutia/solutiile identificate modificarea cerintei astfel:
# Să se identifice cel mai scurt drum care pleacă dintr-un nod și revine în locația de start folosind un algoritm evolutiv.

filename = "tsp//easy_01_tsp.txt"


def readGraph(filename):
    G = nx.Graph()
    matx = []
    no_cities = -1
    k = -1
    source = -1
    destination = -1
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if no_cities == -1:
                no_cities = int(line[0])
            else:
                a = []
                k = k + 1
                l = line.split(',')
                for j in range(0, no_cities):
                    # print(l[j])
                    a.append(l[j])
                matx.append(a)

    param = {'noNodes': no_cities,
             'mat': matx,
             'edgesNo': (no_cities * (no_cities - 1)) // 2}
    # #
    # for i in range(0, param['noNodes']):
    #     for j in range(0, param['noNodes']):
    #         print(param['mat'][i][j])

    return param, G


def run():
    param, G = readGraph(filename)
    nodes = param['noNodes']
    param['populationSize'] = nodes
    mat = param['mat']
    edges = param['edgesNo']
    pop_size = param['populationSize']
    geneticAlg = GeneticAlg(param)
    # Pasul 1. Crearea populatiei
    geneticAlg.initialisation()
    # Pasul 2. Selectia
    geneticAlg.evaluation()
    # ch1, ch2 = geneticAlg.selection()
    # for i in range(0, nodes):
    #     print('Generatia ' + str(i))
    #     geneticAlg.oneGenerationElitism()
    #print(geneticAlg.bestChromosome().fitness)
    #off1 = geneticAlg.crossover(ch1, ch2)
    # off2 = geneticAlg.crossoverv2(ch1, ch2)
    # print(ch1)
    # print(ch2)
    # print(off1)
    # print(off2)

    for i in range(0, 5):
        print("Generatia " + str(i))
        geneticAlg.oneGenerationElitism()
        print(geneticAlg.bestChromosome().rep)


run()
# readGraph(filename)
