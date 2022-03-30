liczby = []
liczby_3 = []

#Zapisywanie danych do listy
with open('przyklad.txt', 'r') as file:
    for line in file:
        liczby.append(line.strip())

#Tworzymy druga liste poteg liczby 3
p = 1
i = 0

while True:
    p = 3 ** i
    liczby_3.append(p)
    if p > 100000:
        break
    i += 1

zlicz4_1 = 0

#Metoda liczenia
for liczba in liczby:
    if int(liczba) in liczby_3:
        zlicz4_1 += 1
        # print(liczba)

print(f'\nOdp 4.1 {zlicz4_1}')

def silnia(n):
    if n > 1:
        return n * silnia(n- 1)
    return 1

zlicz4_2 = 0
#Biezemy liczbe z tablicy
for liczba in liczby:
    #Biezemy kazda cyfre z liczby
    if len(liczba) == 0 :
        continue

    temp = 0

    for cyfra in liczba:
        # silnia(cyfra)
        temp += silnia(int(cyfra))

    if temp == int(liczba):
        zlicz4_2 += 1

print(f'\nOdp 4.2 {zlicz4_2}')

def NWD(a, b):  # // funkcja znajdujaca najwiekszy wspolny dzielnik (NWD) dwóch liczb
    k = 1
    while b != 0:
        k = b
        b = a % b
        a = k
    return a


file = open("liczby.txt", "r")  # jezeli plik nie bedzie istnial, to program zwroc blad
lines = file.read().splitlines()  # pozbywamy sie znakow nowego wiersza
file.close()  # zamykamy plik
pom = []  # zmienna przechowujaca liczby spelniajace warunki
dzielnik = int(lines[0])  # zmienna przechowujaca aktualny dzielnik (lub pierwsza liczbe ciagu)
pierwszaMax = 0  # zmienna przechowujaca pierwsza liczbe ciagu
dlugoscMax = 0  # zmienna przechowujaca dlugosc ciagu
dzielnikMax = 1  # zmienna przchowujaca dzielnik ciagu

for i in range(1, 500):  # iterujemy z pominieciem pierwszej liczby(bo uzylismy ja powyzej)
    num = int(lines[i])  # zamieniamy tekst na liczbe
    nwd = NWD(dzielnik, num)  # liczymy Najwiekszy Wspolny Dzielnik dla przechowanej liczby/dzielnika
    if nwd != 1:  # jeżeli mają wspólny dzielnik (inny niż 1)
        if len(pom) == 0:  # sprawdzamy najpierw czy pomocniczy zbior liczb jest pusty (co oznaczałoby, ze w n jest przechowana liczba, a nie dzielnik)
            pom.append(dzielnik)  # jezeli tak to od razu dodajemy ta liczbe do zbioru (aby jej nie pominac)
        pom.append(num)  # nastepnie dodajemy liczbe z aktualnego wiersza
        dzielnik = nwd  # i przypisujemy za n nowy dzielnik
    else:
        if len(pom) > dlugoscMax:  # w przeciwnym wypadku sprawdzamy czy pomocniczy zbior jest dluzszy, niz przechowana dlugosc
            dlugoscMax = len(pom)  # jezeli tak to zapisujemy jego dlugosc
            dzielnikMax = dzielnik  # dzielnik
            pierwszaMax = pom[0]  # oraz pierwszy wyraz
        if len(pom) != 0:  # jezeli zas pomocniczy zbior nie jest pusty (co oznacza, że wlasnie znalezlismy koniec ciagu)
            if NWD(pom[len(pom) - 1], num) > 1:  # musimy sprawdzic ostatni wyraz i pierwszy nastepnego ciagu
                a = pom[len(pom) - 1]  # jezeli liczby maja wspolny dzielnik
                pom.clear()  # czyscimy zbior pomocniczy
                pom.append(a)  # a nastepnie dodajemy do niego od razu dwie liczby
                pom.append(num)  # ktore spelniaja warunki zadania
            else:
                pom.clear()  # w innym razie po prostu czyscimy zbior pomocniczy
        dzielnik = num  # na koniec za dzielnik przypisujemy aktualna liczbe (aby na poczatku petli mozna bylo policzyc nowy NWD)
print("\nPierwsza liczba z ciagu: " + str(pierwszaMax) + ", dzielnik " + str(dzielnikMax) + ", dlugosc ciagu: " + str(
    dlugoscMax))