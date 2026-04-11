def input_float(prompt):
    str_input = input(prompt)
    float_res = float(str_input)
    return float_res

def calc(a, b, c, x):
    return a*x**2 + b*x + c

a = input_float("Podaj a: ")
b = input_float("Podaj b: ")
c = input_float("Podaj c: ")
x = input_float("Podaj x: ")
y = calc(a, b, c, x)
print("Wynik", y)