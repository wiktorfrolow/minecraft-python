
plik = open('dane_wejsciowe.txt', 'r')
linie = list(plik)

for linia in range(0,len(linie)):
    #print(linie[linia])
    for znak in linie[linia]:
        print(znak)

plik.close()


