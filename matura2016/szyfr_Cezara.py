
if __name__ == "__main__":
    f = open("dane_6_1.txt", "r")
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V",
             "W", "X",
             "Y", "Z"]
    words=[]
    end_list = []
    for line in f:
        words.append(line.rstrip("\n"))
    for word in words:
        encrypted_word = ""
        for letter in word:
            shifted_position = alphabet.index(letter) + 3
            if shifted_position > 25:
                shifted_position = shifted_position - 26
            shifted_letter = alphabet[shifted_position]
            encrypted_word = encrypted_word + shifted_letter
        end_list.append(encrypted_word)

    print(end_list)


    end_list = []
    for word in words:
        encrypted_word = ""
        for letter in word:
            shifted_position = (alphabet.index(letter) + 107) % len(alphabet)
            shifted_letter = alphabet[shifted_position]
            encrypted_word = encrypted_word + shifted_letter
        end_list.append(encrypted_word)

    print(end_list)
