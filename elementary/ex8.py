if __name__ == "__main__":
    x = 1
    dzielnik = 1
    for i in range(1, 20):
        for dzielnik in range(2,i):
            if (i % dzielnik) == 0:
                break
            else:
                print("Liczby pierwsze to: " + str(i))
        

