# Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător pe linii, să se identifice indexul liniei care conține cele mai multe elemente de 1.
# De ex. în matricea
# [[0,0,0,1,1],
# [0,1,1,1,1],
# [0,0,1,1,1]]
# a doua linie conține cele mai multe elemente 1.

# functia care determina indexul liniei care are cele mai multe elemente de 1 in matrice
# parametrii de intrare:
# parametrii de iesire:
# complexitate: O(m*n)
def index_el_1(matrice):
    suma_maxima = -1
    index = -1
    # nr coloane
    m = len(matrice[0])
    # nr linii
    n = len(matrice)
    for i in range(0, n):
        suma = 0
        for j in range(0, m):
            suma = suma + matrice[i][j]
        if suma > suma_maxima:
            suma_maxima = suma
            index = i
    return index + 1


print(index_el_1([[0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 1],
                  [0, 0, 1, 1, 1]]))

print(index_el_1([[0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]))

assert index_el_1([[0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 1],
                  [0, 0, 1, 1, 1]]) == 2

assert index_el_1([[0, 0, 0, 1, 1],
                  [0, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]) == 3
