"""Controle simples de estoque com validação de dados."""

from decimal import Decimal, InvalidOperation

Produto = dict[str, str | int | Decimal]


def ler_decimal_positivo(mensagem: str) -> Decimal:
    while True:
        valor_digitado = input(mensagem).replace(",", ".").strip()

        try:
            valor = Decimal(valor_digitado)
            if valor < 0:
                print("O valor não pode ser negativo.")
                continue
            return valor
        except InvalidOperation:
            print("Digite um número válido.")


def ler_inteiro_positivo(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("A quantidade não pode ser negativa.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_sim_ou_nao(mensagem: str) -> bool:
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in {"s", "sim"}:
            return True
        if resposta in {"n", "nao", "não"}:
            return False

        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def cadastrar_produtos() -> list[Produto]:
    estoque: list[Produto] = []

    while True:
        produto = input("Digite o nome do produto: ").strip().title()
        preco = ler_decimal_positivo("Digite o preço do produto: R$ ")
        quantidade = ler_inteiro_positivo("Digite a quantidade em estoque: ")

        estoque.append(
            {
                "produto": produto or "Produto sem nome",
                "preco": preco,
                "quantidade": quantidade,
            }
        )

        if not ler_sim_ou_nao("Deseja adicionar outro produto? (s/n): "):
            return estoque


def calcular_total_item(item: Produto) -> Decimal:
    return Decimal(item["quantidade"]) * Decimal(item["preco"])


def calcular_total_estoque(estoque: list[Produto]) -> Decimal:
    return sum((calcular_total_item(item) for item in estoque), Decimal("0"))


def formatar_moeda(valor: Decimal) -> str:
    return f"R$ {valor:.2f}"


def exibir_relatorio(estoque: list[Produto]) -> None:
    print(f"\nProdutos cadastrados: {len(estoque)}\n")

    for item in estoque:
        total_item = calcular_total_item(item)

        print(f"Produto: {item['produto']}")
        print(f"Preço unitário: {formatar_moeda(Decimal(item['preco']))}")
        print(f"Quantidade: {item['quantidade']}")
        print(f"Total do item: {formatar_moeda(total_item)}\n")

    print(f"Valor total do estoque: {formatar_moeda(calcular_total_estoque(estoque))}")


def main() -> None:
    estoque = cadastrar_produtos()
    exibir_relatorio(estoque)


if __name__ == "__main__":
    main()
