# 33. Jogo de dados. Dois jogadores estão confrontando-se entre si, usando dois dados, 
# numerados de 1 até 6 (dado --> RAND(5) + 1). Vence uma rodada quem obtiver o maior número no lançamento. 
# Entretanto, caso um jogador obtiver um lançamento com dois dados iguais (por exemplo, 1 e 1, 2 e 2, ) 
# e o outro jogador não, o jogador que tiver lançado a dupla ganha. Caso os dois jogadores fizerem o 
# lançamento e o resultado for de duas duplas para os dois jogadores, ganha o jogador com a dupla maior. 
# A disputa é em 11 lançamentos. 
# Indique o jogador vencedor ou se houve empate.

import random       
import sys 
a = input("TO START THE GAME TYPE 'yes' and TO QUIT TYPE 'no'\n") 
if a.lower() == "no": 
    sys.exit() 
else: 
    print("LET'S START THE GAME")  
      
a = input("welcome to the game of chance,are you ready to test your fortune ,\ndo you need instructions type (yes) or (no) \n") 
  
if a.lower() == "yes": 
    print(
                                ) 
  
elif a.lower() == "no": 
    print("all the best, player") 
  
  
def diceNumber(): 
    
    _ = input("press enter to roll the dice ") 
      
    
    
    die1 = random.randrange(1, 7) 
    die2 = random.randrange(1, 7) 
      
    
    
    return (die1, die2)   
def twoDice(dices): 
    die1, die2 = dices 
    print("player- the sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1, die2, sum(dices))) 
  
  
value = diceNumber() 
twoDice(value) 
sum_of_dices = sum(value) 
  
  
if sum_of_dices in (7, 11): 
    result = "congratulations you won"
elif sum_of_dices in (2, 3, 12): 
    result = "you lost, \ntry again next time"
      
else:   
    result = "continue your game please"
    currentpoint = sum_of_dices 
    print("good game, your current point is", currentpoint) 
  
  
while result == "continue your game please": 
    value = diceNumber() 
    twoDice(value) 
    sum_of_dices = sum(value) 
      
    if sum_of_dices == currentpoint: 
        result = "congratulations you won"
          
    elif sum_of_dices == 7: 
        result = "you lost,\n try again next time"
if result == "congratulations you won": 
    print("congratulations,you won") 
      
else: 
    print("you lost, \ntry again next time")