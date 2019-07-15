def a(ele):
    for n in range(0, 10):
        if ele == 3 ** n:
            return True
    return False


if __name__ == "__main__":
    print(a(949))
    f = open("liczby.txt", "r")
    list = []
    for line in f:
        list.append(int(line))
    for elem in list:
        print(a(elem))
    result = []
    for elem in list:
        res = a(elem)
        result.append(res)
    a = []
    for i in result:
        if str(i) == "True":
            a.append(i)
    print(len(a))