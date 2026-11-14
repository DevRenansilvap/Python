# Empréstimo
# Leia o salário de um trabalhador e o valor da prestação. Se a prestação for maior que 20% do salário, imprima Empréstimo não concedido. Caso contrário, imprima Empréstimo concedido.

salario = float(input("Digite o valor do seu Salario: "))

emprestimo = float(input("Digite o valor da Prestação: "))

if emprestimo > (salario*0.2):
    print("Emprestimo Negado Major!!")
else:
    print("Emprestimo Concedido Autarquia!!")