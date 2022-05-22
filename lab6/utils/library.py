import numpy as np

# functia care ia datele din fisierul tsp si le pune intr-un dictionar
from numpy import dtype


def readData(file):
    input_file = open(file, 'r')
    # NAME
    name = input_file.readline().strip().split()[1]
    # TYPE
    type = input_file.readline().strip().split()[1]
    # COMMENT
    comm = input_file.readline().strip().split()[1]
    # DIMENSION
    dimension = input_file.readline().strip().split()[1]
    # EDGE WEIGHT TYPE
    edge_weight_type = input_file.readline().strip().split()[1]
    node_coord_section = []
    input_file.readline()

    # citirea coordonatelor nodurilor si stocarea lor in x,y
    for i in range(0, len(dimension)):
        x, y = input_file.readline().strip().split()[1:]
        node_coord_section.append([float(x), float(y)])

    # close input file
    input_file.close()

    # store in dictionary info from the tsp file
    return {
        'name': name,
        'type': type,
        'comm': comm,
        'dim': dimension,
        'edgeWeightType': edge_weight_type,
        'node_coord_section': node_coord_section
    }


def displayData(dictionary):
    print('\nName: ', dictionary['name'])
    print('Type: ', dictionary['type'])
    print('Comm: ', dictionary['comm'])
    print('Dimension: ', dictionary['dim'])
    print('Edge Weight Type: ', dictionary['edge_weight_type'], '\n')


# returneaza un vector al distantei inverse
# vizibilitatea din orasul x spre orasul y <=> atractivitatea alegerii muchiei (x,y)
# parametrii de intrare: int - spatiu
# parametrii de iesire:
def inverseDistances(space):
    #
    distances = np.zeros((space.shape[0], space.shape[0]))

    # calcularea distantei pentru toate nodurile la toate nodurile
    for index, point in enumerate(space):
        distances[index] = np.sqrt(((space - point) ** 2).sum(axis=1))

    with np.errstate(all='ignore'):
        # inversarea distantei
        inv_dist = 1 / distances

    inv_dist[inv_dist == np.inf] = 0

    # se returneaza eta, distanta inversa
    return inv_dist


# functia de initializare a coloniei de furnici
# parametrii de intrare - int - space
#                       - int - colony - nr de furnici din colonie
# parametrii de iesire: un vector de indici initiali care indica pozitiile initiale ale furnicilor
# in spatiul dat
def initializeAnts(space, colony):
    # se genereaza random pozitiile initale ale furnicilor in spatiu
    return np.random.randint(space.shape[0], size=colony)


# functia care deplaseaza furnicile din pozitia initiala
# astfel incat sa treaca prin toate nodurile
# parametrii de intrare: int - space
#                        positions -
def moveAnts(space, positions, inv_dist, pheromones, alpha, beta, del_tau):
    paths = np.zeros((space.shape[0], positions.shape[0]), dtype == int) - 1

    # pozitia initiala la nodul 0
    paths[0] = positions

    # pentru fiecare nod
    for node in range(1, space.shape[0]):
        # pentru fiecare furnica
        for ant in range(positions.shape[0]):
            # probabilitatea urmatoarei trecerii in urmatorul oras
            prob_next_city = (inv_dist[positions[ant]] ** alpha + pheromones[positions[ant]] ** beta /
                              inv_dist[positions[ant]].sum() ** alpha + pheromones[positions[ant]].sum() ** beta)

            # gasirea nodului cu probabilitatea maxima
            next_pos = np.argwhere(prob_next_city == np.amax(prob_next_city))[0][0]

            # verficare daca nodul a fost vizitat
            while next_pos in paths[:, ant]:
                # inlocuirea probabiliatii vizitatilor cu 0
                prob_next_city[next_pos] = 0.0

                # cautare nod cu probabilitatea cea mai mare
                next_pos = np.argwhere(prob_next_city == np.amax(prob_next_city))[0][0]

            # adaugare nod in drum
            paths[node, ant] = next_pos

            # actualizare feromoni
            pheromones[node, next_pos] = pheromones[node, next_pos] + del_tau

    # drumurile parcurse de furnici
    # swapaxes => interchange 2 axis of an array
    return np.swapaxes(paths, 0, 1)


def runACO(space, iterations=80, colony=50, alpha=1.0, beta=1.0, del_tau=1.0, ro=0.5):
    # distanta inversa pentru toate nodurile
    inv_dist = inverseDistances(space)

    # ridicam la puterea beta inversul distantei
    # beta - cat de aproape e urmatorul oras <=> importanta vizibilitatii
    inv_dist = inv_dist ** beta

    # initializam cantiatea de feromon a drumului
    pheromones = np.zeros((space.shape[0], space.shape[0]))

    # initializate distanta minima si drum
    min_dist = None
    min_path = None

    # parcurgem numarul de iteratii
    for i in range(iterations):
        # initializare cu pozitii random furnicile in spatiul dat
        positions = initializeAnts(space, colony)

        # parcurgem un drum
        paths = moveAnts(space, positions, inv_dist, pheromones, alpha, beta, del_tau)

        # evaporare feromoni
        pheromones *= (1 - ro)

        # pentru fiecare drum
        for path in paths:
            # intializare distanta
            dist = 0

            # pentru fiecare nod de la al doilea pana la ultimul
            for node in range(1, path.shape[0]):
                # calculez distanta pana la ultimul nod
                dist += np.sqrt(((space[int(path[node])] - space[int(path[node - 1])]) ** 2).sum())

            # actualizam distanta minima si drumul daca gasim una mai mica sau neexistenta
            if not min_dist or dist < min_dist:
                min_dist = dist
                min_path = path

        # copiem si adaugam primul nod la sfarsitul drumului minim
        min_path = np.append(min_path, min_path[0])

        # returnez un tuplu
        return (min_path, min_dist)
