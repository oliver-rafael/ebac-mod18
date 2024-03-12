# código de geração do gráfico 
import pandas as pd
import seaborn as sns
df_gasolina = pd.read_csv('./gasolina.csv')

# grafico
with sns.axes_style('darkgrid'):
  grafico = sns.lineplot(data=df_gasolina, x='dia', y='venda', palette='dark')
  grafico.set(title=' Valor médio da gasolina em São Paulo/SP - Julho de 2021', xlabel='Dez primeiros dias de Julho 2021', ylabel='Valor em R$')
# Salva o gráfico como um arquivo PNG
  grafico.figure.savefig('gasolina.png')