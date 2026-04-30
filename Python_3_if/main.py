weather = str(input("What is the weather like today? "))
if weather == "Sunny" or weather == "sunny":
    print ("Go outside and enjoy the sun!")
elif weather == "Rainy" or weather == "Cloudy":
    print ("Take an umbrella with you just in case.")
elif weather == "Snowy" or weather == "Windy":
    print ("Wear a warm jacket.")
else:
    print ("I don't know what the weather is like, but I hope you have a good day!")




print ("Kalkulator")
dzialanie = str(input("1. Wybierz działanie: + - dodawnie, - odejmowanie, * mnożenie, / dzielenie: "))
if dzialanie == "+":
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print ("Wynik: ",a + b)
elif dzialanie == "-":
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print ("Wynik: ", a - b)
elif dzialanie == "*":
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    print ("Wynik: ",a * b)
elif dzialanie == "/":
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    if b == 0:
        print ("Nie można dzielić przez zero!")
    else:
        print ("Wynik: ", a / b)