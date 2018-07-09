def sumaelementow(lista):  # sum(lista)
    wynik = 0
    for element in lista:
        wynik += element
    return wynik


def sum_of_list_using_while_loop(lista):
    wynik2 = 0
    while element2 < len(lista):
        wynik2 += element2
    return wynik2


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    print(sumaelementow(lista))
