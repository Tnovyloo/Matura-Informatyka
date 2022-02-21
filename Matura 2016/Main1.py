def cesar_code_exercise1(data):
    changed_data = []
    k = 107
    char = ord('Z') - ord('A') + 1
    a = ord('A')
    for word in data:
        text = str()
        for j in word:
            text += (str(chr((ord(j) - a + k)%char + a) + ""))
        changed_data.append(text)
    return changed_data

def cesar_code_exercise2(data):
    changed_data = []
    print(words)
    # print(keys)

    char = ord('Z') - ord('A') + 1 # = 27 - len of alphabet
    a = ord('A') # = 65 - ASCII of A
    for line in data:
        # print(line.split(' ')[1])
        word = line.split(' ')[0]
        k = int(line.split(' ')[1])
        text = str()
        for j in line:
            text += (str(chr((ord(j) - a - k)%char + a) + ""))
        changed_data.append(text)
    return changed_data

with open('dane_6_1.txt', 'r') as file:
    words = [line.rstrip() for line in file.readlines()]
    zad1 = cesar_code_exercise1(words)
    print(zad1)

with open('dane_6_2.txt', 'r') as file:
    words = [line.rstrip() for line in file.readlines()]
    zad2 = cesar_code_exercise2(words)
    print(zad2)