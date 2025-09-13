import pandas as pd

# Carregar os dados PRATA
tabela_prata = pd.read_csv("data/prata/data_prata.csv")

# Converter Data_Chegada para datetime
tabela_prata["Data_Chegada"] = pd.to_datetime(
    tabela_prata["Data_Chegada"], errors="coerce", dayfirst=True
)

# Criar colunas Ano e Mes
tabela_prata["Ano"] = tabela_prata["Data_Chegada"].dt.year
tabela_prata["Mes"] = tabela_prata["Data_Chegada"].dt.month

# Agrupar por Produto e Sentido (quantidade de navios)
agrupado = (
    tabela_prata.groupby(["Produto", "Sentido"])
    .size()
    .reset_index(name="Quantidade_Navios")
)

# Salvar o resultado em CSV
tabela_prata.to_csv("data/ouro/data_ouro.csv", index=True)
agrupado.to_csv("data/ouro/product_grouping_ouro.csv", index=True)
