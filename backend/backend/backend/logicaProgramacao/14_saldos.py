nome = input("Nome: ")
saldo = 0
opcao = ""

while opcao != "4":
    print("\n1. Depositar\n2. Sacar\n3. Saldo\n4. Sair")
    opcao = input("Opção: ")

    match opcao:
        case "1":
            saldo += float(input("Valor: "))
        case "2":
            valor = float(input("Valor: "))
            if valor <= saldo:
                saldo -= valor
            else:
                print("Você não tem essa quantia! Seu saldo:", saldo)
        case "3":
            print(f"Saldo: R$ {saldo:.2f}")
        case "sair":
            print("Até logo", nome)
        case _:
            print("Opção inválida!")

