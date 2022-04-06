with open('punkty.txt', 'r') as file:
    data_file = [line.rstrip().split() for line in file]

print(data_file)

def prime_number(number):
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False
    pierw = int(number**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if number % dzielnik == 0:
            return False
    return True

def anagram(numbers):
    word1_list = [char for char in numbers[0]]
    word2_list = [char for char in numbers[1]]
    if set(word1_list) == set(word2_list):
        return True
    return False

def find_primes(data):
    primes = []
    for numbers in data:
        if prime_number(int(numbers[0])) and prime_number(int(numbers[1])):
            primes.append(numbers)
    return primes

def find_anagrams(data):
    anagrams = [numbers for numbers in data if anagram(numbers)]
    return anagrams

#4.1
print(len(find_primes(data_file)))
#4.2
print(len(find_anagrams(data_file)))
