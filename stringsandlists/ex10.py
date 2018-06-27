def decToBin(n):
    if n == 0: return ""
    else:
        return decToBin(n // 2) + str(n % 2)


if __name__ == "__main__":
    print("Podaj liczbę")
    liczba = int(input())
    print(decToBin(liczba))

