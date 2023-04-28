# Fazer um algoritmo para ler o peso de 8 bolas. Assumindo que todas tem o
# peso igual e apenas uma de peso DIFERENTE, imprimir a bola de peso
# DIFERENTE.

b1 = int(input('b1: '))
b2 = int(input('b2: '))
b3 = int(input('b3: '))
b4 = int(input('b4: '))
b5 = int(input('b5: '))
b6 = int(input('b6: '))
b7 = int(input('b7: '))
b8 = int(input('b8: '))
               
if b1+b2+b3 == b4+b5+b6:
    if b7 != b1:
        print ('b7 ', b7)
    else:
        print ('b8 ', b8)
elif b1+b2 == b3+b4:
    if b5 != b1:
        print ('b5 ', b5)
    else:
        print ('b6 ', b6)
elif b1 == b2:
    if b3 != b1:
        print ('b3 ', b3)
    else:
        print ('b4 ', b4)
else:
    if b1 != b8:
        print ('b1 ', b1)
    else:
        print ('b2 ', b2)