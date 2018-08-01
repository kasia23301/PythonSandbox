def search4vowels():
    """Wyświetla samogłoski znalezione w słowie podanym przez użytkownika"""
    vowels = set('aeiou')
    word = input('Podaj słowo, w którym należy wyszukać samogłoski: ')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


if __name__ == '__main__':
    search4vowels()


def search4vowels(word):
    """Wyświetla samogłoski znalezione w słowie podanym jako argument"""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


if __name__ == '__main__':
    print(search4vowels("hm"))
