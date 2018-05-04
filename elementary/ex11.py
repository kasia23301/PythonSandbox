if __name__ == "__main__":
    lista_wynikow = []
    for i in range(1, 1000000):
        if i % 2 == 0:
            wynik = (-1/(2*i-1))
            lista_wynikow.append(wynik)
        else:
            wynik2 = (1/(2*i-1))
            lista_wynikow.append(wynik2)
    print(sum(lista_wynikow) * 4)
