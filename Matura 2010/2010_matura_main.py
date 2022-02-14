with open('anagram.txt', 'r') as file:
    file_lines = [line.rstrip() for line in file.readlines()]

print(file_lines)

def anagram_len(temp_list):
    """Checking if all words are in the same length"""
    word1_list = [char for char in temp_list[0]]
    word2_list = [char for char in temp_list[1]]
    word3_list = [char for char in temp_list[2]]
    word4_list = [char for char in temp_list[3]]
    word5_list = [char for char in temp_list[4]]

    if len(word1_list) == len(word2_list) == len(word3_list) == len(word4_list) == len(word5_list):
        return True
    else:
        return False

def anagram_char(temp_list):
    word1_list = [char for char in sorted(temp_list[0])]
    word2_list = [char for char in sorted(temp_list[1])]
    word3_list = [char for char in sorted(temp_list[2])]
    word4_list = [char for char in sorted(temp_list[3])]
    word5_list = [char for char in sorted(temp_list[4])]

    if word1_list == word2_list == word3_list == word4_list == word5_list:
        return True
    else:
        return False

index_list_nums = []
index_list_char = []
index = 0

for line in file_lines:
    temp_list = [word for word in line.split(' ')]
    if anagram_len(temp_list):
        index_list_nums.append(index)
    if anagram_char(temp_list):
        index_list_char.append(index)
    index += 1

print(index_list_nums)
print(index_list_char)

with open('odpowiedz_zad4', 'w') as file:
    for x in index_list_nums:
        file.writelines(f'{file_lines[x]}\n')
    file.writelines("\nodp 4.2\n")
    for x in index_list_char:
        file.writelines(f'{file_lines[x]}\n')