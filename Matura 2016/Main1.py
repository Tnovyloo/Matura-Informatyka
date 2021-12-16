file = open('dane_6_1.txt')

lista_slow = []
lista_po_szyfr = []

for slowo in file:
    lista_slow.append(slowo.rstrip("\n"))

print(lista_slow,"\n",len(lista_slow))

k = 107
litera = ord('Z') - ord('A') + 1
a = ord('A')

teskt = ""

for i in range(100):
    we = lista_slow[i] #wejsciowe slowo do algorytmu
    print(we)

    tekst = str() #string do operacji

    for j in we: #dla literki w wejsciowym slowie
        tekst += (str(chr((ord(j) - a + k)%litera + a) + ""))


    print(tekst)
    lista_po_szyfr.append(tekst)

print(lista_po_szyfr)
print(len(lista_po_szyfr))