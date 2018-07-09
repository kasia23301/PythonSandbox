def funkszyn_największy_element(lista):
    najwiekszy_element = lista[0]
    for element in lista:
        if element > najwiekszy_element:
            najwiekszy_element = element
    return najwiekszy_element


if __name__ == "__main__":
    lista = [2, 3, 5, 7, 4]
    print(funkszyn_największy_element(lista))
