from random import randint

def generate_random_list(array_len, minimal, maximal):
    user_array = []
    for num in range(array_len):
        user_array.append(randint(minimal, maximal))
    return user_array

def znajdz_ciag(user_arr):
    temp = 1
    max_dlugosc_ciagu = 1
    liczba_w_ciagu = ''
    for num in range(len(user_arr)-1):
        if temp > max_dlugosc_ciagu:
            max_dlugosc_ciagu = temp
            liczba_w_ciagu = user_arr[num]

        if user_arr[num] == user_arr[num+1]:
            # liczba_w_ciagu = str(user_arr[num]) #to nie moze tutaj byc bo
            # jezeli pod koniec list beda chociaz dwa elementy takie same to
            # nasz program zapisuje liczbe do zmiennej
            temp += 1

        if user_arr[num] != user_arr[num+1]:
            temp = 1

    return liczba_w_ciagu, max_dlugosc_ciagu


arr = generate_random_list(10, 1, 2)

# PROBLEMATIC ARRAYS TO MY ALGHORITM
# arr = [2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2]
# arr = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
# arr = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
# arr = [2, 2, 1, 1, 1, 1, 1, 1, 2, 2]

# seq = find_sequence(arr)
# char 2, len(maximal) 8

seq = znajdz_ciag(arr)

print(f"liczba w ciagu {seq[0]}, dlugosc ciagu {seq[1]}")

#TODO szukaj ciągu geometrycznego