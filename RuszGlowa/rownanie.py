if __name__ == "__main__":
    a = int(input("Podaj współczynnik a równania: "))
    b = int(input("Podaj współczynnik b równania: "))
    if a == 0 and b == 0:
        print("Równanie tożsamościowe")
    elif a == 0 and b != 0:
        print("Równanie sprzeczne")
    elif a != 0:
        x = -b / a
        print(x)
    else:
        print("Wprowadzono złe dane")
