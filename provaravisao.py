#Você tem um conjunto de dados fictícios que representa informações sobre a produção anual de diferentes culturas em várias fazendas ao longo de vários anos. Seu objetivo é realizar uma análise simples desses dados utilizando funções agregadoras.

#Tarefas:
#Encontre o ano com a produção total máxima e o ano com a produção total mínima:

#Você deve somar a produção total de todas as fazendas para cada ano e determinar qual foi o ano com a maior e a menor produção.
#Identifique a cultura com a maior e a menor produção total ao longo dos anos:

#Some a produção de cada cultura em todas as fazendas e anos, e identifique qual cultura teve a maior produção e qual teve a menor produção.
#Encontre a fazenda com a produção máxima e a fazenda com a produção mínima em um determinado ano:

#Selecione um ano e, dentro desse ano, identifique a fazenda que obteve a maior produção e a que obteve a menor produção.
#Dados Fictícios:
#Para simplificar, vamos construir dados fictícios representando a produção anual de três culturas (milho, soja e trigo) em três fazendas (Fazenda A, Fazenda B, Fazenda C) ao longo de três anos (2021, 2022, 2023).


import pandas as pd

# Criando os dados fictícios
dados = {
    "Ano": [2021, 2021, 2021, 2022, 2022, 2022, 2023, 2023, 2023],
    "Fazenda": ["Fazenda A", "Fazenda B", "Fazenda C"] * 3,
    "Milho": [1200, 1500, 1100, 1300, 1400, 1150, 1250, 1550, 1180],
    "Soja": [1000, 950, 1200, 1100, 1050, 1250, 1150, 1080, 1300],
    "Trigo": [800, 700, 750, 900, 850, 780, 890, 920, 800],
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Calculando a produção total por ano
df["Produção Total"] = df[["Milho", "Soja", "Trigo"]].sum(axis=1)
prod_total_ano = df.groupby("Ano")["Produção Total"].sum()

# Encontrando o ano com maior e menor produção total
ano_max = prod_total_ano.idxmax()
ano_min = prod_total_ano.idxmin()

# Calculando a produção total por cultura
prod_total_cultura = df[["Milho", "Soja", "Trigo"]].sum()

# Identificando a cultura com maior e menor produção total
cultura_max = prod_total_cultura.idxmax()
cultura_min = prod_total_cultura.idxmin()

# Selecionando um ano específico para análise de fazendas
ano_especifico = 2022
df_ano = df[df["Ano"] == ano_especifico]

# Identificando a fazenda com maior e menor produção total no ano específico
fazenda_max = df_ano.loc[df_ano["Produção Total"].idxmax(), "Fazenda"]
fazenda_min = df_ano.loc[df_ano["Produção Total"].idxmin(), "Fazenda"]

# Funções agregadoras de análise simples
def analise_simples():
    print("Ano com maior produção total:", ano_max)
    print("Ano com menor produção total:", ano_min)
    print("Cultura com maior produção total:", cultura_max)
    print("Cultura com menor produção total:", cultura_min)
    print("Fazenda com maior produção no ano de", ano_especifico, ":", fazenda_max)
    print("Fazenda com menor produção no ano de", ano_especifico, ":", fazenda_min)
    
# Executando a análise
analise_simples()
