instrukcje = [] #W niej przechowujemy wszystkie instrukcje
with open('instrukcje.txt', 'r') as file:
    for line in file:
        instrukcje.append(line.strip())

# print(lista)

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

    # best = ['start', 0]
    # poprzedni = 'start'
    # dlugosc = 0
    # for idx, item in enumerate(lista):
    #     krok = item.split()[0]
    #     if krok == poprzedni:
    #         dlugosc += 1
    #     else:
    #         if dlugosc > best[1]:
    #             best[0] = lista[idx - 1].split()[0]
    #             best[1] = dlugosc
    #         poprzedni = krok
    #         dlugosc = 1
    # return best

def zadanie4_3(lista):
    # char = ''
    # temp = 1
    # max = 0
    # for var in lista:
    #     if var.__contains__('DOPISZ'):
    #         if temp > max:
    #             temp += 1
    #             char = var.split()[1]
    #             max = temp
    #         else:
    #             temp = 0
    # return char, max

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
    print("3)", najczesciej_litera, najczesciej)



print(zadanie4_1(instrukcje))
print(zadanie4_2(instrukcje))
print(zadanie4_3(instrukcje))

#TODO ZADANIE 4_4

# print(lista[0][0:3])
