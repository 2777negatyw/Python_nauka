plik1 = open("C:\\Users\\Przemysław\\Documents\\Pyton_Nauka\\python_7_notatnik\\notatki.txt", "a")
print("Witaj w notatniku!")

menu = int(input("Wybierz opcję: \n1. Dodaj notatkę \n2. Zobacz notatki \n3. Wyjdź\n"))

if menu == 1:
    notatka = str(input("Wpisz nową notatkę: "))
    plik1.write(notatka + "\n")
    print("Notatka dodana pomyślnie!")
plik1.close()

if menu == 2:
    plik1 = open("C:\\Users\\Przemysław\\Documents\\Pyton_Nauka\\python_7_notatnik\\notatki.txt", "r")
    print("Twoje notatki: \n")
    print(plik1.read())
    plik1.close()
elif menu == 3:
    print("Do zobaczenia!")