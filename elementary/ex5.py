if __name__ == "__main__":
    print("Podaj liczbę")
    liczba = int(input())
    suma = 0
    licznik = 1
    dzielnik = 3
    dzielnik2 = 5
    while licznik <= liczba:
        if licznik % dzielnik == 0 or licznik % dzielnik2 == 0:
            suma = suma + licznik
        licznik += 1
    print(str(suma))