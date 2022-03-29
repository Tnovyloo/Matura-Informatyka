import math

lista = []
with open('pary.txt') as file:
    for line in file:
        lista.append(line.strip())

def czy_pierwsza(n):
    s = int(math.sqrt(n))
    for i in range(2, s+1):
        if n % i == 0:
            return False
    return True

def goldbach(n):
    if n % 2 == 0:
        return
    num1 = 0
    num2 = 0
    for i in range(3, n+1):
        r = n - 1
        if r % 2 == 0 or i % 2 == 0:
            continue
        if not czy_pierwsza(r) or not czy_pierwsza(i):
            continue
        if num2 - num1 <= r - i:
            num2 = r
            num1 = i
    print(f'{n} {num1} {num2}')

for i in lista:
    num = int(i.split(" ")[0])
    goldbach(num)

word = ""
for line in lista:
    word = line.split(" ")[1]
    longest = ""
    current = ""
    for i in range(len(word)):
        if len(current) == 0 or current[0] == word[i]:
            current += word[i]
        else:  # w przeciwnym wypadku
            if len(current) > len(longest):
                longest = current
            current = ""
            current += word[i]
    if len(current) > len(longest):
        longest = current
    if len(longest) == 0:
        longest = current
    print(longest + " " + str(len(longest)))