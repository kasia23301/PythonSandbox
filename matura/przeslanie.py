def co_cztredzieste_slowo(list):
    l = []
    for elem in list[39: 1000: 40]:
        l.append(elem)
    return l


def co_dziesiata_litera(l):
    result = []
    for elem in l:
        result.append(elem[9])
    return result


if __name__ == "__main__":
    f = open("sygnaly.txt", "r")
    list = []
    for line in f:
        list.append(line)
    a = co_cztredzieste_slowo(list)
    wynik = co_dziesiata_litera(a)
    print(wynik)
