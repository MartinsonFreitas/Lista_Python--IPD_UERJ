# 29. Crie um algoritmo que leia um número decimal (com qualquer número de dígitos) e o 
# converta para a base hexadecimal.
#
# Ver: https://pt.stackoverflow.com/questions/217090/convers%C3%A3o-decimal-para-hexadecimal

hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
n = int(input("\nDigite um número inteiro: "))
r = []
print('O número convertido em Hexadecimal é:')

while n > 0:
    r.append(hex[(n % 16)])
    n = n // 16
for i in range(len(r)-1,-1,-1):
    print(r[i],end="")
    
print('\n')