from models.alumno import Alumno

# Lista simple con 1 alumno de ejemplo (puedes agregar más)
_alumnos = [Alumno("12345678", "Ana Pérez", "ana@correo.com")]

def get_alumnos():
    """Devuelve la lista completa de alumnos."""
    return _alumnos

def add_alumno(dni, nombre, correo):
    """Agrega un nuevo alumno si el DNI no existe. Retorna el alumno o None si es duplicado."""
    if any(a.dni == dni for a in _alumnos):
        return None  # Ya existe
    alumno = Alumno(dni, nombre, correo)
    _alumnos.append(alumno)
    return alumno

def get_alumno_por_dni(dni):
    """Devuelve el alumno con el DNI dado, o None si no existe."""
    return next((a for a in _alumnos if a.dni == dni), None)
