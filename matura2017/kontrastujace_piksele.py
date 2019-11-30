def kontrastujace_piksele(row1, row2):
    k_p = 0
    for i in range(0, len(row1) - 1):
        if abs(row1[i] - row1[i+1]) > 128 or abs(row1[i] - row2[i]) > 128:
            k_p += 1
    return k_p

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
    wynik = []
    for row in range(0, len(matrix) -1):
        wynik.append(kontrastujace_piksele(matrix[row], matrix[row+1]))
    print(sum(wynik))


