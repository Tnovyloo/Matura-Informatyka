obraz = []
#zmienne do odpowiedzi
zadanie6min = -1
zadanie6max = -1
zadanie6_2 = 0
zadanie6_3 = 0
zadanie6_4 = 0
#Ogarnąc krotki/Tuple
kordynaty = ((1,0),(-1,0),(0,1),(0,-1))

with open("dane.txt", 'r') as file:
    for linia in file:
        temp = linia.rstrip().split(" ")
        obraz.append([int(x) for x in temp])

#Dla x w dlugości 200 wierszy
for x in range(200):
    #Zadanie 6.2
    #Sprawdź oś symetrii (palindrom)
    if obraz[x][::] != obraz[x][::-1]:
        zadanie6_2 += 1

    #Zadanie 6.1
    #Dla Y w długości 320 liczb naturalnych
    for y in range(320):
        if obraz[x][y] > zadanie6max or zadanie6max == -1:
            zadanie6max = obraz[x][y]

        if obraz[x][y] < zadanie6min or zadanie6min == -1:
            zadanie6min = obraz[x][y]

#Zadanie 6.3
# for x in range(0, 320):
#     for y in range(0, 200):
#         licznik = 0
#         for k in kordynaty:
#             if x + k[0] > 319 or x + k[0] < 0 or y + k[1] > 199 or y + k[1] < 0:
#                 continue
#             else:
#                 if abs(list[x][y] - list[y + k[1]][x + k[0]]) > 128:
#                     licznik += 1
#         if licznik != 0:
#             zadanie6_3 += 1

zadanie6_4 = 0
for y in range(0, 320):
    z = 1
    for x in range(1,200):
        if obraz[x - 1][y] == obraz[x][y]:
            z += 1
        else:
            if z > zadanie6_4:
                zadanie6_4 = z
            z = 1


with open("wyniki6.txt", 'w') as file:
    file.write(f'Zadanie 6.1'
               f'\nMinimalna wartosc to {zadanie6min}'
               f'\nMaksymalna wartosc to {zadanie6max}')
    file.write(f"\n\nZadanie 6.2\nIlosc wierszy do usuniecia {zadanie6_2}")
    file.write(f"\n\nZadnie 6.3\nIlosc pikseli {zadanie6_3}")
    file.write(f"\n\nZadanie 6.4\nNajdluzsza linia pionowa {zadanie6_4}")
