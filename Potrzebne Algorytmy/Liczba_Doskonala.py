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
    lista = dzielniki(n)
    print(f"Dzielniki liczb mniejsze od liczby '{n}'\n"
          f"{dzielniki(n)}")
    # print(sum(dzielniki(n)))
    if sum(lista) == n:
        print(f"Liczba {n} jest liczbą doskonałą")
    else:
        print(f"Liczba {n} nie jest liczbą doskonałą")


czy_doskonala(int(input('Podaj liczbę,\nżeby sprawdzić czy jest doskonała: ')))