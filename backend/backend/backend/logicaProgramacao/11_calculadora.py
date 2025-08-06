num1 = int(input("Digite o 1° número:"))
num2 = int(input("Digite o 2° número:"))

operacao = input("Escolha uma operacao (+,-,*,/):")
match operacao:
    case "+":
        soma = num1 + num2
        print("O resultado é:", soma)

    case "-":
        subtracao = num1 - num2
        print("O resultado é:", subtracao)

    case "*":
        multiplicacao = num1 * num2
        print("O resultado é:", multiplicacao)

    case "/":
        divisao = num1 / num2
        print("O resultado é:", divisao)
