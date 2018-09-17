if __name__ == '__main__':
    n = 11111111
    wynik = 0
    while n != 0:
        wynik = wynik + (n % 10)
        n = n // 10
    print(wynik)
