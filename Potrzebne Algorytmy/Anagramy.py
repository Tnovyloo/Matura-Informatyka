def anagram(slowo1, slowo2):
    print(f"Długość słowa pierwszego {len(slowo1)},\n"
          f"Długość słowa drugiego {len(slowo2)}.")
    if len(slowo1) == len(slowo2):
        templist = []
        templist2 = []
        for char in slowo1:
            templist.append(str(char).lower())
        for char in slowo2:
            templist2.append(str(char).lower())
        if sorted(templist) == sorted(templist2):
            return print(f'{slowo1} == {slowo2}')
    else:
        return print('Słowa mają inną długość')

var1 = input(f"Podaj słowo pierwsze: ")
var2 = input(f"Podaj słowo drugie: ")
anagram(var1, var2)