# def podnoszenie_do_kwadratu(liczba):
#     return liczba ** 2
#
#
# def podnies_liste_do_kwadratu(lista):
#     lista_do_kwadratu = []
#     for i in range(0, len(lista)):
#         liczba_do_kwadratu = podnoszenie_do_kwadratu(lista[i])
#         lista_do_kwadratu.append(liczba_do_kwadratu)
#     return lista_do_kwadratu
#
#
# if __name__ == "__main__":
#     lista = [1, 2, 3, 4]
#     print(podnies_liste_do_kwadratu(lista))


def podnoszenie_do_kwadratu(liczba):
    return liczba ** 2


def podnies_liste_do_kwadratu(lista):
    for i in range(0, len(lista)):
        lista.podnoszenie_do_kwadratu(lista[i])


if __name__ == "__main__":
    lista = [1, 2, 4, 6]
    podnies_liste_do_kwadratu(lista)
    print(lista)
