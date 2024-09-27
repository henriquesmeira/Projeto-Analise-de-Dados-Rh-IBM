
**Análise de Recursos Humanos**

📖 **Introdução**
A análise de Recursos Humanos (RH) é o processo de coleta e análise de dados de RH para melhorar o desempenho da força de trabalho de uma organização. Esse processo também é conhecido como análise de talentos, análise de pessoas ou análise da força de trabalho. O objetivo principal é correlacionar os dados coletados rotineiramente pelo departamento de RH com os objetivos estratégicos e organizacionais, fornecendo evidências mensuráveis de como as iniciativas de RH estão impactando os resultados da empresa.

Este projeto utiliza um conjunto de dados de uma empresa fictícia para realizar uma análise abrangente, visualizando padrões como desligamentos (attrition), salários, equilíbrio entre vida profissional e pessoal, e outros fatores.


🛠️ **Tecnologias e Bibliotecas Utilizadas**
Este projeto foi desenvolvido em Python e faz uso das seguintes bibliotecas:

pandas

seaborn

matplotlib


📈 **Análise e Visualização de Dados**
1️⃣ Desligamentos por Idade :


![Gráfico de Desligamentos por Idade](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/image_1.png?raw=true)

2️⃣ **Média Salarial por Anos de Empresa**
Aqui, analisamos como a média salarial varia de acordo com o tempo de empresa:

![Média Salarial Por Anos de Empresa](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/media%20salarial%20por%20anos%20de%20empresa.png?raw=true)

3️⃣ **Média Salarial por Setor e Anos de Empresa**
Para uma análise mais detalhada, visualizamos a média salarial de acordo com o tempo de empresa, mas desta vez segmentado por setor:

![Média Salarial Por Anos e Setor](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/media%20salarial%20por%20departamente.png?raw=true)


4️⃣ **Funcionários Desligados por Setor e Anos de Empresa :**

Agora analisamos os colaboradores que se desligaram da empresa, divididos por setor e tempo de empresa:

![Média Salarial Por Anos e Setor](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/Desligamentos%20por%20setor.png?raw=true)


5️⃣ **Equilíbrio Vida-Trabalho**
Analisamos agora como o equilíbrio entre vida pessoal e trabalho se distribui entre colaboradores ativos e desligados:

![Equilibrio Entre Vida e Trabalho](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/equilibrio%20vida%20trab%20%20por%20departmento.png?raw=true)



6️⃣ **Taxa de Desligamento por Setor**
Esta análise mostra qual setor tem a maior taxa de desligamentos:

![Desligamentos por Setor](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/taxa%20media%20de%20desliga%20por%20departamento.png?raw=true)

7️⃣ **Equilíbrio Vida-Trabalho por Setor**
Finalmente, analisamos o equilíbrio vida-trabalho médio para cada setor da empresa:

![Business Travel por Setor](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/travelporsetor.JPG?raw=true)


 **Verificando se Existe Correlações entra Variáveis**

Para verificar se algumas das variáveis influenciava diretamente em fatores das outras variáveis, fiz uma analise com base na correção de Pearson, vendo se existia valores significativos para variáveis como : WorkLifeBalance, MonthIncome e DistanceFromHome.
Passada a análise foi visto que nenhuma das duas influeciava diretamente na variavel WorkLifeBalance. 

Dessa forma, fica evidente que embora o salário possa ser uma fator relevante dentro de um processo de Desligamento ou não , nesse caso , aparentemente não é o fator principal para tal, assim como também a Distancia entre Trabalho e Casa.



![Pearson Monthly Income e WorkLifeBalance](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/Pearson%20WorkLife%20Balance%20e%20MonthlyIncome.png?raw=true)

![Pearson DistanceFromHome e WorkLifeBalance](https://github.com/henriquesmeira/Projeto-Analise-de-Dados-Rh-IBM/blob/ReadMe/Imagens/WorkLife%20Balance%20e%20DistanceFromHome.png?raw=true)

