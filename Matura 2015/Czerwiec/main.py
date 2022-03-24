code_dict_helper = {
    '0':10101110111010,
    '1':11101010101110,
    '2':10111010101110,
    '3':11101110101010,
    '4':10101110101110,
    '5':11101011101010,
    '6':10111011101010,
    '7':10101011101110,
    '8':11101010111010,
    '9':10111010111010
    }

with open('kody.txt','r') as file:
    numbers_from_file = [line.rstrip() for line in file]

def sum_of_odd_and_even(numbers):
    temp_list = []
    controll_numbers = []
    encrypted_numbers = []
    for number in numbers:
        # 6.1 solved problem
        sum_of_odd = 0
        sum_of_even = 0
        for i in range(1, len(number) + 1):
            if i % 2 == 0:
                sum_of_even += int(number[i-1])
            else:
                sum_of_odd += int(number[i-1])
        temp_list.append(f'{sum_of_even} {sum_of_odd}, number - {number}')
        # 6.2 solved problem
        controlled_num = (10 - (((sum_of_even * 3) + sum_of_odd) % 10)) % 10
        controll_numbers.append(f'{controlled_num} {code_dict_helper.get(str(controlled_num))}')
        # 6.3 solved problem
        encrypted_text = '11011010'
        for num in number:
            encrypted_text += str(code_dict_helper.get(str(num)))
        encrypted_text += str(code_dict_helper.get(str(controlled_num)))
        encrypted_text += '11010110'
        encrypted_numbers.append(encrypted_text)
    return temp_list, controll_numbers, encrypted_numbers

answer1, answer2, answer3 = sum_of_odd_and_even(numbers_from_file)
print(answer3)

test = '110110101010101110111010111011101010101011101011101110111010101010111010101110111010101011101010101110111011010110'
print(test == answer3[0])
