# 25. Crie um algoritmo que leia as taxas de juros (r) de um financiamento price (1% é igual a 0,01), 
# os valores das parcelas (pmt) e o número de parcelas (n).
#
# Em seguida, calcule o valor presente do financiamento que é feito pela seguinte fórmula: 
# ∑ de 𝑛 a i=1 : 𝑝𝑚𝑡/(1 + 𝑟)*i

print('Informe os dados a seguir para cálculo do Financiamento\n')

# Juros nominal
juros=float(input('Digite a taxa de juros ao mês: '))
# Cálculo do juros
r=float(juros/100)
# valor da parcela
pmt=float(input('Digite o valor da parcela: '))
# número de parcelas
n=int(input('Digite o número de parcelas: '))
soma=0

for i in range(1,n):
    PV=(pmt/( ( (1+r)**i)))
    soma=soma+PV
    total=round(soma,3)
print(f'R$ {total:.2f}')