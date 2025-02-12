#converter a temperatura de Ceulsius para  Fahrenheite e Kelvin
# 1 grau celcius equivale a 33,8 ºF
# 1 grau celcius é C X 1.8 + 32
import math
import random
print('coloque a temperatura em Celcius')
graus_C = float(input())
fahrenheit = graus_C*9/5+32
kelvin = graus_C+273.15
print(f'{graus_C} grau Celcius equivale a {fahrenheit} (ºF) e a {kelvin} (K)')
