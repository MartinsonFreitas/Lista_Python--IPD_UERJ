# 14. Crie um algoritmo que:
# a) Leia a idade de várias pessoas. 
# O final da lista contém o valor da idade igual a -1 que deverá ser computado.
# 
# b) Calcule e mostre a idade média desse grupo de indivíduos. 
# Escreva também a porcentagem de pessoas entre 21 e 65 anos inclusive.

# zerando as variáveis
idade=0
cont=0
n=0
média=0

# Enquanto a idade não for negtiva
# vai lendo os dados
while idade!= -1:
    idade=int(input('Digite a idade: '))
    média+=idade
    cont+=1
    if idade>=25 and idade<=65:
        n+=1
        
# imprimindo os valores
print('Média de idade: ', round(média/cont))
print('Porcentagem de pessoas entre 21 e 65 anos', round((n*100)/cont), '%')    