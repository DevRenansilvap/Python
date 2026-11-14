#Número positivo
#Leia um número. Caso ele seja positivo, calcule e mostre:

#O número ao quadrado.
# A raiz quadrada do número.

while True:
    num = float(input("Qual o Numero?"))

    if num % 2 == 0:
        print("É Par!")
        print(f"{num} ao Quadrado é:{num**2}")
        print(f"A Raiz Quadrada é:{num*0.5}")
        break
    else:
        print(f"O Numero {num} não é Par!!")