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
    list = [12, 4, 5, 7]
    for elem in list:
