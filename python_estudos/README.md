# Python Estudos

Exercícios práticos de Python com foco em lógica de programação, funções, validação de dados, arquivos CSV, cálculos e testes automatizados.

Esta pasta reúne estudos pequenos e objetivos. Eles ajudam a registrar minha evolução com Python sem tentar transformar cada exercício em um projeto completo.

## Conteúdos Praticados

| Tema | Onde aparece |
| --- | --- |
| Entrada e saída de dados | scripts de terminal em `01_inicio` |
| Condicionais e validações | classificação de idade, maioridade e cadastro |
| Funções pequenas | separação entre leitura, cálculo e exibição |
| Listas e dicionários | cadastro de pessoas e produtos |
| CSV | leitura e escrita de dados tabulares |
| Cálculos | totais de estoque e valores de vendas |
| Testes com `unittest` | validação de regras de negócio |

## Estrutura

| Pasta | Conteúdo |
| --- | --- |
| `01_inicio` | Primeiros scripts e miniaplicações de terminal |
| `02_exercicios` | Exercícios práticos com regras de negócio simples |
| `03_preparacao_etl` | Estudo de tratamento de dados de vendas com biblioteca padrão |
| `tests` | Testes automatizados com `unittest` |

## Destaques

- `01_inicio/04_cadastro_pessoas_csv.py`: cadastra pessoas, salva em CSV e lê os dados novamente para análise.
- `02_exercicios/01_controle_estoque.py`: calcula totais de produtos em estoque.
- `03_preparacao_etl/01_mini_etl_vendas.py`: trata registros de vendas, padroniza campos e calcula `valor_total`.
- `tests/test_funcoes.py`: testa funções de classificação, maioridade, CSV, estoque e vendas.

## Como executar

Use Python 3.10 ou superior.

```powershell
cd python_estudos
python 01_inicio/04_cadastro_pessoas_csv.py
```

Outro exemplo:

```powershell
python 03_preparacao_etl/01_mini_etl_vendas.py
```

## Como testar

Os testes usam apenas a biblioteca padrão do Python.

```powershell
python -m unittest discover -s tests
```
