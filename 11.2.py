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
    cesarskie = []
    slowa = set(open("slowa.txt").read().split())
    list_slowa = list(slowa)
    for j in range(len(slowa)):
        k = list_slowa[j]
        for i in range(1, len(alf)):
            nowe = cesar(k,i)
            if nowe in slowa:
                t = (k, nowe)
                cesarskie.append(t)
                print (10000 * j // len(slowa) / 100.0, k, nowe)


    return cesarskie
    
def najdluzsze():
    najdluzsze = ''
    cesarskie = czyCesarskie()
    for para in cesarskie:
        if len(para[0]) > len(najdluzsze):
            najdluzsze = para[0]
    return najdluzsze

print (najdluzsze())
