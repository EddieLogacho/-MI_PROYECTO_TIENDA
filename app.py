from flask import Flask

app = Flask(__name__)

# Ruta principal: muestra el nombre del sistema (no "Hola mundo")
@app.route("/")
def inicio():
    return "Bienvenido a Tienda Tech – Catálogo y ofertas"

# Ruta dinámica 1: producto por nombre
# Ejemplo: http://127.0.0.1:5000/producto/Laptop
@app.route("/producto/<nombre>")
def producto(nombre):
    return f"Producto: {nombre} – disponible."

# Ruta dinámica 2: oferta por código (entero)
# Ejemplo: http://127.0.0.1:5000/oferta/101
@app.route("/oferta/<int:codigo>")
def oferta(codigo):
    return f"Oferta #{codigo} – consulta exitosa."

if __name__ == "__main__":
    app.run(debug=True)