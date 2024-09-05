
# %%

# Lê o arquivo usando pandas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from feature_engine import encoding
from sklearn import tree

# Carregando o DataFrame
df = pd.read_csv("C:/Users/henri/Desktop/IBM/WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Exibir as primeiras linhas do DataFrame
print(df.head())

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
renda_idade = df.groupby(['MonthlyIncome', 'Attrition']).size().reset_index(name='Count')
renda_idade['MonthlyIncome'] = pd.to_numeric(renda_idade['MonthlyIncome'], errors='coerce')
renda_idade['MonthlyIncome'] = renda_idade['MonthlyIncome'].round(-3)  # Arredondar para o milhar mais próximo
renda_idade = renda_idade.groupby(['MonthlyIncome', 'Attrition']).sum().reset_index()

# Montagem de gráfico de renda
plt.figure(figsize=(8, 6))
plt.plot(renda_idade['MonthlyIncome'], renda_idade['Count'], marker='o', linestyle='dashed', color='green')
plt.title('Desligamentos de acordo com a renda')
plt.xlabel('Salário (milhares)')
plt.ylabel('Número de Colaboradores')
plt.grid(True)
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

# Media Salarial por Setor



# Supondo que df seja o seu DataFrame original

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


## novo

import pandas as pd
import matplotlib.pyplot as plt

# Supondo que df seja o seu DataFrame original e que a coluna 'Attrition' seja binária (1 para desligado, 0 para não desligado)

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

## TravelBusiness por WorkLifeBalance

df['WorkLifeBalance'] = pd.to_numeric(df['WorkLifeBalance'], errors='coerce')
work_travel = df.groupby('BusinessTravel').agg(
    WorkLifeBalance_mean=('WorkLifeBalance', 'mean'),
    Count=('WorkLifeBalance', 'size')
).reset_index()

plt.figure(figsize=(10, 6))
bars = plt.bar(work_travel['BusinessTravel'], work_travel['WorkLifeBalance_mean'], color='blue')

for bar, count in zip(bars, work_travel['Count']):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'N={count}', ha='center', va='bottom', fontsize=10)

plt.title('Média de WorkLife Balance por BusinessTravel')
plt.xlabel('BusinessTravel')
plt.ylabel('Média de WorkLifeBalance')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Preparar dados para árvore de decisão

features = [ "MonthlyIncome","Department","WorkLifeBalance"]

# Converter variáveis categóricas
cat_features = ['Department']

# Selecionar as características
X = df[features]

# Codificar variáveis categóricas
onehot = encoding.OneHotEncoder(variables=cat_features)
onehot.fit(X)
X_encoded = onehot.transform(X)

# Ajustar o modelo de árvore de decisão
y = df['Attrition']
arvore = tree.DecisionTreeClassifier(max_depth=3)
arvore.fit(X_encoded, y)

# Verificar as colunas em X_encoded
print("Colunas em X_encoded:", X_encoded.columns)

# Verificar as classes usadas na árvore
print("Classes na árvore:", arvore.classes_)

# Plotar a árvore de decisão
plt.figure(dpi=600)
tree.plot_tree(
    arvore,
    class_names=[str(cls) for cls in arvore.classes_],  # Convertendo classes para strings
    feature_names=X_encoded.columns.tolist(),  # Convertendo colunas para lista
    filled=True,
    max_depth=3
)
plt.show()






    ##Subir Nova Atualização

# %%


# %%
