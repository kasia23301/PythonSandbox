import random
if __name__ == "__main__":
    liczbawylosowana = random.randint(0, int(input('podaj zakres: ')))
    zbior = []
    while True:
        print()
        print("Podaj liczbe")
        liczba = int(input())
        if liczbawylosowana == liczba:
            print("Zgadłeś liczbe")
            if liczba not in zbior:
                zbior.append(liczba)
            break
        elif liczba < liczbawylosowana:
            print("liczba podana przez ciebie jest za mała")
            if liczba not in zbior:
                zbior.append(liczba)
        elif liczba > liczbawylosowana:
            print("liczba podana przez ciebie jest za duza")
            if liczba not in zbior:
                zbior.append(liczba)
    print("liczba prób " + str(len(zbior)))