# 03 - Preparação Para ETL

Estudo prático de tratamento de dados de vendas usando apenas a biblioteca padrão do Python.

A proposta é praticar etapas comuns em dados: leitura de CSV, padronização de campos, conversão de tipos, tratamento de registros inválidos, cálculo de métricas e geração de um novo arquivo.

## Fluxo Do Estudo

```text
CSV bruto -> transformação com Python -> CSV processado
```

## Arquivos

| Arquivo | O que demonstra |
| --- | --- |
| `01_mini_etl_vendas.py` | mini pipeline ETL usando `csv`, `datetime`, `decimal` e funções |

## Como Executar

Na pasta `python_estudos`, rode:

```powershell
python 03_preparacao_etl/01_mini_etl_vendas.py
```

## O Que Aprendi

- ler registros de vendas em CSV;
- padronizar campos;
- converter datas e valores;
- calcular `valor_total`;
- gravar um CSV processado;
- separar funções de extração, transformação e carga.

## Limitações

- usa apenas dados pequenos de exemplo;
- não usa pandas;
- não salva em banco de dados;
- não tem agendamento ou automação.

## Próximos Passos

- comparar esta versão com uma implementação usando pandas;
- adicionar testes para as regras de transformação;
- gerar métricas simples por produto.
