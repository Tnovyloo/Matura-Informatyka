from collections import Counter

with open('NAPIS.TXT', 'r') as file:
    file_lines = [line.rstrip() for line in file.readlines()]

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sum_ascii(text):
    number = 0
    for char in text:
        number += ord(char)
    if is_prime(number):
        return True

def is_ascending(text):
    for char in range(1, len(text)):
        if ord(text[char-1]) < ord(text[char]):
            return False
        return True

#4.1
primes_in_text = [line for line in file_lines if sum_ascii(line)]
print(f'5.1: {len(primes_in_text)}')

#4.2
ascending_texts = [line for line in file_lines if is_ascending(line)]
print(f'5.2: {ascending_texts}')

#4.3
count = Counter(file_lines)
most_common = count.most_common(3)
print(f'5.3: {most_common}')

