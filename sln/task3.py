def input_int(prompt):
    return int(input(prompt))

def factorial(limit):
    res = 1
    if limit == 0:
        return res
    
    # Pętla mnoży kolejne liczby.
    for i in range(1, limit + 1):
        res *= i
    return res

def rec_factorial(value):
    # Wersja rekurencyjna. Rekurencja nie była omawiana na wykładzie,
    # ale czasami jest lepszym rozwiązaniem niż użycie pętli.
    if value == 0:
        return 1
    return value * rec_factorial(value-1)
        

limit = input_int("Wylicz silnię z liczby: ")
loop_fac = factorial(limit)
rec_fac = rec_factorial(limit)

print("Silnia z liczby ", limit, " wynosi ", loop_fac, " lub z rekurencji: ", rec_fac)