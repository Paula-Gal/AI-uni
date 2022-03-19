# Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
# De ex. matricea \
# [[1,1,1,1,0,0,1,1,0,1],
# [1,0,0,1,1,0,1,1,1,1],
# [1,0,0,1,1,1,1,1,1,1],
# [1,1,1,1,0,0,1,1,0,1],
# [1,0,0,1,1,0,1,1,0,0],
# [1,1,0,1,1,0,0,1,0,1],
# [1,1,1,0,1,0,1,0,0,1],
# [1,1,1,0,1,1,1,1,1,1]]
# *devine *
# [[1,1,1,1,0,0,1,1,0,1],
# [1,1,1,1,1,0,1,1,1,1],
# [1,1,1,1,1,1,1,1,1,1],
# [1,1,1,1,1,1,1,1,0,1],
# [1,1,1,1,1,1,1,1,0,0],
# [1,1,1,1,1,1,1,1,0,1],
# [1,1,1,0,1,1,1,0,0,1],
# [1,1,1,0,1,1,1,1,1,1]]\

# functia care


import np as np

# functia are afiseaza o matrice
# parametrii de intrare: matrice - o matrice de dimensiune nxm
# parametrii de iesire: -
def afisare_matrice(matrice):
    arr = np.array(matrice)
    print(arr)


# functia care boredeaza o matrice cu -1
# parametrii de intrare: matrice - matricea de bordat
#                        n - int - nr de linii ale matricei
#                        m - int - nr de coloane ale matricei
# parametrii de iesire - matricea data bordata
# complexitate: O(m*n)
def bordare_matrice(matrice, n, m):
    # generez o matrice cu el 0 de dimensiune nxm
    matrice_bordata = np.zeros((n, m))
    for i in range(0, n):
        for j in range(0, m):
            if i == 0 or i == n - 1:
                # prima si ultima linie
                matrice_bordata[i][j] = -1
            else:
                # prima si ultima coloana
                if j == 0 or j == m - 1:
                    matrice_bordata[i][j] = -1
    # copiez matricea data inauntrul matricii construite
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrice_bordata[i][j] == 0:
                matrice_bordata[i][j] = matrice[i - 1][j - 1]

    return matrice_bordata


# functia care umple cu valori toate posibilele iesiri din matrice
# parametrii de intrare: matrice - matricea de bordat
#                        n - int - nr de linii ale matricei
#                        m - int - nr de coloane ale matricei
#                        i - int - indicele liniei curente
#                        j - int -indicele coloanei curente
#                        k - int - val cu care se umple o casuta in matrice
# parametrii de iesire -
def umplere(matrice, i, j, k, n, m):
    matrice[i][j] = k
    if matrice[i - 1][j] == 0:
        umplere(matrice, i - 1, j, k, n, m)
    if i + 1 < n and matrice[i + 1][j] == 0:
        umplere(matrice, i + 1, j, k, n, m)
    if matrice[i][j - 1] == 0:
        umplere(matrice, i, j - 1, k, n, m)
    if j + 1 < m and matrice[i][j + 1] == 0:
        umplere(matrice, i, j + 1, k, n, m)


# functia care inlocuieste valorile înlocuiască cu 1 toate aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
# parametrii de intrare: matrice - o matrice de dimensiune nxm
# parametrii de iesire: matricea rezultat
# complexitate: O(m*n)
def inlocuire(matrice):
    # nr linii
    m = len(matrice[0]) + 2
    # nr coloane
    n = len(matrice) + 2
    k = 1
    print("matrice initiala: ")
    afisare_matrice(matrice)
    matrice = bordare_matrice(matrice, n, m)
    print("matrice dupa bordare: ")
    afisare_matrice(matrice)
    for i in range(0, n):
        for j in range(0, m):
            if matrice[i][j] == -1:
                k = k + 1
                umplere(matrice, i, j, k + 1, n, m)
    print("matrice dupa marcare: ")
    afisare_matrice(matrice)
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrice[i][j] > 1:
                matrice[i][j] = 0
            else:
                if matrice[i][j] == 0:
                    matrice[i][j] = 1
    print("matrice finala: ")
    # sterg bordarea
    matrice = matrice[1:n - 1, 1:m - 1]
    afisare_matrice(matrice)
    return matrice


matrice_rezultat = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

matrice = inlocuire([[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                     [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
                     [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                     [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                     [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
                     [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
                     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]])

assert np.all(matrice) == np.all(matrice_rezultat)
