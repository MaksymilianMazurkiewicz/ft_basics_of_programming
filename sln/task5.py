def input_float(prompt):
    return float(input(prompt))


def calc(a, b, c):
    # UWAGA:
    # operator 'and' zwraca True tylko wtedy, gdy WSZYSTKIE warunki są True
    # jeśli którykolwiek jest False → wynik całego wyrażenia to False

    if a == 0 and b == 0:
        if c == 0:
            return "Równanie ma nieskończenie wiele rozwiązań", None, None
        else:
            return "Równanie nie ma rozwiązań", None, None

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "Równanie nie ma rozwiązań rzeczywistych", None, None
    elif delta == 0:
        res = -b / (2 * a)
        return "Równanie ma jedno rozwiązanie", res, None
    # W tym przypadku możemy pominąć else, ponieważ kod i tak się wykona jezeli porzednie warunki nie zostały spełnione
    # Jeżeli zostanę spełnione to zwróća wartość i reszta kodu się nie wykona
    
    delta_sqrt = delta ** 0.5

    res1 = (-b + delta_sqrt) / (2 * a)
    res2 = (-b - delta_sqrt) / (2 * a)

    return "Równanie ma dwa rozwiązania", res1, res2


a = input_float("Podaj a: ")
b = input_float("Podaj b: ")
c = input_float("Podaj c: ")

# rozpakowanie wyniku funkcji (tuple unpacking)
info, res1, res2 = calc(a, b, c)

print(info, res1, res2)