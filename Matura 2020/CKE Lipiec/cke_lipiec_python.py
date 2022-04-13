with open('identyfikator.txt') as file:
    id_list = [line.rstrip() for line in file]

def sum_number(n):
    result = 0
    for i in n:
        result += int(i)
    return result

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def count_numbers_in_id(list_of_id):
    numbers_list = [number[3:] for number in list_of_id]
    sum_numbers_list = [sum_number(number) for number in numbers_list]
    maximal = max(sum_numbers_list)

    for num, element in enumerate(sum_numbers_list):
        if element == maximal:
            print(list_of_id[num])

def check_palindrome_in_list(list_of_id):
    numbers_list = [number for number in list_of_id if check_palindrome(number[3:])]
    word_list = [word for word in list_of_id if check_palindrome(word[:3])]

    print(numbers_list)
    print(word_list)

def check_control_number(number):
    # print(ord('A') - 55, ord('Z') - 55)
    weight = (7, 3, 1, 7, 3, 1, 7, 3)
    control_number = number[3]
    text = number[:3]
    numbers = number[4:]
    result = 0
    actual_multiplier = 0

    for iterator, char in enumerate(text):
        result += int(ord(char) - 55) * weight[iterator]
        actual_multiplier = iterator

    for iterator, number in enumerate(numbers, start=actual_multiplier+1):
        result += int(number) * weight[iterator]

    result = result % 10
    if int(control_number) == int(result):
        return True
    else:
        return False

def run_control_algorithm(list_of_id):
    invalid_id = [line for line in list_of_id if not check_control_number(line)]
    print(invalid_id)

count_numbers_in_id(id_list)
check_palindrome_in_list(id_list)
# print(check_control_number('CIS459437'))
run_control_algorithm(id_list)

with open('odpowiedzi', 'a') as file:
    file.write(f"1\n{count_numbers_in_id(id_list)}"
               f"2\n{check_palindrome_in_list(id_list)}"
               f"3\n{run_control_algorithm(id_list)}")
