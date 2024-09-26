
if __name__ == "__main__":
    english_word = ["lounge", "loft", "cutlery", "kettle", "oven", "sink"]
    polish_translation = ["salon", "strych", "sztucce", "czajnik", "piekarnik", "zlew"]
    score = []
    elem_of_polish_translation = 0
    for eng_words in english_word:
        print(eng_words)
        a = input("Wpisz tlumaczenie wyrazu: ")
        if a == polish_translation[elem_of_polish_translation]:
            print("Good")
            elem_of_polish_translation += 1
            score.append(1)
        else:
            print("Not good")
            elem_of_polish_translation += 1
    print("Twoj wynik to: " + str(sum(score)) + " /6 punktow")

    english_translation = ["lounge", "loft", "cutlery", "kettle", "oven", "sink"]
    polish_word = ["salon", "strych", "sztucce", "czajnik", "piekarnik", "zlew"]
    score_2 = []
    elem_of_english_translation = 0
    for pol_words in polish_word:
        print(pol_words)
        b = input("Wpisz tlumaczenie wyrazu: ")
        if b == english_translation[elem_of_english_translation]:
            print("Good")
            elem_of_english_translation += 1
            score_2.append(1)
        else:
            print("Not good")
            elem_of_english_translation += 1
    print("Twoj wynik to: " + str(sum(score_2)) + " /6 punktow")

    if (sum(score) + sum(score_2)) < 6:
        print("You are so weak!")
    else:
        print("not bad!")
