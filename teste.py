print("Boa noite!")

nome = input("Por favor, digite o seu nome!")

print("Você parece ser uma pessoa incrível, " + nome) ## proibido!! nunca fazer assim!

print("Você parece ser uma pessoa incrível, {}".format(nome)) ## essa é top

print(f"Você parece ser uma pessoa incrível, {nome}") ## essa é top também

valor1 = float(input("Informe um valor numérico!"))
valor2 = float(input("Informe outro valor numérico!"))

resultado = valor1 + valor2
print(f"O resultado é {resultado}")