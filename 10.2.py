from itertools import combinations, permutations

def slowoNaCyfry(s,dic):    #zamieniam slowo na liczbę wg podanego klucza
    s = list(s)
    nowe = ""
    for k in s:
        nowe += str(dic[k])
    return nowe

def rozwiaz(s):      # tutaj tworze liste slow (zmiennych) równania
    slowa = []     
    tab = s.split(" ")
    for i in tab:
        if i != "+" and i != "=" and i != " ":
            slowa.append(i)

    a = slowa[0]
    b = slowa[1]
    c = slowa[2]

    x = list(s)       # tutaj litery wystepujace w rownaniu (potem zamienione na cyfry)
    litery = []
    for i in x:
        if i != "+" and i != "=" and i != " ":
            litery.append(i)
    litery = list(set(litery))


    cyfry = [0,1,2,3,4,5,6,7,8,9]     # tworze możliwe klucze rozwiazan
    for p in permutations(cyfry):
        klucz = dict(zip(litery,p))    # warunek: liczba nie moze zaczynac sie od 0
        
        if klucz[a[0]] == 0 or klucz[b[0]] == 0 or klucz[c[0]] == 0: continue

        rozw = []
        for s in slowa:
            rozw.append(slowoNaCyfry(s,klucz))    # zamieniam slowo na liczbe wg klucza

        if (int(rozw[0]) + int(rozw[1]) == int(rozw[2])):
            return(klucz)
    return None


print(rozwiaz("ciacho + ciacho = nadwaga"))

print(rozwiaz("send + more = money"))
