print('insira as informações do produto')
descricao_do_produto = input("descrição:    ")
valor_Do_produto = float(input('preço:  '))
print('Agora insira o valor do desconto desejado')
desconto = float(input('valor do desconto '))

valordescontado = valor_Do_produto*desconto/100
precofinal = valor_Do_produto-valordescontado
produtoacrescimo = valor_Do_produto+valordescontado
valorparcela = produtoacrescimo/12
print(descricao_do_produto)
print(f'com valor de R${valor_Do_produto} com desconto de {desconto:.0f}% é de R${precofinal:.2f}.')
print(f'O parcelamento da compra em 12X da um acrescimento de {desconto:.0f}% no valor do produto, ficando R${produtoacrescimo:.2f} ou R${valorparcela:.2f} em 12X sem juros no cartão')

