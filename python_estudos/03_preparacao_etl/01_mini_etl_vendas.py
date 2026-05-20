"""Mini ETL de vendas usando apenas a biblioteca padrão do Python."""

import csv
import re
import unicodedata
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path

ARQUIVO_ENTRADA = Path(__file__).with_name("vendas_brutas.csv")
ARQUIVO_SAIDA = Path(__file__).with_name("vendas_processadas.csv")

CAMPOS_SAIDA = [
    "id_venda",
    "data_venda",
    "cliente",
    "produto",
    "quantidade",
    "preco_unitario",
    "desconto",
    "valor_total",
]

VENDAS_EXEMPLO = [
    {
        "ID Venda": "1001",
        "Data Venda": "01/05/2026",
        "Cliente": " Ana Silva ",
        "Produto": "Notebook",
        "Quantidade": "1",
        "Preco Unitario": "3500.00",
        "Desconto": "150.00",
    },
    {
        "ID Venda": "1002",
        "Data Venda": "02/05/2026",
        "Cliente": "Bruno Costa",
        "Produto": "Mouse",
        "Quantidade": "2",
        "Preco Unitario": "80.50",
        "Desconto": "0",
    },
    {
        "ID Venda": "1003",
        "Data Venda": "data invalida",
        "Cliente": "Carla Lima",
        "Produto": "Teclado",
        "Quantidade": "1",
        "Preco Unitario": "230.90",
        "Desconto": "10.90",
    },
]


def normalizar_coluna(coluna: str) -> str:
    texto = unicodedata.normalize("NFKD", coluna.strip().lower())
    texto = texto.encode("ascii", "ignore").decode("ascii")
    texto = re.sub(r"[^a-z0-9]+", "_", texto)
    return texto.strip("_")


def converter_decimal(valor: str) -> Decimal:
    try:
        return Decimal(str(valor).replace(",", ".").strip() or "0")
    except InvalidOperation:
        return Decimal("0")


def converter_inteiro(valor: str) -> int:
    try:
        numero = int(str(valor).strip())
        return max(numero, 0)
    except ValueError:
        return 0


def converter_data(valor: str) -> str | None:
    try:
        data = datetime.strptime(valor.strip(), "%d/%m/%Y")
        return data.date().isoformat()
    except ValueError:
        return None


def calcular_valor_total(
    quantidade: int,
    preco_unitario: Decimal,
    desconto: Decimal,
) -> Decimal:
    total = Decimal(quantidade) * preco_unitario - desconto
    return max(total, Decimal("0")).quantize(Decimal("0.01"))


def padronizar_registro(registro: dict[str, str]) -> dict[str, str]:
    return {normalizar_coluna(chave): valor.strip() for chave, valor in registro.items()}


def transformar_venda(registro: dict[str, str]) -> dict[str, str] | None:
    venda = padronizar_registro(registro)
    data_venda = converter_data(venda.get("data_venda", ""))

    if data_venda is None:
        return None

    quantidade = converter_inteiro(venda.get("quantidade", "0"))
    preco_unitario = converter_decimal(venda.get("preco_unitario", "0"))
    desconto = converter_decimal(venda.get("desconto", "0"))
    valor_total = calcular_valor_total(quantidade, preco_unitario, desconto)

    return {
        "id_venda": venda.get("id_venda", ""),
        "data_venda": data_venda,
        "cliente": venda.get("cliente") or "Não informado",
        "produto": venda.get("produto") or "Não informado",
        "quantidade": str(quantidade),
        "preco_unitario": f"{preco_unitario:.2f}",
        "desconto": f"{desconto:.2f}",
        "valor_total": f"{valor_total:.2f}",
    }


def transformar_vendas(registros: list[dict[str, str]]) -> list[dict[str, str]]:
    vendas_processadas = []

    for registro in registros:
        venda = transformar_venda(registro)
        if venda is not None:
            vendas_processadas.append(venda)

    return vendas_processadas


def criar_csv_exemplo(caminho: Path = ARQUIVO_ENTRADA) -> None:
    if caminho.exists():
        return

    with caminho.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=list(VENDAS_EXEMPLO[0].keys()))
        escritor.writeheader()
        escritor.writerows(VENDAS_EXEMPLO)


def ler_csv(caminho: Path = ARQUIVO_ENTRADA) -> list[dict[str, str]]:
    with caminho.open("r", encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def salvar_csv_processado(
    vendas: list[dict[str, str]],
    caminho: Path = ARQUIVO_SAIDA,
) -> None:
    with caminho.open("w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CAMPOS_SAIDA)
        escritor.writeheader()
        escritor.writerows(vendas)


def executar_mini_etl() -> list[dict[str, str]]:
    criar_csv_exemplo()
    vendas_brutas = ler_csv()
    vendas_processadas = transformar_vendas(vendas_brutas)
    salvar_csv_processado(vendas_processadas)
    return vendas_processadas


def main() -> None:
    vendas_processadas = executar_mini_etl()
    print(f"Vendas processadas: {len(vendas_processadas)}")
    print(f"Arquivo gerado: {ARQUIVO_SAIDA.name}")


if __name__ == "__main__":
    main()
