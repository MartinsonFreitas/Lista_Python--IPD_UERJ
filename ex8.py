# Faça um programa para somar o FATORIAL dos 5 primeiros números

soma = 0
for i in range(1,6):
    fat = 1
    for j in range(1, i+1):
        fat = fat*j
    print ('fat: ', j, 'é', fat)
    soma += fat
    
print ('soma:', soma)