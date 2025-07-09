from models.prestamo import Prestamo

# Lista de préstamos (vacía al inicio)
_prestamos = []

def get_prestamos():
    """Devuelve la lista completa de préstamos."""
    return _prestamos

def add_prestamo(alumno_dni, libro_id, fecha):
    """Agrega un préstamo nuevo con ID automático."""
    max_id = 0
    for p in _prestamos:
        if p.id > max_id:
            max_id = p.id
    nuevo_id = max_id + 1

    prestamo = Prestamo(nuevo_id, alumno_dni, int(libro_id), fecha, devuelto=False)
    _prestamos.append(prestamo)
    return prestamo

def marcar_devuelto(prestamo_id):
    """Marca un préstamo como devuelto usando su ID."""
    for prestamo in _prestamos:
        if prestamo.id == int(prestamo_id):
            prestamo.devuelto = True
            break

def get_prestamos_por_alumno(dni):
    """Devuelve todos los préstamos realizados por un alumno (por DNI)."""
    prestamos_alumno = []
    for p in _prestamos:
        if p.alumno_dni == dni:
            prestamos_alumno.append(p)
    return prestamos_alumno
