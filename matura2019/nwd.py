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

