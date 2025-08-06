operacao = int(input("Coloque sua idade:"))
match operacao:
    case x if x<12 and x>0:
        print("Criança")
    case x if x>12 and x<18:
        print("Adolescente")
    case x if x>18 and x<60:
        print("Adulto")
    case x if x>60 and x<100:
        print("Idoso")
    case x if x>100:
        print("Mumia")
    