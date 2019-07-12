def k(n):
    if n < 4:
        return 1
    else:
        return k(n - 1) - k(n - 3)


if __name__ == "__main__":
    list = []
    a = int(input("Podaj liczbe elemntow "))
    for i in range(0, a):
        result = k(i)
        list.append(result)
    print(list)
