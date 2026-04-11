def input_float(prompt):
    # Pobiera dane od użytkownika i zamienia je na float (liczba zmiennoprzecinkowa)
    return float(input(prompt))

# Funkcja zwraca DWIE wartości:
# 1. komunikat (string)
# 2. wynik równania (float albo None)
#
# Python pozwala zwracać wiele wartości jednocześnie jako (tuple),
# czyli wartości oddzielone przecinkiem.
def calc(a, b):
    if a == 0:
        if b == 0:
            return "Równanie ma nieskończenie wiele rozwiązań", None
        else:
            return "Równanie nie ma rozwiązań", None

    res = -b / a
    return "Równanie ma jedno rozwiązanie", res



a = input_float("Podaj a: ")
b = input_float("Podaj b: ")

# rozpakowanie krotki (tuple unpacking)
info, res = calc(a, b)

# wypisanie wyniku w zależności od tego, czy istnieje rozwiązanie
if res is None:
    print(info)
else:
    print(info, "x =", res)