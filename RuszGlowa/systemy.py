if __name__ == "__main__":
    lista = []
    wprowadzona_liczba = input("Podaj liczbe w systemie dziesietnym: ")
    while int(wprowadzona_liczba) > 0:
        reszta_z_dzielenia = int(wprowadzona_liczba) % 2
        lista.append(reszta_z_dzielenia)
        wprowadzona_liczba = int(wprowadzona_liczba) / 2
    lista.reverse()
    print(lista)


