class Parking:
    def __init__(self, geo_x, geo_y, nazwa):
        self.geo_x = geo_x
        self.geo_y = geo_y
        self.nazwa = nazwa
    def oblicz_odl(self, user_geo_x, user_geo_y):
        return (user_geo_x - self.geo_x) + (user_geo_y - self.geo_y)

if __name__=='__main__':
    par_kar = Parking(12.678, 23.998, "Karuzela")
    print(par_kar.nazwa)
    parking = [Parking(12.678, 24.908, "Karuzela"),
               Parking(13.918, 27.948, "Korona"),
               Parking(13.648, 25.918, "Pasaż"),
               Parking(17.378, 28.988, "Ferio")]

    print("dupa dupa dupa")