from flask import Flask, request, jsonify, render_template
from heapsort import heapsort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ordenar', methods=['POST'])
def ordenar():
    data = request.get_json()
    try:
        numeros = list(map(int, data.get('numeros', [])))
    except:
        return jsonify({'erro': 'Entrada inválida. Use apenas números separados por vírgula.'}), 400

    resultado = heapsort(numeros)
    return jsonify({'ordenado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
