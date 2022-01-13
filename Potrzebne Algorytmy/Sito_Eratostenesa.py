import math

def sito(n):
    if n < 2:
        print('Brak liczb pierwszych w podanym zakresie')
    else:
        liczby = [True] * (n + 1)  # Tworzymy tablice n+1
        for i in range(2, int(math.sqrt(n))):  # Dla in range(2 do pierwiastka z n)
            if liczby[i]:  # Jezeli liczba jest pierwsza
                for k in range(i * i, n + 1, i):
                    #Oznacz wszystkie liczby jej wielokrotnosci jako liczby złożone
                    liczby[k] = False

    print("Liczby pierwsze z przedzialu <2," + str(n) + "> : ")
    for i in range(2, n + 1):  # wypisujemy elementy utworzonej tablicy
        if liczby[i]:
            print(str(i), end=" | ")


sito(1000)


