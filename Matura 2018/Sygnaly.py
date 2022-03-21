sygnaly = []
przeslanie = []
przeslanie_po_konwersji = ''

with open('sygnaly.txt') as plik:
    for x in plik:
        sygnaly.append(x.strip('\n'))

# with open('przyklad.txt') as plik:
#     for x in plik:
#         sygnaly.append(x.strip('\n'))

# print(sygnaly) #Przetrzymujemy tutaj cały plik

for x in range(1, 1001):
    if x % 40 == 0:
        przeslanie.append(sygnaly[x - 1])
        # przeslanie.append(sygnaly[x - 1][9])

# print(przeslanie) #Zbieramy co czterdziesta linie

for slowo in przeslanie:
    przeslanie_po_konwersji += slowo[9]

# print(przeslanie_po_konwersji) #Konwertujemy do stringa

word = ''
max = 0
for slowo in sygnaly:
    k = 0
    chars = []
    for litera in slowo:
        if chars.__contains__(litera): #Jesli lista zawiera litere to jej nie dodawaj
            # __contains__ specjalna metoda do sprawdzenia czy dany str jest zawarty w str
            continue
        chars.append(litera)
        k += 1
    if k > max:
        max = k
        word = slowo

words = ''
for slowo in sygnaly:
    b = True
    for litera in slowo:
        if b:
            for litera2 in slowo[1:]:
                diff = abs(ord(litera) - ord(litera2))
                if diff > 10:
                    b = False
        else:
            break
    if b:
        words = words + '\n' + slowo

with open('odpowiedzi.txt', 'w+') as file:
    file.writelines(f"Zadanie 4.1:\n{przeslanie_po_konwersji}\n")
    file.writelines(f"Zadanie 4.2:\n{word} {max}\n")
    file.writelines(f"Zadanie 4.3:\n{words}\n")