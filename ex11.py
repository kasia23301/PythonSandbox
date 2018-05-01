if __name__ == "__main__":
    suma = []
    for i in range(1, 1000000):
        if i % 2 == 0:
            wynik = (-1/(2*i-1))
            suma.append(wynik)
        else:
            wynik2 = (1/(2*i-1))
            suma.append(wynik2)
    print(sum(suma)*4)


