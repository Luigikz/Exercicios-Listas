print("Bem-vindo ao programa!")
print()

valores = [0] * 18

for i in range(len(valores)):
    valores[i] = int(input(f"Digite o {i + 1}º número: "))

print()
print("Números em ordem inversa:")
for i in range(len(valores) - 1, -1, -1):
    print(valores[i])