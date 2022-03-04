from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def saludar():
    return "hola mundo"

@app.route('/getnombre/<nombre>', methods=['GET'])
def getnombre(nombre):
    return f"su nombre es {nombre}"

@app.route('/getapellido', methods=['POST'])
def getapellido():
    ape=request.json["apellido"]
    return jsonify({"data": f"un gran saludo al apellido de {ape}"})

@app.route('/op/<n1>/<n2>',methods=['GET'])
def op(n1,n2):
    num1 = int(n1)
    num2 = int(n2)
    sum = num1 + num2
    mul = num1 * num2
    return jsonify({"suma":sum,"multiplicacion": mul})

@app.route('/cuadrado/<base>',methods=['GET'])
def cuadrado(base):
    intBase = int(base)
    perimetro = intBase * 4
    area = intBase * intBase
    return jsonify({"medida":base ,
     "area": area, 
     "perimetro":perimetro})

@app.route('/get_respuesta/<numPalabras>/<tamCentimetros>/<numColores>',methods=['GET'])
def getRespuesta(numPalabras,tamCentimetros,numColores):
    cost_palabra = int(numPalabras) * 25000
    cost_cm = int(tamCentimetros) * 10000
    cost_color = int(numColores) *30000
    cost_dias = 30000
    monto = cost_color + cost_cm + cost_palabra + cost_dias
    return jsonify({"costo palabra":cost_palabra,
     "costo centimetros":cost_cm,
     "costo color": cost_color,
     "costo dias": cost_dias,
     "monto":monto})

app.run(port=5000)