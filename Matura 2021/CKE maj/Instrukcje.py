instrukcje = [] #W niej przechowujemy wszystkie instrukcje
with open('instrukcje.txt', 'r') as file:
    for line in file:
        instrukcje.append(line.strip())

def zadanie4_1(lista):
    dlugosc = 0
    for var in lista:
        if var.__contains__('DOPISZ'):
            dlugosc += 1
        if var.__contains__('USUN'):
            dlugosc -= 1
    return dlugosc

def zadanie4_2(lista):
    max = 0
    temp = 1
    text = ''
    for var in range(len(lista)-1): #1999
        if lista[var][0:3] == lista[var+1][0:3]:
            temp += 1
            # text = lista[var]
        else:
            if temp > max:
                max = temp
                text = lista[var]
            temp = 1
    return max, text

def zadanie4_3(lista):
    litery = {}
    for var in lista:
        rodzaj, znak = var.split()
        if rodzaj == "DOPISZ":
            if znak in litery:
                litery[znak] += 1
            else:
                litery[znak] = 1
    najczesciej_litera = None
    najczesciej = 0
    for litera in litery:
        if litery[litera] > najczesciej:
            najczesciej_litera = litera
            najczesciej = litery[litera]
    # skrócona wersja powyższego dla ciekawych:
    # najczesciej = max(litery.items(), key=lambda x: x[1])
    return najczesciej_litera, najczesciej

def dopisz(tekst, litera):
    return tekst + litera

def usun(tekst):
    return tekst[:len(tekst)-1]

def zmien(tekst, litera): #funckja zmieniajaca ostatni znak
    txtlist = list(tekst) #uwaga: w pythonie teksty musimy potraktowac jako liste
    txtlist[len(tekst) - 1] = litera #jezeli chcemy podmienic znak na danej pozycji
    return "".join(txtlist) #na koniec liste ta musimy zmienic z powrotem na tekst

def przesun(tekst, litera):
    index = tekst.find(litera)
    if index == -1:  # jezeli nie znalezlismy znaku, przerywamy dzialanie
        return tekst
    if litera == 'Z':  # jezeli jest to ostatnia litera alfabetu, to wracamy na poczatek
        litera = 'A'
    else:  # w przeciwnym przypadku przesuwamy znak o 1
        litera = chr(ord(litera) + 1)
    txtlist = list(tekst)  # nastepnie musimy ponownie zamienic text na liste znakow
    txtlist[index] = litera  # podmienic znak
    return "".join(txtlist)  # i zwrocic ja jako ciag znakow


def zadanie4_4(lista):
    result = ''
    for var in lista:
        args = var.split(" ")
        char = args[1]
        command = args[0]
        if command == "DOPISZ":
            result = dopisz(result, char)
        if command == "ZMIEN":
            result = zmien(result, char)
        if command == "USUN":
            result = usun(result)
        if command == "PRZESUN":
            result = przesun(result, char)
    return result

print(zadanie4_1(instrukcje))
print(zadanie4_2(instrukcje))
print(zadanie4_3(instrukcje))
print(zadanie4_4(instrukcje))

#TODO ZADANIE 4_4

# print(lista[0][0:3])
