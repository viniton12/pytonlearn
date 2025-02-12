print('Veja quanto fica seu produto importado')

#inserindo as informações do produto
produto11 = input('nome do produto:')
produto1 = float(input('valor do produto R$'))
 
#inserir o valor de desconto
valor_desconto_p1 = float(input('valor do desconto:  '))

#calcúlo para saber o valor do produto com desconto
desconto_final = produto1 * valor_desconto_p1/100
produto_descontado = produto1 - desconto_final

# Calcúlo para saber valor do produto descontado com o imposto de importação
imposto_importação = produto_descontado * 0.2
produto_com_imposto =  produto_descontado + imposto_importação
icms = produto_com_imposto * 0.17

# valor do produto com os impostos 
valor_final_produto_imposto = produto_com_imposto +icms

# Exibindo o as iformações sobre o produto 
print(f'o preço do seu {produto11} com desconto de {valor_desconto_p1}% é de R$ {produto_descontado}.')
print(f'Entretanto, temos o imposto de importação, de 20%, mais o ICMS de 17%.  Fazendo com que  o valor final do seu produto seja de R${valor_final_produto_imposto}')


