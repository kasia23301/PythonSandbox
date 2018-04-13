if __name__ == "__main__":
    print("Podaj stezenie alkoholu")
    A = int(input())
    print("podaj stezenie substancji uzytej do rozcienczenia ")
    B = int(input())
    print("Jakie stezenie chcesz uzyskac")
    C = int(input())
    stosunekalkoholu = (C - B)
    print("wrong value")
    if stosunekalkoholu == 0:
        print("wprowadziłeś złe dane")
    else:
        stosunekwody = (A - C)
        iloscwody = (stosunekwody * 100) / stosunekalkoholu
        print("Musisz dodac" + str(iloscwody) + "wody")
