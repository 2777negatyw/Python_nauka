class Adress:
    def __init__(self, street:int, street_number:int, postal_code:str, city:str):
        print("Tworzę nowy obiekt klasy Adress")
        self.street = street
        self.street_number = street_number
        self.postal_code = postal_code
        self.city = city


class Flat:
    def __init__(self, adress: Adress, area: int, rooms: int):
        print("Tworzę nowy obiekt klasy Flat")
        self.adress = adress
        self.area = area
        self.rooms = rooms

adress1 = Adress(street="ul. Kwiatowa", street_number=15, postal_code="00-000", city="Warszawa")
adress2 = Adress(street="ul. Słoneczna", street_number=10, postal_code="00-000", city="Warszawa")

my_flat = Flat(adress=adress1, area=60, rooms=5)

print("Mój adres to: " + my_flat.adress.street + " " + str(my_flat.adress.street_number))
print("Mój metraż to: " + str(my_flat.area) + " m2")
print("Liczba pokoi to: " + str(my_flat.rooms))

your_flat = Flat( adress="ul. Słoneczna 10", area=80, rooms=4)
print("Twój adres to: " + your_flat.adress)
print("Twój metraż to: " + str(your_flat.area) + " m2")
print("Liczba pokoi to: " + str(your_flat.rooms))