# 12. Crie um algoritmo que calcule a soma dos primeiros 50 números pares. 
# Os primeiros números pares são: 2, 4, 6, ...

somaPar=0

for i in range(1,51):
     if i%2==0:        
        somaPar+=i
        
print('Total da soma dos números pares: ', somaPar)