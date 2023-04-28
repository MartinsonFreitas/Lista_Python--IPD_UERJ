# 28. Crie um algoritmo que leia um número (com qualquer número de dígitos) 
# em uma base numérica de ordem < 10 e calcule o número correspondente na base decimal.
#
# O número da ordem da base (e.g., 2 para binária, 3 para ternária, 8 para octal, etc.) 
# deve também ser informado pelo usuário.
#
# Ver: https://pt.stackoverflow.com/questions/401653/convertendo-bases-em-python

print('\nATENÇÃO: Os dígitos devem ser menores que a base!\n')
N=input('\nDigite o número para conversão de base: ')
b=int(input('Informe a base para conversão: '))

print(int(N, b))