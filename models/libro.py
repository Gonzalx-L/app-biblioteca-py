class Libro:
    def __init__(self, id, titulo, autor, genero, stock):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "genero": self.genero,
            "stock": self.stock
        }
