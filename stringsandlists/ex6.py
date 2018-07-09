# if __name__ == "__main__":
#     print("Podaj palindrom")
#     dlugosc = 0
#     liczba = 0
#     plik = open("alfabet.txt")
#     slowo = plik.readline()
#     while slowo:
#         slowo = slowo.rstrip()
#         j = -1
#         for i in range(len(slowo) / 2):
#             if slowo[i] != slowo[j]:
#                 break
#             j -= 1
#         else:
#             print(slowo)
#             liczba += 1
#         if len(slowo) > dlugosc:
#             dlugosc = len(slowo)
#             licznik = 1
#
#     slowo = plik.readline()


def czy_jest_pal(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def czy_jest_palindromem(string):
    odwrocony_wyraz = string[::-1]
    if string == odwrocony_wyraz:
        return True
    else:
        return False


if __name__ == "__main__":
    wyraz = "abba"
    print(czy_jest_palindromem(wyraz))
    print(czy_jest_pal(wyraz))
