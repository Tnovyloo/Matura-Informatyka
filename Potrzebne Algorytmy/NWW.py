def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    else:
        return a

def nww(a, b):
    return a * b // nwd(a, b)

print(nww(10, 5))

