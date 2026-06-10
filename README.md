# Projetos

Repositório usado para exercícios, testes e estudos em Python.

Aqui mantenho scripts pequenos, práticas de lógica, manipulação de arquivos, CSV e alguns testes simples antes de transformar ideias em projetos separados.

## Conteúdo

Os estudos estão organizados em [`python_estudos`](python_estudos/):

- `01_inicio`: fundamentos, validação, funções e arquivos CSV;
- `02_exercicios`: resolução de pequenos problemas com listas e dicionários;
- `03_preparacao_etl`: mini pipeline de vendas usando a biblioteca padrão;
- `tests`: testes básicos com `unittest`.

## Tecnologias

- Python
- CSV
- unittest

## Como Executar

Na raiz do repositório:

```powershell
python python_estudos/01_inicio/04_cadastro_pessoas_csv.py
python python_estudos/03_preparacao_etl/01_mini_etl_vendas.py
```

Para executar os testes:

```powershell
python -m unittest discover -s python_estudos/tests
```

Mais detalhes estão no [README de Python Estudos](python_estudos/README.md).

## Repositórios Relacionados

Alguns estudos acabaram evoluindo para projetos próprios:

- [etl-vendas-python](https://github.com/ypernambuco/etl-vendas-python)  
  ETL simples de vendas com Python, pandas e Parquet.

- [etl-clima-python-sqlite](https://github.com/ypernambuco/etl-clima-python-sqlite)  
  Pipeline simples de clima usando API, pandas e SQLite.

- [dashboard-clima-streamlit](https://github.com/ypernambuco/dashboard-clima-streamlit)  
  Dashboard de clima com Streamlit, histórico, previsão e filtros.
