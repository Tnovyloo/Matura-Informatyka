with open('liczby.txt', 'r') as file:
    file_numbers = [line.rstrip() for line in file]

def power_3():
    power_of_3 = []
    i = 0
    num = 1
    while True:
        num = 3 ** i
        power_of_3.append(num)
        if num > 100000:
            break
        i += 1
    return power_of_3

def strong(n):
    if n > 1:
        return n * strong(n - 1)
    return 1

def NWD(a, b):
    if b > 0:
        return NWD(b, a%b)
    else:
        return a

def check_1(numbers):
    power_of_3 = power_3()
    temp_list = [line for line in numbers if int(line) in power_of_3]
    return temp_list

def check_2(numbers):
    temp_list = []
    for number in numbers:
        temp_result = 0
        for num in number:
            temp_result += strong(int(num))
        if temp_result == int(number):
            temp_list.append(number)
    return temp_list

def check_3(numbers):
    pom = []  # zmienna przechowujaca liczby spelniajace warunki
    dzielnik = int(numbers[0])  # zmienna przechowujaca aktualny dzielnik (lub pierwsza liczbe ciagu)
    pierwszaMax = 0  # zmienna przechowujaca pierwsza liczbe ciagu
    dlugoscMax = 0  # zmienna przechowujaca dlugosc ciagu
    dzielnikMax = 1  # zmienna przchowujaca dzielnik ciagu

    for i in range(1, 500):  # iterujemy z pominieciem pierwszej liczby(bo uzylismy ja powyzej)
        num = int(numbers[i])  # zamieniamy tekst na liczbe
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



print(len(check_1(file_numbers)))
print(check_2(file_numbers))
