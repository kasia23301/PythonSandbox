def polaczone_na_zmiane(lista1, lista2):
    lista_polaczona=[]
    for element1, element2 in zip(lista1, lista2):
        print(str(element1) + ' - ' + str(element2))

# def polacz_na_miane(lista1, lista2):
#     lista_z_elementami = []
#     # for element in lista1:
#     #     lista_z_elementami.append(element)
#     # for element in lista2:
#     #     lista_z_elementami.append(element)
#     for i in range(0, len(lista1)):
#         lista_z_elementami.append(i[0])
#     i += 1
#     for i in range(0, len(lista2)):
#         lista_z_elementami.append(i[0])
#     i += 1
#     return lista_z_elementami


if __name__ == "__main__":
    lista1 = [1, 3, 5, 7, 9, 11]
    lista2 = [2, 4, 6, 8, 10, 12]
    polaczone_na_zmiane(lista1, lista2)
    # polacz_na_miane(lista1, lista2)
