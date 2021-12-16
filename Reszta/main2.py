pary_plik = open("pary.txt", "r")
we = pary_plik.readlines()
pary_plik.close()

print(we)

WE = []
WE1 = []
WE2 = []

for i in we:
    i = i.split()       #splitowanie kazdego elementu
    WE.append((int(i[0]), i[1]))    # WE Posiada inta i tekst
    WE1.append(int(i[0]))           # WE1 Posiada inta
    WE2.append(i[1])                # WE2 Posiada tekst

##Zrobmy to profejsonalnie tak jak przystalo na prawdziwego pythonowaca

# WE = [(a.split()) for a in we]
# WE1 = [(int(a), b) for a,b in we]
# WE1,WE2 = zip(*we)

n = 100
P = [1] * (n + 1)
for i in range(2, int(n**0.5) + 1):
    if P[i]:
        for j in range(2*i, n+1, i):
            P[j] = 0

for i in WE1:
    if not i % 2 and i>4:
        for j in range(3,100):
            if P[j] and P[i - j]:
                print(i, j, i - j)
                break

                # 9:32

we3 = ("abc", "aaaallll", "aasdasdasdbbbb", "aaaalamapsa")
for i in we3:
    maks = -1
    lokalna_dlugosc = 0
    poprzednia_litera = "-"
    litera = "-"
    for j in i+"-":
        if poprzednia_litera == j:
            lokalna_dlugosc += 1

        else:
            if maks<lokalna_dlugosc:
                maks = lokalna_dlugosc
                litera = poprzednia_litera
            lokalna_dlugosc = 1
            poprzednia_litera = j

    print(i, litera*maks, maks)


mini = (we[0])
for a,b in we:
    if a == len(b) and (a < mini[0] or a == mini[0] and b < mini[1]):
        mini=(a, b)

print(mini)