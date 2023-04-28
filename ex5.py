# Fazer um programa em PYTHON para ler o nome, sexo e duas notas dos alunos de
# uma turma até que seja digitado o nome FIM. Imprimir a média pessoal APENAS das
# alunas. Imprimir também a média aritmética dos homens.

cont = 0
soma = 0
nome = input('nome: ')

while nome != 'fim':
    sexo = input('sexo: ')
    n1 = float(input('n1: '))
    n2 = float(input('n2: '))
    mediaPessoal = float((n1+n2)/2)
    if sexo == 'f':
        print ('media f:', mediaPessoal)
    else:
        cont += 1
        soma = soma + mediaPessoal
        
    nome = input('nome: ')
    
print ('media homens: ', float(soma/cont))