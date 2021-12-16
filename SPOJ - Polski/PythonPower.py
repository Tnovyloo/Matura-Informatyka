a = int(input("Podaj podstawe potegi: "))
b = int(input("Podaj wykładnik potęgi: "))

wynik = 1

for i in range(b):
    if i > b:
        break
    else:
        wynik = wynik * a

print(wynik)
