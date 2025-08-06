operacao = int(input("Qual sua nota:"))
match operacao:
    case 10:
        print("Parabéns, vc tirou nota máxima")
    case 7|8|9:
        print("Aprovado")
    case 0|1|2|3|4|5|6:
        print("Reprovado")
    case _:
        print("Valor Inválido")
