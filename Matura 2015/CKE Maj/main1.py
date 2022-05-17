with open('liczby.txt') as file:
    file_numbers = [line.rstrip() for line in file]

def count_zeros(numbers):
    final_numbers = []
    for number in numbers:
        count_zero = 0
        count_one = 0
        for num in number:
            if num == "0":
                count_zero += 1
            else:
                count_one += 1
        if count_zero > count_one:
            final_numbers.append(number)
    return len(final_numbers)

def count_dividors(numbers):
    list_of_two = []
    list_of_eight = []
    for number in numbers:
        int_number = int(number, 2)
        if int_number % 2 == 0:
            list_of_two.append(number)
        if int_number % 8 == 0:
            list_of_eight.append(number)
    return len(list_of_two), len(list_of_eight)

def find_max_min(numbers_file):
    numbers = [int(num,2) for num in numbers_file]
    return numbers.index(max(numbers)) + 1, numbers.index(min(numbers)) + 1

print(count_zeros(file_numbers))
print(count_dividors(file_numbers))
print(find_max_min(file_numbers))