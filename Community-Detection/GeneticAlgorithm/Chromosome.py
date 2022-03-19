from random import randint


# functia care genereaza cromozom
# parametrii de intrare: nr_gene - int - nr de gene de generat
#                        limit1 - int - limita inferioara de unde iau valori genele
#                        limit2 - int - limita superioada de unde iau valori genele
# parametrii de iesire: o lista de gene reprezentand un cromozom
def genChromosome(nr_gene, limit1, limit2):
    chromo = []
    for i in range(0, nr_gene):
        # generez nr_gene gene
        chromo.append(randint(limit1, limit2))
    return chromo


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        # generez 1 cromozom cu nr de gene egal cu nr de noduri ale grafului
        # din intervalul (1,nr_noduri/2)
        self.__rep = genChromosome(problParam["noNodes"], 1, int(problParam["noNodes"] // 2))
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

    # functia de crossover (One-way crossover)
    # recombina parti dintr-un parinte cu parti din celalalt parinte
    # parametrii de intrare:c - un cromozom
    # parametrii de iesire: offspring - rezultatul incrucisarii
    def crossover(self, c):
        # se alege random un crossover point dintre gene
        crossover_point = randint(0, len(self.__rep) - 1)
        new_representation = []
        # incrucisez genele pana la crossover point
        for i in range(crossover_point):
            new_representation.append(self.__rep[i])
        for i in range(crossover_point, len(self.__rep)):
            new_representation.append(c.__rep[i])
        offspring = Chromosome(c.__problParam)
        offspring.rep = new_representation

        return offspring

    # functia care realizeaza mutatia/modificarea in noul offspring format
    # modificarea unor gene provenite de la parinti
    def mutation(self):
        # generez random o gena de modificat
        p = randint(0, len(self.__rep) - 1)
        for i in range(0, len(self.__problParam["mat"][p])):
            # pe poz unde am 1 in matricea de adiacenta schimb gena din cromozom
            # cu cea de pe pozitia 4
            if self.__problParam["mat"][p][i] == 1:
                self.__rep[i] = self.__rep[p]

    def __str__(self):
        return '\nChromosome: ' + str(self.__rep) + ' has fitness: ' + str(self.__fitness)

    def __eq__(self, c):
        return self.__rep == c.__repres and self.__fitness == c.__fitness

    def __repr__(self):
        return self.__str__()
