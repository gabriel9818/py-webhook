from flask import Flask, request, abort,jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Extraemos los datos JSON enviados en el cuerpo de la solicitud
        data = request.json
        num1 = data.get('num1')
        num2 = data.get('num2')

        # Validamos que los números estén presentes
        if num1 is None or num2 is None:
            return {"error": "Both 'num1' and 'num2' are required"}, 400
        
        # Realizamos la suma
        suma = num1 + num2
        print(f"Suma recibida: {num1} + {num2} = {suma}")
        return {"suma": suma}, 200
    else:
        abort(400)

@app.route('/sumar', methods=['GET'])
def sumar():
    num1 = request.args.get('num1', default=0, type=int)
    num2 = request.args.get('num2', default=0, type=int)
    resultado = {'suma': num1 + num2}
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
