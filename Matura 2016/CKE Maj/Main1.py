def cesar_code_exercise1(data):
    changed_data = []
    k = 107
    alphabet_len = ord('Z') - ord('A') + 1 # Długość alfabetu
    a = ord('A') # Liczba 65
    for word in data: # Dla słowa w pliku
        text = str() # Tworzymy zmienna do przechowywania tekstu
        for char in word:
            text += (str(chr((ord(char) - a + k)%alphabet_len + a) + "")) # zmienamy liczbe ord(char) - a czyli 65 w ascii + dodajemy klucz i bierzemy reszte z dzielenia przez 26 (dlugosc alfabetu) i zmieniamy ta wartosc na liczbe w ascii
        changed_data.append(text)
    return changed_data

def cesar_code_exercise2(data):
    changed_data = []
    print(words)
    # print(keys)

    char = ord('Z') - ord('A') + 1 # = 25 - len of alphabet
    a = ord('A') # = 65 - ASCII of A
    for line in data:
        if len(line.split(' ')) == 1:
            continue
        else:
            word = line.split(' ')[0]
            k = int(line.split(' ')[1])
            text = str()
            for j in word:          #ord ((j) - 65 - k) % 26 + 65
                text += (str(chr((ord(j)-a-k)%char+a) + ""))
            changed_data.append(text)
    return changed_data

def cesar_code_exercise3(data):
    changed_data = []
    for line in data:
        boolean = False
        if len(line.split(' ')) == 1:
            continue
        else:
            word = line.split(' ')[0]
            word_coded = line.split(' ')[1]
            for k in range(0, 26): # in range of alphabet
                result = ''
                for i in word:
                    #Code word for specific 'k' ,'k' is specific letter on alphabet
                    result += chr(((ord(i)-65+k)%26)+65)
                if result == word_coded:
                    boolean = True
            if not boolean:
                changed_data.append(word)
    return changed_data

with open('dane_6_1.txt', 'r') as file:
    words = [line.rstrip() for line in file.readlines()]
    zad1 = cesar_code_exercise1(words)
    print(zad1)

with open('dane_6_2.txt', 'r') as file:
    words = [line.rstrip() for line in file.readlines()]
    zad2 = cesar_code_exercise2(words)
    print(zad2)

with open('dane_6_3.txt', 'r') as file:
    words = [line.rstrip() for line in file.readlines()]
    zad3 = cesar_code_exercise3(words)
    print(zad3)