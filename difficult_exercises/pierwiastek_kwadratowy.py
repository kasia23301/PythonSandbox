def calculate_root(number):
    for i in range(number):
        if i * i == number:
            return i
    return False


if __name__ == "__main__":
    number = int(input("Podaj liczbe: "))
    print(calculate_root(number))
