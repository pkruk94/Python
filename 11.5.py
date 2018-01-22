from itertools import permutations

alf = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
slowa = open("slowa.txt").read().split()

def cesar(s,k):  
    s = s.lower() 
    nowe = "" 
    for j in s:
        if j in alf:
            nowyId = ((alf.index(j)) - k) % len(alf) 
            nowe += (alf[nowyId]) 
        else: nowe += j
    return nowe

def deszyfruj(s):
    noweSlowa = []
    s = s.split(" ")    # tutaj chce miec same slowa, bez interpunkcji
    for i in s:
        if i == "?" or i == "!" or i == "." or i == ",":
            s.remove(i)

    liczby = []
    licznik = 0
    for i in range(1, len(alf)+1):
        liczby.append(i)
    for p in permutations(liczby):
        slownik = dict(zip(list(alf),p))    # permutacje mozliwycj kluczy
        for i in s:     # zamieniam kazde slowo osobno
            slowo = list(i)
            nowe = ""
            for k in slowo:
                nowe += cesar(k,slownik[k])
            if nowe in slowa: 
                noweSłowa.append(nowe)
                licznik += 1
            else: break
        if licznik == len(s): print(noweSłowa)
                    
                


deszyfruj("czwbn")
