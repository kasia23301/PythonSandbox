def ilosc_jedynek(liczba):
    ilosc_j = 0
    for el in liczba:
        if str(el) == "1":
            ilosc_j += 1
    return ilosc_j


def ilosc_zer(liczba):
    ilosc_z = 0
    for e in liczba:
        if str(e) == "0":
            ilosc_z += 1
    return ilosc_z


if __name__ == "__main__":
    f = open("liczby.txt", "r")
    numbers = []
    for line in f:
        numbers.append(line)
    result = 0
    for elem in numbers:
        if ilosc_zer(elem) > ilosc_jedynek(elem):
            result += 1
    print(result)
