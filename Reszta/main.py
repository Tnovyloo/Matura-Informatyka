pairs_file = open("pary.txt", "r")
pairs = []

odp = open("wyniki4.txt", "w")

#Prosta petla do wczytania danych
for _ in range(100):
    n, word = pairs_file.readline().split()
    pairs.append([int(n), word])
pairs_file.close()

#Sprawdzanie czy liczba podana n jest liczbą pierwsza
def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n ** 0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

odp.write("Zadanie4.1.\n")
for [n, _] in pairs:
    if n % 2 == 0 and n > 4:
        for i in range(3, n, 2):
            if czy_pierwsza(i) and czy_pierwsza(n-i):
                odp.write(f"{n} {i} {n+i}\n")
                break

odp.write("\n Zadanie 4.2.\n")
for [n, word] in pairs:
    max = 1
    max_letter = word[0]
    cur_max = 0
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            cur_max += 1
        else:
            cur_max = 1

        if cur_max > max:
            max = cur_max
            max_letter = word[i]
    odp.write(f"{max * max_letter} {max}\n")