with open('tj.txt', 'r') as file:
    tekst_jawny = [line.rstrip() for line in file.readlines()]

with open('klucze1.txt','r') as file:
    klucze1 = [line.rstrip() for line in file.readlines()]

with open('klucze2.txt') as file:
    klucze2 =[line.rstrip() for line in file.readlines()]

with open('sz.txt', 'r') as file:
    tekst_zaszyfrowany = [line.rstrip() for line in file.readlines()]

print(tekst_jawny)
print(klucze1)

def szyfruj(words_lines, keys):
    # zip_iterator = zip(text, keys)
    # temp_dict = dict(zip_iterator)
    # temp_list = []
    # for text, key in temp_dict.items():
    #     for char in range(len(text)):
    #         new_char = ord(text) + ord()
    templist = [] #Lista do zwrocenia
    for text in range(len(words_lines)): # Tekst to ilosc wyrazow
        code = '' # aktualny zaszyfrowany tekst
        pivot = 0 # zmienna ktorą sprawdzana jest dlugosc klucza
        for char in range(len(words_lines[text])): # dla znaku w dlugosci wyrazu
            char_ascii = ord(words_lines[text][char]) # znak w ASCII
            num_key = ord(keys[text][pivot]) - 64 # numer alfabetyczny
            pivot += 1 # zwiekszamy zmienna do sprawdzania dlugosci klucza
            if pivot == len(keys[text]):
                pivot = 0 # jesli pivot jest wiekszy od dlugosci klucza to zacznij od nowa
            new_ascii = char_ascii + num_key # nowy znak z ascii
            if new_ascii > 90:
                new_ascii -= 26 # jesli ascii jest wieksze od 90 to odejmij 26
            code += chr(new_ascii) # dodaj nowy znak do szyfrowanej zmiennej
        templist.append(code) #dodaj caly wyraz
    return templist

def deszyfruj(words_lines, keys):
    templist = [] #Lista do zwrocenia
    for text in range(len(words_lines)): # Tekst to ilosc wyrazow
        uncoded = '' # aktualny deszyfrowany tekst
        pivot = 0 # zmienna ktorą sprawdzana jest dlugosc klucza
        for char in range(len(words_lines[text])): # dla znaku w dlugosci wyrazu
            char_ascii = ord(words_lines[text][char]) # znak w ASCII
            num_key = ord(keys[text][pivot]) - 64 # numer alfabetyczny
            pivot += 1 # zwiekszamy zmienna do sprawdzania dlugosci klucza
            if pivot == len(keys[text]):
                pivot = 0 # jesli pivot jest wiekszy od dlugosci klucza to zacznij od nowa
            new_ascii = char_ascii - num_key # nowy znak z ascii
            if new_ascii < 65:
                new_ascii += 26 # jesli ascii jest wieksze od 90 to odejmij 26
            uncoded += chr(new_ascii) # dodaj nowy znak do szyfrowanej zmiennej
        templist.append(uncoded) #dodaj caly wyraz
    return templist

coded = szyfruj(tekst_jawny, klucze1)
print(coded)

decrypted = deszyfruj(tekst_zaszyfrowany, klucze2)
print(decrypted)

decrypted1 = deszyfruj(coded, klucze1)
print(decrypted1)