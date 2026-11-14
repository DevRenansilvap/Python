# Classificação de Sexo 
while True:
    sexo=input("Qual o sexo F/M ?").upper().strip()
    if sexo == "M":
        print("Sexo Masculino")
        break
    elif sexo =="F":
        print("Sexo Feminino")
        break
    else:
        print("Sexo Invalido!")