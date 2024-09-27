
# %%
# Lê o arquivo usando pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engine import encoding
from sklearn import tree
import plotly.express as px
import numpy as np

# Carregando o DataFrame
df = pd.read_csv("C:/Users/henri/Desktop/IBM/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Exibir as primeiras linhas do DataFrame e entendendo o DataFrame

print(df.head(3))
df.shape
df.columns
df.describe()
df.describe(include ='all')
df.info()

df.isnull().any()


# Convertendo variáveis categóricas
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0}) # Alterando os valores de Attrition para valores binarios
df['WorkLifeBalance'] = df['WorkLifeBalance'].astype('category')

# Visualização dos desligamentos por idade
resig_idade = df.groupby(['Age', 'Attrition']).size().reset_index(name='Count')
plt.figure(figsize=(10, 6))
for attrition in resig_idade['Attrition'].unique():
    subset = resig_idade[resig_idade['Attrition'] == attrition]
    plt.plot(subset['Age'], subset['Count'], label='Attrition' if attrition == 1 else 'No Attrition')
plt.title('Desligamentos de acordo com a idade na organização')
plt.xlabel('Age')
plt.ylabel('Counts')
plt.legend()
plt.grid(True)
plt.show()


# Análise da Renda dos Colaboradores e como ela influencia nos desligamentos

filtro_desligado = df[df['Attrition'] == 1]
renda_idade = filtro_desligado.groupby(['MonthlyIncome', 'Attrition','Department']).size().reset_index(name='Count')
renda_idade['MonthlyIncome'] = pd.to_numeric(renda_idade['MonthlyIncome'], errors='coerce')
renda_idade['MonthlyIncome'] = renda_idade['MonthlyIncome'].round(-3)  # Arredondar para o milhar mais próximo
renda_idade = renda_idade.groupby(['MonthlyIncome', 'Attrition','Department']).sum().reset_index()

pivot_data = renda_idade.pivot_table(index='MonthlyIncome', columns='Department', values='Count', fill_value=0)
colors = {
    'Research & Development': 'blue',
    'Sales': 'orange',
    'Human Resources': 'green'
}

pivot_data.plot(kind='bar', stacked=True, figsize=(10, 7), color=[colors[col] for col in pivot_data.columns])

#Montagem Grafico

plt.title('Desligamentos por Faixa Salarial e Setor')
plt.xlabel('Salário (milhares)')
plt.ylabel('Número de Colaboradores Desligados')
plt.legend(title='Setor')
plt.grid(axis='y')
plt.show()

# Tempo de trabalho por Salário

media_salarial = df.groupby('TotalWorkingYears')['MonthlyIncome'].mean().reset_index()


# Plotando o gráfico da média salarial por anos de empresa
plt.figure(figsize=(8, 6))
plt.plot(media_salarial['TotalWorkingYears'], media_salarial['MonthlyIncome'], marker='o', linestyle='dashed', color='blue')
plt.title('Média Salarial por Anos de Empresa')
plt.xlabel('Anos de Empresa')
plt.ylabel('Média Salarial')
plt.grid(True)
plt.show()



# Agrupando por TotalWorkingYears e Department para calcular a média salarial
media_salarial_setor_anos = df.groupby(['TotalWorkingYears', 'Department'])['MonthlyIncome'].mean().reset_index()

# Criando o gráfico
plt.figure(figsize=(12, 8))

# Iterando sobre cada departamento para plotar as linhas
for department in media_salarial_setor_anos['Department'].unique():
    dept_data = media_salarial_setor_anos[media_salarial_setor_anos['Department'] == department]
    plt.plot(dept_data['TotalWorkingYears'], dept_data['MonthlyIncome'], marker='o', linestyle='-', label=department)

plt.title('Média Salarial por Departamento e Anos de Empresa')
plt.xlabel('Anos de Empresa')
plt.ylabel('Média Salarial')
plt.legend(title='Departamento')
plt.grid(True)
plt.show()

# 1. Filtrar os funcionários com Attrition = 1
desligados = df[df['Attrition'] == 1]

# 2. Agrupar os dados por anos de empresa e departamento e calcular a média salarial
media_salarial_por_anos_setor = desligados.groupby(['TotalWorkingYears', 'Department'])['MonthlyIncome'].count().reset_index()

# 3. Plotar o gráfico
plt.figure(figsize=(12, 8))

# Iterar sobre cada departamento para adicionar linhas ao gráfico
for department in media_salarial_por_anos_setor['Department'].unique():
    dept_data = media_salarial_por_anos_setor[media_salarial_por_anos_setor['Department'] == department]
    plt.plot(dept_data['TotalWorkingYears'], dept_data['MonthlyIncome'], marker='o', linestyle='-', label=department)

plt.title('Contagem de  Funcionários com Attrition = 1 por Anos de Empresa e Departamento')
plt.xlabel('Anos de Empresa')
plt.ylabel('Contagem')
plt.legend(title='Departamento')
plt.grid(True)
plt.xticks(range(int(media_salarial_por_anos_setor['TotalWorkingYears'].min()), int(media_salarial_por_anos_setor['TotalWorkingYears'].max()) + 1))
plt.show()





# Equilíbrio entre vida pessoal e trabalho
equilibrio_trab = df.groupby(['WorkLifeBalance', 'Attrition']).size().reset_index(name='Counts')

# Configurar o estilo do seaborn
sns.set(style="whitegrid")

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(data=equilibrio_trab, x='WorkLifeBalance', y='Counts', hue='Attrition')
plt.title('Equilibro Vida e Trabalho na Organização')
plt.xlabel('Equilibrio Vida e Trabalho')
plt.ylabel('Contagem ')
plt.show()


## setor com mais desligamentos
desliga_setor = df.groupby('Department')['Attrition'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(desliga_setor['Department'], desliga_setor['Attrition'], color='blue')
plt.title('Taxa Média de Desligamento por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Taxa Média de Desligamento')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


## WorLife Balance por Departamento
df['WorkLifeBalance'] = pd.to_numeric(df['WorkLifeBalance'], errors='coerce')
work_departament = df.groupby('Department')['WorkLifeBalance'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(work_departament['Department'], work_departament['WorkLifeBalance'], color='blue')
plt.title('Media de WorkLife Balance por Departamento')
plt.xlabel('Departamento')
plt.ylabel('WorkLibeBalance')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

## novo  
distanciamedia_dep = df.groupby('Department')['DistanceFromHome'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(distanciamedia_dep['Department'], distanciamedia_dep['DistanceFromHome'], color='blue')
plt.title('Taxa Média de Distancia de Casa por Departmento')
plt.xlabel('Departamento')
plt.ylabel('Taxa Média de Distancia')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

## TravelBusiness por Setor
# Agrupar por BusinessTravel e Department para obter a contagem de pessoas
work_travel = df.groupby(['BusinessTravel', 'Department']).size().reset_index(name='Count')

# Configurar o gráfico
fig = px.bar(work_travel, x='Department', y='Count', color='BusinessTravel')
fig.show()


# Correlação de Pearson

A = df['WorkLifeBalance']
B = df['MonthlyIncome']
 
 # Calculando Correlacao      ]
correlacao = np.corrcoef(A,B)
print(f"Correlaçao de Pearson: {correlacao}")
# Montando Grafico :
sns.lmplot(x='WorkLifeBalance', y='MonthlyIncome',data=df , ci=None)

#Rotulos 
plt.title('Correlação entre WorkLifeBalance e MonthlyIncome')
plt.xlabel('WorkLifeBalance')
plt.ylabel('MontlyIncome')
plt.show()

# Correlação de Pearson para Distance From Home

A = df['WorkLifeBalance']
B = df['DistanceFromHome']
 
 # Calculando Correlacao      ]
correlacao = np.corrcoef(A,B)
print(f"Correlaçao de Pearson: {correlacao}")
# Montando Grafico :
sns.lmplot(x='WorkLifeBalance', y='DistanceFromHome',data=df , ci=None)

#Rotulos 
plt.title('Correlação entre WorkLifeBalance e DistanceFromHome')
plt.xlabel('WorkLifeBalance')
plt.ylabel('DistanceFromHome')
plt.show()


    ##Subir Nova Atualização

# %%


