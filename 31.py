# 31. Faça a fatoração de um numero A inteiro, que é uma entrada do usuário. (leitura)
# Supondo, por exemplo, que A seja igual a 12, sua saída de ser:
# 2 ^ 2
# 3 ^ 1

n = int(input('Digite um número inteiro: '))
print('\nFatores:')
fator = 2 # primeiro fator

while n != 1:
    # conta a multiplicidade de fator em n
    mult = 0
    while n%fator == 0:
        n = n / fator
        mult = mult + 1

    # imprime a multiplicade do fator
    if mult != 0:        
        print("  %d ^ %d" %(fator, mult))

    fator = fator + 1