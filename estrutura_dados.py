
#Este programa vai cadastrar um produto em um dicionário
print("CADASTRO DE PRODUTO")
#O dicionário abaixo está vazio, e vai ser usado para guardar os dados
produto = {}

#Nessas linhas, vamos indicar o dicionário e a chave onde será armazenado o dado
produto["id"] = int(input("Insira o código do produto: "))
produto["nome"] = input("Insira o nome do produto: ")
produto["preco"] = float(input("Insira o preço do produto: "))

#Esta linha exibe o dicionário completo, com a mesma estrutura do código
print(produto)

#o código abaixo percorre os items do dicionário, separando chave e valor e exibe
for chave, valor in produto.items():
    print(f"{chave.upper()} \t {valor}")
