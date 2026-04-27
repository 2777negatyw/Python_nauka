"""
Program do zbierania informacji osobistych
Zbiera dane o użytkowniku i wyświetla je w sformatowanej formie
"""

import random

# Lista cytatów
QUOTES = [
    "Sukces to 1% inspiracji i 99% potu. - Thomas Edison",
    "Jedynym sposobem na świetną pracę jest kochać to co robisz. - Steve Jobs",
    "Nie poddawaj się, nawet jeśli jest trudno. - Walt Disney",
    "Możliwości są ograniczone tylko wyobraźnią. - Unknown",
    "Każdy dzień to nowa szansa na zmianę. - Ralph Marston",
    "Twoja jedynym ograniczeniem jesteś ty sam. - Unknown",
    "Nigdy się nie kończmy uczyć i rosnąć. - Brian Tracy",
    "Dzisiaj jest idealny dzień na rozpoczęcie czegoś nowego. - Unknown",
    "Wierz w siebie, a inni również będą wierzyć. - Joseph Murphy",
    "Wszystko jest możliwe dla tych, którzy wierzą. - Unknown",
]


def get_positive_float(prompt):
    """Pobiera dodatnią liczbę zmiennoprzecinkową od użytkownika"""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Proszę podaj liczbę dodatnią.")
        except ValueError:
            print("Błąd: Proszę podaj prawidłową liczbę.")


def get_positive_int(prompt):
    """Pobiera dodatnią liczbę całkowitą od użytkownika"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Proszę podaj liczbę dodatnią.")
        except ValueError:
            print("Błąd: Proszę podaj prawidłową liczbę całkowitą.")


def get_text(prompt):
    """Pobiera tekst od użytkownika"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Błąd: Pole nie może być puste.")


def main():
    """Główna funkcja programu"""
    print("=" * 50)
    print("Witaj w programie, który zbiera informacje o Tobie!")
    print("=" * 50 + "\n")

    # Zbieranie danych od użytkownika
    imie = get_text("Podaj swoje imię: ")
    wzrost = get_positive_float("Podaj swój wzrost (w cm): ")
    wiek = get_positive_int("Podaj swój wiek: ")
    waga = get_positive_float("Podaj swoją wagę (w kg): ")
    kraj = get_text("Podaj swój kraj: ")
    obywatelstwo = get_text("Podaj swoje obywatelstwo: ")
    pochodzenie = get_text("Podaj swoje pochodzenie: ")
    plec = get_text("Podaj swoją płeć: ")

    # Obliczenie wieku za 10 lat
    wiek_za_10_lat = wiek + 10

    # Wyświetlanie zebranych informacji
    print("\n" + "=" * 50)
    print("PODSUMOWANIE TWOICH DANYCH")
    print("=" * 50 + "\n")

    print(f"Imię: {imie}")
    print(f"Wzrost: {wzrost} cm")
    print(f"Wiek: {wiek} lat")
    print(f"Waga: {waga} kg")
    print(f"Kraj: {kraj}")
    print(f"Obywatelstwo: {obywatelstwo}")
    print(f"Pochodzenie: {pochodzenie}")
    print(f"Płeć: {plec}")

    print(f"\nZa 10 lat będziesz mieć {wiek_za_10_lat} lat.")
    print("=" * 50)

    # Wyświetlanie losowego cytatu
    print("\n💡 Cytat dnia:")
    print(f'"{random.choice(QUOTES)}"')
    print("=" * 50)


if __name__ == "__main__":
    main()
