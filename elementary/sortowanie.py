if __name__ == "__main__":
    print("Program porzadkuje rosnaco elementy wprowadzonej przez uzytkownika listy ")
    lista = []
    dlugosc_listy = int(input("Podaj dlugosc listy: "))
    i = 0
    while i < dlugosc_listy:
        a = 1
        element_listy = input("Podaj element listy: ")
        lista.append(element_listy)
        i += 1
    posortowane = sorted(lista)
    print(posortowane)


