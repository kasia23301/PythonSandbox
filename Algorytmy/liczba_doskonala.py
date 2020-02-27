def dzielniki(liczba):
    result = []
    for i in range(1, (liczba // 2) + 1):
        if liczba % i == 0:
            result.append(i)
    return result


def liczba_doskonala(liczba):
    if liczba == sum(dzielniki(liczba)):
        return True
    return False


if __name__ == "__main__":
    l = int(input("Podaj liczbe: "))
    if liczba_doskonala(l) == True:
        print("To jest liczba doskonala")
    else:
        print("To nie jest liczba doskonala")
