# Fazer um programa para ler duas notas e imprimir a sua
# situação de acordo com os critérios da UERJ

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = float((n1+n2)/(2))
if media >= 7:
    print ('APROVADO ', media)
else:
    if media >= 4:
        print ('PROVA FINAL ', media)
    else:
        print ('REPROVADO ', media)