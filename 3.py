# 3. Crie um algoritmo que leia uma quantidade não determinada de números inteiros. 
# O programa deve calcular e escrever a quantidade de números pares e ímpares 
# e a média aritmética dos números pares. 
# A leitura deve ser encerrada quando for lido o número zero, que não deve ser considerado.

contPar=0
contImpar=0
somaPar=0
n=int(input('Digite um número inteiro: '))

while n!=0:
    if n%2==0:
        contPar=contPar+1
        somaPar=somaPar+n
        mediaPar=float(somaPar/contPar)
    else:
        contImpar=contImpar+1
        
    n=int(input('Digite um número inteiro: '))
        
print('A quantidade de números pares é: ', contPar)
print('A quantidade de números ímpares é: ', contImpar)
print('A média aritmética dos números pares é: ', mediaPar)