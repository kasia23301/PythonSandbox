if __name__ == "__main__":
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    while a != b:
        if a > b:
            a = a - b
        if b > a:
            b = b - a
    print(a)

if __name__ == "__main__":
    a = int(input("Podaj 1 liczbe: "))
    b = int(input("Podaj 2 liczbe: "))
    while b != 0:
        pom = b
        b = a % b
        a = pom
    print(a)
    