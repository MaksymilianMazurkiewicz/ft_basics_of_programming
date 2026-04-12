import math

def input_int(prompt):
    return int(input(prompt))

def sum_numbers(number, pow = 1):
    n = number
    res = 0


    while n != 0:
        res += (n % 10) ** pow
        n = n // 10
    return res

n = input_int("Podaj liczbę: ")
if n <= 0:
    print("Podaj wartość większą od 0")
else:
    n_count = math.floor(math.log10(n)) + 1
    armstrong_res = sum_numbers(n, n_count) == n
    niven_res = n % sum_numbers(n) == 0
    print("Czy liczba armstronga ", armstrong_res, ". Czy liczba nivena: ", niven_res)