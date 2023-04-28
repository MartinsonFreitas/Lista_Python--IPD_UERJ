# 23. Crie um algoritmo de caixa eletrônico que lê a quantidade de dinheiro a ser sacado e 
# imprime a menor quantidade de notas a ser dada ao usuário. 
# Assume-se que existam notas de 50, 20, 10, 5 e 1. 
# Imprimir também a quantidade de cada nota a ser dada ao usuário. 
# O final da leitura é marcado pelo valor 0 que não deve ser calculado.
# Exemplo: 98 = uma nota de 50, duas notas de 20, uma nota de 5, e três notas de 1.

	
#Obter dados
valor=int(input("Digite um valor: "))
	
#Calcular quantas possíveis notas de 50 terei
# e armazenar o resto para calcular quantas terei das próximas notas/moedas
n50=int(valor/50)
resto=valor%50
	
# Calcular quantas possíveis notas de 20 terei
# e armazenar o resto para calcular quantas terei das próximas notas/moedas
n20=int(resto/20)
resto=resto%20
	
# Calcular quantas possíveis notas de 10 terei
# e armazenar o resto para calcular quantas terei das próximas notas/moedas
n10=int(resto/10)
resto=resto%10
	
# Calcular quantas possíveis notas de 5 terei
# e armazenar o resto para calcular quantas terei das próximas notas/moedas
n5=int(resto/5)
resto=resto%5
	
# Calcular quantas possíveis notas de 2 terei
# e armazenar o resto para calcular quantas terei das próximas notas/moedas
n2=int(resto/2)
resto=resto%2
	
# Depois de todo esse processo, se sobrar algum dinheiro será dado em notas de 1 (Ainda existem?!)
n1=resto
	
# Exibindo resultado
print('Necessarias', n50, 'notas de 50 \n', n20, 'notas de 20 \n', n10, 'notas de 10 \n', n5, 'notas de 5 \n', n2, 'notas de 2 \n e', n1, 'notas de 1 real')
	
