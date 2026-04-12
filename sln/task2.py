def input_int(prompt):
    return int(input(prompt))

def avg(limit):
    if limit == 0:
        return 0
    res = 0
    for i in range(limit):
        prompt = "Podaj wartość " + str(i) + " : "
        res += input_int(prompt)
    return res / limit

limit = input_int("Podaj ile liczb wczytać: ")
if limit < 0:
    print("Liczba powinna być większa od 0")
else:
    res = avg(limit)
    print("Rezulat", res)