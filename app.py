from flask import Flask, jsonify

app = Flask(__name__)

# Datos simulados del inventario de Logistica Andina
inventario = [
    {"id": 1, "producto": "Laptop Corporativa", "stock": 15},
    {"id": 2, "producto": "Lector Codigo de Barras", "stock": 40},
    {"id": 3, "producto": "Impresora Termica", "stock": 8}
]

@app.route('/')
def home():
    return jsonify({
        "empresa": "Logistica Andina Huancayo",
        "modulo": "Control de Inventario",
        "estado": "Operativo"
    })

@app.route('/inventario')
def get_inventario():
    return jsonify(inventario)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
