if __name__ == "__main__":
    file = open("C:\\Users\\M\\Desktop\\DANE_PR\\DANE_PR\\dziennik.txt", "r")
    list = []
    for line in file:
        list.append(line)
    result = max(list)
    number = list.index(result)
    print(result)
    print(number)

    list_result = []
    for elem in list:
        i = elem
        list_of_elem = []
        if elem < list[i+1]:
            elem = list[i+1]
            list_of_elem.append(elem)
            if len(list_of_elem) == 4:
                list_result.append(list_of_elem)
        else:
            elem = list[i+1]

    result2 = sum(list_result)
    print(result2)



