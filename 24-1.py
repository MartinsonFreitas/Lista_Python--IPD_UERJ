# 24. Crie um algoritmo que imprima os N primeiros números que sejam primos 
# e façam parte da série de Fibonacci.
#
# Lembrando: A sequência de Fibonacci é uma sequência de números, 
# onde o número 1 é o primeiro e segundo termo da ordem 
# e os demais são originados pela soma de seus antecessores.
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
          73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
          163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 
          251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 
          349, 353, 359, 367, 373, 379, 383, 389, 397]


N = int(input("Digite um número: "))
anterior=1
atual=1

if N < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if N >= 1:
        # 2 é o 1ª número primo
        #print("2")
        x=2
        # p é o contador de primos
        p = 1
        # 3 é o 2º número primo
        y = 3
        # enquanto o número de primos for menor que 'n'
        while p < N:
            proximo = anterior + atual
            anterior = atual
            atual = proximo
            
            #if (anterior==x):
            print('Esse é um número de Fibonacci: ',anterior)
 
            x = 3
            # Quando 'x' for menor do que 'y'...
            while(x < y):
                # se a divisão de y/x tiver resto 0
                if y % x == 0:
                    # para o programa
                    break
                # caso não, acrescenta 2 a x
                x = x + 2
            # se x for igual a y
            if x == y:
                # imprime...
                print('Esse é um número primo: ', x)
                # adiciona 1 no contador de primos
                p = p + 1
            # adiciona 2 em y para continuar...
            y = y + 2