def divisors(n):
    number = n
    divisors = []
    for x in range(n+1):
        if x != 0 and x != n:
            if n % x == 0:
                divisors.append(x)
        else:
            continue
    return divisors

def ideal_number(n):
    list_of_divisors = divisors(n)
    print(f"Dzielniki liczb mniejsze od liczby '{n}'\n"
          f"{divisors(n)}")
    # print(sum(dzielniki(n)))
    if sum(list_of_divisors) == n:
        print(f"Liczba {n} jest liczbą doskonałą")
    else:
        print(f"Liczba {n} nie jest liczbą doskonałą")


ideal_number(int(input('Podaj liczbę,\nżeby sprawdzić czy jest doskonała: ')))