if __name__ == "__main__":
    a = input("Podaj numer pesel: " )
    pesel_list = list(map(int, list(a)))
    if len(pesel_list) != 11:
        print("Zły rozmiar wprowadzonego peselu")
    else:
        suma_iloczynow = str(
        (pesel_list[0] * 1) + (pesel_list[1] * 3) + (pesel_list[2] * 7) + (pesel_list[3] * 9) + (pesel_list[4] * 1) + (
        pesel_list[5] * 3) + (pesel_list[6] * 7) + (pesel_list[7] * 9) + (pesel_list[8] * 1) + (pesel_list[9] * 3) + (
        pesel_list[10] * 1))
        sprawdzenie = list(map(int, list(suma_iloczynow)))
        if sprawdzenie[-1] == 0:
            print("Pesel jest poprawny")
        else:
            print("Pesel niepoprawny")

