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

print("\nVamos iniciar  Jogo!\n")

# zeramos os totalizadores
rodada=0
resultado_dupla1=0
resultado_dupla2=0
score1=0
score2=0

# iniciamos as rodadas
for rodada in range(1, 12):
    _=input('\nJogador 1 aperte ENTER para continuar!\n')
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    total1= dado1+dado2

    print('dado 1 = ', dado1)
    print('dado 2 = ', dado2)
    print('Total = ', total1)
      
    _=input('\nJogador 2 aperte ENTER para continuar!\n')
    
    dado3 = random.randrange(1, 7)
    dado4 = random.randrange(1, 7)
    total2= dado3+dado4

    print('dado 1 = ', dado3)
    print('dado 2 = ', dado4)
    print('Total = ', total2)
        
    # analisando se os dados dos dois jogadores são iguis
    if(dado1==dado2 and dado3==dado4):
        if(total1>total2):
            score1=score1+1
        elif(total2>total1):
            score2=score2+1
        else:
            score1=score1+1
            score2=score2+1
    
    # analisando se apenas um dos jogadores possui dados iguais
    elif(dado1==dado2 or dado3==dado4):
        if(dado1==dado2):
            score1=score1+1
        else:
            score2=score2+1
    
    # analisando o valor total obtido nos dados
    # se o total da soma dos dados do jogador 1 for maior do que o jogador 2
    # jogador 1 pontua
    elif(total1>total2):
        score1=score1+1
     # se o total da soma dos dados do jogador 2 for maior do que o jogador 1
    # jogador 2 pontua   
    elif(total2>total1):
        score2=score2+1
    # se nada anterior até aqui aconteceu, quer dizer que o total dos dados
    # dos dois jogadores são iguais e ambos pontuam
    else:
        score1=score1+1
        score2=score2+1
        
    print('\nPontuação do jogador 1: ', score1)
    print('Pontuação do jogador 2: ', score2)
    
if(score1>score2):
    print('\nJogador 1 é vencedor com %d rodadas vencidas' %(score1))
elif(score2>score1):
    print('\nJogador 2 é vencedor com %d rodadas vencidas' %(score2))
else:
    print('\nHouve empate entre os jogadores, jogador 1 pontuou em %d rodadas e jogador 2 em %d ' %(score1, score2))