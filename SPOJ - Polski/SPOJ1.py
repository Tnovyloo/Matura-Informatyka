def PrimeNumber(n):
    if n % 2 == 0:
        pass
    else:
        print("Tak")

t = int(input("Podaj liczbę testów: "))

for n in range(t):
    PrimeNumber(int(input("Podaj liczbę: ")))