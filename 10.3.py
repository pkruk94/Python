from itertools import combinations


def podzbiory(L):
    podzbiory = [j for i in range(len(L)) for j in combinations(L,i)]
    return (podzbiory)
    

L= [1,2,3,100]


def funkcjaA(L):
    subsets = podzbiory(L)
    print(subsets)


funkcjaA(L)
