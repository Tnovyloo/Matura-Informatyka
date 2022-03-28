def palindrom(slowo):
    # for i in range(len(slowo)):
    #     if slowo[i] == slowo[abs(i)]:
    if len(slowo) == 1 or 0:
        return print(f"Jest palindromem")
    if slowo[0] == slowo[-1]:
        return palindrom(slowo[1:-1])
    else:
        return print(f"Nie jest palindromem")

palindrom('kajak')

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

check_palindrome('kajak')