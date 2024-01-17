# iportanto as bibliotecas que vamos utilizar
from flask import Flask

# instanciando o Flask
app = Flask(__name__)

# criando a primeira rota
@app.route("/<int:numero>", methods=["Get","POST"])
def ola(numero):
    return f"Olá Website {numero}  "

if __name__ == "__main__":
    app.run(debug=True)