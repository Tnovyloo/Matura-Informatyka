with open('dane.txt', 'r') as file:
    list_of_numbers = [line.rstrip() for line in file.readlines()]

print(list_of_numbers)

# 203 8 = 131 10
print(int('203', 8), int('131', 10))
#7123 8 = 3667 10
print(int('7123', 8), int('3667', 10))

def check_for_reply1(numbers):
    count = 0
    for num in numbers:
        if num[0] == num[-1]:
            count += 1
    return count

reply1 = check_for_reply1(list_of_numbers)
print(reply1)

def check_for_reply2(numbers_oct):
    count = 0
    numbers_decimal = [str(int(num, 8)) for num in numbers_oct] #Bład byl spodowdowany tym ze
    # int zamienia nam na system dziesiatkowy,
    # a ja podalem ze liczba do konwersji jest w systemie dziesiatkowym
    # a powinna byc w osemkowym (i tak jest teraz)
    for num in numbers_decimal:
        if num[0] == num[-1]:
            count += 1
    return count

reply2 = check_for_reply2(list_of_numbers)
print(reply2)

def check_if_true(number):
    for i in range(1, len(number)):
        if number[i] >= number[i - 1]:
            continue
        else:
            return False
    return True


def check_for_reply3(numbers_oct):
    numbers_decimal = [str(int(num, 8)) for num in numbers_oct]
    temp_list = [num for num in numbers_oct if check_if_true(num)]
    num_dec = [int(num, 8) for num in temp_list]
    print('************')
    length = len(num_dec)
    maximal =max(num_dec)
    minimal = min(num_dec)

    print(f'dlugosc {length}, wynik osemkowy: max {oct(maximal)[2:]}, min {oct(minimal)[2:]}')
    print(f'dlugosc {length}, wynik dziesietny: max {maximal}, min {minimal}')

    return f'dlugosc {length}, wynik osemkowy: max {oct(maximal)[2:]}, min {oct(minimal)[2:]}\ndlugosc {length}, wynik dziesietny: max {maximal}, min {minimal}'

check_for_reply3(list_of_numbers)

with open('odpowiedzi2013', 'a') as file:
    file.writelines(f"{str(check_for_reply1(list_of_numbers))}\n")
    file.writelines(f"{str(check_for_reply2(list_of_numbers))}\n")
    file.writelines(f"{str(check_for_reply3(list_of_numbers))}\n")

