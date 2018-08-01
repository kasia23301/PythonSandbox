# if __name__ == "__main__":
#     liczba_graczy = input("Podaj liczbę graczy: ")
#     liczba_liczb = input("Podaj liczbe liczb: ")
#     print("Gramy do 30 punktów. Za każdą liczbę wspólną z liczbą innego gracza dostajesz punkt.")
#     gracz1_zbior_liczb = set()
#     gracz2_zbior_liczb = set()
#     gracz3_zbior_liczb = set()
#     for i in range((int(liczba_liczb)), 0, -1):
#         gracz1_liczba = input("Podaj liczbe gracz nr 1")
#         gracz1_zbior_liczb.append(gracz1_liczba)
#         gracz2_liczba = input("Podaj liczbe gracz nr 2")
#         gracz2_zbior_liczb.append(gracz2_liczba)
#         gracz3_liczba = input("Podaj liczbę gracz nr 3")
#         gracz3_zbior_liczb.append(gracz3_liczba)
#     print(gracz1_zbior_liczb)
#     print(gracz2_zbior_liczb)
#     print(gracz3_zbior_liczb)

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
            if numer_gracza != gracz_do_sprawdzenia_liczby:
                points += len(set(wybierz_gracza).intersection(set(aktualne_typy_gracza)))
        gracze[gracz_do_sprawdzenia_liczby] += points


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

    print(sorted(((v, k) for k, v in gracze.items()), reverse=True))
