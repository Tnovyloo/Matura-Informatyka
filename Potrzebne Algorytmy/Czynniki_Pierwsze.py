def rozloz(n):
    czynniki = []
    k = 2
    #Pierwszy warunek 'n' jest rozne od 1
    while n != 1:
        #Wejdz w petle kiedy reszta z dzielenia przez 'k' daje 0
        while n % k == 0:
            # n //= k
            print(n)
            #Podziel n przez k
            n = n // k
            print(n)
            print(f'Dodaje {k} do tablicy\n')
            czynniki.append(k)
        k += 1
    return czynniki

print(rozloz(35))
