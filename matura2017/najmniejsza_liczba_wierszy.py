def is_row_valid(row):
    for l_i in range(0, len(row) - 1):
        r_i = len(row) - 1 - l_i
        if row[l_i] != row[r_i]:
            return False
    return True

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
    num_of_elems_to_remove = 0
    for row in matrix:
        if not is_row_valid(row):
            num_of_elems_to_remove += 1
    print(num_of_elems_to_remove)




