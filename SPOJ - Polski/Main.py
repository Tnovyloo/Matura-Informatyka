def horner(wsp, st, x):
    wynik = wsp[0]
    for i in range(st):
        wynik = wynik * x + wsp[i]

    return wynik

def Main():
    argument = int
    wspolczynniki = []

    stopien = int(input("Podaj stopien wielomianu"))

    wspolczynniki = [stopien + 1]

    #wczytanie wspólczynników
    for i in range(stopien):
        print(len(wspolczynniki))
        wspolczynniki.append(int(input('Podaj wspolczynnik stojacy przy potedze')))
        stopien -= i



    argument = int(input("Podaj argument"))
    print(horner(wsp=wspolczynniki, st=stopien, x=argument))

Main()