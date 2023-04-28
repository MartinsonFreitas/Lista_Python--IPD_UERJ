# 20. Crie um algoritmo que leia um número N e imprima se ele é perfeito ou não. 
# Um número é perfeito quando a soma dos seus divisores é igual a ele mesmo, e.g., 6 = 3 + 2 + 1.

# leia o valor de n
n = int(input("Digite o valor de n: "))
soma = 0
  
for divisor in range(1,n):
    if n % divisor == 0:
        soma += divisor # soma = soma + divisor

if n == soma:
    print("O numero %d é perfeito" %(n))
else: 
    print("O numero %d nao é perfeito\n" %(n))