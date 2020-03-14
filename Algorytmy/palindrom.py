def palindrom(slowo):
    i = 0
    j = len(slowo)-1
    while i < j:
        if slowo[i] == slowo[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    slowo = input("Podaj slowo: ")
    slowo = list(slowo)
    if palindrom(slowo):
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")
