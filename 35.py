# 35. Jogo da subtração. 
# 
# Seu algoritmo deverá ler uma variável positiva T e
# posteriormente mais três variáveis positivas S1, S2 e S3, 
# sendo que estas variáveis são obrigatoriamente menores que T. 
# 
# O jogo consiste de dois jogadores, J1 e J2. 
# 
# A cada rodada a variável T é subtraída por uma das variáveis S1 ou S2 ou S3, 
# escolhida pelo jogador da rodada. 
# 
# Perde o jogo quando o jogador ao executar sua subtração, obtém um valor menor do que zero.
# O seu programa deve apontar o jogador VENCEDOR.

# Declaração de variáveis utilizadas
opjogo='S'

print("Bem Vindo ao Jogo da Subtração em Python!!\n")

T = int(input('Digite um número inteiro: '))
S1 = int(input('Digite um número menor do que o primeiro: '))
S2 = int(input('Digite um número menor do que o primeiro: '))
S3 = int(input('Digite um número menor do que o primeiro: '))

totalj1 = T
totalj2 = T

print
print('Perde o jogo quando o jogador ao executar sua subtração, obtém um valor menor do que zero.')
print("\nVamos iniciar  Jogo!\n")

while opjogo=='s' or opjogo=='S':   #Laço que deixa as jogadas a critério do usuário.
    opjogo = input("Jogador 1 deseja fazer a jogada?[S/N] \n")
    if opjogo=='n' or opjogo=='N':
        break
    
    x=int(input('Escolha o número a ser subtraído: 1 - 2 - 3: '))
    if(x==1):
        totalj1 = totalj1-S1
    elif(x==2):
        totalj1 = totalj1-S2
    elif(x==3):
        totalj1 = totalj1-S3
    
print
print('Agora é a vez do jogador 2!')
print

opjogo='S'

while opjogo=='s' or opjogo=='S':   #Laço que deixa as jogadas a critério do usuário.
    opjogo = input("Jogador 2 deseja fazer a jogada?[S/N] \n")
    if opjogo=='n' or opjogo=='N':
        break
    
    x=int(input('Escolha o número a ser subtraído 1 - 2 - 3: '))
    if(x==1):
        totalj2 = totalj2-S1
    elif(x==2):
        totalj2 = totalj2-S2
    elif(x==3):
        totalj2 = totalj2-S3
    
print
print('O vendcedor é!!!!')
print

print("O jogador 1 terminou com {0} pontos e o jogador com {1} pontos, portanto...".format(totalj1,totalj2))
if totalj1 < 0:
    print("O jogador 2 ganhou, pois o jogador 1 negativou a pontuação!\n")
elif totalj2 < 0:
    print("O jogador 1 ganhou, pois o jogador 2 negativou a pontuação!\n")
elif totalj1 > totalj2:
    print("O jogador 1 tem um número maior de pontos do que o jogador 2... O jogador 2 venceu!\n")
elif totalj1 < totalj2:
    print("O jogador 2 tem um número maior de pontos do que o jogador 1... O jogador 1 venceu!\n")
else:
    print("Houve empate na jogada!")