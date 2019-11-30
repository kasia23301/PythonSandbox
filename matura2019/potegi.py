def a(ele):
    for n in range(0, 11):
        if ele == 3 ** n:
            return True
    return False


if __name__ == "__main__":
    f = open("liczby.txt", "r")
    list = []
    for line in f:
        list.append(int(line))
    result = 0
    for elem in list:
        if a(elem) == True:
            result += 1
    print("Wynikiem to: " + str(result))
