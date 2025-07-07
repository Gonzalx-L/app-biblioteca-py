class Alumno:
    def __init__(self, dni, nombre, correo):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo

    def to_dict(self):
        return {
            "dni": self.dni,
            "nombre": self.nombre,
            "correo": self.correo
        }
