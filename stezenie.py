from datetime import datetime

if __name__ == "__main__":
    print("Podaj rok urodzenia")
    rokurodzenia = int(input())
    wynik = (2018 - rokurodzenia)
    print("masz " + str(wynik) + " lat")
    #print ("podaj miesiac urodzenia liczbą")
    # miesiacurodzenia = input()
    #wynik = 3 - miesiacurodzenia
    #print("podaj dzien urodzenia")
    #dzienurodzenia = input()
    print("Podaj ile masz lat")
    wiek = int(input())
    wynik2 = (2018 - wiek)
    print("Urodziłeś sie w " + str(wynik2))

    date_format = "%d/%m/%Y"
    date_of_birth = input("Data urodzenia: ")
    a = datetime.strptime(date_of_birth, date_format)
    b = datetime.now()
    delta = b - a
    print(delta.days)




