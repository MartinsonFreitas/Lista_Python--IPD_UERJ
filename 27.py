# 27. Crie um algoritmo que verifique se existe alguma raiz na equação Ax3 + Bx2 + Cx + D 
# no intervalo [-1.000, 1.000]. 
# Seu algoritmo deve ter os coeficiente A, B, C e D.
# 
# Dica: incremente o valor de x de uma unidade a cada interação e 
# verifique se houve uma mudança de sinal no resultado da equação, 
# se o sinal mudou, existe a ocorrência de uma raiz (não é necessário calcular a raiz).
#
# Ver código original: https://www.mecsoltech.com/single-post/2020/07/31/c%C3%B3digo-para-solu%C3%A7%C3%A3o-de-equa%C3%A7%C3%B5es-polinomiais-de-3-grau
# 
# Calculadora: https://www.blogcyberini.com/p/calculadora-de-equacoes-do-terceiro-grau.html

print ('Formato geral da equacao de 3° grau é  Ax^3 + Bx^2 + Cx + D = 0 \n')

a=float(input('Digite o valor de A: '))
#a=float(a) #Converte o texto num valor numérico real

b=float(input('Digite o valor de B: '))
b=float(b) #Converte o texto num valor numérico real

c=float(input('Digite o valor de C: '))
#c=float(c) #Converte o texto num valor numérico real

d=float(input('Digite o valor de D: '))
#d=float(d) #Converte o texto num valor numérico real

# Método de Newton Raphson:
x0=(2**0.5)
i = 0
MF = 1.0

while (MF > 10**(-17)):
    F = a*x0**3 + b*x0**2 + c*x0 + d
    dF = 3*a*x0**2 + 2*b*x0 + c

    if dF == 0.0:
        x1 = x0 - F/(dF + 10**(-13))

    else:
        x1 = x0 - F/dF

    F = a*x1**3 + b*x1**2 + c*x1 + d
    MF = abs(F)
    i=i+1
    x0=x1

    if i > 500:
        #print ("\nNão convergiu!\n")
        print('\n')
        break

print(f'x1 = {x0:.3f}') 

# Divisao de polinômios
A = a
B = a*x0 + b
C = a*x0**2 + b*x0 + c 

# Solução Equação de 2 grau
# Calculo do valor delta

delta = B**2 - 4*A*C

if delta>=0:

    x1=(-B-delta**0.5)/(2*A)
    x2=(-B+delta**0.5)/(2*A)

    print (f'x2 = {x1:.3f}')
    print (f'x3 = {x2:.3f}')

elif delta<0:

    raizdelta=complex(0,abs(delta))
    x1=(-B-raizdelta)/(2*A)
    x2=(-B+raizdelta)/(2*A)

    print (f'x2 = {x1:.3f}')
    print (f'x3 = {x2:.3f}')