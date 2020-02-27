if __name__ == "__main__":
    f = open("dane_6_3.txt", "r")
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V",
                "W", "X",
                "Y", "Z"]
    words = []
    end_list = []
    for line in f:
        words.append(line.rstrip("\n").split(" "))

    for elem in words:
        encrypted_word = ""
        k = 0
        for letter in elem[0]:
            shifted_position = (alphabet.index(letter) + k) % len(alphabet)
            shifted_letter = alphabet[shifted_position]
            encrypted_word = encrypted_word + shifted_letter
        if k < 27 and encrypted_word == elem[1]:
            break
        if k < 26 and encrypted_word != elem[1]:
            k += 1
        if k == 26 and encrypted_word != elem[1]:
            end_list.append(encrypted_word)
            break
    print(end_list)
    