def gerar_lista_alunos():
    print("------} TERCEIRAO SESI 2025 {------")
    print("[ao encerrar digite encerrar]")

    with open("terceirao.txt", 'w') as alunos:
       while True:
            aluno = input("Coloque o nome: ")
            if aluno.lower() == "encerrar":
               print("----encerrando lista de alunos----")
               break
            alunos.write(aluno + "\n")
gerar_lista_alunos()
def listar_todos():
    with open ("terceirao.txt", 'r') as lista:
        print("------] Lista de Alunos [------")
        for aluno1 in lista:
            produto = aluno1.strip() #strip é pra cortar linha de produto
            print("Aluno:", produto)
listar_todos()