import random
if __name__ == "__main__":
    liczba = random.randint(1,10)
    for i in range(3):
        odp = input("zgadnij jaka liczbe komputerek ma na mysli ")
        print("podałeś liczbe: ", odp)
        if liczba == int(odp):
            print("wygrałes")
            break
        else:
            print("nie udało ci się")