# def suma_elementow_listy(lista):
#     wynik2 = 0
#     while element2 < len(lista):
#         wynik2 += element2
#     return wynik2
#
def suma_el(lista2):
    wynik = 0
    for element in lista2:
        wynik += element
    return wynik

def Suma_elem(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + Suma_elem(lista[1:])





if __name__ == "__main__":
    listaa = [1,2,3,4,5]
    # print(suma_elementow_listy(listaa))
    print(suma_el(listaa))
    print(Suma_elem(listaa))
