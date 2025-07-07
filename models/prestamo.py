class Prestamo:
    def __init__(self, id, alumno_dni, libro_id, fecha, devuelto=False):
        self.id = id
        self.alumno_dni = alumno_dni
        self.libro_id = libro_id
        self.fecha = fecha
        self.devuelto = devuelto

    def to_dict(self):
        return {
            "id": self.id,
            "alumno_dni": self.alumno_dni,
            "libro_id": self.libro_id,
            "fecha": self.fecha,
            "devuelto": self.devuelto
        }
