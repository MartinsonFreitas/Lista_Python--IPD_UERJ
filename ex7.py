# Faça um programa para somar os números pares entre 1000 e 2000, inclusive.

soma = 0

for i in range(1000, 2001, 2):
    soma += i
    
print ('soma:', soma)