# Faça um programa que mostre os números ENTRE 100 e 200 que
# divididos por 7 dão resto 4

num = 101
while num < 200:
    if num % 7 == 4:
        print (' ', num)
    num += 1