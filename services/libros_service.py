from models.libro import Libro

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
    return _libros

def add_libro(titulo, autor, genero, stock):
    nuevo_id = max([libro.id for libro in _libros], default=0) + 1
    libro = Libro(nuevo_id, titulo, autor, genero, int(stock))
    _libros.append(libro)
    return libro

def get_libro_por_id(libro_id):
    return next((l for l in _libros if l.id == libro_id), None)

def get_libros_paginados(page=1, per_page=6):
    """
    Devuelve una lista de libros paginados.
    :param page: Número de página (comienza en 1)
    :param per_page: Cantidad de libros por página
    :return: (libros_en_pagina, total_paginas)
    """
    total = len(_libros)
    start = (page - 1) * per_page
    end = start + per_page
    libros_pagina = _libros[start:end]
    total_pages = (total + per_page - 1) // per_page
    return libros_pagina, total_pages

