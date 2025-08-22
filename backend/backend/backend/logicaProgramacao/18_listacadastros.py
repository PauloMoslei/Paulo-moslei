# EXEMPLO DA INTERNET
# import json
# import os

# ARQUIVO = "usuarios.txt"

# # Função para carregar usuários do arquivo
# def carregar_usuarios():
#     try:
#         if os.path.exists(ARQUIVO):
#             with open(ARQUIVO, "r") as f:
#                 return json.load(f)
#         else:
#             return []
#     except Exception as e:
#         print("Erro ao carregar usuários:", e)
#         return []

# # Função para salvar usuários no arquivo
# def salvar_usuarios(lista):
#     try:
#         with open(ARQUIVO, "w") as f:
#             json.dump(lista, f, indent=4)
#         print("Dados salvos com sucesso.")
#     except Exception as e:
#         print("Erro ao salvar usuários:", e)

# # Função para adicionar novo usuário
# def adicionar_usuario():
#     try:
#         nome = input("Digite o nome do usuário: ").strip()
#         email = input("Digite o e-mail do usuário: ").strip()

#         usuarios = carregar_usuarios()
#         usuarios.append({"nome": nome, "email": email})
#         salvar_usuarios(usuarios)
#     except Exception as e:
#         print("Erro ao adicionar usuário:", e)

# # Função para listar todos os usuários
# def listar_usuarios():
#     usuarios = carregar_usuarios()
#     if not usuarios:
#         print("Nenhum usuário cadastrado.")
#         return
#     print("\n--- Usuários Cadastrados ---")
#     for i, u in enumerate(usuarios):
#         print(f"{i + 1}. Nome: {u['nome']}, Email: {u['email']}")
#     print("----------------------------")

# # Função para alterar um usuário
# def alterar_usuario():
#     usuarios = carregar_usuarios()
#     listar_usuarios()
#     try:
#         indice = int(input("Digite o número do usuário a alterar: ")) - 1
#         if 0 <= indice < len(usuarios):
#             nome = input("Novo nome (deixe em branco para manter): ").strip()
#             email = input("Novo e-mail (deixe em branco para manter): ").strip()
#             if nome:
#                 usuarios[indice]['nome'] = nome
#             if email:
#                 usuarios[indice]['email'] = email
#             salvar_usuarios(usuarios)
#             print("Usuário alterado com sucesso.")
#         else:
#             print("Usuário não encontrado.")
#     except ValueError:
#         print("Entrada inválida.")
#     except Exception as e:
#         print("Erro ao alterar usuário:", e)

# # Função para excluir um usuário
# def excluir_usuario():
#     usuarios = carregar_usuarios()
#     listar_usuarios()
#     try:
#         indice = int(input("Digite o número do usuário a excluir: ")) - 1
#         if 0 <= indice < len(usuarios):
#             usuario_removido = usuarios.pop(indice)
#             salvar_usuarios(usuarios)
#             print(f"Usuário '{usuario_removido['nome']}' removido com sucesso.")
#         else:
#             print("Usuário não encontrado.")
#     except ValueError:
#         print("Entrada inválida.")
#     except Exception as e:
#         print("Erro ao excluir usuário:", e)

# # Menu principal
# def menu():
#     while True:
#         print("\n==== MENU ====")
#         print("1. Adicionar Usuário")
#         print("2. Listar Usuários")
#         print("3. Alterar Usuário")
#         print("4. Excluir Usuário")
#         print("5. Sair")
#         try:
#             opcao = int(input("Escolha uma opção: "))
#             if opcao == 1:
#                 adicionar_usuario()
#             elif opcao == 2:
#                 listar_usuarios()
#             elif opcao == 3:
#                 alterar_usuario()
#             elif opcao == 4:
#                 excluir_usuario()
#             elif opcao == 5:
#                 print("Saindo do programa.")
#                 break
#             else:
#                 print("Opção inválida.")
#         except ValueError:
#             print("Digite um número válido.")

# # Executa o menu
# menu()

# DESENVOLVIDO POR MIM:

def adicionar():
    try:
        nome = input("Nome: ")
        with open("usuarios.txt", "a") as f:
            f.write(nome + "\n")
        print("Usuário adicionado.")
    except:
        print("Erro ao adicionar.")

def listar():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        for i, u in enumerate(usuarios):
            print(f"{i + 1}. {u.strip()}")
    except:
        print("Nenhum usuário cadastrado.")

def alterar():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines() 
        listar()
        i = int(input("Número do usuário para alterar: ")) - 1
        novo = input("Novo nome: ")
        usuarios[i] = novo + "\n"
        with open("usuarios.txt", "w") as f:
            f.writelines(usuarios)
        print("Usuário alterado.")
    except:
        print("Erro ao alterar.")

def excluir():
    try:
        with open("usuarios.txt", "r") as f:
            usuarios = f.readlines()
        listar()
        i = int(input("Número do usuário para excluir: ")) - 1
        usuarios.pop(i)
        with open("usuarios.txt", "w") as f:
            f.writelines(usuarios)
        print("Usuário excluído.")
    except:
        print("Erro ao excluir.")

def menu():
    while True:
        print("\n1. Adicionar\n2. Listar\n3. Alterar\n4. Excluir\n5. Sair")
        op = input("Escolha: ")
        match op:
            case "1":
                adicionar()
            case "2":
                listar()
            case "3":
                alterar()
            case "4":
                excluir()
            case "5":
                break
            case _:
                print("Opção inválida.")

menu()

