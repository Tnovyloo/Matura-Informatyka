def anagram(word1, word2):
    print(f"Długość słowa pierwszego {len(word1)},\n"
          f"Długość słowa drugiego {len(word2)}.")
    if len(word1) == len(word2):
        templist = []
        templist2 = []
        for char in word1:
            templist.append(str(char).lower())
        for char in word2:
            templist2.append(str(char).lower())
        if sorted(templist) == sorted(templist2):
            return print(f'{word1} == {word2}')
    else:
        return print('Słowa mają inną długość')

var1 = input(f"Podaj słowo pierwsze: ")
var2 = input(f"Podaj słowo drugie: ")
anagram(var1, var2)