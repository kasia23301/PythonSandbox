def dlugosc_slowa(slowo):
    b = []
    for elem in slowo:
        if elem not in b:
            b.append(elem)
    return len(b)


if __name__ == "__main__":
    f = open("sygnaly.txt", "r")
    list = f.read().splitlines()
    list_with_length = []
    for elem in list:
        list_with_length.append(dlugosc_slowa(elem[:-1]))
    r = list_with_length.index(max(list_with_length))
    print(str(list[r]) + '\n' + str(max(list_with_length)))
