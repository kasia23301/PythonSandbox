def rozklad_na_czynniki(liczba):
    k = 2
    result = []
    while liczba != 1:
        while liczba % k == 0:
            result.append(k)
            liczba = liczba // k
        k += 1
    return result


if __name__ == "__main__":
    print(rozklad_na_czynniki(20))
