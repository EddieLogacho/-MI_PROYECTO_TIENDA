from flask import Flask, render_template, request

app = Flask(__name__)

# ====== Datos de ejemplo (puedes reemplazar por tu base de datos) ======
PRODUCTOS = [
    {"id": 1, "nombre": "iPhone 14", "categoria": "celulares", "precio": 999.0, "stock": 0},
    {"id": 2, "nombre": "Samsung Galaxy S23", "categoria": "celulares", "precio": 879.0, "stock": 5},
    {"id": 3, "nombre": "Acer Aspire 5", "categoria": "laptops", "precio": 569.0, "stock": 3},
    {"id": 4, "nombre": "HP ProBook 430", "categoria": "laptops", "precio": 589.0, "stock": 0},
    {"id": 5, "nombre": "Sony WH-CH520", "categoria": "audifonos", "precio": 49.9, "stock": 12},
]
# ======================================================================


@app.route("/")
def index():
    """Página de inicio con algunos destacados."""
    destacados = PRODUCTOS[:4]
    return render_template(
        "index.html",
        productos_destacados=destacados,
        active_page="home"
    )


@app.route("/catalogo")
def catalogo():
    """Catálogo completo con búsqueda por ?q=..."""
    q = request.args.get("q", "").strip().lower()
    productos = PRODUCTOS
    if q:
        productos = [
            p for p in productos
            if q in p["nombre"].lower() or q in p["categoria"].lower()
        ]
    return render_template(
        "catalogo.html",
        productos=productos,
        query=q,
        active_page="catalogo"
    )


@app.route("/stock")
def stock():
    """Solo productos con stock > 0."""
    disponibles = [p for p in PRODUCTOS if p["stock"] > 0]
    return render_template(
        "stock.html",
        productos=disponibles,
        active_page="stock"
    )


@app.route("/about")
def about():
    """Página Acerca de."""
    return render_template("about.html", active_page="about")


# Punto de entrada de la app
if __name__ == "__main__":
    # NOTA: debug=False para que no aparezca el debugger y el autoreload.
    # La advertencia en rojo de "development server" es normal al usar Flask localmente.
    app.run(debug=True)