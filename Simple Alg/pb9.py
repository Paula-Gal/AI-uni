# Considerându-se o matrice cu n x m elemente întregi și o listă cu perechi formate din coordonatele a 2 căsuțe din matrice ((p,q) și (r,s)),
# să se calculeze suma elementelor din sub-matricile identificate de fieare pereche.
# De ex, pt matricea
# [[0, 2, 5, 4, 1],
# [4, 8, 2, 3, 7],
# [6, 3, 4, 6, 2],
# [7, 3, 1, 8, 3],
# [1, 5, 7, 9, 4]]
# și lista de perechi ((1, 1) și (3, 3)), ((2, 2) și (4, 4)), suma elementelor din prima sub-matrice este 38, iar suma elementelor din a 2-a sub-matrice este 44.

# functia care realizeaza suma elementelor sub-matricei generate de 2 puncte date
# parametrii de intrare:
#   matrice - matricea data
#   (x1, y1) si (x2, y2) - perechile de coordonate  a 2 puncte din matrice
# parametrii de iesire: suma sub-matricei determinata de coordonatele celor 2 puncte date
# complexitate: O(N*M)

def suma_sub_matrice(matrice, x1, y1, x2, y2):
    suma = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            suma = suma + matrice[i][j]
    return suma


print(suma_sub_matrice([[0, 2, 5, 4, 1],
                        [4, 8, 2, 3, 7],
                        [6, 3, 4, 6, 2],
                        [7, 3, 1, 8, 3],
                        [1, 5, 7, 9, 4]], 1, 1, 3, 3))

print(suma_sub_matrice([[0, 2, 5, 4, 1],
                        [4, 8, 2, 3, 7],
                        [6, 3, 4, 6, 2],
                        [7, 3, 1, 8, 3],
                        [1, 5, 7, 9, 4]], 2, 2, 4, 4))

assert suma_sub_matrice([[0, 2, 5, 4, 1],
                         [4, 8, 2, 3, 7],
                         [6, 3, 4, 6, 2],
                         [7, 3, 1, 8, 3],
                         [1, 5, 7, 9, 4]], 1, 1, 3, 3) == 38

assert suma_sub_matrice([[0, 2, 5, 4, 1],
                         [4, 8, 2, 3, 7],
                         [6, 3, 4, 6, 2],
                         [7, 3, 1, 8, 3],
                         [1, 5, 7, 9, 4]], 2, 2, 4, 4) == 44
