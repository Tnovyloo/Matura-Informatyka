
def lucky_numbers(n, lucktab):
    for number in lucktab:
        if n == number:
            return True
    return False

def create_luckyTab():
    temp = 0 # Zmienna aktualnej szczesliwej liczby
    lucky_tab = [] # Tablica przechowujaca szczesliwe numery
    lucky_tab_current = [] # Pomocniczna tablica
    for i in range(1, 10001): #Tworzymy tablice z nieparzystymi liczbami
        if i % 2 != 0:
            lucky_tab.append(i)

    temp += 1

    new_lucky_number = lucky_tab[temp] # Przypisujemy do zmiennej liczbe

    while new_lucky_number < len(lucky_tab): # Dopoki zmienna nie bedzie mniejsza od luckytab
        for i in range(0, len(lucky_tab)): # Petla rowna dlugosci listy
            if (i+1) % new_lucky_number != 0: # Wrzucamy do pomocniczej liczby zmienne spod indeksow
                lucky_tab_current.append(lucky_tab[i])

        lucky_tab = [x for x in lucky_tab_current] # Podmieniamy aktulana tablice na nową
        lucky_tab_current.clear()
        temp += 1 # Zwiekszamy zmienna
        # print(lucky_tab)
        new_lucky_number = lucky_tab[temp]

    return lucky_tab



with open('dane.txt', 'r') as file:
    count = 0
    numbers = create_luckyTab()
    temp_list = []
    maximal = 0
    length = 0
    for line in file:
        if lucky_numbers(int(line), numbers):
            temp_list.append(line)
            maximal += 1
            count += 1
            if length > maximal:
                maximal = length
                pierwsza = temp_list[0]
        else:
            temp_list.clear()
            length = 0

print("4.1 zadanie: ", count)
print("4.2 zadanie: ", maximal, pierwsza)
