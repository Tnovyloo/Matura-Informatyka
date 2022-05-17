with open('liczby.txt','r') as file:
    file_numbers = [line.rstrip() for line in file]

with open('pierwsze.txt','r') as file:
    file_primes = [line.rstrip() for line in file]

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

def weight_prime_number(number):
    temp_number = number
    # while temp_number >= 10:
    #     sum_of_num = 0
    #     for num in temp_number:
    #         sum_of_num += num
    #     temp_number = sum_of_num
    while int(temp_number) > 10:
        sum_of_num = 0
        for num in temp_number:
            sum_of_num += int(num)
        temp_number = sum_of_num

    sum_of_number = 0
    for num in temp_number:
        sum_of_number += int(num)
    return sum_of_number

prime_numbers = [int(number) for number in file_numbers if check_prime_number(int(number)) and 100 < int(number) < 5000]
print(prime_numbers)

reverse_primes = [int(number) for number in file_primes if check_prime_number(int(number[::-1]))]
print(reverse_primes)

weight_prime_number('1109')