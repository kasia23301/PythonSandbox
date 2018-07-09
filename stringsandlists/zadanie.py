def funkszyn_najdłuższy_skok(lista):
    najwiekszy_element = lista[0]
    for element in lista:
        if element > najwiekszy_element:
            najwiekszy_element = element
    return najwiekszy_element


if __name__ == "__main__":
    tablica_z_wynikami=[]
    print("Pokażę Ci jaki najlepszy wynik w skoku w dal uzyskałeś w tym tygodniu " 
          "(Wiem, że jesteś antysportowcem ale wyobraź sobie, że skaczesz XD). " 
          "Podaj wynik, który uzyskałeś w poniedziałek (w metrach):")
    poniedziałek = int(input())
    tablica_z_wynikami.append(poniedziałek)
    print("We wtorek:")
    wtorek = int(input())
    tablica_z_wynikami.append(wtorek)
    print("W środę: ")
    sroda = int(input())
    tablica_z_wynikami.append(sroda)
    print("W czwartek: ")
    czwartek = int(input())
    tablica_z_wynikami.append(czwartek)
    print("W piatek: ")
    piatek = int(input())
    tablica_z_wynikami.append(piatek)
    print("W sobote: ")
    sobota = int(input())
    tablica_z_wynikami.append(sobota)
    print("W niedziele ")
    niedziela = int(input())
    tablica_z_wynikami.append(niedziela)
    print("Twój najdłuższy skok to ")
    print(funkszyn_najdłuższy_skok(tablica_z_wynikami))
    print("Kongratulejszyn :)")

