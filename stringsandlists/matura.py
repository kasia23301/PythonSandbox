if __name__ == "__main__":
    print("Podaj liczbe")
    zmienna = int(input())
    print("Podaj drugą liczbe")
    zmienna2 = int(input())
    print("Chcesz dodać, odjąć czy pomnożyć liczby? (wpisz suma,roznica lub iloczyn)")
    dzialanie = str(input())
    while dzialanie == "suma" or dzialanie == "roznica" or dzialanie == "iloczyn":
        if dzialanie == "suma":
            wynik = zmienna + zmienna2
            print("Wynik dodawania tych liczb to " + str(wynik))
        elif dzialanie == "roznica":
            wynik2 = zmienna - zmienna2
            print("Wynik odejmowania tych liczb to " + str(wynik2))
        elif dzialanie == "iloczyn":
            wynik3 = zmienna*zmienna2
            print("Wynik mnożenia tych liczb to " + str(wynik3))