def convert_temp(temp):
    return (temp * 9/5) + 32

def list_temp():
     # Iteracja co 2 stopnie od 0 do 40
    for temp_c in range(0, 41, 2):
        temp_f = convert_temp(temp_c)
        print("Temperatura w C", temp_c, "W farenahitach", temp_f)

list_temp()