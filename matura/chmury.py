from decimal import Decimal
def make_dictionary(line):
    x = line.rstrip("\n").split(";")
    dictionary = {
        "Dzien": x[0],
        "Temperatura": x[1],
        "Opad": x[2],
        "Kategoria_chmur": x[3],
        "Wielkosc_chmur": x[4]}
    return dictionary


if __name__ == "__main__":
    f = open("pogoda.txt", "r")
    list_of_dicts = []
    result = []
    for line in f:
        res = make_dictionary(line)
        list_of_dicts.append(res)
    del list_of_dicts[0]
    for elem in list_of_dicts:
        if float(elem["Temperatura"].replace(",", ".")) >= 20 and int(elem["Opad"]) <= 5:
            result.append(elem)
    print(result)