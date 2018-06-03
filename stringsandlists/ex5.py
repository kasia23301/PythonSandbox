def sumaelementow(lista):
    element = 0
    lista2 = []
    while element in lista:
        lista2.append(element)
        element += 1
    return sum(lista2)


if __name__ == "__main__":
    lista = [1, 2, 3, 4]
    print(sumaelementow(lista))
