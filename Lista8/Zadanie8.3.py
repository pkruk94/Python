def slownik(s):
    litery = list(s)
    liczbyWyst = []
    for l in litery:
        i = 0
        for k in litery:
            if k == l:
                i += 1
        liczbyWyst.append(i)
    krotnosciLiter = dict(zip(litery, liczbyWyst))
    return(krotnosciLiter)

def czyUkladalne(a,b):
    x = slownik(a)
    y = slownik(b)
    ukladalne = 1
    for key in x:
        if key not in b:       
            y.update({key:0})  
        if x[key] > y[key]:  
            ukladalne = 0
            break;
    if ukladalne == 1:
        return True
    else:
        return False

def nazw(s):
    litery = list(s)            #usuwam spację, bede korzystał z funkcji z poprzedniego zadania
    if " " in litery:
        litery.remove(" ")
        litery = "".join(litery)
    litery = litery.lower()    # tylko małe litery   (np. boleslawprus)
    return litery


def generujZagadkę(s):
    litery = nazw(s)

    polskieSlowa = open('slowa.txt').readlines()   #słownik polskich słów, (zwraca string)

    naziwsko = litery
    for slowo in polskieSlowa:              #sprawdza czy dane slowo ze slownika jest ukladalne z dostepnego ciagu
        if czyUkladalne(slowo, litery):     #jakim jest nazwisko
            pierwsze = slowo

            slowo = list(slowo)            # ten fragment usuwa litery znalezionego pierwszego z dostepnego ciagu
            litery = list(litery)          # żeby nie bylo powtórzeń
            for i in slowo:
                if i in litery:       
                    litery.remove(i)
            slowo = "".join(slowo)        # z powrotem na string
            litery = "".join(litery)      # np. wsparl, boleus
            
            for drugie in polskieSlowa:          # z dostepnego ciagu szukamy czy uda sie stworzyc drugie do pary
               if czyUkladalne(drugie, litery):
                   print(pierwsze, drugie)
            litery = nazwisko

s = "Bolesław Prus"
generujZagadkę(s)
