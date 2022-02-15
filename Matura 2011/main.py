with open('liczby.txt','r') as file:
    file_lines = [line.rstrip() for line in file.readlines()]


def check_even(num):
    if num % 2 == 0:
        return True

def prime_number(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def perfect_number(num):
    dividers = []
    for i in range(1, num):
        if num % i == 0:
            dividers.append(i)
        else:
            continue
    if sum(dividers) == num:
        return True
    else:
        return False

numbers = [int(number, 2) for number in file_lines]
print(numbers)

even_numbers = [num for num in numbers if check_even(num)]
print(even_numbers)

prime_numbers = [num for num in numbers if prime_number(num)]
print(prime_numbers)

perfect_numbers = [num for num in numbers if perfect_number(num)]
print(perfect_numbers)

nine_len_numbers = [num for num in numbers if len(str(num)) == 9]

print(f'4.1 - {len(even_numbers)}\n'
      f'4.2 - {bin(max(numbers))[2:]}, {oct(max(numbers))}\n'
      f'4.3 - {bin(sum(nine_len_numbers))[2:]}\n')