if __name__ == "__main__":
    phrase = "Podaj jajko!"
    plist = list(phrase)
    print(phrase)
    print(plist)
    plist.remove("!")
    plist.remove("k")
    plist.pop(9)
    plist.pop(0)
    plist.pop(2)
    plist.pop(2)






    new_phrase = "".join(plist)
    print(plist)
    print(new_phrase)
