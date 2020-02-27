def nwd(a, b):
    if b != 0:
        a = nwd(b, a % b)
    return a


if __name__ == "__main__":
    print(nwd(25, 8))
