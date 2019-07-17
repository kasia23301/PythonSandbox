
if __name__ == "__main__":
    lataprzestepne = []
    i = 2018
    while len(lataprzestepne) < 20:
        if i % 4 == 0 and i % 100 != 0:
            lataprzestepne.append(i)
        elif i % 400 == 0:
            lataprzestepne.append(i)
        i += 1
    print(lataprzestepne)
