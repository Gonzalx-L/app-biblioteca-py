from models.alumno import Alumno

_alumnos = [
    Alumno("12345678", "Ana Pérez", "ana@correo.com")
]

def get_alumnos():
    return _alumnos

def add_alumno(dni, nombre, correo):
    if any(a.dni == dni for a in _alumnos):
        return None  # Evitar duplicados
    alumno = Alumno(dni, nombre, correo)
    _alumnos.append(alumno)
    return alumno

def get_alumno_por_dni(dni):
    return next((a for a in _alumnos if a.dni == dni), None)
