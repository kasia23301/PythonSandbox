import numpy as np

if __name__ == "__main__":
    # TODO: ZROBIC TAKI SAM PROGRAM BEZ UZYCIA DWOCH LIst (imiona i nazwiska) - uzyc jednej z krotkami - tuple - (a konkretnie parami)
    imiona = []
    nazwiska = []

    taknie = "tak"
    while taknie == "tak":
        print("podaj imie")
        imie = input()
        imiona.append(imie)
        print("podaj nazwisko")
        nazwisko = input()
        nazwiska.append(nazwisko)
        print("czy chcesz dodac kolejnego ucznia?")
        taknie = input()
    for index in range(0, len(imiona)):
        print("imie: " + imiona[index] + ", nazwisko: " + nazwiska[index])
