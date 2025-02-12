print('Insira a numeração da placa do seu carro')
num_placa = str(input('Número da placa: '))
ultimo_digito =int(num_placa[-1])
print(f'A numeração da placa do seu carro é {num_placa} com final {ultimo_digito}')

if ultimo_digito == 0 or ultimo_digito == 1:
    print('seu carro Não circula nas segundas-feiras')
elif ultimo_digito == 2 or ultimo_digito == 3:
    print('Seu carro não circula nas terças-feiras')
elif ultimo_digito == 4 or ultimo_digito == 5:
    print('Seu carro não circula nas quartas-feiras')
elif ultimo_digito == 6 or ultimo_digito == 7:
    print('Seu carro não pode circular nas quintas-feiras')
elif ultimo_digito == 8 or ultimo_digito == 9:
    print('Seu carro não pode circular nas sextas-feiras')
