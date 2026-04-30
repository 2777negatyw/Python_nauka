file = open("C:\\Users\\Przemysław\\Documents\\Pyton_Nauka\\python_5_tracker-wydatkow\\wydatki.json", "a")
print("Witaj w trackerze wydatków!")
menu = int(input("Wybierz opcję: \n1. Dodaj wydatek \n2. Zobacz wydatki \n3. Wyjdź\n"))
if menu == 1:
    try:
        wydatki = float(input("Podaj swoje wydatki: "))
        while wydatki == 0:
            print("Nie można dodać wydatku o wartości 0.")
            wydatki = float(input("Podaj swoje wydatki: "))
        else:
            file.write("\n kwota: " + str(wydatki) + " zl ")
            kategoria = str(input("Podaj kategorie wydatku (np. jedzenie, transport, rozrywka): "))
            file.write(", kategoria: " + kategoria)
    except ValueError:
        print("Nieprawidłowa wartość. Proszę podać liczbę.")
    file.close()
elif menu == 2:
    file = open("C:\\Users\\Przemysław\\Documents\\Pyton_Nauka\\python_5_tracker-wydatkow\\wydatki.json", "r")
    print("Twoje wydatki:")
    print(file.read())
    file.close()
elif menu == 3:
    print("Do zobaczenia!")
else:
    print("Nieprawidłowa opcja. Proszę wybrać 1, 2 lub 3.")
