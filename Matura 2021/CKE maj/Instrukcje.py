from collections import Counter

with open('instrukcje.txt', 'r') as file:
    instructions_data = [line.rstrip() for line in file]

def exercise1(instructions):
    length = 0
    for var in instructions:
        if var.__contains__('DOPISZ'):
            length += 1
        if var.__contains__('USUN'):
            length -= 1
    return length

def exercise2(instructions):
    maximal = 0
    temp = 1
    text = ''
    for i in range(len(instructions)-1): #1999
        if instructions[i][0:3] == instructions[i+1][0:3]:
            temp += 1
            # text = lista[var]
        else:
            if temp > maximal:
                maximal = temp
                text = instructions[i]
            temp = 1
    return maximal, text

def exercise3(instructions):
    # letters = {}
    # for var in lista:
    #     instruction, char = var.split()
    #     if instruction == "DOPISZ":
    #         if char in letters:
    #             letters[char] += 1
    #         else:
    #             letters[char] = 1
    # most_common = None
    # common = 0
    # for litera in letters:
    #     if letters[litera] > common:
    #         most_common = litera
    #         common = letters[litera]
    # # skrócona wersja powyższego dla ciekawych:
    # # najczesciej = max(litery.items(), key=lambda x: x[1])
    # return most_common, common

    # Better solution:
    add_commands = []
    for command in instructions:
        if command.__contains__('DOPISZ'):
            add_commands.append(command)
    result = Counter(add_commands).most_common(1)
    return result

def add(text, char):
    return text + char

def delete(text):
    return text[:len(text) - 1]

def change(text, litera): #funckja zmieniajaca ostatni znak
    txt_list = list(text) #uwaga: w pythonie teksty musimy potraktowac jako liste
    txt_list[len(text) - 1] = litera #jezeli chcemy podmienic znak na danej pozycji
    return "".join(txt_list) #na koniec liste ta musimy zmienic z powrotem na tekst

def move_char(tekst, char):
    index = tekst.find(char)
    if index == -1:  # jezeli nie znalezlismy znaku, przerywamy dzialanie
        return tekst
    if char == 'Z':  # jezeli jest to ostatnia litera alfabetu, to wracamy na poczatek
        char = 'A'
    else:  # w przeciwnym przypadku przesuwamy znak o 1
        char = chr(ord(char) + 1)
    txt_list = list(tekst)  # nastepnie musimy ponownie zamienic text na liste znakow
    txt_list[index] = char  # podmienic znak
    return "".join(txt_list)  # i zwrocic ja jako ciag znakow

def exercise4(instructions):
    result = ''
    for var in instructions:
        args = var.split(" ")
        char = args[1]
        command = args[0]
        if command == "DOPISZ":
            result = add(result, char)
        if command == "ZMIEN":
            result = change(result, char)
        if command == "USUN":
            result = delete(result)
        if command == "PRZESUN":
            result = move_char(result, char)
    return result

print(exercise1(instructions_data))
print(exercise2(instructions_data))
print(exercise3(instructions_data))
print(exercise4(instructions_data))