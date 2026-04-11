def input_int(prompt):
    return int(input(prompt))

def get_mark(points):
    #Zapomniałem jakie są progi punktowe więc dam losowe xD
    res = "Nie ma takiej oceny" # wartość początkowa zwalania nas z użycią na końcu else

    # Używamy elif a nie if, ponieważ:
    # elif sprawdza tylko wtedy, gdy poprzedni warunek był False
    # if sprawdzałby wszystkie warunki niezależnie
    if points < 50:
        res = "Dopuszczający +"
    elif points < 55:
        res = "Dostateczny"
    elif points < 60:
        res = "Dostateczny +"
    elif points < 75:
        res = "Dobry"
    elif points < 80:
        res = "Dobry +"
    elif points < 95:
        res = "Bardzo dobry"
    elif points < 100:
        res = "Bardzo dobry +"
    return res

points = input_int("Podaj liczbę punktów: ")
mark = get_mark(points)
print("Twoja ocena to: ", mark)