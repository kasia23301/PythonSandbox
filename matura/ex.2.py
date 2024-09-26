if __name__ == "__main__":
    wynik = 0
    n = 36789
    while n != 0:
        wynik = wynik + (n % 10)
        n = n // 10
    print(wynik)