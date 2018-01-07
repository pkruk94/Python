##### wprawka III wtorek, 21.11, PR

def dzielniki(N):
    dzielPierw = []
    i = 2
    for i in range(2,N+1):
        while(N%i == 0):
            dzielPierw.append(i)
            N /= i
    i += 1
    return dzielPierw


print(dzielniki(24))
print(dzielniki(13))
print(dzielniki(625))
print(dzielniki(32821))


def na_iloczyny(L):
    iloczyny = []
    for i in L:
        lista = dzielniki(i)
        s = ""
        for j in lista:
            s += str(j) + '*'
        s = s[:-1]   #usuwam ostatni *
        iloczyny.append(s)

    print(iloczyny)

L=[4,24,26]
na_iloczyny(L)

L=[4,8,15,16,23,42]
na_iloczyny(L)
