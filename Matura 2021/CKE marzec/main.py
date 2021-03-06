country = dict()
premises_list = list()
zad43_max = 0
zad43_min = 0
zad43_city_max = ''
zad43_city_min = ''

with open('galerie.txt', 'r') as file:
    for line in file:
        #   Zadanie 4.1
        line = line.rstrip() # Rozdzielamy tekst na pojedyncze linie
        temp = line.split(" ") # Rozdzielamy zawartosc w danej lini
        if temp[0] in country: # Jezeli pierwszy element z temp[0] np "IRL" jest w Country
            country[temp[0]] += 1 # To iteruj wartosc w IRL
        else:
            country[temp[0]] = 1 # Jezeli nie to go dodaj

        #   Zadanie 4.2a
        full_place = dim1 = dim2 = count_premises = 0 # Zmienna calej powierzchni, dlugosci i szerokosci, oraz lokali
        premises = set()
        for x in range(2, 142): # Dla dlugosci wynikajacej z polecen zadania
            if x % 2 == 0: # Nadawanie dlugosci
                dim1 = int(temp[x])
            else: # Nadawanie szerokosci
                dim2 = int(temp[x])
                if dim2 != 0: # Iteruj lokale jesli one istnieja
                    count_premises += 1
                    premises.add(dim1 * dim2)
                full_place += dim1 * dim2 # Sumuj powierzchnie kolejnych lokali
        premises_list.append((temp[1], full_place, count_premises))

        #   Zadanie 4.2b
        max_gallery = min_gallery = 0 # Zmienne do min i max galerii
        city_max = city_min = "" # Zmienne do nazw miast

        for x in premises_list:
            if x[1] > max_gallery or max_gallery == 0:
                city_max = x[0]
                max_gallery = x[1]
            if x[1] < min_gallery or min_gallery == 0:
                city_min = x[0]
                min_gallery = x[1]

        #   Zadanie 4.3
        if len(premises) > zad43_max or zad43_max == 0:
            zad43_max = len(premises)
            zad43_city_max = temp[1]
        if len(premises) < zad43_min or zad43_min == 0:
            zad43_min = len(premises)
            zad43_city_min = temp[1]


def save_to_txt():
    """Zapisywanie danych do txt"""
    with open("wynik4_1.txt", "w") as file:
        file.write("Zadanie 4.1\n")
        for x in country:
            file.write(f"{x}  {country[x]}\n")

    with open("wynik4_2a.txt", "w") as file:
        file.write("Zadanie 4.2\n")
        for x in premises_list:
            for y in x:
                file.write(f"{y} ")
            file.write("\n")

    with open("wynik4_2b.txt", "w") as file:
        file.write(f'{city_max} {max_gallery}\n'
                   f'{city_min} {min_gallery}')

    with open("wynik4_3.txt", "w") as file:
        file.write(f"{zad43_city_min} {zad43_min}\n"
                   f"{zad43_city_max} {zad43_max}")

save_to_txt()