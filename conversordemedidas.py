import math
# organizando as conversões

# de metro (m) para decametro (dm) multiplico por 1*10

#  de metro (m) para centimetro (cm) multiplico por 1*100

# de um metro (m) para milimetro (mm) multiplico por 1*1000

# de um kilometro (KM) para metro (m) multiplico por 1*1000

# de hectometro para (hm) para metro (m) multiplico por 1*100

#de decametro (dm) para metro (m) multiplico por 1*10

#de um milimetro para metro divido por 1000 1/1000

# de um centimetro para metro divido por 100 1/100

# de um decimentro para metro divido por 10 1/10

# de metro para um kilometro divido por 1000 1/1000

# de metro para hectometro divido por 100 1/100

#de metro para decametro divido por 10 1/10

#

print('insira o valor em metros') 
medida = float(input('metros:'))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
km = medida / 1000
he = medida / 100
dc = medida / 10
print ('{:.0f} metros equivalem a \n{:.0f} milimetros\n{:.0f} centímetros \n{:.0f} decimetros \n{} kilomentros \n{} hectometros \n{} decametros'.format(medida, mm, cm, dm, km, he, dc))  
    
