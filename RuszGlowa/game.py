'''
1. Możliwość wyboru liczby graczy
2. Możliwość wyboru/modyfikacji kryterium kończącego grę - np. próg punktów sprawdzany po każdej kolejce
'''


def przekroczony_limit_punktowy(players, punkty_koncowe):
    for _, punkty in players.items():
        if punkty >= punkty_koncowe:
            return True
    return False


def czytaj_liczby(count):
    liczby = []
    for i in range(0, count):
        liczby.append(input("Podaj liczbe nr" + str(i) + ":"))
    return liczby


def dodaj_punkty_dla_rundy_dla_graczy(gracze, aktualne_typy_rundy):
    for gracz_do_sprawdzenia_liczby in range(len(gracze)):
        points = 0
        wybierz_gracza = aktualne_typy_rundy[gracz_do_sprawdzenia_liczby]
        for numer_gracza, aktualne_typy_gracza in aktualne_typy_rundy.items():
            if numer_gracza != gra():
                points += len(set(wybierz_gracza)
                gracze[gracz_do_sprawdzenia_liczby] += points

                import random

    def gra():
        liczba = random.randint(1, 10)
        for i in range(3):
            odp = input("zgadnij jaka liczbe komputerek ma na mysli ")
            print("podałeś liczbe: ", odp)
            if liczba == int(odp):
                print("wygrałes")
                break
            else:
                print("nie udało ci się")


if __name__ == "__main__":
    liczba_graczy = int(input("Wpisz liczbę graczy: "))
    liczba_liczb = int(input("Wpisz ile razy chcesz zgadywać liczby: "))
    punkty_koncowe = int(input("Do ilu punktów chcesz grać: "))

    gracze = {}
    for i in range(0, liczba_graczy):
        gracze[i] = 0

    while not przekroczony_limit_punktowy(gracze, punkty_koncowe):
        aktualne_typy_rundy = {}
        for numer_gracza in gracze:
            print("Gracz nr " + str(numer_gracza))
            aktualne_typy_rundy[numer_gracza] = czytaj_liczby(liczba_liczb)
        dodaj_punkty_dla_rundy_dla_graczy(aktualne_typy_rundy=aktualne_typy_rundy, gracze=gracze)
