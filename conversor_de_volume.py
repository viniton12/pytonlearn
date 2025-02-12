print('insira o valor  que deseja converter')
medida = float(input('valor:'))

m3 = medida * 1000
dm3 = medida * 1
cm3 = dm3 * 1000

print('{} equivale a: {:.0f} litros\n {:.0f} litros\n {:.0f} mililitros'.format(medida, m3, dm3, cm3))



