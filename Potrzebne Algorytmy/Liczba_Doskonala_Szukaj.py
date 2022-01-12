def dzielniki(n):
    liczba = n
    dzielniki = []
    for x in range(n+1):
        if x != 0 and x != n:
            if n % x == 0:
                dzielniki.append(x)
        else:
            continue
    return dzielniki

def czy_doskonala(n):
    templist = dzielniki(n)
    if sum(templist) == n and sum(templist) != 0:
        return n
    else:
        return None

def zakres(n):
    mainlist = []
    for x in range(n+1):
        y = czy_doskonala(x)
        if y is not None:
            mainlist.append(x)
    return mainlist

print(zakres(10000))