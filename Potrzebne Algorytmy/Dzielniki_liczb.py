def find_divisors(n):
    divisors = []
    for x in range(n+1):
        if x != 0:
            if n % x == 0:
                divisors.append(x)
        else:
            continue
    return divisors

print(find_divisors(32))