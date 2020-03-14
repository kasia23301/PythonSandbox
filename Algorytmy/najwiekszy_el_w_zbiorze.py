def najwiekszy_element_w_zbiorze(l):
    a = l[0]
    for i in range(1, len(l)):
        if a < l[i]:
            a = l[i]
    return a


if __name__ == "__main__":
    l = [65, 76, 3, 12, 30]
    print(najwiekszy_element_w_zbiorze(l))
