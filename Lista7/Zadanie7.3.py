def najdluzsze():
    słowa = []
    najdl = []
    plik = open('test.txt').read()
    for word in plik.split():
        if (word[len(word)-1] == ',' or word[len(word)-1] == '.'): #ignoruje znaki inteprunkcyjne na koncu słowa
            word = list(word)
            word.remove(word[len(word)-1])
            word = "".join(word)
            słowa.append(word)
        else:
            słowa.append(word)
    słowa.sort(key=len, reverse = True)      #sortuje słowa tekstu od najdłuższego do najkrótszego
    najdl.append(słowa[0])                   # tablica najdluzszych słow
    for word in słowa:                       #jezeli są słowa o takiej samej dlugosci jak najdlusze to dodaje je 
        if len(word) == najdl[0]:            # do listy najdluzszych 
            najdl.append(word)
    sorted(najdl, key=str.lower)     #sortuje alfabetycznie, ignorując wielie i małe litery
    print(najdl)


najdluzsze()
