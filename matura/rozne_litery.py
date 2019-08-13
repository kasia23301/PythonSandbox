def zbior(list):
    result = []
    for elem in list:
        l = []
        a = set(elem)
        b = (len(a))
        l.append(a)
        l.append(b)
        result.append(l)
    return result

def najdluzsze_slowo(list):
    return max(list)

if __name__ == "__main__":
    f = open("sygnaly.txt", "r")
    list = []
    for line in f:
        list.append(line.rstrip("\n"))
    a = zbior(list)
    print(a)
