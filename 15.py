# 15. Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão contendo seu número de 
# identificação e seu peso. Crie um algoritmo que escreva o número e peso do boi mais gordo e do boi mais magro.
# Além disso, responda: se houver dois ou mais bois com o mesmo peso, maior que todos os demais, 
# este algoritmo escreverá o número de qual deles?

qtdBois = 0
PMG = 0
pmm = 2000

for qtdeBois in range(qtdBois,5,1):
    NBoi=input('informe o numero de identificacao: ')
    PBoi=float(input('informe o peso do boi: '))
    if( PBoi > PMG ):
        PMG = PBoi
        NMG = NBoi

    if ( PBoi < pmm ):
        pmm = PBoi
        nmm = NBoi

print( "Boi mais gordo: ", NMG, " pesou ", PMG )
print( "Boi mais magro: ", nmm, " pesou ", pmm )