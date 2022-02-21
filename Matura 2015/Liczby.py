file = open('liczby.txt')

list = []

for liczba_w_pliku in file:
    list.append(liczba_w_pliku.rstrip('\n'))

# list = []
# list.append(input("Podaj binarny "))

# print(len(list))

liczbyzadanie = 0

    #dla liczby w liscie
for liczba in list:
    #dla cyfry w liczbie
    l_jeden = 0
    l_zero = 0
    # Cyfra to dana litera w liczbie
    for cyfra in liczba:

        # print(cyfra + " To jest cyfra")
        # print(liczba + " To jest libcza")

        if cyfra == "1":
            l_jeden += 1

        elif cyfra == "0":
            l_zero += 1

        # print(f"To jest liczba jedynek {l_jeden}"
        #       f"\nTo jest liczba zer {l_zero}")

    if l_zero > l_jeden:
        liczbyzadanie += 1

print(f"Liczb z wieksza iloscia zer to {liczbyzadanie}")

#             do systemu dwojkowego osmego lub innego :)
#int('liczba', 2)

convert_list = []

for liczba in list:
    convert_list.append(int(liczba, 2))

# print(len(convert_list))

ile2 = 0
ile8 = 0
for liczba in convert_list:
    # if liczba % 8 and liczba % 2 == 0:
    #     podzielne_przez_dwa += 1
    #     podzielne_przez_osiem += 1

    if liczba % 2 == 0:
        ile2 += 1

    if liczba % 8 == 0:
        ile8 += 1

print(f"Podzielne przez osiem to {ile8},\n"
      f"Podzielne przez dwa to {ile2}")


temp = 0
queue = 0
for liczba in convert_list:
    if liczba > temp:
        temp = liczba

indeks_max = convert_list.index(temp) + 1 #poniewaz indeks liczy od zera a miejsca w notatniku sa od 1 :)

tymczasowa = 0
minimalna = 0
n = 0
for liczba in convert_list:
    tymczasowa = liczba
    if tymczasowa >= convert_list[n + 1]:
        continue
    else:
        minimalna = tymczasowa

indeks_min = convert_list.index(minimalna)

print(f"Minimalna to: {indeks_min}\n"
      f"Maksymalna to: {indeks_max}")

min = -1
max = 260
krotkie = []
dlugie = []
for liczba in list:
    if len(liczba) == min:
        krotkie.append(liczba)
    if len(liczba) == max:
        dlugie.append(liczba)
    if len(liczba) < min:
        min = len(liczba); krotkie = [liczba]
    if len(liczba) > max:
        max = len(liczba); dlugie = [liczba]
print(list.index((int(krotkie)) + 1))
print(list.index((int(dlugie)) + 1))