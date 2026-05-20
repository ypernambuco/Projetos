# 03 - Preparação Para ETL

Estudo prático de tratamento de dados de vendas usando apenas a biblioteca padrão do Python.

A proposta é exercitar etapas comuns em rotinas de dados: leitura de CSV, padronização de campos, conversão de tipos, tratamento de registros inválidos, cálculo de métricas e geração de um novo arquivo.

## Etapas

| Etapa | O que acontece |
| --- | --- |
| Extração | leitura de registros de vendas em CSV |
| Transformação | padronização de colunas, datas e valores |
| Cálculo | criação de `valor_total` |
| Carga | gravação de um CSV processado |

## Arquivos

| Arquivo | O que demonstra |
| --- | --- |
| `01_mini_etl_vendas.py` | mini pipeline ETL usando `csv`, `datetime`, `decimal` e funções puras |

## Como executar

```powershell
python 03_preparacao_etl/01_mini_etl_vendas.py
```
