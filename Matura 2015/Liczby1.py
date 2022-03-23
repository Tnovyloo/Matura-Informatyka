with open('liczby.txt', 'r') as file:
    binary_numbers = [number.rstrip() for number in file.readlines()]

def count_numbers(numbers):
    temp_list = []
    for number in numbers:
        count_one = 0
        count_zero = 0
        for char in number:
            if char == '1':
                count_one += 1
            else:
                count_zero += 1
        if count_zero > count_one:
            temp_list.append(number)
    return temp_list

print(len(count_numbers(binary_numbers)))

def check_divisors(numbers):
    temp_list = [int(num, 2) for num in numbers]
    list_of_two = []
    list_of_eight = []
    for number in temp_list:
        if number % 2 == 0:
            list_of_two.append(number)
        if number % 8 == 0:
            list_of_eight.append(number)
    return len(list_of_two), len(list_of_eight)

print(check_divisors(binary_numbers))

def find_max_and_min(numbers):
    temp_list = [int(num, 2) for num in numbers]
    return temp_list.index(min(temp_list)) + 1, temp_list.index(max(temp_list)) + 1

print(find_max_and_min(binary_numbers))