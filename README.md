# Desafio para avaliação técnica para vaga na Veeries

Desafio para avaliação técnica para vaga na Veeries

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Python
- Pandas
- Outras dependências listadas no arquivo `requirements.txt`


## Instalação das Dependências

Crie e ative um ambiente virtual
```bash
python3 -m venv venv

source venv/bin/activate
```

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Rodar o projeto

Git clone:
```bash
https://github.com/Joao-Batista-Dev/veeries_challenge
```

Entre no diretório do projeto
```bash
cd veeries_challenge
```

Execute no terminal:

1 - Dados brutos
```bash
python src/get_data_bronze.py
```

2 - Dados tratados
```bash
python src/get_data_prata.py
```

3 - Análise
```bash
python src/get_data_ouro.py
```

Após isso, o sistema estará pronto para ser acessado na pasta data:
```bash
data/bronze/data_bronze.csv
```
```bash
data/prata/data_prata.csv
```
```bash
data/ouro/data_ouro.csv
```