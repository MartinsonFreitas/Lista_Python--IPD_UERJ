# 1.	A prefeitura de uma cidade resolveu fazer uma pesquisa entre os seus trabalhadores. 
# Para isso ela coletou alguns dados como idade, sexo (M ou F) e salário. 
# Crie um algoritmo que leia estes dados e que escreva ao final:
# a)	a média salarial dos homens, a média salarial das mulheres
# b)	o maior salário encontrado entre as pessoas abaixo de 30 anos. 
# Obs: O final da leitura de dados é marcado por uma idade negativa.

maiorSal = -1
# M asculino 
# F eminino
# Soma os Salários de acordo com o sexo
somaSalF = 0
somaSalM = 0
# Cálculo da Média salarial de acordo com o sexo
mediaSalF = 0
mediaSalM = 0
# Contador de funcionários Masculinos e Femininos
totalF = 0
totalM = 0

# Lê a idade do Funcionário
idade=int(input('Digite a sua idade: '))
# Enquanto a idade for positiva, vai rodando o barco
while idade>0:
    # Lê o sexo do Funcionário
    sexo=input('Sexo (M ou F): ')
    # Lê o salário do Funcionário
    salario=float(input('Digite o seu salário: '))
    # compara a idade... Se for menor do que 30 anos
    # compara o salário do Funcionário com o maior salário cadastrado, 
    # que por estratégia, foi colocado como -1,
    # assim qualquer salário positivo, tomará o lugar do registrado e tomará o 
    # seu lugar de referência.
    if idade <= 30 and salario > maiorSal:
        # Comparou? Se for maior toma o lugar
        maiorSal=salario
        # Se não for maior o barco continua em frente...
    # Verifica o sexo do Funcionário
    # Masculino?    
    if sexo=='M':
        # Pega o valor do salário e soma aos salários já registrados
        # iniciamos essa variável com 0
        somaSalM=somaSalM + salario
        # Adiciona 1 na contagem de funcionários Masculinos para calcular a Média
        # dos salários
        totalM+=1
    # Se não for Masculino, só pode ser Feminino (De acordo com o programa!)
    else:
        #Soma o salário
        somaSalF = somaSalF + salario
        # Adiciona 1 no contador de funcionários Femininos para calcular a Média
        # dos salários das Mulheres
        totalF+=1
     # Volta ao início do registro das idades, até que a Idade seja menor que 0
     # ou negativa, como pede o enunciado   
    idade=int(input('Digite a sua idade: '))
# Imprime os resultados
# Cálculo da média salarial Feminino
print('Media Salarial das Mulheres é: ', float(somaSalF/totalF))
# Cálculo da média salarial Masculino
print('Media Salarial das Homens é: ', float(somaSalM/totalM))
# Imprime o maior salário entre os funcionários abaixo de 30 anos
print('Maior salário registrado de funcionários abaixo de 30 anos é: ', maiorSal)