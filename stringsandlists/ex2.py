# def odwroc_liste(l):
# l.reverse()

# if __name__ == "__main__":
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odwroc_liste(lista)
# print(lista)

def funkszyn(listawejsciowa):
    lista = []
    for i in range(len(listawejsciowa) - 1, -1, -1):
        lista.append(listawejsciowa[i])
    return lista


if __name__ == "__main__":
    lista2 = [1, 4, 5, 7, 9, 12]
    print(funkszyn(lista2))
