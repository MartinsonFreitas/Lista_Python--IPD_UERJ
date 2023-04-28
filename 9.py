# 9.	Crie um algoritmo que apure os votos de uma eleição municipal, numa cidade com 20.000 eleitores, 
# onde concorreram quatro candidatos. Um servidor da Justiça Eleitoral digitará cada voto individualmente. 
# Cada voto equivale a um número inteiro. 
# 
# Os votos válidos podem ser 1, 2, 3 e 4, e estão relacionados aos seguintes candidatos:# 
# 1 – João da Silva 
# 2 – José Ramalho 
# 3 – Maria Mattos
# 4 – Pedro Américo

# atribuindo o total de votos de cada candidato
joão=0
josé=0
maria=0
pedro=0
branco=0
nulo=0

# executa o laço para ler 20.000 votos
#for i in range (1,20001):
# para testar usamos apenas 10
for i in range (1,11):
    voto=int(input('Digite seu voto: '))
    if voto== 1:
        joão+=1
    elif voto==2:
        josé+=1
    elif voto==3:
        maria+=1
    elif voto==4:
        pedro+=1
    elif voto==0:
        branco+=1
    else:
        nulo+=1

# imprimimos os resultaods
print('Total de votos do candidato João da Silva: ', joão,'votos')
print('Total de votos do candidato José Ramalho: ', josé,'votos')
print('Total de votos do candidato Maria Mattos: ', maria,'votos')
print('Total de votos do candidato Pedro Américo: ', pedro,'votos')
print('Total de votos Brancos: ', branco,'votos')
print('Total de votos Nulos: ', nulo,'votos')

# Simples assim!