# Python Estudos

Pasta com exercícios práticos de Python.

Os exemplos são pequenos e servem para registrar minha evolução com lógica, funções, validação de dados, arquivos CSV, cálculos e testes.

## Objetivo

- praticar fundamentos de Python;
- resolver problemas simples de terminal;
- trabalhar com listas, dicionários e funções;
- ler e escrever arquivos CSV;
- criar testes básicos com `unittest`.

## Tecnologias Utilizadas

- Python
- biblioteca padrão
- CSV
- unittest

## Estrutura De Pastas

```text
python_estudos/
|-- 01_inicio/
|-- 02_exercicios/
|-- 03_preparacao_etl/
|-- tests/
|-- README.md
```

## Conteúdos Praticados

| Tema | Onde aparece |
| --- | --- |
| Entrada e saída de dados | `01_inicio` |
| Condicionais e validações | classificação de idade e maioridade |
| Listas e dicionários | cadastro de pessoas e produtos |
| CSV | cadastro de pessoas e mini ETL |
| Cálculos | estoque e vendas |
| Testes | `tests/test_funcoes.py` |

## Como Executar

Use Python 3.10 ou superior.

```powershell
python 01_inicio/04_cadastro_pessoas_csv.py
```

Outro exemplo:

```powershell
python 03_preparacao_etl/01_mini_etl_vendas.py
```

## Como Testar

```powershell
python -m unittest discover -s tests
```

## O Que Aprendi

- criar funções pequenas;
- validar entradas simples;
- organizar scripts por tema;
- usar CSV para salvar dados;
- escrever testes básicos.

## Limitações

- os scripts são exercícios de estudo;
- não há interface gráfica;
- não há banco de dados;
- o foco é prática de base, não arquitetura.

## Próximos Passos

- adicionar exercícios com SQL;
- melhorar comentários em alguns scripts;
- criar exemplos pequenos de análise com pandas.
