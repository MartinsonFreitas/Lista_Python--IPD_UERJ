# 22. Crie um algoritmo que leia um número N e calcule:
# Somatório de 1/i, onde i varia de 1 a N.

N=int(input('Digite um número inteiro: '))
soma=0

for i in range(1, N+1):
    soma=soma+(1/i)
    # print('O somatório é: ', soma)
    # se quiser conferir a soma por etapa é só tirar o '#' da linha acima
print('O somatório é: ', soma)