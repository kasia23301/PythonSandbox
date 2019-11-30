def zbior(list):
    result = []
    for elem in list:
        l = []
        l.append(elem)
        l.append(len(set(elem)))
        result.append(l)
    return result


def najdluzsze_slowo(list):
    return max(list, key=lambda x: x[1])


def old_najdluzsze_slowo(list_a):
    k = map(lambda x: x[1], list_a)
    a = list(k)
    max_slowo = None
    max_len = -1
    for elem in list_a:
        if elem[1] > max_len:
            max_slowo = elem[0]
            max_len = elem[1]
    return max_slowo, max_len


