def input_int(prompt):
    return int(input(prompt))

def convert_to_decimal(value, base):
    n = value
    res = 0
    i = 0

    # Rozbijanie liczby na cyfry
    while n != 0:
        res += (n % 10) * (base ** i)
        i += 1
        n = n // 10
    return res

base = input_int("Podaj system: ")
value = input_int("Podaj wartość: ")
res = convert_to_decimal(value, base)
print("W systemie 10: ",res)