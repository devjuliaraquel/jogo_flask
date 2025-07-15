from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hanoi", methods=["GET", "POST"])
def hanoi():
    return render_template("hanoi.html")

@app.route("/adivinha", methods=["GET", "POST"])
def adivinha():
    mensagem = ""
    if request.method == "POST":
        palpite = int(request.form["palpite"])
        numero = int(request.form["numero_aleatorio"])
        if palpite == numero:
            mensagem = "Você acertou!"
        elif palpite > numero:
            mensagem = "Palpite alto demais."
        else:
            mensagem = "Palpite baixo demais."
        return render_template("adivinha.html", mensagem=mensagem, numero_aleatorio=numero)
    numero_aleatorio = random.randint(1, 100)
    return render_template("adivinha.html", numero_aleatorio=numero_aleatorio, mensagem=mensagem)

@app.route("/ppt", methods=["GET", "POST"])
def PedraPapelTesoura():
    resultado = ""
    if request.method == "POST":
        opcoes = ["pedra", "papel", "tesoura"]
        escolha_usuario = request.form["escolha"]
        escolha_computador = random.choice(opcoes)
        if escolha_usuario == escolha_computador:
            resultado = "Empate!"
        elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
             (escolha_usuario == "papel" and escolha_computador == "pedra") or \
             (escolha_usuario == "tesoura" and escolha_computador == "papel"):
            resultado = "Você ganhou!"
        else:
            resultado = "Você perdeu!"
        return render_template("pedra_papel_tesoura.html", resultado=resultado, computador=escolha_computador)
    return render_template("ppt.html", resultado=resultado)

@app.route("/batalha", methods=["GET", "POST"])
def batalha():
    return render_template("batalha.html")

@app.route("/forca", methods=["GET", "POST"])
def forca():
    return render_template("forca.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    return render_template("quiz.html")

if __name__ == "__main__":
    app.run(debug=True)
