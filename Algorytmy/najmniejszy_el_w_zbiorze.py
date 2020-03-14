def najmniejszy_element_w_zbiorze(l):
    a = l[0]
    for i in range(1, len(l)):
        if a > l[i]:
            a = l[i]
    return a


if __name__ == "__main__":
    l = [23, 32, 9, 34, 27, 5, 8]
    print(najmniejszy_element_w_zbiorze(l))
