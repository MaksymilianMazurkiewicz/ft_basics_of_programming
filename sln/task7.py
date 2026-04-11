def input_float(prompt):
    return float(input(prompt))

# Funkcja zwraca:
# longest = najdłuższy bok
# short1, short2 = pozostałe
def pseudo_sort(a, b, c):
    if a >= b and a >= c:
        return a, b, c
    elif b >= a and b >= c:
        return b, a, c
    return c, a, b


def check_triangle(a, b, c):
    # rozpakowanie boków
    longest, short1, short2 = pseudo_sort(a, b, c)

    # warunek istnienia trójkąta
    if longest >= short1 + short2:
        return "Nie da się zbudować trójkąta z tych odcinków"

    res = "Da się zbudować trójkąt. "

    if a == b and b == c:
        res += "Trójkąt jest równoboczny."
    elif a == b or a == c or b == c:
        # operator OR (lub) zwraca True, jeśli przynajmniej jeden warunek jest prawdziwy
        # w tym przypadku sprawdzamy czy jakiekolwiek dwa boki są równe
        res += "Trójkąt jest równoramienny."
    else:
        res += "Trójkąt jest różnoboczny."

    return res

a = input_float("Podaj a: ")
b = input_float("Podaj b: ")
c = input_float("Podaj c: ")

triangle_res = check_triangle(a, b, c)
print(triangle_res)