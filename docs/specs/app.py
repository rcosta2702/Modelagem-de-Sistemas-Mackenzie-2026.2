"""Servidor web da calculadora de frete."""

from flask import Flask, jsonify, render_template, request

from frete import calcular_frete


app = Flask(__name__, template_folder="../templates")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/calcular")
def calcular():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify(erro="Envie um objeto JSON com valor_carrinho e cep"), 400

    try:
        resultado = calcular_frete(dados.get("valor_carrinho"), dados.get("cep"))
    except ValueError as erro:
        return jsonify(erro=str(erro)), 400
    return jsonify(resultado)


if __name__ == "__main__":
    app.run()
