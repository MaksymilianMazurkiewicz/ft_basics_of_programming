def input_int(prompt):
    return int(input(prompt))


def is_leap_year(year):
    # Warunek roku przestępnego:
    # - podzielny przez 4 i NIE podzielny przez 100
    # LUB
    # - podzielny przez 400

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap:
        return "jest przestępny"
    return "nie jest przestępny"


year = input_int("Podaj rok: ")
leap_res = is_leap_year(year)

print("Rok", year, leap_res)