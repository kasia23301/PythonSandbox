# def czy_zawiera(element_dosprawdzenia ,  lista ):
#     if element_dosprawdzenia in lista:
#         return True
#     # if element_dosprawdzenia not in lista:
#     return False
#
# if __name__ == "__main__":
#     lista = [1, 2, 3, 4, 8, 9, 12, 16, 14]
#     element_dosprawdzenia = 20
#     print(czy_zawiera(element_dosprawdzenia, lista))
#     print(lista[::2])


def czy_zawiera(element_do_sprawdzenia, lista):
    for element in lista:
        if element_do_sprawdzenia == element:
            return True
    return False


if __name__ == "__main__":
    lista = [1, 35, 7, 8, 4, 23, 9]
    element_do_sprawdzenia = 23
    print(czy_zawiera(element_do_sprawdzenia, lista))
