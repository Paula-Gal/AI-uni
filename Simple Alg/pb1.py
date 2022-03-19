# Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text care
# conține mai multe cuvinte separate prin ” ” (spațiu). De ex. ultimul (dpdv alfabetic) cuvânt din
# ”Ana are mere rosii si galbene” este cuvântul "si".


# functia care returneaza cuvintele dintr-o propozitie data
# parametrii de intrare: sentence - propozitia data
# parametrii de iesire: words - lista de cuvinte
def words(sentence):
    w = sentence.split(' ')
    return w


# functia care sorteaza alfabetic o lista de cuvinte
# parametrii de intrare: words - lista de cuvinte
# parametrii de iesire: words - lista de cuvinte sortata
# complexitate: best case: O(nlogn), average case: O(nlogn), worst case: O(n^2)
def quick_sort(words_list):
    if len(words_list) == 0:
        return []
    # aleg primul element din words ca si pivot
    p = words_list[0]
    mai_mic = [x for x in words_list[1:] if x < p]
    mai_mare = [x for x in words_list[1:] if x >= p]
    return quick_sort(mai_mic) + [p] + quick_sort(mai_mare)


# functia care returneaza ultimul cuvant (dpdv alfabetic) dintr-un text
# parametrii de intrare: sentence - propozitia data
# parametrii de iesire: word - cuvantul ultim (dpdv alfabetic)
def last_word(sentence):
    w = words(sentence)
    w = quick_sort(w)
    return w[len(w) - 1]


print(last_word('Ana are mere rosii si galbene'))

assert last_word('Ana are mere rosii si galbene') == 'si'
assert last_word('diana maria ioana') == 'maria'
assert last_word(' ') == ''
