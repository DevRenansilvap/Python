# Aumento de preço

# Um produto sofrerá aumento conforme a tabela. Leia o preço antigo, calcule e mostre o novo preço e o percentual aplicado.

# Até R$ 50,00      |       # 5%

# Acima de:
# R$ 50,00 até R$ 100,00|   # 10%

# Acima de R$ 100,00    |   # 15%

preco = float(input("Digite o Preço do Produto para Aplicar o Reajuste: "))

if preco > 0 and preco <= 50:
    print(f"""  Ajuste de 5%
    Preço Atual:{preco}Preço com Ajuste:{preco+(preco*0.05)}""")
elif preco >50 and preco <=100:
    print(f"""  Ajuste de 10%
    Preço Atual:{preco}
    Preço com Ajuste:{preco+(preco*0.1)}""")
elif preco > 100:
    print(f"""  Ajuste de 15%
    Preço Atual:{preco}
    Preço com Ajuste:{preco+(preco*0.15)}""")
else:
    print("Preço invalido!!")