# 11.	Crie um algoritmo que calcule a soma dos N primeiros números inteiros ímpares e positivos. 
# O valor de N deve ser lido do usuário.

# Lê o número
n=int(input('Valor de N:'))

somaImpar=0

for i in range (1,n+1):
    if i%2!=0:
        somaImpar = somaImpar + i
    
print('\nValor total dos números ímpares: ', somaImpar) 
