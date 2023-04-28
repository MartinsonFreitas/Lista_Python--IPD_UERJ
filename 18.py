# 18. Crie um algoritmo que leia um número N e verifique se ele é primo.
count = 0
n = int(input('Digite o Número: '))
multiplos = 0

while multiplos <= n or count < 2:
    multiplos += 1
    p = n % multiplos
    
    if p == 0:
        count += 1        
        print('Multiplos ', multiplos)
    
if count <= 2:
    print('\n',n, 'é Primo')
else:
    print('\n',n, 'Não é primo')