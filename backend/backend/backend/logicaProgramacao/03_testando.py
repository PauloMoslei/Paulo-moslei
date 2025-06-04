salario = int(input("Qual seu salario mensal?"))
if salario > 6500:
    print("Alta classe")
elif salario >= 3000 and salario <= 6499:
    print("Média classe")
else:
    print("classe baixa")