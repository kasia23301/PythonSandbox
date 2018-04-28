if __name__ == "__main__":
    print("Podaj liczbe")
    liczba = int(input())
    print("Chcesz sume czy iloczyn?")
    wybor = str(input())
    suma = 0
    licznik = 1
    iloczyn = 1
    if wybor == "suma":
        while licznik <= liczba:
            suma = suma + licznik
            licznik += 1
        print(str(suma))
    elif wybor == "iloczyn":
        while licznik <= liczba:
            iloczyn = iloczyn * licznik
            licznik +=1
        print(str(iloczyn))
