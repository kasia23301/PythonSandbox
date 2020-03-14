if __name__ == "__main__":
    l = [5, 7, 3, 4, 9, 12, 67, 54, 234, 43]
    for i in range(len(l) - 1, 0, -1):
        for a in range(i):
            if l[a] > l[a + 1]:
                l[a], l[a + 1] = l[a + 1], l[a]
    print(l)