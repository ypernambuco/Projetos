# Pergunta o nome de um produto
# Pergunta o preço dele
# Pergunta a quantidade em estoque
# Faz isso se repetir até o usuário digitar "n" pra parar
# No final, mostra todos os produtos cadastrados

estoque = []

while True:
    produto = input("Digite o nome do produto: ").capitalize()
    while True:        
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco < 0:
                print("Preço não pode ser negativo.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido para o preço.")

    while True:
        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido para a quantidade.")

    estoque.append({
        "produto": produto,
        "preço": preco,
        "quantidade": quantidade
    })

    resposta = input("Deseja adicionar outro produto? (s/n): ").lower()
    if resposta == "n":
        break                 

print(f"\nProdutos cadastrados: {len(estoque)}\n")

total = 0

for item in estoque:
    print(f"Produto: {item['produto']}, Preço: R${round(item['preço'], 2)}, Quantidade: {item['quantidade']}")
    print(f"{item['produto']}*{item['quantidade']} = R${round(item['preço']*item['quantidade'], 2)}\n")
    total += item['preço']*item['quantidade']

print(f"Valor total do estoque: R${round(total, 2)}")