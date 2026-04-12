def input_float(prompt):
    return float(input(prompt))

def read_data():
    res = round(2 ** (1/2), 4)
    print("Prawidłowy wynik to: ", res)
    user_input = 0

    # Pętla trwa dopóki wynik się nie zgadza
    while round(abs(user_input - res), 4) > 0:
        user_input = input_float("Podaj wartość: ")
    
read_data()