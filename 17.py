# 17. Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um novo produto lançado 
# no mercado. Para isso, forneceu o sexo do entrevistado e sua resposta (sim ou não). 
# Sabendo-se que foram entrevistadas 2.000 pessoas, crie um algoritmo que calcule e escreva:
# a) o número de pessoas que responderam sim;
# b) o número de pessoas que responderam não; 
# c) a porcentagem de pessoas do sexo masculino que responderam não.

cont_Sim = 0
cont_Nao = 0
cont_M=0
cont_M_N = 0

for i in range(0,5):
    sexo=input('Digite o sexo (M/F):')
    resposta=input('Gostou do produto (S/N):')
    
    if sexo == 'M':
        cont_M=cont_M+1
    
    if resposta == 'S':
        cont_Sim=cont_Sim+1
    else:
        cont_Nao=cont_Nao+1
        if sexo == 'M':
            cont_M_N=cont_M_N+1

porcentagem=round((cont_M_N/cont_M)*100, 2)

print('Pessoas que gostaram: ', cont_Sim)
print('Pessoas que não gostaram: ', cont_Nao)
print('A porcentagem de homens que não gostaram: ', porcentagem, '%')