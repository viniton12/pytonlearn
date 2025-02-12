import math
#cotação das moedas 

#dolar = 5,75 reais
#euro = 6, 09 reais
#iene = 0,037 reais
# yuan = 0,79 reais

print('conversor de moeda')

print('digite o valor que deseja converter:')
valor = float(input('valor'))

dolar = valor / 5.75
euro = valor / 6.09
iene = valor / 0.037
yuan = valor / 0.79

print('{:.0f} reais equivalem a {:.2f} dolares \n {:.2f} euros \n {:.2f} ienes \n {:.2f} yuans'.format(valor, dolar, euro, iene, yuan))

#convertendo outras moedas para real
print('-----------------')
print('insira o valor')
valor1 = float(input("valor"))

dolar_para_real = valor1 * 5.75
euro_para_real = valor1 * 6.09
iene_para_real = valor1 * 0.037
yuan_para_real = valor1 * 0.79

print('{} dolares são {} reais \n {} euros são {} reais \n {} ienes são {} reais \n {} yuans são {} reais'.format(valor1, dolar_para_real, valor1, euro_para_real, valor1, iene_para_real, valor1, yuan_para_real))
