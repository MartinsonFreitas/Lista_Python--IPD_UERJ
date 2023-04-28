#10.	Uma empresa lançou um novo produto no mercado e fez uma pesquisa para saber se os consumidores 
# estavam satisfeitos, para isso eles deveriam responder sim ‘S’ ou não ‘N’. 
# 
# Crie um algoritmo que leia a resposta de todas as pessoas e escreva a porcentagem dos que disseram sim 
# e dos que disseram não. 
# 
# Obs: O final da leitura de dados é marcado pela resposta ‘F’.

# zerando as variáveis
resposta=' '
sim=0
nao=0

# Lê as opiniões até ser digitado F
while resposta !='F':
    resposta=input('Esta satisfeito com o produto? ')
    if resposta=='S' or resposta=='s':
        sim+=1
    elif resposta=='N' or resposta=='n':
        nao+=1

# printa o resultado
print('Total de pessoas que gostaram do produto: ', round(sim*100)/(sim+nao),'%')
print('Total de pessoas que não gostaram do produto: ', round(nao*100)/(sim+nao),'%')
