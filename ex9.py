import random
if __name__ == "__main__":
    liczbawylosowana = random.randint(0, int(input('podaj zakres: ')))
    zbior = set()
    while True:
        print()
        print("Podaj liczbe")
        liczba = int(input())
        if liczbawylosowana == liczba:
            print("Zgadłeś liczbe")
            zbior.add(liczba)
            break
        elif liczba < liczbawylosowana:
            print("liczba podana przez ciebie jest za mała")
            zbior.add(liczba)
        elif liczba > liczbawylosowana:
            print("liczba podana przez ciebie jest za duza")
            zbior.add(liczba)
    print("liczba prób " + str(len(zbior)))