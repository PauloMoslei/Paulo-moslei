#ATV1
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#ATV2
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#ATV3
for numero in range(10, 0, -1):
    print(numero)

#ATV4
numero = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#ATV5
soma_total = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero == 0:
        break
    
    soma_total += numero 

print(f"A soma total dos números digitados é: {soma_total}")

#ATV6
numero_secreto = 5

print("Descubra o número secreto!")

while True:
    palpite = int(input("Digite seu número (entre 1 e 10): "))
    
    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")

print("Fim do jogo!")

#ATV7
lista_compras = ["maçã", "banana", "leite"]

print("\nLista Inicial:")
print(*[f"{i+1}. {item}" for i, item in enumerate(lista_compras)], sep="\n")

while True:
    novo_item = input("\nNovo item (ou 'sair' para encerrar): ").strip()
    
    if novo_item.lower() == 'sair':
        break
        
    if novo_item:
        lista_compras.append(novo_item)
        print("\nLista Atualizada:")
        print(*[f"{i+1}. {item}" for i, item in enumerate(lista_compras)], sep="\n")
    else:
        print("Por favor, digite um item")

print("\nLista Final:", lista_compras)

#ATV8
numeros = [10, 5, 20, 8, 15]
print(f"O maior número é: {max(numeros)}")
