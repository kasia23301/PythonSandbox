def rozklad_na_czynniki(liczba):
    i = 2
    lista_dzielnikow = []
    for j in range(liczba):
        if liczba % i == 0:
            lista_dzielnikow.append(i)
            liczba = liczba / i
            if liczba == 1:
                return lista_dzielnikow
        else:
            i += 1
    return lista_dzielnikow


def nwd(liczba1, liczba2):
    l1 = rozklad_na_czynniki(liczba1)
    l2 = rozklad_na_czynniki(liczba2)
    l3 = []
    for elem in l1:
        if elem in l2:
            l3.append(elem)
    result = 1
    for i in l3:
        result = result * i
    return result


def nwd_2(l1, l2):
    for i in range(l1, 0, -1):
        if l1 % i == 0 and l2 % i == 0:
            return i


def longest_seq(ciag):
    sequences = []
    for start in range(len(ciag)):
        nwd = ciag[start]
        s = [nwd]
        for e in ciag[(start + 1):]:
            res = nwd_2(nwd, e)
            if res == 1:
                break
            else:
                nwd = res
                s.append(e)
        sequences.append({"seq": s, "nwd": nwd})
    return sequences


if __name__ == "__main__":
    f = open("liczby.txt", "r")
    list = []
    for line in f:
        list.append(int(line))
    res = longest_seq(list)

    longest = {'seq': []}
    for e in res:
        if len(e['seq']) > len(longest['seq']):
            longest = e
    print(longest['seq'][0])
    print(len(longest['seq']))
    print(longest['nwd'])



    # f = open("liczby.txt", "r")
    # list = []
    # result = []
    # b = []
    # for line in f:
    #     list.append(int(line))
    # for elem in list:
    #     for i in range(0, 99604):
    #         a = nwd(elem, list[i + 1])
    #         if a != 1:
    #             b.append(elem)
    #             b.append(list[i + 1])
    #             for ele in list:
    #                 if a == nwd(a, list[i + 2]):
    #                     b.append(list[i + 2])
    #                 result.append(b)
    # print(result)
