# 30. Seu algoritmo deve ler as variáveis inteiras A e B. 
# Posteriormente, calcule o Máximo Divisor Comum (MDC) entre A e B 
# e a quantidade de divisores comuns entre A e B.
#
# Ver: https://www.ime.usp.br/~macmulti/exercicios/inteiros/12Python.html

A=int(input('Digite A: '))
B=int(input('Digite B: '))

# em cada iteração mdc é o candidato a mdc(n,m)
mdc = B
cont=0

while B % mdc != 0 or A % mdc != 0: 
    mdc = mdc - 1

if (A>B):
    maior=A
    menor=B
else:
    maior=B
    menor=A

for i in range(1, menor+1):
    if ((A%i==0) and (B%i==0)):
        cont=cont+1

print("MDC de (%d, %d) = %d" %(A,B,mdc))
print(cont)