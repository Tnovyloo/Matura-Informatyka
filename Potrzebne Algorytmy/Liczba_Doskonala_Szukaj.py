def divisors(n):
    number = n
    divs = []
    for x in range(n+1):
        if x != 0 and x != n:
            if n % x == 0:
                divs.append(x)
        else:
            continue
    return divs

def check_ideal(n):
    temp_list = divisors(n)
    if sum(temp_list) == n and sum(temp_list) != 0:
        return n
    else:
        return None

def range_of_user(n):
    main_list = []
    for x in range(n+1):
        y = check_ideal(x)
        if y is not None:
            main_list.append(x)
    return main_list

print(range_of_user(10000))