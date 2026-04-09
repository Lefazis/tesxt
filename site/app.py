from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# 🔑 API que estamos utilizando no projeto
genai.configure(api_key="AIzaSyBf9ivxwHF7Qp8FDc1HIUx--_u1hJR2z6E")

model = genai.GenerativeModel("gemini-2.5-flash")

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota do chatbot
@app.route("/chat", methods=["POST"])
def chat():
    mensagem = request.json["mensagem"]

    try:
        resposta = model.generate_content(mensagem)
        return jsonify({"resposta": resposta.text})
    except Exception as e:
        return jsonify({"resposta": f"Erro: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)