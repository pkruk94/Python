alf = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

def cesar(s,k):    # tutaj zostawia wielkie litery 
    nowe = ""  # nowe slowo po zaszyfrowaniu
    for j in s:
        if j.isupper():  # sprawdza czy mamy wielką literę
            j = j.lower()
            wielka = True
        if j in alf:
            nowyId = ((alf.index(j)) + k) % len(alf) #bierzemy nrindeksu litery starego slowa w alfabecie i przesuwamy a dzieki modulo nie wyjdziemy poza zakres
            m = alf[nowyId]    # litera po przsunięciu
            if wielka: m = m.upper()
            nowe += (m)  # dodaj do slowa przesunieta litere
            wielka = False
        else: nowe += j
    return nowe

s = "Logika dla informatyków"

def cesar2(s,k):
    s = s.lower()  # jezeli nie byloby wielkich liter w alf
    alf2 = []
    nowe = ""
    for i in alf:               # z poprzedniej funkcji
        j = ((alf.index(i)) + k) % len(alf)
        alf2.append(alf[j])     #tablica iter po przesunieciu
    slownik = dict(zip(list(alf), alf2))   # slownik odpowiadajaych
    for j in s:
        if j in alf:
            nowe += slownik[j]
        else:
            nowe += j
    return nowe


print(cesar(s,3))
print(cesar2(s,3))

s = "Wstęp do programowania w języku Python"
print(cesar(s,5))
print(cesar2(s,5))
