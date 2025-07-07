from flask import Flask, render_template, request, redirect, url_for, session
import datetime

app = Flask(__name__)
app.secret_key = "biblioteca123"

# Importa el service con alias para evitar conflicto de nombres
from services.libros_service import get_libros, add_libro
from services.alumnos_service import get_alumnos, add_alumno
from services.prestamos_service import get_prestamos, add_prestamo, marcar_devuelto as marcar_devuelto_service

USUARIOS = {"admin": "1234"}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]
        if user in USUARIOS and USUARIOS[user] == pwd:
            session["usuario"] = user
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))
    return render_template(
        "dashboard.html",
        libros=get_libros(),
        alumnos=get_alumnos(),
        prestamos=get_prestamos()
    )

@app.route("/libros", methods=["GET", "POST"])
def libros():
    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_libro(
            request.form["titulo"],
            request.form["autor"],
            request.form["genero"],
            request.form["stock"]
        )
        return redirect(url_for("libros"))

    # Parámetros de búsqueda
    q_titulo = request.args.get("q_titulo", "").strip().lower()
    q_autor = request.args.get("q_autor", "").strip().lower()
    q_genero = request.args.get("q_genero", "").strip().lower()

    # FILTRADO SIEMPRE CON get_libros(), NUNCA _libros DIRECTO
    libros_all = get_libros()
    libros_filtrados = [l for l in libros_all
                        if (not q_titulo or q_titulo in l.titulo.lower()) and
                           (not q_autor or q_autor in l.autor.lower()) and
                           (not q_genero or q_genero in l.genero.lower())]

    # Paginación (6 por página)
    page = int(request.args.get("page", 1))
    per_page = 6
    total = len(libros_filtrados)
    start = (page - 1) * per_page
    end = start + per_page
    libros_pagina = libros_filtrados[start:end]
    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "libros.html",
        libros=libros_pagina,
        page=page,
        total_pages=total_pages,
        q_titulo=q_titulo,
        q_autor=q_autor,
        q_genero=q_genero
    )

    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_libro(
            request.form["titulo"],
            request.form["autor"],
            request.form["genero"],
            request.form["stock"]
        )
        return redirect(url_for("libros"))

    # Parámetros de búsqueda
    q_titulo = request.args.get("q_titulo", "").strip().lower()
    q_autor = request.args.get("q_autor", "").strip().lower()
    q_genero = request.args.get("q_genero", "").strip().lower()

    # Filtrado
    libros_filtrados = [l for l in _libros
                        if (not q_titulo or q_titulo in l.titulo.lower()) and
                           (not q_autor or q_autor in l.autor.lower()) and
                           (not q_genero or q_genero in l.genero.lower())]

    # Paginación
    page = int(request.args.get("page", 1))
    per_page = 6
    total = len(libros_filtrados)
    start = (page - 1) * per_page
    end = start + per_page
    libros_pagina = libros_filtrados[start:end]
    total_pages = (total + per_page - 1) // per_page

    return render_template(
        "libros.html",
        libros=libros_pagina,
        page=page,
        total_pages=total_pages,
        q_titulo=q_titulo,
        q_autor=q_autor,
        q_genero=q_genero
    )

    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_libro(
            request.form["titulo"],
            request.form["autor"],
            request.form["genero"],
            request.form["stock"]
        )
        return redirect(url_for("libros"))
    # Búsqueda
    q_titulo = request.args.get("q_titulo", "").strip().lower()
    q_autor = request.args.get("q_autor", "").strip().lower()
    q_genero = request.args.get("q_genero", "").strip().lower()
    libros_all = get_libros()
    if q_titulo:
        libros_all = [l for l in libros_all if q_titulo in l.titulo.lower()]
    if q_autor:
        libros_all = [l for l in libros_all if q_autor in l.autor.lower()]
    if q_genero:
        libros_all = [l for l in libros_all if q_genero in l.genero.lower()]
    # Paginación
    page = int(request.args.get("page", 1))
    per_page = 10
    total = len(libros_all)
    start = (page - 1) * per_page
    end = start + per_page
    libros_pagina = libros_all[start:end]
    total_pages = (total + per_page - 1) // per_page
    return render_template(
        "libros.html",
        libros=libros_pagina,
        page=page,
        total_pages=total_pages,
        q_titulo=q_titulo,
        q_autor=q_autor,
        q_genero=q_genero
    )

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_alumno(
            request.form["dni"],
            request.form["nombre"],
            request.form["correo"]
        )
        return redirect(url_for("alumnos"))
    q_dni = request.args.get("q_dni", "").strip().lower()
    q_nombre = request.args.get("q_nombre", "").strip().lower()
    q_correo = request.args.get("q_correo", "").strip().lower()
    alumnos_all = get_alumnos()
    if q_dni:
        alumnos_all = [a for a in alumnos_all if q_dni in a.dni.lower()]
    if q_nombre:
        alumnos_all = [a for a in alumnos_all if q_nombre in a.nombre.lower()]
    if q_correo:
        alumnos_all = [a for a in alumnos_all if q_correo in a.correo.lower()]
    page = int(request.args.get("page", 1))
    per_page = 10
    total = len(alumnos_all)
    start = (page - 1) * per_page
    end = start + per_page
    alumnos_pagina = alumnos_all[start:end]
    total_pages = (total + per_page - 1) // per_page
    return render_template(
        "alumnos.html",
        alumnos=alumnos_pagina,
        page=page,
        total_pages=total_pages,
        q_dni=q_dni,
        q_nombre=q_nombre,
        q_correo=q_correo
    )

@app.route("/prestamos", methods=["GET", "POST"])
def prestamos():
    if "usuario" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        add_prestamo(
            request.form["alumno_dni"],
            request.form["libro_id"],
            request.form["fecha"]
        )
        return redirect(url_for("prestamos"))
    return render_template(
        "prestamos.html",
        prestamos=get_prestamos(),
        alumnos=get_alumnos(),
        libros=get_libros()
    )

@app.route("/marcar_devuelto/<int:prestamo_id>", methods=["POST"])
def marcar_devuelto(prestamo_id):
    if "usuario" not in session:
        return redirect(url_for("login"))
    marcar_devuelto_service(prestamo_id)
    return redirect(url_for("prestamos"))

@app.route('/estadisticas')
def estadisticas():
    return "<h2>Página en construcción</h2>"

if __name__ == "__main__":
    app.run(debug=True)
