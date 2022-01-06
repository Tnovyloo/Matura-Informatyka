from random import randint

def generate_random_list(array_len, minimal, maximal):
    """Generate random list"""
    user_array = []
    for num in range(array_len):
        user_array.append(randint(minimal, maximal))
    return user_array

def find_number_sequence(user_arr):
    """Finding number sequence in list"""
    temp = 1
    max_len_sequence = 1
    number_sequence = ''
    for num in range(len(user_arr)-1):
        if temp > max_len_sequence:
            max_len_sequence = temp
            number_sequence = user_arr[num]

        if user_arr[num] == user_arr[num+1]:
            temp += 1

        if user_arr[num] != user_arr[num+1]:
            temp = 1

    return number_sequence, max_len_sequence

def find_geometrical_seq(user_arr):
    """Find geometrical sequence in list"""
    sequence = []
    for num in range(len(user_arr)-1):
        if user_arr[num] * user_arr[num] != user_arr[num-1] * user_arr[num+1]:
            continue
        else:
            sequence.append(user_arr[num])
    return sequence

def find_geometrical_seq_ver2(user_arr):
    sequence = []
    for num in range(len(user_arr)-1):
        q = user_arr[num] / user_arr[num]
        if user_arr[num + 1] / user_arr[num - 1] == q:
            sequence.append(user_arr[num])
        else:
            continue
    return sequence

arr = generate_random_list(100, 1, 10)

# PROBLEMATIC ARRAYS TO MY FIND SEQUENCE ALGHORITM
# arr = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2]
# arr = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
# arr = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
# arr = [2, 2, 1, 1, 1, 1, 1, 1, 2, 2]
#NOW IS WORKING

seq = find_number_sequence(arr)
print(f"liczba w ciagu {seq[0]}, dlugosc ciagu {seq[1]}")

geometrical_seq = find_geometrical_seq(arr)
print(geometrical_seq)

var = find_geometrical_seq_ver2(arr)
print(var)