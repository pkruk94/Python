def funkcja():
    przedmioty = {}
    dziennik = open('plik.txt').readlines()
    for line in dziennik:
        if "przedmiot" in line:
            przedmioty[line] = {}
    for l in dziennik:
        if "przedmiot" in l:
            klucz = l
        else:
            lista = l.split()
            if len(lista):
                imie = lista[0]
                lista.pop(0)
                lista = "".join(lista)
                lista = lista.split(",")
                if imie in przedmioty[klucz]:
                    przedmioty[klucz][imie] += (lista)
                else:
                    przedmioty[klucz][imie] = (lista)
    
    print(przedmioty["przedmiot: Historia\n"])
   

    for key in przedmioty:
        for key2 in przedmioty[key]:
            srednia = 0
            for j in przedmioty[key][key2]:
                srednia += int(j)
                srednia /= len(przedmioty[key][key2])
        print(key, key2, srednia)

    print(przedmioty)

funkcja()
