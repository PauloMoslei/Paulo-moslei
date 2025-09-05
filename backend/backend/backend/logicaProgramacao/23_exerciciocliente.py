# Eu como um dono de concessionaria de 
# carro importados, preciso de um sistema
# para controlar meu estoque de veículos. Para
# me organizar melhor, além do nome gostaria de
# guardar o ano, quilometragem, marca, preço, menu,
# onde eu possa cadastrar, alterar, excluir e listar
# meus veículos. Para me sentir especial, quero
# que o nome da minha loja apareça no topo do menu

import json

print("\n=== Moya's Imports ===\n")

try:
    with open("estoque.json", "r") as f:
        veiculos = json.load(f)
except FileNotFoundError:
    veiculos = []

def cadastrar():
    nome = input("Nome: ")
    marca = input("Marca: ")
    ano = input("Ano: ")
    km = input("Quilometragem: ")
    preco = input("Preço: ")

    veiculo = {
        "Nome": nome,
        "Marca": marca,
        "Ano": ano,
        "KM": km,
        "Preço": preco
    }

    veiculos.append(veiculo)
    print("Veículo cadastrado!\n")

def listar():
    if not veiculos:
        print("Nenhum veículo cadastrado.\n")
        return
    for i, v in enumerate(veiculos):
        print(f"\nVeículo [{i+1}]:")
        for chave, valor in v.items():
            print(f"{chave}: {valor}")
    print()

def alterar():
    listar()
    try:
        i = int(input("Número do veículo a alterar: ")) - 1
        veiculos[i]["Nome"] = input("Novo nome: ")
        veiculos[i]["Marca"] = input("Nova marca: ")
        veiculos[i]["Ano"] = input("Novo ano: ")
        veiculos[i]["KM"] = input("Nova quilometragem: ")
        veiculos[i]["Preço"] = input("Novo preço: ")
        print("Veículo alterado!\n")
    except:
        print("Erro ao alterar.\n")

def excluir():
    listar()
    try:
        i = int(input("Número do veículo a excluir: ")) - 1
        veiculos.pop(i)
        print("Veículo excluído!\n")
    except:
        print("Erro ao excluir.\n")

def salvar():
    with open("estoque.json", "w") as f:
        json.dump(veiculos, f, indent=4)
    print("Dados salvos!\n")

while True:
    print("1. Cadastrar\n2. Listar\n3. Alterar\n4. Excluir\n5. Sair")
    op = input("Opção: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    elif op == "3":
        alterar()
    elif op == "4":
        excluir()
    elif op == "5":
        salvar()
        print("Saindo...")
        break
    else:
        print("Opção inválida.\n")



