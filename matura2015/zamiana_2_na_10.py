if __name__ == "__main__":
    i = input("Podaj liczbe w systemie dwojkowym: ")
    dec = 0
    l = list(i)
    l.reverse()
    for index, v in enumerate(l):
        dec += int(v) * (2 ** index)
    print(dec)
