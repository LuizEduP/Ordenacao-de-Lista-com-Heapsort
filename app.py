from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = "http://localhost:5000/ordenar"  # Porta onde o back-end estará rodando

@app.route('/ordenar', methods=['POST'])
def ordenar():
    dados = request.get_json()

    if not dados or 'numeros' not in dados:
        return jsonify({'erro': 'A chave "numeros" é obrigatória.'}), 400

    numeros_str = dados['numeros']

    try:
        # Converte a string "5, 3, 1" para [5, 3, 1]
        lista = [int(n.strip()) for n in numeros_str.split(',')]
    except ValueError:
        return jsonify({'erro': 'Todos os valores devem ser números inteiros separados por vírgula.'}), 400

    try:
        # Envia os dados para o BACK-END que faz o Heapsort
        resposta = requests.post(BACKEND_URL, json={'numeros': lista})
        resposta.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({'erro': 'Erro ao se comunicar com o back-end.', 'detalhes': str(e)}), 500

    return jsonify(resposta.json()), resposta.status_code

if __name__ == '__main__':
    app.run(port=5000, debug=True)
