if __name__ == "__main__":
    f = open("dane_6_2.txt", "r")
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
        for letter in elem[0]:
            if elem[1] == '':
                elem[1] = '0'
            shifted_position = (alphabet.index(letter) - int(elem[1])) % len(alphabet)
            shifted_letter = alphabet[shifted_position]
            encrypted_word = encrypted_word + shifted_letter
        end_list.append(encrypted_word)
    print(end_list)

    with open("wyniki.txt", mode="w+") as f:
        for elem in end_list:
            f.write(elem + "\n")
