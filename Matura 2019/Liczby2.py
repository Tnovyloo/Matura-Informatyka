with open('liczby.txt', 'r') as file:
    numbers = [line.rstrip() for line in file]

power = 0
number = 1
numbers_of_3_power = []

while True:
    number = 3 ** power
    numbers_of_3_power.append(number)
    if number > 100000:
        break
    power += 1

count = 0

for x in numbers:
    if int(x) in numbers_of_3_power:
        count += 1

print(count)

def silnia(n):
    if n > 0:
        return silnia(n - 1)
    return 1

count = 0
for num in numbers:
    if len(num) == 0:
        continue
    temp = 0
    for n in num:
        temp += silnia(int(n))
    if temp == int(num):
        count += 1

print(count)