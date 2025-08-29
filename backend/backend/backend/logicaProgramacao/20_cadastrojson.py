import json 
usuarios = []

try:
    with open ('usuarios.json', 'r') as arquivo:
        usuarios = json.load (arquivo)
        print ("cadastros feitos!!")
except FileNotFoundError:
    print ("cadastro não encontrado")

    print("\n ---- Cadastrar usuario ---- ")

    nome_usuario = input ("digite o seu nome: ")
    while True:
        try:
            telefone = int (input("digite o seu telefone: "))
            break
        except ValueError:
            print("digite apenas números")
    while True:
        try:
            cidade = input ("digite a sua cidade: ")
            break
        except Exception:
            print ("Digite sem espaco burro!")
    while True:
        try:
            idade = int (input("digite a sua idade: "))
            break
        except ValueError:
            print ("digite apenas numeros")
    while True:
        try:
            sexo = input ("digite o seu sexo: ")
            break
        except Exception:
            print ("digite apenas uma palavra")

    novo_usuario = {
        "nome: ": nome_usuario,
        "telefone: ": telefone,
        "cidade: ": cidade,
        "idade: ": idade,
        "sexo: ": sexo,
        "maior_de_idade: ": idade > 18,
    }

    usuarios.append (novo_usuario)
    with open ('usuarios.json', 'w') as arquivo:
        json.dump (usuarios, arquivo, indent=6)
    print (f"\n cadastro de {nome_usuario} foi realizado com sucesso")

