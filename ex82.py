print("Bem-vindo ao programa!")
print()
print("----------------")
valores = [0] * 11

for i in range(len(valores)):
    valores[i] = float(input(f"Informe o {i+1}º valor: "))

print()
print("Valores informados:")
print("----------------")
for i in range(len(valores)):
    print(valores[i])
    print("----------------")