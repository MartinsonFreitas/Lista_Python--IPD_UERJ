# 32.	Leia um número N inteiro. Calcule sua raiz INTEIRA. Exemplo: N=21, raiz inteira = 4.

import math

n = int(input('Digite um número inteiro: '))

raiz = int(math.sqrt(n))
print(f'\nA raiz quadrada de {n} é {raiz:.0f}\n') 