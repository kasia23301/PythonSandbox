if __name__ == "__main__":
    a = int(input("Podaj bok a trojkata: "))
    b = int(input("Podaj bok b trojkata: "))
    c = int(input("Podaj bok c trojkata: "))
    if a + b > c and a + c > b and b + c > a:
        print("Mozna zbudowac trojkat")
    else:
        print("Nie mozna zbudowac trojkata")
