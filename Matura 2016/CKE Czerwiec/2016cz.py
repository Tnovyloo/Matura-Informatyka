with open('liczby.txt','r') as file:
    numbers_from_file = [line.rstrip() for line in file]
    print(numbers_from_file)

def answer1(numbers):
    temp_list = [number for number in numbers if number[-1] == '8']
    return len(temp_list)

def answer2(numbers):
    temp_list = [number for number in numbers if number[-1] == '4' and not number.__contains__('0')]
    return len(temp_list)

def answer3(numbers):
    temp_list = [number for number in numbers if number[-1] == '2' and int(number[:-1], 2) % 2 == 0]
    return len(temp_list)

def answer4(numbers):
    temp_list = [int(number[:-1], 8) for number in numbers if number[-1] == '8']
    return sum(temp_list)

def answer5(numbers):
    temp_list = [(int(number[:-1], int(number[-1]))) for number in numbers]
    maximal = max(temp_list)
    minimal = min(temp_list)
    minimal_index = temp_list.index(maximal)
    maximal_index = temp_list.index(minimal)
    return maximal, numbers[maximal_index], minimal, numbers[minimal_index]


print(answer1(numbers_from_file))
print(answer2(numbers_from_file))
print(answer3(numbers_from_file))
print(answer4(numbers_from_file))
print(answer5(numbers_from_file))