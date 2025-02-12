import math

#faazendo uma tabuada em pyton

print('digite o valor para fazer a operação')
valor = float(input('valor'))

#soma

n1 = valor + 1
n2 = valor + 2
n3 = valor + 3
n4 = valor + 4
n5 = valor + 5
n6 = valor + 6
n7 = valor + 7
n8 = valor + 8
n9 = valor + 9

#subtração

n10 = valor - 1
n11 = valor - 2
n12 = valor - 3
n13 = valor - 4
n14 = valor - 5
n15 = valor - 6
n16 = valor - 7
n17 = valor - 8
n18 = valor - 9

#multiplicação

n19 = valor * 1
n20 = valor * 2
n21 = valor * 3
n22 = valor * 4
n23 = valor * 5
n24 = valor * 6
n25 = valor * 7
n26 = valor * 8
n27 = valor * 9

#divisão 

n28 = valor / 1
n29 = valor / 2
n30 = valor / 3
n31 = valor / 4 
n32 = valor / 5
n33 = valor / 6
n34 = valor / 7
n35 = valor / 8
n36 = valor / 9

raiz = math.sqrt(valor)

print('os resultados para esse valor são:')
print('------------')
print(" {:.0f} + 1 = {:.0f} \n {:.0f} + 2 = {:.0f} \n {:.0f} + 3 = {:.0f} \n {:.0f} + 4 = {:.0f} \n {:.0f} + 5 = {:.0f} \n {:.0f} + 6 = {:.0f} \n {:.0f} + 7 = {:.0f} \n {:.0f} + 8 = {:.0f} \n {:.0f} + 9 = {:.0f}".format(valor,n1,valor,n2,valor,n3,valor,n4,valor,n5,valor,n6,valor,n7,valor,n8,valor,n9))
print('------------')
print("{:.0f} - 1 = {:.0f} \n {:.0f} - 2 = {:.0f} \n {:.0f} - 3 = {:.0f} \n {:.0f} - 4 = {:.0f} \n {:.0f} - 5 = {:.0f} \n {:.0f} - 6 = {:.0f} \n {:.0f} - 7 = {:.0f} \n {:.0f} - 8 = {:.0f} \n {:.0f} - 9 = {:.0f}".format(valor,n10,valor,n11,valor,n12,valor,n13,valor,n14,valor,n15,valor,n16,valor,n17,valor,n18))
print('------------')
print('{:.0f} X 1 = {:.0f} \n{:.0f} X 2 = {:.0f} \n{:.0f} X 3 = {:.0f} \n{:.0f} X 4 = {:.0f} \n{:.0f} X 5 = {:.0f} \n{:.0f} X 6 = {:.0f} \n{:.0f} X 7 = {:.0f} \n{:.0f} X 8 = {:.0f} \n {:.0f} X 9 = {:.0f} '.format(valor, n19, valor, n20, valor, n21, valor, n22, valor, n23, valor, n24, valor, n25, valor, n26, valor, n27))
print('------------')
print(" {:.0f} / 1 = {:.0f} \n {:.0f} / 2 = {:.0f} \n {:.0f} / 3 = {:.0f} \n {:.0f} / 4 = {:.0f} \n {:.0f} / 5 = {:.0f} \n {:.0f} / 6 = {:.0f} \n {:.0f} / 7 = {:.0f} \n {:.0f} / 8 = {:.0f} \n {:.0f} / 9 = {:.0f}".format(valor,n28,valor,n29,valor,n30,valor,n31,valor,n32,valor,n33,valor,n34,valor,n35,valor,n36))
print('a raiz desse valor é {:.1f}'.format(raiz))