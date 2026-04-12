def input_float(prompt):
    return float(input(prompt))

def calculate_value(prev):
    return 1/2 * (prev + 2 / prev)

def find_sln(curr):
    target = 2 ** (1/2)

    sln = curr
    while round(abs(sln - target), 4) > 0:
        sln = calculate_value(sln)
        print(sln)

curr = input_float("Podaj pierwszą wartość: ")
find_sln(curr)