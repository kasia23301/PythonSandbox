def codrugielement(lista):
    return lista[::2]

lista3=[]
def dupa(lista2):
   for i in range(0, len(lista2), 2):
       lista3.append(i)
print(lista3)


if __name__ == "__main__":
    lista =[1,3,6,7,8,9,12,14,17,25]
    print(codrugielement(lista))

if __name__ == "__main__":
    lista2 = [1,2,3,4,5,6,7,8,9,10]
    print(dupa(lista2))


