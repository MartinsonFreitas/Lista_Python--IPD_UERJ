# 36. Elabore um programa que calcule a quantidade de dias existentes entre duas datas. 
# Dica: utilize as variáveis D1, M1, A1, D2, M2, A2. Por hipótese, as variáveis dos anos 
# não precisam considerar a correção do calendário gregoriano. 
# 
# Lembre-se que há regras especiais de anos bissextos conforme o ano específico.
#
# Ver: https://medium.com/@mstuttgart/python-calculando-diferen%C3%A7a-de-dias-entre-duas-datas-f5b85accaeee

from datetime import datetime

# Exemplo fornecido pelo site acima...

# Data final
# d2 = datetime.strptime('2017-05-05', '%Y-%m-%d')
# Data inicial
# d1 = datetime.strptime('2017-05-01', '%Y-%m-%d')

# Realizamos o calculo da quantidade de dias
# quantidade_dias = abs((d2 - d1).days)
# print(quantidade_dias)

# A partir desse exemplo vamos ao que interessa

# Vamos ler a data inicial
d1 = datetime.strptime(input('Digite a data inicial (dd-mm-AAAA): '), '%d-%m-%Y')

# Vamos ler a data final
d2 = datetime.strptime(input('Digite a data final (dd-mm-AAAA): '), '%d-%m-%Y')

# Realizamos o calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days)
print(quantidade_dias)
