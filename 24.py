# 24. Crie um algoritmo que imprima os N primeiros números que sejam primos 
# e façam parte da série de Fibonacci.
#
# Lembrando: A sequência de Fibonacci é uma sequência de números, 
# onde o número 1 é o primeiro e segundo termo da ordem 
# e os demais são originados pela soma de seus antecessores.

N = int(input("Digite um número: "))

if N < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if N >= 1:
        anterior=1
        atual=1
        total=0
        print('2')
        
        while (total < N-1):
            proximo = anterior + atual
            anterior = atual
            atual = proximo            
            
            x = 3
            # Quando 'x' for menor do que 'y'...
            while(x < proximo):
                # se a divisão de y/x tiver resto 0
                if proximo % x == 0:
                    # para o programa
                    break
                # caso não, acrescenta 2 a x
                x = x + 2
            # se x for igual a y
            if x == proximo:
                # imprime...
                print(x)
                # adiciona 1 no contador
                total = total + 1          