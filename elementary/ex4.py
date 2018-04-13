def myrange(start, end):
    while start < end:
        yield start
        start += 1


if __name__ == "__main__":
    print("Podaj liczbę")
    liczba = int(input())
    suma = 0
    licznik = 1
    while licznik <= liczba:
        suma = suma + licznik
        licznik += 1
    print(str(suma))

    print("Podaj liczbę")
    liczba = int(input())
    suma = 0
    while 1 <= liczba:
        suma = suma + liczba
        liczba -= 1
    print(str(suma))

    liczba = int(input("Podaj liczbę"))
    print(sum(range(1, liczba + 1)))
