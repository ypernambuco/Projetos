"""Cadastro de pessoas com gravação e leitura de arquivo CSV."""

import csv
from pathlib import Path

ARQUIVO_CSV = Path(__file__).with_name("pessoas.csv")
MAIORIDADE = 18

Pessoa = dict[str, str | int]


def ler_texto(campo: str) -> str:
    while True:
        valor = input(f"Digite {campo}: ").strip()
        if valor:
            return valor
        print(f"{campo.capitalize()} não pode ficar em branco.")


def ler_idade() -> int:
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade < 0:
                print("Idade não pode ser negativa.")
                continue
            return idade
        except ValueError:
            print("Por favor, digite um número inteiro válido.")


def ler_sim_ou_nao(mensagem: str) -> bool:
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in {"s", "sim"}:
            return True
        if resposta in {"n", "nao", "não"}:
            return False

        print("Resposta inválida. Digite 's' para sim ou 'n' para não.")


def cadastrar_pessoas() -> list[Pessoa]:
    pessoas: list[Pessoa] = []

    while True:
        pessoa: Pessoa = {
            "nome": ler_texto("o nome"),
            "profissao": ler_texto("a profissão"),
            "idade": ler_idade(),
        }
        pessoas.append(pessoa)

        if not ler_sim_ou_nao("Deseja adicionar outra pessoa? (s/n): "):
            return pessoas


def descrever_maioridade(idade: int) -> str:
    if idade >= MAIORIDADE:
        return "é adulto(a) e já atingiu a maioridade"

    anos_restantes = MAIORIDADE - idade
    return f"é menor de idade e faltam {anos_restantes} ano(s) para a maioridade"


def exibir_pessoas(pessoas: list[Pessoa]) -> None:
    print(f"\nTotal de pessoas cadastradas: {len(pessoas)}\n")

    for pessoa in pessoas:
        nome = pessoa["nome"]
        idade = int(pessoa["idade"])
        profissao = pessoa["profissao"]
        maioridade = descrever_maioridade(idade)

        print(f"{nome} trabalha como {profissao}, {maioridade}.")


def salvar_csv(
    pessoas: list[Pessoa],
    caminho: Path = ARQUIVO_CSV,
    mostrar_mensagem: bool = True,
) -> None:
    with caminho.open("w", newline="", encoding="utf-8") as arquivo:
        campos = ["nome", "idade", "profissao"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(pessoas)

    if mostrar_mensagem:
        print(f"\nArquivo gerado: {caminho.name}")


def carregar_csv(caminho: Path = ARQUIVO_CSV) -> list[Pessoa]:
    pessoas: list[Pessoa] = []

    with caminho.open("r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            pessoas.append(
                {
                    "nome": linha["nome"],
                    "idade": int(linha["idade"]),
                    "profissao": linha["profissao"],
                }
            )

    return pessoas


def contar_adultos(pessoas: list[Pessoa]) -> int:
    return sum(1 for pessoa in pessoas if int(pessoa["idade"]) >= MAIORIDADE)


def analisar_csv(caminho: Path = ARQUIVO_CSV) -> int:
    pessoas = carregar_csv(caminho)

    print("\nAnálise dos dados salvos:\n")

    for pessoa in pessoas:
        nome = pessoa["nome"]
        idade = pessoa["idade"]
        profissao = pessoa["profissao"]
        print(f"{nome} tem {idade} anos e trabalha como {profissao}.")

    total_adultos = contar_adultos(pessoas)
    print(f"\nTotal de adultos: {total_adultos}")
    return total_adultos


def main() -> None:
    pessoas = cadastrar_pessoas()
    exibir_pessoas(pessoas)
    salvar_csv(pessoas)
    analisar_csv()


if __name__ == "__main__":
    main()
