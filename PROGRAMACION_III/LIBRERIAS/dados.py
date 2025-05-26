import random

carta1=random.randint(1,10)
carta2=random.randint(1,10)
carta3=random.randint(1,10)
print("Primer carta: ",carta1)
print("Segunda carta: ",carta2)
suma=carta1+carta2
if suma==18 or 19 or 20 or 21:
    print(suma)
    print("Ganaste")
    suma2=(carta1 and carta2)+carta3
if suma2<18:
    print("Tercer carta: ",carta3)
    print(suma2)
else:
    print(suma2)
    print("Perdiste")