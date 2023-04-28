# 34. Implemente o jogo Blackjack ou 21. 
# No caso temos apenas dois jogadores, o cliente (humano) e a banca (computador). 
# O ás pode valer 1 ou 11, de acordo com as cartas que o jogador possui. 
# O valete (J), a dama (Q) e o rei (K) valem 10. 
# A simulação da obtenção das cartas deve ser feita com o uso de números aleatórios
# (Dica: carta  RAND(12) +1, isto é, variando de 1 a 13).
# Os números 11, 12 e 13 representam respectivamente J, Q e K. 
# Não há a necessidade de representar um baralho real de 52 cartas. 
# O cliente recebe inicialmente duas cartas aleatoriamente e decide se pede outra ou não, dependendo do somatório. 
# Caso a soma das cartas seja maior que 21, o cliente perde. 
# O cliente pode passar a vez para a banca (que não possui cartas no início do jogo), que, 
# para vencer, terá que obter obrigatoriamente um número maior que o cliente e MENOR do que 21, 
# caso contrário, o cliente ganha. O jogo tem apenas uma rodada. Informe quem ganhou ou se houve empate.

# referências: 
# https://gist.github.com/mjhea0/5680216
# http://blog.abraseucodigo.com.br/exercicio-03-blackjack-parte-01-grupo-de-estudos-python.html
# https://www.vivaolinux.com.br/script/Blackjack-simples-para-estudo-de-iniciantes-em-Python

import os                           #Necessário para limpar a tela
import random                       #Necessário para utilizar a função random
import time                         #Necessário para utilizar a função sleep
#Variáveis que armazenam as opções dos jogadores em relação ao jogo.
opjogo = 0
jogada = 0
totalj = 0
totalc = 0
#Variáveis da jogada atual e do total de pontos.
total1 = 0
total2 = 0
print("Bem Vindo ao BlackJack em Python!! \n")
opjogo =input("Quantos jogadores participarão da partida? \n")
if opjogo == '1':
#Vez do usuário.
    opjogo='S'
    os.system('clear')
    print("Você tem que fazer 21 pontos para ganhar, porém sem estourar esse limite, podendo parar após cada jogada.\n");
    print
    totalj=0
    while opjogo=='s' or opjogo=='S':   #Laço que deixa as jogadas a critério do usuário.
        opjogo = input("Deseja fazer a jogada?[S/N] \n")
        if opjogo=='n' or opjogo=='N':
            break
        jogada= random.randint(1,10) #Gera números aleatórios de 1 até 10.
        totalj=(totalj+jogada)
        if totalj >= 21:
            break
        print
        print("Você tirou {0} e até agora marcou {1} pontos.\n".format(jogada,totalj))
        print

    print("Você marcou {0} pontos, vamos ver o computador...\n".format(totalj))
    #Vez do Computador
    print("Agora é minha vez de jogar. Vejo que você fez {0} pontos...\n".format(totalj))
    totalc=0
    while (totalc < 21):
        jogada= random.randint(1,10) #Gera números aleatórios de 1 até 10.
        totalc=(totalc+jogada)
        if totalj > 21:
                break
        print("Tirei {0} pontos e pretendo continuar jogando, pois ainda estou com {1}.\n".format(jogada,totalc))
        time.sleep(1.2)

    print

    print("O jogador terminou com {0} pontos e o computador com {1} pontos, portanto...".format(totalj,totalc))
    if totalj == 21:
        print("O jogador ganhou, fazendo os gloriosos 21 pontos =D...\n")
    elif totalc == 21:
        print("O computador ganhou, fazendo os gloriosos 21 pontos =D...\n")
    elif totalc > 21 and totalj <= 21:
        print("O computador tem um número maior de pontos do que é permitido...O jogador vence.\n")
    elif totalj > 21 and totalc <= 21:
        print("O jogador tem um número maior de pontos do que é permitido...O computador vence.\n")
    elif 21 - totalc > 21 - totalj:
        print("O computador vence por estar mais perto de 21.\n")
    elif 21 - totalc < 21 - totalj:
        print("O jogador vence por estar mais perto de 21.\n")
        print

if opjogo=='2':
    print("O jogo funciona por turnos, cada jogador terá sua vez e decidirá o que fazer...\n")
#Vez do jogador número 1.
    opjogo='S'
    os.system('clear')
    print("Você tem que fazer 21 pontos para ganhar, porém sem estourar esse limite, podendo parar após cada jogada.\n")
    print
    totalj=0
    while opjogo=='s' or opjogo=='S':        #Laço que deixa as jogadas a critério do usuério.
        opjogo = input("Deseja fazer a jogada?[S/N] \n")
        if opjogo=='n' or opjogo=='N':
            break
        jogada= random.randint(1,10) #Gera números aleatórios de 1 até 10.
        total1=(total1+jogada)
        if totalj >= 21:
            break
        print
        print("Você tirou {0} e até agora marcou {1} pontos.\n".format(jogada,totalj))
        print
#Vez do jogador número 2.
    opjogo='S'
    os.system('clear')
    print("Você tem que fazer 21 pontos para ganhar, porém sem estourar esse limite, podendo parar após cada jogada.\n")
    print("Cuidado, pois o jogador 1 marcou {0} pontos".format(total1))
    print
    totalj=0
    while opjogo=='s' or opjogo=='S':   #Laço que deixa as jogadas a critério do usuário.
        opjogo = input("Deseja fazer a jogada?[S/N] \n")
        if opjogo=='n' or opjogo=='N':
            break
        jogada= random.randint(1,10) #Gera números aleatórios de 1 atÃ© 10.
        total2=(total2+jogada)
        if total2 >= 21:
            break
        print
        print("Você tirou {0} e até agora marcou {1} pontos.\n".format(jogada,total2))

    print("O jogador 1 terminou com {0} pontos e o jogador 2 com {1} pontos, portanto...".format(total1,total1))
    if total1 == 21:
        print("O jogador 1 ganhou, fazendo os gloriosos 21 pontos =D...\n")
    elif total2 == 21:
        print("O computador ganhou, fazendo os gloriosos 21 pontos =D...\n")
    elif total2 > 21 and total1 <= 21:
        print("O computador tem um número maior de pontos do que é permitido...O jogador vence.\n")
    elif total1 > 21 and total2 <= 21:
        print("O jogador tem um número maior de pontos do que é permitido...O computador vence.\n")
    elif total1==total2:
        print("Houve um empate...")
    elif 21 - total2 > 21 - total1:
        print("O jogador 2 vence por estar mais perto de 21.\n")
    else:
        print("O jogador 1 vence por estar mais perto de 21.\n")
        print

else:
    print("O máximo de jogadores permitidos é de 2 \n")