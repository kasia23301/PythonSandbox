def k(n):
    wynik = 0
    if n < 4:
        wynik = 1
    if n >= 4:
        wynik = k(n - 1) - k(n - 3)
    return wynik


if __name__ == "__main__":
    list = []
    a = int(input("Podaj liczbe elemntow "))
    for i in range(0, a):
        result = k(i)
        list.append(result)
    print(list)



