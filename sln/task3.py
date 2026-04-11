def input_float(prompt):
    """
    Funkcja pobiera wartość od użytkownika i zamienia ją na liczbę.

    Dlaczego:
    - funkcja input() w Pythonie zawsze zwraca string (czyli tekst)
    - żeby móc robić obliczenia, musimy zamienić to na liczbę

    Argumenty:
    prompt (str) - tekst, który wyświetli się użytkownikowi

    Zwraca:
    int - liczba wprowadzona przez użytkownika
    """
    str_input = input(prompt)
    float_res = float(str_input)  # konwersja na liczbę (float)
    return float_res


def to_celsius(temp):
    """
    Zamienia temperaturę z Fahrenheitów na Celsjusze.

    Wzór:
    (F - 32) * 5/9

    Argumenty:
    temp (float) - temperatura w Fahrenheitach

    Zwraca:
    float - temperatura w Celsjuszach
    """
    return (temp - 32) * 5/9


def to_fahrenheit(temp):
    """
    Zamienia temperaturę z Celsjuszy na Fahrenheity.

    Wzór:
    C * 1.8 + 32

    Argumenty:
    temp (float) - temperatura w Celsjuszach

    Zwraca:
    float - temperatura w Fahrenheitach
    """
    return temp * 1.8 + 32


def convert(temp, unit):
    """
    Funkcja konwertuje temperaturę na podstawie podanej jednostki.

    Argumenty:
    temp (float) - temperatura
    unit (str) - jednostka ('C' albo 'F')

    Zwraca:
    (wynik, jednostka) albo (None, komunikat błędu)
    """
    print(temp, unit)

    if unit == 'C':
        return to_fahrenheit(temp), 'F'
    elif unit == 'F':
        return to_celsius(temp), 'C'

    return None, 'Niepoprawna jednostka'


# --- GŁÓWNA CZĘŚĆ PROGRAMU ---

# Pobieramy temperaturę od użytkownika
temp = input_float("Podaj wartość temperatury: ")

# Zakładamy, że użytkownik poda 'C' albo 'F'

unit = input("Podaj jednostkę (C/F): ")

# Konwersja temperatury
con_temp, con_unit = convert(temp, unit)

# Wyświetlenie wyniku
print(con_temp, con_unit)