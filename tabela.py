import pandas as pd
import matplotlib.pyplot as plt
#inserindo os dados na tabela 
data = {
    'meses':['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jnh', 'Jlh', 'Agos', 'Set', 'Out', 'Nov', 'Dez'], 
    'canetas':[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2, 1000],
    'borracha':[10, 20, 30, 40, 40, 50, 60, 70, 80, 90, 100, 120], 
    'cadernos':[100, 200, 300, 4000, 500, 6000, 7000, 880, 900, 1003, 1111, 1200],
    'grafite': [110, 120, 130, 140, 150, 160, 170, 180, 190, 110, 110, 120],
    'giz':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
}
#criando o dataframe

df = pd.DataFrame(data)
print(df)
plt.bar (df['meses'], df['canetas'])
plt.title('venda do ano de 2023')
plt.xlabel('meses')
plt.ylabel('canetas')
plt.show()


plt.bar (df['meses'], df['borracha'],)
plt.title('venda do ano de 2023')
plt.xlabel('meses')
plt.ylabel('borracha')
plt.show()

plt.bar (df['meses'], df['cadernos'],)
plt.title('venda do ano de 2023')
plt.xlabel('meses')
plt.ylabel('cadernos')
plt.show()