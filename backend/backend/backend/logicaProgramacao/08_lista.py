meus_carros = ["Chevette", "Panamera", "Corvette", "Opala", "Aventador"]
print(f"Todos os carros: {meus_carros}")

meus_carros.append("Maverick")
print(f"carro adicionado: {meus_carros}")

meus_carros.insert(1, "Mustang")
print(f"Carro em lugar específico: {meus_carros}")

meus_carros.remove("Chevette")
print(f"Carro removido: {meus_carros}")

carro_removido = meus_carros.pop()
print(f"Último carro removido ('{carro_removido}'): {meus_carros}")
