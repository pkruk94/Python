
def add(a,b):
    return simplify((((a[0] * b[1]) + (b[0] * a[1])), a[1] * b[1]))

def mult(a,b):
    return simplify((a[0] * b[0], a[1] * b[1]))

def sub(a,b):
    return simplify((((a[0] * b[1]) - (b[0] * a[1])), a[1] * b[1]))

def div(a,b):
    return simplify((a[0] * b[1], a[1] * b[0]))

def make(licznik,mianownik):
    return (licznik,mianownik)

def nwd(n,m):
    if n < 0:
        n *= -1
    if m < 0:
        m *= -1
    if m == 0:
        return n
    if m > n:
        return nwd(m,n)
    return nwd(m, n%m)

def simplify(a):
    return ((a[0]//nwd(a[0], a[1])),(a[1]//nwd(a[0], a[1])))


def add2(a,b):
    b[0] = ((a[0] * b[1]) + (b[0] * a[1]))
    b[1] = a[1] * b[1]
    return simplify(b[0],b[1])

def mult2(a,b):
    b[0] = a[0] * b[0]
    b[1] = a[1] * b[1]
    return simplify(b[0], b[1])

def sub2(a,b):
    b[0] = (a[0] * b[1]) - (b[0] * a[1])
    b[1] = a[1] * b[1]
    return simplify(b[0], b[1])

def div2(a,b):
    b[0] = a[0] * b[1]
    b[1] = a[1] * b[0]
    return simplify(b[0], b[1])