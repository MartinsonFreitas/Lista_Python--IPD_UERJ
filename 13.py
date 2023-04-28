# 13.	Crie um algoritmo para calcular a área de um triângulo qualquer, 
# considerando que são fornecidos os comprimentos dos seus lados. 
# 
# Esse programa não pode permitir a entrada de dados inválidos, 
# ou seja, medidas menores ou iguais a 0.

# importando a biblioteca math
import math

# lendo os lados do triângulo
lado1=float(input('Entre com a medida do primeiro lado: '))
lado2=float(input('Entre com a medida do segundo lado: '))
lado3=float(input('Entre com a medida do terceiro lado: '))

# verificando os valores
if lado1>0 or lado2>0 or lado3>0:
    s=float(0.5*(lado1+lado2+lado3))
    area=float(math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3)))
else:
    print('Entrada de dados inválida!')
    
print('Medida da área: ', area)
