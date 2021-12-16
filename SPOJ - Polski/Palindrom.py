x = input("Podaj slowo").lower().replace(" ","")
n = len(x)
for i in range(n - 1):
    if x[i] != x[n-1-i]:
        print("Falsz")
    print("Prawda")