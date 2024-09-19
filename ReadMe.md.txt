#Git e Github

**Análise de Recursos Humanos**

📖 **Introdução**
A análise de Recursos Humanos (RH) é o processo de coleta e análise de dados de RH para melhorar o desempenho da força de trabalho de uma organização. Esse processo também é conhecido como análise de talentos, análise de pessoas ou análise da força de trabalho. O objetivo principal é correlacionar os dados coletados rotineiramente pelo departamento de RH com os objetivos estratégicos e organizacionais, fornecendo evidências mensuráveis de como as iniciativas de RH estão impactando os resultados da empresa.

Este projeto utiliza um conjunto de dados de uma empresa fictícia para realizar uma análise abrangente, visualizando padrões como desligamentos (attrition), salários, equilíbrio entre vida profissional e pessoal, e outros fatores.


🛠️ **Tecnologias e Bibliotecas Utilizadas**
Este projeto foi desenvolvido em Python e faz uso das seguintes bibliotecas:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engine import encoding
from sklearn import tree

📊 **Carregando e Preparando os Dados**
O dataset contém informações sobre os colaboradores, como idade, salário, tempo de empresa, setor, entre outros. Para carregar os dados em um DataFrame:

df = pd.read_csv("C:/Users/henri/Desktop/IBM/WA_Fn-UseC_-HR-Employee-Attrition.csv

📋 **Exibindo as primeiras linhas do DataFrame**

df.head()

🔄 **Convertendo Variáveis Categóricas**
Convertendo variáveis categóricas para valores numéricos para facilitar o uso em modelos de aprendizado de máquina. Um exemplo é a variável Attrition, que indica se o colaborador se desligou da empresa:

df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['WorkLifeBalance'] = df['WorkLifeBalance'].astype('category')


📈 **Análise e Visualização de Dados**
1️⃣ Desligamentos por Idade
A seguir, visualizamos os desligamentos (attrition) por faixa etária:


resig_idade = df.groupby(['Age', 'Attrition']).size().reset_index(name='Count')

plt.figure(figsize=(10, 6))
for attrition in resig_idade['Attrition'].unique():
    subset = resig_idade[resig_idade['Attrition'] == attrition]
    plt.plot(subset['Age'], subset['Count'], label='Attrition' if attrition == 1 else 'No Attrition')
plt.title('Desligamentos de acordo com a idade na organização')
plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.legend()
plt.grid(True)
plt.show()

![Texto alternativo](C:\Users\henri\Desktop\Dados IBM\Imagens\image_1)

2️⃣ **Média Salarial por Anos de Empresa**
Aqui, analisamos como a média salarial varia de acordo com o tempo de empresa:

media_salarial = df.groupby('TotalWorkingYears')['MonthlyIncome'].mean().reset_index()

plt.figure(figsize=(8, 6))
plt.plot(media_salarial['TotalWorkingYears'], media_salarial['MonthlyIncome'], marker='o', linestyle='dashed', color='blue')
plt.title('Média Salarial por Anos de Empresa')
plt.xlabel('Anos de Empresa')
plt.ylabel('Média Salarial')
plt.grid(True)
plt.show()

3️⃣ **Média Salarial por Setor e Anos de Empresa**
Para uma análise mais detalhada, visualizamos a média salarial de acordo com o tempo de empresa, mas desta vez segmentado por setor:


media_salarial_setor_anos = df.groupby(['TotalWorkingYears', 'Department'])['MonthlyIncome'].mean().reset_index()

plt.figure(figsize=(12, 8))
for department in media_salarial_setor_anos['Department'].unique():
    dept_data = media_salarial_setor_anos[media_salarial_setor_anos['Department'] == department]
    plt.plot(dept_data['TotalWorkingYears'], dept_data['MonthlyIncome'], marker='o', linestyle='-', label=department)
plt.title('Média Salarial por Departamento e Anos de Empresa')
plt.xlabel('Anos de Empresa')
plt.ylabel('Média Salarial')
plt.legend(title='Departamento')
plt.grid(True)
plt.show()


4️⃣ **Funcionários Desligados por Setor e Anos de Empresa :**

Agora analisamos os colaboradores que se desligaram da empresa, divididos por setor e tempo de empresa:

desligados = df[df['Attrition'] == 1]
media_salarial_por_anos_setor = desligados.groupby(['TotalWorkingYears', 'Department'])['MonthlyIncome'].count().reset_index()

plt.figure(figsize=(12, 8))
for department in media_salarial_por_anos_setor['Department'].unique():
    dept_data = media_salarial_por_anos_setor[media_salarial_por_anos_setor['Department'] == department]
    plt.plot(dept_data['TotalWorkingYears'], dept_data['MonthlyIncome'], marker='o', linestyle='-', label=department)
plt.title('Contagem de Funcionários Desligados por Anos de Empresa e Departamento')
plt.xlabel('Anos de Empresa')
plt.ylabel('Contagem')
plt.legend(title='Departamento')
plt.grid(True)
plt.xticks(range(int(media_salarial_por_anos_setor['TotalWorkingYears'].min()), int(media_salarial_por_anos_setor['TotalWorkingYears'].max()) + 1))
plt.show()


5️⃣ **Equilíbrio Vida-Trabalho**
Analisamos agora como o equilíbrio entre vida pessoal e trabalho se distribui entre colaboradores ativos e desligados:

equilibrio_trab = df.groupby(['WorkLifeBalance', 'Attrition']).size().reset_index(name='Counts')

sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=equilibrio_trab, x='WorkLifeBalance', y='Counts', hue='Attrition')
plt.title('Equilíbrio Vida-Trabalho na Organização')
plt.xlabel('Equilíbrio Vida-Trabalho')
plt.ylabel('Contagem')
plt.show()


6️⃣ **Taxa de Desligamento por Setor**
Esta análise mostra qual setor tem a maior taxa de desligamentos:

desliga_setor = df.groupby('Department')['Attrition'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(desliga_setor['Department'], desliga_setor['Attrition'], color='blue')
plt.title('Taxa de Desligamento por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Taxa de Desligamento')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

7️⃣ **Equilíbrio Vida-Trabalho por Setor**
Finalmente, analisamos o equilíbrio vida-trabalho médio para cada setor da empresa:


df['WorkLifeBalance'] = pd.to_numeric(df['WorkLifeBalance'], errors='coerce')
work_departament = df.groupby('Department')['WorkLifeBalance'].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(work_departament['Department'], work_departament['WorkLifeBalance'], color='blue')
plt.title('Média de WorkLife Balance por Departamento')
plt.xlabel('Departamento')
plt.ylabel('WorkLife Balance')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

