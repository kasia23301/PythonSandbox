import random
if __name__ == "__main__":
    listaKrotek = []
    listaKrotek.append(("Matuesz", 21, 1996))
    imie, wiek, _ = listaKrotek[0]
    krotka = listaKrotek[0]
    krotka[0]
    krotka[1]

    dodaneliczby = []
    komputerkoweliczby = []
    mergedDodaneLiczbyAndKomputerkoweLiczby = []
    for i in range(3):
        liczba = random.randint(1, 10)
        # print("Wylosowana liczba: " + str(liczba))
        komputerkoweliczby.append(liczba)

    for i in range(1):
        print("podaj pierwsza liczbe")
        liczba1 = input()
        dodaneliczby.append(liczba1)
        print("podaj druga liczbe")
        liczba2 = input()
        dodaneliczby.append(liczba2)
        print("podaj trzecia liczbe")
        liczba3 = input()
        dodaneliczby.append(liczba3)
        print(komputerkoweliczby)
        print(dodaneliczby)
        print(set(komputerkoweliczby))
        print(set(dodaneliczby))
        print(set(komputerkoweliczby) & set(dodaneliczby))
        if len(set(komputerkoweliczby) & set(dodaneliczby)) == 3:
            print("Brawo, udało Ci się. Wygrałeś 10zł ")
        else:
            print("Niestety nie udało Ci się")

