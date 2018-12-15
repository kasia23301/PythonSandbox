if __name__ == "__main__":
    lista = []
    dlugosc_listy = int(input("Podaj dlugosc listy: "))
    i = 0
    while i < dlugosc_listy:
        element_listy = input("Podaj element listy: ")
        lista.append(element_listy)
        i += 1

    for i in range(len(lista) - 1, 0, -1):
        for a in range(i):
            if lista[a] > lista[a+1]:
                lista[a], lista[a+1] = lista[a+1], lista[a]
    print(lista)


