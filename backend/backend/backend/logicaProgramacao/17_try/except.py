# try:
#    numero = int(input("Digite um número inteiro: "))
#    print(f"Você digitou o número {numero}")
# except ValueError:
#    print("Erro: isso não é um número inteiro válido.")

# Exemplo 1°
def pedir_numero():
    try:
        return float(input("Digite um número: "))
    except ValueError:
        print("Número inválido!")
        return 0.0

n = pedir_numero()
print("Você digitou:", n)

# Exemplo 2°
def salvar_texto(texto):
    try:
        with open("saida.txt", "w") as f:
            f.write(texto)
        print("Salvo com sucesso.")
    except Exception as e:
        print("Deu erro:", e)

salvar_texto("Chegamo no baguio!")

