from models.libro import Libro

# Lista de libros de ejemplo
_libros = [
    Libro(1, "1984", "George Orwell", "Distopía", 5),
    Libro(2, "Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 3),
    Libro(3, "El principito", "Antoine de Saint-Exupéry", "Fábula", 7),
    Libro(4, "Orgullo y prejuicio", "Jane Austen", "Romántico", 4),
    Libro(5, "Don Quijote de la Mancha", "Miguel de Cervantes", "Aventura", 2),
    Libro(6, "Crónica de una muerte anunciada", "Gabriel García Márquez", "Novela corta", 6),
    Libro(7, "Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", 8),
    Libro(8, "Fahrenheit 451", "Ray Bradbury", "Ciencia ficción", 5),
    Libro(9, "El señor de los anillos", "J.R.R. Tolkien", "Fantasía épica", 3),
    Libro(10, "La sombra del viento", "Carlos Ruiz Zafón", "Misterio", 4),
]

def get_libros():
    """Devuelve la lista completa de libros."""
    return _libros

def add_libro(titulo, autor, genero, stock):
    """Agrega un libro nuevo con ID automático."""
    max_id = 0
    for libro in _libros:
        if libro.id > max_id:
            max_id = libro.id
    nuevo_id = max_id + 1

    libro = Libro(nuevo_id, titulo, autor, genero, int(stock))
    _libros.append(libro)
    return libro

def get_libro_por_id(libro_id):
    """Busca un libro por su ID. Devuelve el libro o None si no existe."""
    for l in _libros:
        if l.id == libro_id:
            return l
    return None

def get_libros_paginados(page=1, per_page=6):
    """Devuelve libros paginados. Retorna (libros_en_pagina, total_paginas)."""
    total = len(_libros)
    start = (page - 1) * per_page
    end = start + per_page
    libros_pagina = []
    for i in range(start, min(end, total)):
        libros_pagina.append(_libros[i])
    total_pages = (total + per_page - 1) // per_page
    return libros_pagina, total_pages
