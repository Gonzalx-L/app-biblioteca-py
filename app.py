from flask import Flask, render_template, request, redirect, url_for, session
import datetime
from analysis.estadisticas import top_libros_mas_prestados, top_alumnos_mas_prestaron


app = Flask(__name__)
app.secret_key = "biblioteca123"

from services.libros_service import get_libros, add_libro
from services.alumnos_service import get_alumnos, add_alumno
from services.prestamos_service import get_prestamos, add_prestamo, marcar_devuelto as marcar_devuelto_service

USUARIOS = {"admin": "1234"}

# -------------------- LOGIN --------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        if USUARIOS.get(user) == pwd:
            session["usuario"] = user
            return redirect(url_for("dashboard"))
        return render_template("login.html", error="Usuario o contraseña incorrectos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html",
                           libros=get_libros(),
                           alumnos=get_alumnos(),
                           prestamos=get_prestamos())

# -------------------- LIBROS --------------------
@app.route("/libros", methods=["GET", "POST"])
def libros():
    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_libro(request.form["titulo"], request.form["autor"], request.form["genero"], request.form["stock"])
        return redirect(url_for("libros"))
    
    # Filtrado y paginación
    q_titulo = request.args.get("q_titulo", "").strip().lower()
    q_autor = request.args.get("q_autor", "").strip().lower()
    q_genero = request.args.get("q_genero", "").strip().lower()
    page = int(request.args.get("page", 1))
    per_page = 6

    libros_filtrados = [l for l in get_libros()
                        if (not q_titulo or q_titulo in l.titulo.lower()) and
                           (not q_autor or q_autor in l.autor.lower()) and
                           (not q_genero or q_genero in l.genero.lower())]
    total_pages = (len(libros_filtrados) + per_page - 1) // per_page
    libros_pagina = libros_filtrados[(page-1)*per_page : page*per_page]

    return render_template("libros.html",
                           libros=libros_pagina,
                           page=page,
                           total_pages=total_pages,
                           q_titulo=q_titulo,
                           q_autor=q_autor,
                           q_genero=q_genero)

# -------------------- ALUMNOS --------------------
@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_alumno(request.form["dni"], request.form["nombre"], request.form["correo"])
        return redirect(url_for("alumnos"))

    q_dni = request.args.get("q_dni", "").strip().lower()
    q_nombre = request.args.get("q_nombre", "").strip().lower()
    q_correo = request.args.get("q_correo", "").strip().lower()
    page = int(request.args.get("page", 1))
    per_page = 10

    alumnos_filtrados = [a for a in get_alumnos()
                         if (not q_dni or q_dni in a.dni.lower()) and
                            (not q_nombre or q_nombre in a.nombre.lower()) and
                            (not q_correo or q_correo in a.correo.lower())]
    total_pages = (len(alumnos_filtrados) + per_page - 1) // per_page
    alumnos_pagina = alumnos_filtrados[(page-1)*per_page : page*per_page]

    return render_template("alumnos.html",
                           alumnos=alumnos_pagina,
                           page=page,
                           total_pages=total_pages,
                           q_dni=q_dni,
                           q_nombre=q_nombre,
                           q_correo=q_correo)

# -------------------- PRESTAMOS --------------------
@app.route("/prestamos", methods=["GET", "POST"])
def prestamos():
    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_prestamo(request.form["alumno_dni"], request.form["libro_id"], request.form["fecha"])
        return redirect(url_for("prestamos"))
    return render_template("prestamos.html",
                           prestamos=get_prestamos(),
                           alumnos=get_alumnos(),
                           libros=get_libros())

@app.route("/marcar_devuelto/<int:prestamo_id>", methods=["POST"])
def marcar_devuelto(prestamo_id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    marcar_devuelto_service(prestamo_id)
    return redirect(url_for("prestamos"))

# -------------------- ESTADISTICAS --------------------
@app.route('/estadisticas')
def estadisticas():
    top_libros = top_libros_mas_prestados(get_prestamos(), get_libros())
    top_alumnos = top_alumnos_mas_prestaron(get_prestamos(), get_alumnos())
    return render_template(
        'estadisticas.html',
        top_libros=top_libros,
        top_alumnos=top_alumnos
    )

if __name__ == "__main__":
    app.run(debug=True)

