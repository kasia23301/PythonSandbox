def has_not_divider(a):
    for j in range(2, a // 2 + 1):
        if a % j == 0:
            return False
    return True


if __name__ == "__main__":
    a = int(input("Podaj liczbe: "))
    result = []
    if a == 1:
        print("To nie jest liczba pierwsza")
    elif has_not_divider(a):
        print("To jest liczba pierwsza")
