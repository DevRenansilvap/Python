num1 = 0
num2 = 0

while True:
    operador = input("Qual operação você deseja fazer ?   |  Digite 0 p/ Sair. ")
    if operador == "0":
        break
    num1 = float(input("Qual o numero 1: "))
    num2 = float(input("Qual o numero 2: "))

    if operador == "*":
        print(f"{num1} * {num2} = {num1*num2}")
    elif operador == "+":
        print(f"{num1} + {num2} = {num1+num2}")
    elif operador == "/":
        print(f"{num1} / {num2} = {num1/num2}")
    elif operador == "-":
        print(f"{num1} - {num2} = {num1-num2}")
    else:
        print("Operador invalido!!")