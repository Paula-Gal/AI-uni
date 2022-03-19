# 7. Să se determine al k-lea cel mai mare element al unui șir de numere cu n elemente (k < n).
# De ex. al 2-lea cel mai mare element din șirul [7,4,6,3,9,1] este 7.


# functia care sorteaza alfabetic o lista de cuvinte
# parametrii de intrare: sir - sirul de n numere dat
# parametrii de iesire: sirul de numere dat sortat descrescator
# complexitate: best case: O(nlogn), average case: O(nlogn), worst case: O(n^2)

def quick_sort(sir):
    if len(sir) == 0:
        return []
    # aleg primul element din sir ca si pivot
    p = sir[0]
    mai_mic = [x for x in sir[1:] if x > p]
    mai_mare = [x for x in sir[1:] if x <= p]
    return quick_sort(mai_mic) + [p] + quick_sort(mai_mare)


# functia care returneaza al k-lea cel mai mare element al unui sir de n numere
# parametrii de intrare: sir - sir dat de n numere
# parametrii de iesire: val - al k-lea cel mai mare element a unui sir
# complexitate: O(n)

def k_element(sir, k):
    # sortez descrescator sirul
    sir = quick_sort(sir)
    p = 0
    elem = sir[0]
    # caut al k-lea element
    for item in sir:
        if item != elem:
            p += 1
        if p == k-1:
            return item


print(k_element([7, 4, 6, 3, 9, 1], 2))
print(k_element([1, 2, 2, 2], 2))

assert k_element([1, 2, 2, 2], 1) == 2
assert k_element([1, 2, 2, 2], 2) == 1
assert k_element([7, 4, 6, 3, 9, 1], 2) == 7
assert k_element([8, 8, 8, 8, 8, 1], 2) == 1
assert k_element([8, 8, 8, 8, 8, 1, 2], 3) == 1
