#Funkcja rekurencyjna przyjmuje dwa parametry
def nwd(a, b):
    #Jesli b > 0 wtedy wywołaj funkcję z parametrami
    if b > 0:
        #Parametr a%b to reszta z dzielenia
        return nwd(b, a%b)
    else:
        return a

print(nwd(25, 100))