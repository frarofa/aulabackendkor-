#Vamos criar um dicionário com duas chaves e tentar retornar seus dados pela rota
dicionario = {
    "nome":"Luke Skywalker",
    "nascimento":"Tatooine"

}
#Importando flask para podermos usar no nosso programa
from flask import Flask

#criar a aplicação Flask
app = Flask(__name__)

@app.route("/teste")
def mostra_dicionario():
    return dicionario

@app.route("/")
def dados_usuario():
    return f"<b>O usuário {dicionario['nome']} nasceu em {dicionario['nascimento']}</b>"

#colocar a aplicação para rodar
app.run(debug=True)
