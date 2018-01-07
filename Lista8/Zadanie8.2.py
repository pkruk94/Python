def slownik(s):
    litery = list(s)  #tworze slownik z dwoch rownoleglych list
    liczbyWyst = []
    for l in litery:
        i = 0
        for k in litery:   # zliczam lizbe wystapien danej litery
            if k == l:
                i += 1
        liczbyWyst.append(i)
    krotnosciLiter = dict(zip(litery, liczbyWyst))
    return(krotnosciLiter)


def czyUkladalne(a,b):
    a = a.lower()
    b = b.lower()
    print(a," ",b)
    x = slownik(a)
    y = slownik(b)
    ukladalne = 1
    for key in x:
        if key not in b:       # gdy danej litery w ogole nie ma w slowie dodaje do klucza ta litere
            y.update({key:0})  # oraz jej liczbe wystapien = 0
        if x[key] > y[key]:     # porownuje czestosc wystepowania danej litery
            ukladalne = 0
    if ukladalne == 1:
        print("Mozna")
    else:
        print("Nie mozna")


s = "limfangioleiomiomatoza"
p = "lem"
czyUkladalne(p,s)

s = "lokomotywa"
p = "motyl"
czyUkladalne(p,s)

s = "kotka"
p = "żak"
czyUkladalne(p,s)


s = "ziemniak"
p = "nie"
czyUkladalne(p,s)

s = "BolesławPrus"
p = "wsparł"
czyUkladalne(p,s)

s = "CzesławMiłosz"
p = "wmieszał"
czyUkladalne(p,s)
