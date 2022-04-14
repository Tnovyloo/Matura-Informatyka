from math import sqrt

with open('punkty.txt', 'r') as file:
    data_file = [line.rstrip().split() for line in file]

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

def distance_of_points(a, b):
    distance = round(sqrt((pow(int(b[0]) - int(a[0]), 2) + pow(int(b[1]) - int(a[1]), 2))), 0)
    return distance

#4.1
def find_primes(data):
    primes = []
    for numbers in data:
        if prime_number(int(numbers[0])) and prime_number(int(numbers[1])):
            primes.append(numbers)
    return primes

#4.2
def find_anagrams(data):
    anagrams = [numbers for numbers in data if anagram(numbers)]
    return anagrams

#4.3
def find_longest_distance(data):
    maximal_distance = 0
    p1 = []
    p2 = []
    for point_a in data:
        for point_b in data:
            difference = distance_of_points(point_a, point_b)
            if difference > maximal_distance:
                maximal_distance = difference
                if not p1 and not p2:
                    p1.append(point_a)
                    p2.append(point_b)
                else:
                    p1.clear()
                    p2.clear()
                    p1.append(point_a)
                    p2.append(point_b)
    return p1, p2, maximal_distance

#4.4
def check_points_in_square(data):
    interior = 0
    exterior = 0
    on_border = 0
    for point in data:
        if int(point[0]) < 5000 and int(point[1]) < 5000:
            interior += 1
        if int(point[0]) > 5000 or int(point[1]) > 5000:
            exterior += 1
        if int(point[0]) == 5000 or int(point[1]) == 5000:
            on_border += 1
    return f'In square {interior}\nOut of square {exterior}\nOn border {on_border} '

#4.1
print(len(find_primes(data_file)))
#4.2
print(len(find_anagrams(data_file)))
#4.3
print(find_longest_distance(data_file))
#4.4
print(check_points_in_square(data_file))

with open('odpowiedz','a') as file:
    file.write(f'4.1 {len(find_primes(data_file))}\n'
               f'4.2 {len(find_anagrams(data_file))}\n'
               f'4.3 {find_longest_distance(data_file)}\n'
               f'4.4 {check_points_in_square(data_file)}\n')