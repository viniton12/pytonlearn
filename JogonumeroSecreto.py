import random
print("Seja bem-vindo ao jogo do número secreto!")
print("Regas: digite um número que esteja entre 1 e 100 para achar o número secreto")
chute = 0
numerosecreto = 50
while chute != numerosecreto:
    chute = int(input('Diga um número'))
    if chute == numerosecreto:
        print(f'Parabéns, Você achou o número secreto:{numerosecreto} ')
        break
    elif chute > numerosecreto:
        print('o número secreto é menor')
    elif chute < numerosecreto:
        print('o número secreto é maior')
    
    
