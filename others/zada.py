if __name__ == "__main__":
    a = int(input("Podaj dlugosc boku trójkąta, z krórego poprowadzona będzie wysokość: "))
    b = int(input("Podaj długość drugiego boku: "))
    c = int(input("Podaj długość trzeciego boku: "))
    h = int(input("Podaj wysokość trójkąta: "))
    if a+b>c and a+c>b and b+c>a:
        pole = 0.5*a*h
        print("Pole tego trójkąta wynosi: " + str(pole))
    else:
        print("Taki trójkąt nie istnieje")


