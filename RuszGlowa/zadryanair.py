if __name__ == "__main__":
    literki = []
    word = input("Podaj słowo, w którym należy policzyć litery: ")
    for letter in word:
        literki.append(letter)
    found = {}
    for letters in word:
        if letters in literki:
            found.setdefault(letters, 0)
            found[letters] += 1

    for k, v in sorted(found.items()):
        print(k, "znaleziono", v, "raz(y).")