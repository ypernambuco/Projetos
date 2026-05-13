pessoas = []

# =========================
# 1. CADASTRO
# =========================
while True:
    nome = input("Digite seu nome: ")
    profissao = input("Digite sua profissão: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido.")

    pessoa = {
        "nome": nome,
        "profissao": profissao,
        "idade": idade
    }

    pessoas.append(pessoa)

    resposta = input("Deseja adicionar outra pessoa? (s/n): ").lower()
    if resposta == "n":
        break

# =========================
# 2. EXIBIÇÃO
# =========================
print(f"\n=== Total de pessoas cadastradas: {len(pessoas)} ===\n")

for pessoa_atual in pessoas:
    nome = pessoa_atual["nome"]
    idade = pessoa_atual["idade"]
    profissao = pessoa_atual["profissao"]

    mensagem_base = f"Bem-vindo(a), {nome}! Atualmente você é {profissao}."

    if idade < 12:
        falta = 18 - idade
        print(f"{mensagem_base} Você é uma criança! Faltam {falta} anos pra atingir a maioridade.")
    elif idade < 18:
        falta = 18 - idade
        print(f"{mensagem_base} Você é um adolescente! Ainda faltam {falta} anos para a maioridade.")
    else:
        print(f"{mensagem_base} Você é um adulto.")

# =========================
# 3. SALVAR EM CSV
# =========================
import csv

with open("pessoas.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)

    writer.writerow(["nome", "idade", "profissao"])

    for pessoa in pessoas:
        writer.writerow([pessoa["nome"], pessoa["idade"], pessoa["profissao"]])

print("\nArquivo pessoas.csv gerado com sucesso!")

# =========================
# 4. LEITURA E ANÁLISE
# =========================
adultos = 0

print("\n=== Análise dos dados ===\n")

with open("pessoas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)  # pula cabeçalho

    for linha in leitor:
        nome = linha[0]
        idade = int(linha[1])
        profissao = linha[2]

        print(f"{nome} tem {idade} anos e é {profissao}")

        if idade >= 18:
            adultos += 1

print(f"\nTotal de adultos: {adultos}")