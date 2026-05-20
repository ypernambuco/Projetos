"""Calcula quanto tempo falta para uma pessoa atingir a maioridade."""

MAIORIDADE = 18


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


def anos_para_maioridade(idade: int) -> int:
    if idade < 0:
        raise ValueError("A idade não pode ser negativa.")

    return max(MAIORIDADE - idade, 0)


def main() -> None:
    print("Olá!")
    nome = input("Qual é o seu nome? ").strip() or "visitante"
    idade = ler_idade()
    anos_restantes = anos_para_maioridade(idade)

    if anos_restantes == 0:
        print(f"{nome}, você já atingiu a maioridade.")
    else:
        print(f"{nome}, faltam {anos_restantes} ano(s) para você atingir a maioridade.")


if __name__ == "__main__":
    main()
