import random

carta1 = random.randint(1, 10)
carta2 = random.randint(1, 10)
print("Primer carta:", carta1)
print("Segunda carta:", carta2)

suma = carta1 + carta2
print("Suma de las dos primeras cartas:", suma)

if suma >= 19 and suma <= 21:
    print("Ganaste")
elif suma > 21:
    print("Perdiste por pasarte de 21.")
else:
    carta3 = random.randint(1, 10)
    print("Tercer carta:", carta3)
    suma_total = carta1 + carta2 + carta3
    print("Suma de las tres cartas:", suma_total)
    if suma_total >= 19 and suma_total <= 21:
        print("Ganaste")
    elif suma_total > 21:
        print("Perdiste por pasarte de 21.")
    else:
        carta4 = random.randint(1, 10)
        print("Cuarta carta:", carta4)
        suma_total2 = carta1 + carta2 + carta3 + carta4
        print("Suma de las cuatro cartas:", suma_total2)
        if suma_total2 >= 19 and suma_total2 <= 21:
            print("Ganaste")
        elif suma_total2 > 21:
            print("Perdiste por pasarte de 21.")
        else:
            carta5 = random.randint(1, 10)
            print("Quinta carta:", carta5)
            suma_total3 = carta1 + carta2 + carta3 + carta4 + carta5
            print("Suma de las cinco cartas:", suma_total3)
            if suma_total3 >= 19 and suma_total3 <= 21:
                print("Ganaste")
            else:
                print("Perdiste.")