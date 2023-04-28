# 8. Crie um algoritmo que leia 2 números inteiros positivos, A e B, 
# e que calcule a soma de todos os números múltiplos de 4 compreendidos entre eles. 
# 
# Os valores A e B não devem ser considerados no somatório. 
# Caso A seja maior do que B deve ser enviada uma mensagem para o usuário informando 
# que a soma não será realizada.

# Lendo os números
A=int(input('Digite um número inteiro positivo: '))
B=int(input('Digite outro número inteiro positivo: '))

soma=0
if A<B:
    for i in range (A+1,B):
        if i%4==0:
            soma+= i
    print('\nTotal do somatório dos múltiplos de 4: ', soma)
else:
    print('\nA soma não foi realizada, primeiro número maior que o segundo!!!')

