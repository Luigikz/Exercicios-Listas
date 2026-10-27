print("Bem-vindo ao programa!")
print()

valores = [0] * 12
for i in range(len(valores)):
    valores[i] = int(input("Informe o valor: "))

print()
print("Valores pares:")
for i in range(len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i])

print()
print("Valores ímpares:")
for i in range(len(valores)):
    if valores[i] % 2 != 0:
        print(valores[i])