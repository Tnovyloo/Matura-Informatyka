def Silnia(liczba_silni):
    n = 1
    for i in range(2, liczba_silni + 1):
        n *= i
        print(n)

Silnia(10)