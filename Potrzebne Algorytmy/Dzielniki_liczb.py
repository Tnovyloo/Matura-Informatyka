def szukaj_dzielnikow(n):
    dzielniki = []
    for x in range(n+1):
        if x != 0:
            if n % x == 0:
                dzielniki.append(x)
        else:
            continue
    return dzielniki

print(szukaj_dzielnikow(32))