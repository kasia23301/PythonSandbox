def silnia(liczba):
    if liczba == 0:
        return 1
    if liczba == 1:
        return 1
    else:
        result = 1
        for i in range(1, liczba + 1):
            result = result * i
        return result


if __name__ == "__main__":
    f = open("liczby.txt", "r")
    list = []
    for line in f:
        list.append(int(line))
    for elem in list:
        result = 0
        for i in str(elem):
            i = int(i)
            result = result + silnia(i)
        if result == elem:
            print(elem)
