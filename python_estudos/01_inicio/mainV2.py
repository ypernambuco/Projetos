print("Olá, Github! 🚀")

nome = input("Qual é o seu nome?  ")
idade = int(input("Qual é a sua idade?  "))

if idade < 12:
    print(f"Olá, {nome}! Você é uma criança! Bem-vindo(a) ao meu repositório do GitHub! 🌟")
elif idade < 18:
    print(f"Olá, {nome}! Você é menor de idade! Bem-vindo(a) ao meu repositório do GitHub! 🌟")
else:
    print(f"Olá, {nome}! Você é maior de idade! Bem-vindo(a) ao meu repositório do GitHub! 🌟")