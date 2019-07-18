def rozklad_na_czynniki(liczba):
    i = 2
    lista_dzielnikow = []
    for j in range(liczba):
        if liczba % i == 0:
            lista_dzielnikow.append(i)
            liczba = liczba / i
            if liczba == 1:
                return lista_dzielnikow
        else:
            i += 1
    return lista_dzielnikow


def nwd(liczba1, liczba2):
    l1 = rozklad_na_czynniki(liczba1)
    l2 = rozklad_na_czynniki(liczba2)
    l3 = []
    for elem in l1:
        if elem in l2:
            l3.append(elem)
    result = 1
    for i in l3:
        result = result * i
    return result


if __name__ == "__main__":
    f = open("liczby.txt", "r")
    list = []
    result = []
    b = []
    for line in f:
        list.append(int(line))
    for elem in list:
        i = elem
        a = nwd(elem, list[i + 1])
        if a != 1:
            b.append(elem)
            b.append(list[i + 1])
            for ele in list:
                if a == nwd(a, list[i + 2]):
                    b.append(list[i + 2])
                result.append(b)
    print(b)
