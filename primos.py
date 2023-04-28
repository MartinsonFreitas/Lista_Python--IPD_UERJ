# 19. Crie um algoritmo que leia um número N e imprima os N primeiros números primos.

n = int(input("Digite um número: "))
if n < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if n >= 1:
        # 2 é o 1ª número primo
        print("2")
        # p é o contador de primos
        p = 1
        # 3 é o 2º número primo
        y = 3
        # enquanto o número de primos for menor que 'n'
        while p < n:
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
                print(x)
                # adiciona 1 no contador de primos
                p = p + 1
            # adiciona 2 em y para continuar...
            y = y + 2