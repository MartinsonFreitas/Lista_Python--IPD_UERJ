# 5. Crie um algoritmo que imprima o peso total que será carregado por um caminhão. 
# Sabe-se que este caminhão carrega 25 caixas. O peso de cada caixa deve ser informado pelo usuário.

pesoTotal=0
i=0

for i in range (i, 25, 1):
    peso=float(input('Digite o peso da caixa: '))
    pesoTotal=pesoTotal+peso
    
print('Peso total carregado é: ', pesoTotal)