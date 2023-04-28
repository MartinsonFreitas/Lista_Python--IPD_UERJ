# 26. Crie um algoritmo que leia N números inteiros positivos e responda se é possível formar um polígono 
# com o mesmo (dica: maior número < soma dos demais números).

print('A coleta de dados terminará quando digitado 0\n')

cont=0
soma=0
maior=0
N=int(input('Digite a medida de um dos lados do polígono: '))

while(N>0):
    
    soma=soma+N
    
    if (N>maior):
        maior=N
        
    cont=cont+1
    N=int(input('Digite a medida de um dos lados do polígono: '))
        
soma=soma-maior
#print('\n',soma,'\n')

if (cont>=3 and maior<soma):
    print('É um polígono de ', cont, 'lados', 'e perímetro, ', soma+maior)
else:
    print('Não é um polígono')