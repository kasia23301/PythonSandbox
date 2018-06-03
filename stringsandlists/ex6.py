if __name__ == "__main__":
    print("Podaj palindrom")
    dlugosc = 0
    liczba = 0
    plik = open("alfabet.txt")
    slowo = plik.readline()
    while slowo:
        slowo = slowo.rstrip()
        j = -1
        for i in range(len(slowo) / 2):
            if slowo[i] != slowo[j]:
                break
            j -= 1
        else:
            print(slowo)
            liczba += 1
        if len(slowo) > dlugosc:
            dlugosc = len(slowo)
            licznik = 1

    slowo = plik.readline()
