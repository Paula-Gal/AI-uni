from random import randint

from utils.Chromosome import Chromosome


# evaluarea impartirii pe comunitati
# evaluate the quality of previous communities inside a network

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['edgesNo']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if communities[i] == communities[j]:
                Q += mat[i][j] - degrees[i] * degrees[j] / M
    return Q * 1 / M


class GeneticAlg:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    # population getter
    @property
    def population(self):
        return self.__population

    # etapa 1 de intializare -> se creeaza o populatie initiala generata random
    # cu un numar de param['populationSize'] cromozomi
    def initialisation(self):
        for _ in range(0, self.__param['populationSize']):
            chromo = Chromosome(self.__param)
            self.__population.append(chromo)

    # calculare fitness pentru fiecare cromozom din populatie
    def evaluation(self):
        for chromo in self.__population:
            chromo.fitness = modularity(chromo.rep, self.__param)

    # returneaza cel mai bun cromozom -> cel cu fitness-ul mai mare
    def bestChromosome(self):
        best = self.__population[0]
        for chromo in self.__population:
            if chromo.fitness > best.fitness:
                best = chromo

        return best

    # returneaza cel mai slab cromozom
    def worstChromosome(self):
        worst = self.__population[0]
        for chromo in self.__population:
            if chromo.fitness < worst.fitness:
                worst = chromo

        return worst

    # functia de selectie
    # selectarea cromozomilor parinti:
    # 1. se genereaza 2 pozitii aleatoare
    # 2. se alege sa mearga mai departe cromozomul cu fineesul mai mare
    # returneaza cromozomul cu fitnessul mai mare
    def selection(self):
        pos1 = randint(0, self.__param['populationSize'] - 1)
        pos2 = randint(0, self.__param['populationSize'] - 1)
        if self.__population[pos1].fitness > self.__population[pos2].fitness:
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['populationSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        # alege cromozomul cel mai bun
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['populationSize'] - 1):
            # selecteaza 2 parinti cu fitness ul mare
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            # se incruciseaza parintele p1 cu p2
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationSteadyState(self):
        for _ in range(self.__param['populationSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = modularity(off.rep, self.__param)
            worst = self.worstChromosome()
            if off.fitness < worst.fitness:
                worst = off
