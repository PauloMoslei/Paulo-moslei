# open ("arquivo", modo)
# modo de leitura "r"
# modo de escrita "w" substitui o conteudo
# modo de escrita "a" acrescenta conteudo
def gerar_lista_compras():
    print("------} VAMOS AS COMPRAS {------")
    print("[ao encerrar digite fim]")

    with open("comida.txt", 'w') as comidas:
       while True:
            item = input("Digite o item: ")
            if item.lower() == "fim":
               print("encerrando lista")
               break
            comidas.write(item + "\n")
gerar_lista_compras()
def listar_itens():
    with open ("comida.txt", 'r') as lista:
        print("------] Lista de Compras [------")
        for item in lista:
            produto = item.strip() #strip é pra cortar linha de produto
            print("item:", produto)
listar_itens()

