if __name__ == "__main__":
    phrase = "Podaj jajko!"
    plist = list(phrase)
    print(phrase)
    print(plist)
    plist = plist[1:9]
    plist.pop(2)
    plist.pop(2)
    new_pharse = "".join(plist)
    print(plist)
    print(new_pharse)

if __name__ == "__main__":
    phrase = "Podaj jajko!"
    plist = list(phrase)
    print(phrase)
    print(plist)
    new_pharse = "".join(plist[1:3])
    new_pharse = new_pharse + "".join([plist[5], plist[4], plist[7], plist[6]])
    print(plist)
    print(new_pharse)
    