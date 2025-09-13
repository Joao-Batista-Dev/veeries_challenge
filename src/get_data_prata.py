import pandas as pd

# lê bronze csv
tabela_bronze = pd.read_csv("data/bronze/data_bronze.csv")

print("Colunas do bronze:", tabela_bronze.columns.tolist())

# renomeia nomes da tabela 
tabela_prata = tabela_bronze.rename(columns={
    "ATRACADOS Embarcação": "Navio",
    "ATRACADOS IMO": "IMO",
    "ATRACADOS Bordo": "Bordo",
    "ATRACADOS Sentido": "Sentido",
    "ATRACADOS Agência": "Agencia",
    "ATRACADOS Operador": "Operador",
    "ATRACADOS Mercadoria": "Produto",
    "ATRACADOS Chegada": "Data_Chegada"
})

# pega só as colunas necessárias
colunas_prata = ["Navio", "IMO", "Bordo", "Sentido", "Agencia", "Operador", "Produto", "Data_Chegada"]
tabela_prata = tabela_prata[colunas_prata]

# salva prata
tabela_prata.to_csv("data/prata/data_prata.csv", index=True)
print("Prata salvo com sucesso!")
