# 4. Crie um algoritmo que leia os nomes e os preços dos produtos de uma loja 
# e que escreva o nome do produto mais caro. 
#
# Considere que o final da lista é marcado pelo produto ‘XXX’ e que não existem preços repetidos.

maiorValor=0
nomeProduto=input('Insira o nome do produto: ')

while nomeProduto!='XXX':
    valor=float(input('Digite o valor do produto: '))
    
    if (valor>maiorValor):
        produto=nomeProduto
        maiorValor=valor
        
    nomeProduto=input('Insira o nome do produto: ')
    
print('O produto mais caro é ', produto, 'e custa ', maiorValor)