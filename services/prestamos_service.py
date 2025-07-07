from models.prestamo import Prestamo

_prestamos = []

def get_prestamos():
    return _prestamos

def add_prestamo(alumno_dni, libro_id, fecha):
    nuevo_id = max([p.id for p in _prestamos], default=0) + 1
    prestamo = Prestamo(nuevo_id, alumno_dni, int(libro_id), fecha, devuelto=False)
    _prestamos.append(prestamo)
    return prestamo

def marcar_devuelto(prestamo_id):
    for prestamo in _prestamos:
        if prestamo.id == int(prestamo_id):
            prestamo.devuelto = True
            break

def get_prestamos_por_alumno(dni):
    return [p for p in _prestamos if p.alumno_dni == dni]
