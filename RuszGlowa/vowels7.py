if __name__ == "__main__":
    vowels = {"a", "e", "e", "i", "o", "u", "u"}
    print(vowels)
    vowels2 = set("aeeiouu")
    print(vowels2)
    vowels3 = set("aeiou")
    word = "halo"
    u = vowels3.union(set(word))
    u_list = sorted(list(u))
    print(u_list)
    d = vowels3.difference(set(word))
    print(d)
    i = vowels3.intersection(set(word))
    print(i)

if __name__ == "__main__":
    vowels = set("aeiou")
    word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)

if __name__ == "__main__":
    vowels = {"a", "e", "e", "i", "o", "u", "u"}
    word = input("Podaj słowo, w którym należy wyszukać samogłoski: ")
    found = vowels.intersection(set(word))
    print(found)