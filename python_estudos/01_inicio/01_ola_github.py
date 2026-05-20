"""Primeiro contato com entrada e saída de dados em Python."""


def obter_nome() -> str:
    nome = input("Qual é o seu nome? ").strip()
    return nome or "visitante"


def main() -> None:
    print("Olá, GitHub!")
    nome = obter_nome()
    print(f"Muito prazer, {nome}! Bem-vindo(a) ao meu repositório de estudos.")


if __name__ == "__main__":
    main()
