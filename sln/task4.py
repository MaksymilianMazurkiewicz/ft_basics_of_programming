def input_float(prompt):
    str_input = input(prompt)
    float_res = float(str_input)
    return float_res

def calc(a, b, x):
    return a*x + b

a = input_float("Podaj a: ")
b = input_float("Podaj b: ")
x = input_float("Podaj x: ")
y = calc(a, b, x)
print("Wynik", y)