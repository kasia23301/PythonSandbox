def co_cztredzieste_slowo(list):
    return list[39: 1000: 40]

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