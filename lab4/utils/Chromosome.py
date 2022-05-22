import random
from random import randint


# functia care genereaza un cromozom <=> o cale random de la sursa la destinatie
# parametrii de intrare: -
# parametrii de iesire: o lista de gene reprezentand un cromozom
#
def generateChromosome(no_cities):
    # generez genele = orasele din cromozom
    chromosome = random.sample(range(no_cities), no_cities)

    #chromosome.append(chromosome[0])

    return chromosome


class Chromosome:
    def __init__(self, problParam=None):
        self.problParam = problParam
        self.__rep = generateChromosome(problParam['noNodes'])
        self.__fitness = 0.0

    # representation getter
    @property
    def rep(self):
        return self.__rep

    # fitness function getter
    @property
    def fitness(self):
        return self.__fitness

    # representation setter
    @rep.setter
    def rep(self, r=None):
        if r is None:
            r = []
        self.__rep = r

    # fitness setter
    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def __str__(self):
        return '\nChromosome: ' + str(self.__rep) + ' has fitness: ' + str(self.__fitness)

    # def __eq__(self, c):
    #     return self.__rep == c.__repres and self.__fitness == c.__fitness

    def __repr__(self):
        return self.__str__()
