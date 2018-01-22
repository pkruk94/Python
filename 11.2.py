from  itertools import permutations as pp

alf = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"

def cesar(s,k):  
    s = s.lower() 
    nowe = "" 
    for j in s:
        if j in alf:
            nowyId = ((alf.index(j)) + k) % len(alf) #bierzemy nrindeksu litery starego slowa w alfabecie i przesuwamy a dzieki modulo nie wyjdziemy poza zakres
            nowe += (alf[nowyId])  # dodaj do slowa przesunieta litere
        else: nowe += j
    return nowe


def czyCesarskie():
    cesarskie = {}
    slowa = open("slowa.txt").read().split()
    for k in slowa:
        for i in range(1, len(alf)):
            nowe = cesar(k,i)
            if nowe in slowa:
                cesarskie["k"] = nowe
                slowa.remove(nowe)
    print(cesarskie)

czyCesarskie()
