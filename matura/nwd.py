# def nwd_dwoch_liczb(liczba1, liczba2):

def rozklad_na_czynniki(liczba):
    for i in range(2, liczba + 1):
        lista_dzielnikow = []
        if liczba % i == 0:
            lista_dzielnikow.append(i)
            liczba = liczba // i
        if liczba == 1:
            return lista_dzielnikow


if __name__ == "__main__":
    print(rozklad_na_czynniki(10))
