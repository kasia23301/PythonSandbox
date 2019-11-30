

if __name__ == "__main__":
    if __name__ == "__main__":
        f = open("dane.txt", "r")
    lista = []
    for line in f:
        lista.append(list(line.rstrip("\n").split(" ")))
    matrix = []
    for elem in lista:
        new_list = []
        for e in elem:
            new_list.append(int(e))
        matrix.append(new_list)
    lista_elementow = []

