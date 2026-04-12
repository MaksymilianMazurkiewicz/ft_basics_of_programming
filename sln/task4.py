def input_float(prompt):
    return float(input(prompt))

def read_data():
    next = 0
    count = -1
    res = 0

    # Pętla działa dopóki liczba >= 0
    while next >= 0:
        res += next
        count += 1
        next = input_float("Podaj wartość: ")

    if count == 0:
        return 0
    
    return res/count
        
res = read_data()
print(res)
