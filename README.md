# Projetos

Repositório usado como laboratório de estudos em Python.

Aqui mantenho exercícios pequenos, anotações práticas e scripts que mostram minha evolução antes de transformar alguns estudos em repositórios próprios.

## Objetivo Do Repositório

- praticar fundamentos de Python;
- registrar exercícios de lógica e arquivos;
- estudar leitura e escrita de CSV;
- treinar funções, validações e testes simples;
- manter um histórico organizado do aprendizado.

## Tecnologias Utilizadas

- Python
- biblioteca padrão do Python
- unittest
- CSV

## Estrutura De Pastas

```text
Projetos/
|-- python_estudos/
|   |-- 01_inicio/
|   |-- 02_exercicios/
|   |-- 03_preparacao_etl/
|   |-- tests/
|-- LICENSE
|-- README.md
```

## Conteúdo Deste Repositório

| Pasta | Descrição |
| --- | --- |
| [python_estudos](./python_estudos) | Exercícios práticos de Python com funções, validação, CSV, cálculos e testes. |

## Projetos Em Repositórios Próprios

Alguns estudos evoluíram para repositórios separados:

| Projeto | Descrição |
| --- | --- |
| [etl-vendas-python](https://github.com/ypernambuco/etl-vendas-python) | ETL simples de vendas com Python, pandas e Parquet. |
| [etl-clima-python-sqlite](https://github.com/ypernambuco/etl-clima-python-sqlite) | Pipeline simples de clima usando API, pandas e SQLite. |
| [dashboard-clima-streamlit](https://github.com/ypernambuco/dashboard-clima-streamlit) | Dashboard de clima com Streamlit, histórico, previsão e filtros. |

## Como Executar

Entre na pasta de estudos:

```powershell
cd python_estudos
```

Execute um script:

```powershell
python 01_inicio/04_cadastro_pessoas_csv.py
```

Rode os testes:

```powershell
python -m unittest discover -s tests
```

## O Que Aprendi

- escrever scripts pequenos em Python;
- separar regras em funções;
- trabalhar com entrada e saída no terminal;
- ler e gravar arquivos CSV;
- criar validações simples;
- testar funções com `unittest`.

## Limitações

- é um repositório de estudos, não um projeto único;
- os exemplos são pequenos;
- algumas soluções ainda são bem introdutórias;
- não há dependências externas ou estrutura avançada.

## Próximos Passos

- organizar novos exercícios por tema;
- adicionar mais testes simples;
- criar exemplos pequenos com SQL;
- separar novos projetos quando fizer sentido.
