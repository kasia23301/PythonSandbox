def odleglosc(elem):
    lista = index_of_elem(elem)
    for i in lista:
        for j in lista:
            if abs(j - i) > 10:
                return
    print(elem)


def index_of_elem(elem):
    a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X",
         "Y", "Z"]
    b = []
    for i in elem:
        if i in a:
            b.append(a.index(i))
    return b


if __name__ == "__main__":
    f = open("sygnaly.txt", "r")
    lista = []
    for line in f:
        lista.append(line.rstrip("\n"))
    for elem in lista:
        odleglosc(elem)
