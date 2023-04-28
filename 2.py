# 2. Crie um algoritmo que escreva os N primeiros termos de uma progressão aritmética (PA). 
# O primeiro termo e a razão da PA devem ser informados pelo usuário.

# Lê o primeiro Termo da PA
a1 = int(input('Digite o Primeiro Termo da PA: '))
# Lê a razão da PA
r = int(input('Digite a Razão da PA: '))
# Lê a quantidade de termos da PA
n = int(input('Digite o Número de Termos da PA: '))

# Fórmula para descobrir o an
an = a1 + (n-1)*r
i = 1
an = an+1

for Termo_i_PA in range(a1, an, r):
    print ('O termo número ', i , ' da PA é: ', Termo_i_PA)
    i+=1