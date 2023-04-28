# 33. Jogo de dados. Dois jogadores estão confrontando-se entre si, usando dois dados, 
# numerados de 1 até 6 (dado --> RAND(5) + 1). Vence uma rodada quem obtiver o maior número no lançamento.
#
# Entretanto, caso um jogador obtiver um lançamento com dois dados iguais (por exemplo, 1 e 1, 2 e 2, ) 
# e o outro jogador não, o jogador que tiver lançado a dupla ganha. Caso os dois jogadores fizerem o 
# lançamento e o resultado for de duas duplas para os dois jogadores, ganha o jogador com a dupla maior. 
# A disputa é em 11 lançamentos. 
# Indique o jogador vencedor ou se houve empate.

# biblioteca que utiliza a função geradora de números randômicos
import random

# A ideia inicial do jogo é registrar o nome de dois jogadores e atribuir a eles a soma dos dados rolados
jogador1 = input("Jogador 1: Digite o seu nome ")
jogador2 = input("Jogador 2: Digite o seu nome ")

print("\nVamos iniciar  Jogo!\n")

# zeramos os totalizadores
jogada=1
resultado_dupla1=0
resultado_dupla2=0
total1=0
total2=0
score1=0
score2=0

for jogada in range(1,11):    
    
    if (jogada%2 !=0):
        # atribuindo valores randômicos aos dados do jogador 1
        dado1 = random.randrange(1, 7)
        dado2 = random.randrange(1, 7)
        total1=dado1+dado2
        
        if (dado1==dado2):
            resultado_dupla1=dado1
            print('Temos uma dupla de ', dado1, 'para ', jogador1)
        else:
            print=('Total de pontos do ', jogador1, 'é', total1)
    else:
        # atribuindo valores randômicos aos dados do jogador 2
        dado3 = random.randrange(1, 7)
        dado4 = random.randrange(1, 7)
        total2=dado3+dado4
        if (dado3==dado4):
            resultado_dupla2=dado3
            print('Temos uma dupla de ', dado3, 'para ', jogador2)
        else:
            print=('Total de pontos do ', jogador2, 'é', total2)
       
    # comparamos os totais dos lançamentos para ver quem ganhou a rodada e pontuamos o score do jogador
    # Primeiramente vamos comparar se houve valor igual no lançamento de dados...
    
    # houve empate no jogo de dados com duas duplas???
    if(resultado_dupla1==resultado_dupla2):
        print('Houve empate na rodada!')
        score1=score1+1
        score2=score2+1
        
    # dados iguais pro jogador 1 > do jogador 2
    elif(resultado_dupla1>resultado_dupla2):
        print('Vencedor da rodada é ', jogador1)
        score1=score1+1  
        
    # dados iguais pro jogador 2 > do jogador 1
    elif(resultado_dupla2>resultado_dupla1):
        print('Vencedor da rodada é ', jogador2)
        score2=score2+1
    
    # Não houve duplas total jogador 1 > jogador 2
    elif(total1>total2):
         print('Vencedor da rodada é ', jogador1)
         score1=score1+1
         
    # Não houve duplas total jogador 2 > jogador 1
    elif(total2>total1):
         print('Vencedor da rodada é ', jogador2)
         score2=score2+1
         
    # houve empate no total dos dados
    else:
         print('Houve empate na rodada ' , jogada)
         score1=score1+1
         score2=score2+1
    
    # adiciona 1 no contador da jogada
    jogada=jogada+1
        