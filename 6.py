# 6. Crie um algoritmo que leia a quantidade e o preço de 50 produtos comprados por uma empresa. 
# Ao final deve ser escrito o total gasto pela empresa.

totalGasto=0
qtdeTotalProdutos=0
i=0

#Coloquei o range até 5 pra testar... 
for i in range (i, 50, 1):
    produto=input('Digite o produto: ')
    qtde=int(input('Quantidade: '))
    preco=float(input('Digite o valor unitário: '))
    valorGastoProduto=qtde*preco
    print('Valor gasto em', qtde, produto, 'foi R$', valorGastoProduto)
    qtdeTotalProdutos=qtdeTotalProdutos+qtde
    totalGasto=totalGasto+valorGastoProduto
    
print('O gasto total em', qtdeTotalProdutos, ' produtos foi de R$', totalGasto)