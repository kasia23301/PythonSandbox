if __name__ == "__main__":
    vowels = ["a", "e", "i", "o", "u", "y", "ą", "ę","ó"]
    word= input("Podaj słowo, w którym należy wyszuakć samogłoski: ")
    found = []
    for letter in word:
        if letter in vowels:
            if letter not in found:
                found.append(letter)
    for vowel in found:
        print(vowel)