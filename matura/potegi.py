def a(ele):
    for n in range(0, 10):
        if ele == 3 ** n:
            return True
    return False


if __name__ == "__main__":
    with open("liczby.txt", "r") as f:
        list = []
        for line in f:
            list.append(line)
    result = []
    for elem in list:
        res = a(elem)
        result.append(res)
    for el in result:
        if el == "True":
            print(el)
