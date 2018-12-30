if __name__ == "__main__":
    podana_liczba = int(input("Podaj liczbe"))
    lista_czynnikow = []
    while podana_liczba > 1:
        dzielnik = 2
        if podana_liczba % dzielnik == 0 and dzielnik <= podana_liczba:
            czynnik = podana_liczba / dzielnik
            lista_czynnikow.append(czynnik)
        elif podana_liczba % dzielnik != 0:
            dzielnik += 1
    else:
        print(lista_czynnikow)
