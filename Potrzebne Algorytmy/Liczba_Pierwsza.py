def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

print(czy_pierwsza(89))

def test(x):
    liczby = []
    for i in range(0, x):
        liczby.append(i)

    liczby_pierwsze = []
    for i in range(0, x):
        if czy_pierwsza(i):
            liczby_pierwsze.append(i)
        else:
            continue

    print(liczby_pierwsze)

print(test(100000))