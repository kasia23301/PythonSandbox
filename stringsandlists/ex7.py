def czyjestpalindromem(string):
    odwroconystring = string[::-1]
    if string == odwroconystring:
        return "To jest palindrom"
    else:
        return "To nie jest palindrom"


if __name__ == "__main__":
    podanywyraz = "AbcdedcbA"
    print(czyjestpalindromem(podanywyraz))

