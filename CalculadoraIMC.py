#pedindo as informações 
print('Calculadora de IMC (Índice de Massa Corporal)')
print('digite seu peso e sua altura')
peso = float(input('Digite seu peso em kilograma (KG): '))
altura = float(input('Digite sua altura em metros: '))
#Calcúlo do IMC
imc = peso/(altura*altura)

#Alternativas
if imc < 18.5:
    print(f'Seu IMC foi de {imc:.2f}. Por isso  você está Abaixo do peso')
elif 18.5 <= imc < 24.9:
    print(f'Seu IMC foi de {imc:.2f}. Por isso você está com Peso normal')
elif 25 <= imc <= 29.9:
    print(f'Seu IMC foi de {imc:.2f}. Por isso você está com sobrepeso')
else:
    print ('você está com obesidade')