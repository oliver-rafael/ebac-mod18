# código de geração do gráfico 
import pandas as pd
import seaborn as sns
df_gasolina = pd.read_csv('./gasolina.csv')

# grafico
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df_gasolina, x='dia', y='venda', color ='red')
  grafico.set(title=' Valor da gasolina em São Paulo - Julho de 2021', xlabel='Dez primeiros dias de Julho 2021', ylabel='Valor em R$')
# Salvar o gráfico como um arquivo PNG
  grafico.figure.savefig('gasolina.png')