if __name__ == "__main__":
    f = open("dane.txt", "r")
    lista = []
    for line in f:
        lista.append(list(line.rstrip("\n").split(" ")))
    new_list = []
    for elem in lista:
        for e in elem:
            new_list.append(int(e))
    print("Najjasniejszy piksel: " + str(max(new_list)))
    print("Najciemniejszy piksel: " + str(min(new_list)))

