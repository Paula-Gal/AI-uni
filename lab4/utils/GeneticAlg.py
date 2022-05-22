import operator
import random

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


# functia care calculeaza fitnessul unui cromozom (path)
# valoarea fitnessului e lungimea drumului reprezentat de cromozom
# the shorter the total distance the fitter and more superior the chromosome
def computeFitness(chromosome, mat, noNodes):
    sum = 0
    for i in range(0, noNodes - 1):
        x1 = chromosome.rep[i]
        x2 = chromosome.rep[i + 1]
        y1 = int(mat[x1][x2])
        sum = sum + y1

    sum = sum + int(mat[chromosome.rep[0]][chromosome.rep[noNodes - 1]])
    return sum


# returneaza lista cu fitness-urile cromozomilor din populatie
def getFitnessList(population):
    list = []
    for chromosome in population:
        list.append(chromosome.fitness)

    return list


class GeneticAlg:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.problParam = problParam
        self.__population = []

    # population getter
    @property
    def population(self):
        return self.__population

    # Etapa 1 - Initializarea <=> crearea populatiei
    # The algorithm starts from the source
    # Source and destination are constants that user may change as they wish
    def initialisation(self):
        # generez o populatie de cromozomi
        # generez o populatie de n drumuri in graf care trec prin toate orasele o singura data
        for i in range(0, self.__param['populationSize']):
            chromosome = Chromosome(self.__param)
            self.__population.append(chromosome)

    # Etapa 2 - Evaluation
    # calculare fitness pentru fiecare cromozom din populatie
    # evaluate solutions fitness
    def evaluation(self):
        mat = self.__param['mat']
        noNodes = self.__param['noNodes']
        for chromosome in self.__population:
            chromosome.fitness = computeFitness(chromosome, mat, noNodes)

    # Etapa 3 - Selectia celor mai buni cromozomi
    # the algorithm selects 2 individuals from the population with the lowest costs
    def selection(self):
        # sortez fitness-urile
        fitnessList = getFitnessList(self.__population)
        fitnessList = sorted(fitnessList)
        p1 = fitnessList[0]
        p2 = fitnessList[1]
        chr1 = -1
        chr2 = -1
        for chromosome in self.__population:
            if chr1 == -1 or chr2 == -1:
                if chromosome.fitness == p1 and chr1 == -1:
                    chr1 = chromosome
                if chromosome.fitness == p2 and chr2 == -1 and chromosome != chr1:
                    chr2 = chromosome
        return chr1, chr2

    # functia de crossover
    # takes 2 parents to mate
    def crossover(self, chr1, chr2):
        # determinare puncte comune
        common = []
        for i in range(0, len(chr1.rep)):
            if chr1.rep[i] == chr2.rep[i]:
                common.append(chr1.rep[i])
        # se selecteaza un punct random din punctele comune
        # the common nodes are where these 2 paths intersect
        if len(common) > 0:
            crossover_point = random.choice(common)
        else:
            crossover_point = 0
        new_rep = []
        index = 0
        # crossover point index
        for i in range(0, len(chr1.rep)):
            if chr1.rep[i] == crossover_point:
                index = i
                break
        # daca nu au puncte comune inverseaza cromozomii
        # eventual in cazul asta sa alegi un punct random
        for i in range(0, index):
            new_rep.append(chr1.rep[i])
        # off1.append(chr1.rep[i])
        # off2.append(chr2.rep[i])
        for i in range(index, len(chr2.rep)):
            new_rep.append(chr2.rep[i])

        # for j in range(crossover_point, len(chr2.rep)):
        #     new_rep.append(chr2.rep[j])
        offspring = Chromosome(chr1.problParam)
        offspring.rep = new_rep
        # off1.append(chr2.rep[j])
        # off2.append(chr1.rep[j])

        return offspring

    # functia de crossover
    # takes 2 parents to mate
    def crossoverv2(self, chr1, chr2):
        # se alege random un crossover point dintre gene
        crossover_point = random.randint(0, len(chr1.rep) - 1)
        new_representation = []
        # incrucisez
        offspring = []
        for i in range(0, crossover_point):
            offspring.append(chr1.rep[i])
        for j in range(crossover_point, len(chr2.rep)):
            offspring.append(chr2.rep[j])
        return offspring

    # functia care realizeaza mutatia/modificarea in noul offspring format
    # modificarea unor gene provenite de la parinti
    def mutation(self, offspring):
        # generez random o gena de modificat
        x1 = random.randint(0, self.__param['noNodes'] - 1)
        x2 = random.randint(0, self.__param['noNodes'] - 1)
        # schimb random 2 elemntel de pe 2 pozitii
        offspring.rep[x1], offspring.rep[x2] = offspring.rep[x2], offspring.rep[x1]

    # returneaza cel mai bun cromozom -> cel cu fitness-ul mai mare
    def bestChromosome(self):
        best = self.__population[0]
        for chromo in self.__population:
            if chromo.fitness < best.fitness:
                best = chromo

        return best

    # returneaza cel mai slab cromozom
    def worstChromosome(self):
        worst = self.__population[0]
        for chromo in self.__population:
            if chromo.fitness > worst.fitness:
                worst = chromo

        return worst

    def oneGenerationElitism(self):
        # alege cromozomul cel mai bun
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['populationSize'] - 1):
            # selecteaza 2 parinti cu fitness ul mare
            ch1, ch2 = self.selection()
            # se incruciseaza parintele p1 cu p2
            off = self.crossover(ch1, ch2)
            self.mutation(off)
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
