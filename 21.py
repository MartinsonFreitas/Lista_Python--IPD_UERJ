# Crie um algoritmo que imprima os 4 primeiros números perfeitos.
# Um número é perfeito quando a soma dos seus divisores é igual a ele mesmo.
#
# Exemplo: 
#   6 = 3 + 2 + 1
#   28 = 1 + 2 + 4 + 7 + 14; 
#   496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248; 
#   8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064

# Referência:
# https://pt.stackoverflow.com/questions/331864/como-calcular-n%C3%BAmeros-perfeitos-de-forma-r%C3%A1pida

# importando a Classe Math para usar as funções Matemáticas
# --> math.ceil(x)
#       Retorna o limite máximo de x, o menor inteiro maior ou igual que x. Se x não é um float, 
#       delega para x.__ceil__, cujo qual deve retornar um valor do tipo Inteiro.
# 
# --> math.sqrt(x)
#       Retorna a raiz quadrada de x.
#
# Referências: https://docs.python.org/pt-br/3/library/math.html
import math

# Cria um laço de 2 a 8129, já que o próximo número perfeito é: 33.550.336
for n in range(2, 8129):
    soma = 1
    # Laço de 2 até a parte inteira da raiz quadrada de 'n'
    for div in range(2, math.ceil(math.sqrt(n))):
        # pega n/div, se o resto for 0 soma o divisor
        if n % div == 0:
            soma += div
            # div2 é igual a parte inteira da divisão de n/div
            div2 = int(n / div)
            # se o div for diferente de div2, soma div2
            if (div != div2):
                soma += div2
            # se a soma for maior do que n... Para o programa!
            if soma > n:
                break
    # se n for igual a soma... Imprime!        
    if n == soma:
        print(n, 'é um número perfeito')
