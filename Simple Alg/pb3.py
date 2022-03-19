# Să se determine produsul scalar a doi vectori rari care conțin numere reale.
# Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
# De ex. produsul scalar a 2 vectori unidimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.

# functia care realizeaza produsul scalar a 2 vectori rari cu numere reale
# parametrii de intrare: vect1, vect2 - vectori de numere reale
# parametrii de iesire: prod - double - produsul scalar al celor 2 vectori
# complexitate: O(n)
def produs_scalar(vect1, vect2):
    p = 0
    for i in range(0, len(vect1)):
        p = p + vect1[i] * vect2[i]
    return p


print(produs_scalar([1, 2, 3], [1, 2, 3]))
print(produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]))

assert produs_scalar([1, 2, 3], [1, 2, 3]) == 14
assert produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4
