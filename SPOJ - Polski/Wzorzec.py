tekst = input("Podaj tekst: ")
wzorzec = input("Podaj wzorzec: ")

dl_t = len(tekst)
dl_w = len(wzorzec)

dlr = dl_t - dl_w

for i in range(dlr):
    ok = 1

    for j in range(dl_w):
        if tekst[j + i] != tekst[j]:
            ok = 0
            break

    if ok == 1:
        print(f"Znaleziono wzorzec pocztek na pozycji {i + 1}")