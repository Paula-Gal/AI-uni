import math


# Să se determine distanța Euclideană între două locații identificate prin perechi de numere. De ex. distanța între
# (1,5) și (4,1) este 5.0

# functia care determina distanta euclidiana dintre 2 puncte
# parametrii de intrare: x1,y1,x2,y2 - int - coordonatele punctelor a caror distanta se calculeaza
# parametrii de iesire: dist - double - distanta dintre cele 2 puncte date
def distance(x1, y1, x2, y2):
    rad = math.sqrt(((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2)))
    return rad



print(distance(1, 5, 4, 1))
assert distance(1, 5, 4, 1) == 5.0
assert distance(2, 3, 5, 7) == 5.0
assert distance(0, 0, 1, 1) == 1.4142135623730951
