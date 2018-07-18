if __name__ == "__main__":
    vowels = ["a", "e", "i", "o", "u"]
    word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")
    found = {}
    for letters in word:
        if letters in vowels:
            found[letters] += 1
    for k, v in sorted(found.items()):
        print(k, "znaleziono", v, "raz(y).")

