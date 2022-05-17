with open('liczby.txt', 'r') as file:
    numbers = [line.rstrip() for line in file]

with open('pierwsze.txt', 'r') as file:
    primes = [line.rstrip() for line in file]

def check_prime_number(num):
    if num == 2:
        return True
    if num % 2 == 0 or num <= 1:
        return False
    sqrt = int(num**0.5) + 1
    for i in range(3, sqrt, 2):
        if num % i == 0:
            return False
    return True

def weight_1_prime(number):
    sum_of_number = 0
    for num in number:
        sum_of_number += int(num)
    if sum_of_number < 10:
        return True
    return False

#4.1
prime_numbers = [int(number) for number in numbers if check_prime_number(int(number)) and 100 < int(number) < 5000]
print(f'4.1 - {prime_numbers}')

#4.2
reverse_primes = [int(number) for number in primes if check_prime_number(int(number[::-1]))]
print(f'4.2 - {reverse_primes}')

#4.3
weight_1_primes = [int(number) for number in primes if weight_1_prime(number)]
print(f'4.3 Length - {weight_1_primes} - Numbers - {weight_1_primes}')
