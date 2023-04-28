# 16. Crie um algoritmo que:
# a) Leia e escreva o nome e a altura das moças inscritas em um concurso de beleza, 
# até que seja digitada o nome ‘MARIA’, que marca o final da lista, mas é para ser computada no concurso.
# b) Calcule e escreva as duas maiores alturas e quantas moças as possuem.

maiorAltura=0
segundaMaiorAltura=0
contMaior=0
contSegMaior=0

nome=input('Digite o seu nome: ')

while (nome!='Maria'):
    altura=float(input('Digite a sua altura: '))
    
    # Se a altura for maior
    if (altura>maiorAltura):
        # zera o contador
        contMaior=0
        # salva a maior altura
        maiorAltura=altura
        # conta as candidatas
        contMaior=contMaior+1
        
    #Se não for...    
    else:
        # Se a altura for igual a maior altura
        # conta mais uma candidata
        if(altura==maiorAltura):
            contMaior=contMaior+1
    #    else:
            # Compara se a altura é maior do a segunda maior altura
            # Se chegou até aqui é por que é menor do que a maior altura
        elif(altura>segundaMaiorAltura):
                # Se for maior... Zera o contador das candidatas com a segunda maior altura
            contSegMaior=0
                # Salva a nova segunda maior altura
            segundaMaiorAltura=altura
                # e inicia o contador...
            contSegMaior=contSegMaior+1
            # se a altura for igual a segunda maior altura
            # soma mais uma candidata no contador...
        elif(altura==segundaMaiorAltura):
            contSegMaior=contSegMaior+1
            
    # se não for... Inicia o processo todo de novo...
    # até o nome adicionado ser Maria
    nome=input('Digite o seu nome: ')
                
print( contMaior,'candidatas possuem a altura máxima registrada de ', maiorAltura, 'cm ')
print( 'E', contSegMaior, 'candidatas possuem a altura de ', segundaMaiorAltura, 'cm ')