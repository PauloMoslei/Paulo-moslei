import json

try:
    with open("categorias.json", "r") as f:
        categorias = json.load(f)
except FileNotFoundError:
    categorias = []

try:
    with open("produtos.json", "r") as f:
        produtos = json.load(f)
except FileNotFoundError:
    produtos = []

def cadastrar_categoria():
    try:
        id_categoria = int(input("ID da nova categoria: "))
        nome = input("Nome da categoria: ")

        for c in categorias:
            if c["id_categoria"] == id_categoria:
                print("ID já existe. Tente outro.\n")
                return

        nova_categoria = {
            "id_categoria": id_categoria,
            "nome_categoria": nome
        }

        categorias.append(nova_categoria)
        print("Categoria cadastrada com sucesso!\n")
    except ValueError:
        print("ID inválido. Use apenas números.\n")

def listar_categorias():
    if not categorias:
        print("Nenhuma categoria cadastrada.\n")
        return
    print("___ Categorias ___")
    for lista in categorias:
        print(f"[{lista['id_categoria']}]  {lista['nome_categoria']}")
    print()

def cadastrar_produto():
    if not categorias:
        print("Cadastre uma categoria primeiro.\n")
        return

    listar_categorias()

    try:
        id_produto = int(input("ID do produto: "))
        for p in produtos:
            if p["id_produto"] == id_produto:
                print("ID de produto já existe.\n")
                return

        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        id_categoria = int(input("ID da categoria associada: "))

        encontrado = False
        for lista in categorias:
            if lista["id_categoria"] == id_categoria:
                encontrado = True
                break

        if not encontrado:
            print("Categoria não encontrada.\n")
            return

        novo_produto = {
            "id_produto": id_produto,
            "nome_produto": nome,
            "preco": preco,
            "id_categoria_associada": id_categoria
        }

        produtos.append(novo_produto)
        print("Produto cadastrado com sucesso!\n")
    except ValueError:
        print("Entrada inválida. Use apenas números.\n")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.\n")
        return

    print("___ Produtos ___")
    for lista2 in produtos:
        categoria_nome = "Categoria Desconhecida"
        for lista in categorias:
            if lista["id_categoria"] == lista2["id_categoria_associada"]:
                categoria_nome = lista["nome_categoria"]
                break
        print(f"\nID: {lista2['id_produto']}")
        print(f"Nome: {lista2['nome_produto']}")
        print(f"Preço: R$ {lista2['preco']}")
        print(f"Categoria: {categoria_nome}")
    print()

while True:
    print("1. Cadastrar Categoria")
    print("2. Listar Categorias")
    print("3. Cadastrar Produto")
    print("4. Listar Produtos")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_categoria()
    elif opcao == "2":
        listar_categorias()
    elif opcao == "3":
        cadastrar_produto()
    elif opcao == "4":
        listar_produtos()
    elif opcao == "5":
        with open("categorias.json", "w") as f:
            json.dump(categorias, f, indent=4)
        with open("produtos.json", "w") as f:
            json.dump(produtos, f, indent=4)
        print("Dados salvos. Saindo...")
        break
    else:
        print("Opção inválida.\n")
