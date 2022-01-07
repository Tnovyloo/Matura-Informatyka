# Największy wspólny dzielnik (NWD) dla dwóch liczb jest to największa liczba naturalna,
# która dzieli każdą z tych liczb bez reszty.
#
# Na przykład dla 16 i 24,
# największą liczbą naturalną która dzieli
# te dwie liczby bez reszty jest 8.
#
# Dla liczb 3 i 9 jest to 3.
#
# Natomiast dla liczb 3 i 7 NWD będzie wynosić 1

#Funkcja rekurencyjna przyjmuje dwa parametry
def nwd(a, b):
    #Jesli b > 0 wtedy wywołaj funkcję z parametrami powyżej
    if b > 0:
        #Parametr a%b to reszta z dzielenia
        return nwd(b, a%b)
    else:
        return a

print(nwd(25, 100))