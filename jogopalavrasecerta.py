print('Seja bem vindo ao jogo da palavra secreta')
print('Você tem 10 tentativas para adivinhar a palavra secerta')

palavra_secreta = 'Emily'
chance = 10

while chance > 0:
    chute = str(input('palpite:'))
    if chute == palavra_secreta:
        print(f'parabéns você acertou a palavra secreta {palavra_secreta}')
        break
    elif chute != palavra_secreta:
        print('Sinto muito, mas você não acertou a palavra secerta!\n tente mais uma vez')

