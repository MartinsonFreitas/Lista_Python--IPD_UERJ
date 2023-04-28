# 7. Crie um algoritmo que leia 2 números inteiros positivos, A e B, 
# e que calcule a soma de todos os números compreendidos entre eles. 
# 
# Os valores A e B não devem ser considerados no somatório. 
# 
# Caso A seja maior do que B deve ser enviada uma mensagem 
# para o usuário informando que a soma não será realizada.

# ler os números
A=int(input('Digite um número inteiro positivo: '))
B=int(input('Digite outro número inteiro positivo: '))

soma=0

# se A menor do que B
if A<B:
    for i in range (A+1,B):
        
        # efetua a soma e printa na tela
        soma+= i
    print('\nTotal da soma dos números entre o menor e maior número: ', soma)

# se não for printa a mensagem
else:
    print('\nA soma não foi realizada, o segundo número é menor do que o primeiro!')

