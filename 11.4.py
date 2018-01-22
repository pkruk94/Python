def PPN(s):
    slownik = {}
    k = 1
    for i in s:   # przyporządkowuje każdej literze liczbę
        if i not in slownik:
            slownik[i] = k
            k += 1
    s = list(s)
    nowe = []
    for i in s:
        nowe.append(str(slownik[i]) + '-')
    s = "".join(nowe)
    s = s[:-1]
    return s

s = "tak"
print(s, PPN(s))

s = "nie"
print(s, PPN(s))

s = "indianin"
print(s, PPN(s))

s = "tata"
print(s, PPN(s))

s = "żółw"
print(s, PPN(s))

s = "limfangioleiomiomatoza"
print(s, PPN(s))
