import pandas as pd
from datetime import date

url = "https://www.appaweb.appa.pr.gov.br/appaweb/pesquisa.aspx?WCI=relLineUpRetroativo"

tabelas = pd.read_html(url)

tabela = tabelas[1]

# tratamento para retirar espaços
tabela.columns = [' '.join(col).strip() for col in tabela.columns.values]

tabela.to_csv(f"data/bronze/data_bronze.csv", index=True)



