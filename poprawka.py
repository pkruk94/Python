def sortuj(L):
    if len(L) == 1 or len(L) == 0:
        return L
    else:
        s = (len(L))//2
        lewa = L[:s]
        prawa = L[s:]
        
        lewa = sortuj(lewa)
        prawa = sortuj(prawa)
        return scalaj(lewa,prawa)
        
        

def scalaj(L1,L2):
    L = []
    while len(L1) != 0 and len(L2) != 0:
        if L1[0] < L2[0]:
            L.append(L1[0])
            del L1[0]
        else:
            L.append(L2[0])
            del L2[0]
    
    if len(L1) == 0:
        L += L2
    else:
        L += L1
    
    return L
    
    
    
L = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]



print(sortuj(L))
