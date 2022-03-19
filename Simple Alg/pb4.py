# Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
# astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
# De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.

# functia care determina valoarea care apare de 2 ori intr-n sir dat
# parametrii de intrare: sir - sir de numere din multimea {1, 2, ...n-1}
# parametrii de iesire: val - valoarea ce apare de 2 ori in sirul dat
# complexitate: O(n)
def frequency2(sir):
    # folosim formula sumei primelor n numere naturale
    # S = n*(n-1)/2
    n = len(sir)
    s = n * (n - 1) / 2
    suma = 0
    for item in sir:
        suma = suma + item
    return suma - s


print(frequency2([1, 2, 3, 4, 2]))

assert frequency2([1, 2, 3, 4, 2]) == 2
assert frequency2([1, 2, 3, 4, 5, 5]) == 5
