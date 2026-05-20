"""Classifica uma pessoa por faixa etária."""


def ler_idade() -> int:
    while True:
        try:
            idade = int(input("Qual é a sua idade? "))
            if idade < 0:
                print("Idade não pode ser negativa.")
                continue
            return idade
        except ValueError:
            print("Digite um número inteiro válido.")


def classificar_idade(idade: int) -> str:
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")

    if idade < 12:
        return "criança"
    if idade < 18:
        return "adolescente"
    return "adulto"


def main() -> None:
    print("Olá, GitHub!")
    nome = input("Qual é o seu nome? ").strip() or "visitante"
    idade = ler_idade()
    classificacao = classificar_idade(idade)

    print(f"Olá, {nome}! Você está na categoria: {classificacao}.")
    print("Bem-vindo(a) ao meu repositório de estudos em Python.")


if __name__ == "__main__":
    main()
