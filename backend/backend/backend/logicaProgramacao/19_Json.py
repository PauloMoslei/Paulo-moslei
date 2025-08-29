#[
#   {Nome: "Arroz",
#    QTD: 2t,    
#    Valor: 23.00,},
#]

#[ 
#    {Nome: "Jaqueline"},
#    {Nome: "Paulo"},
#    {Nome: "Helloisy"},
#    {Nome: "Lara"},
#]

import json
inventario = []
try:
    with open('loja.json', 'r') as arquivo:
        inventario = json.load(arquivo)
        print ("arquivo carregado")
except FileNotFoundError:
    print ("arquivo não encontrado")
    print ("\n ---- CADASTRAR PRODUTO ----")
    nome_produto = input("Digite o nome do produto: ")
    while True: 
        try:
            quantidade = int(input("Digite a quantidade: "))
            break
        except ValueError: 
            print ("Coloque apenas números!")
    while True:
        try:
            preco = float(input("Digite o preco: "))
            break
        except ValueError:
            print("Digite o preço corretamente")
    novo_produto = {
        "nome_produto": nome_produto,
        "quantidade": quantidade,
        "preco": preco,
        "tem_estoque": quantidade > 0}
inventario.append(novo_produto)
with open('loja.json', 'w') as arquivo:
    json.dump(inventario, arquivo, indent = 4)
    print(f"\n o produto {nome_produto} foi cadastrado")
    

            

