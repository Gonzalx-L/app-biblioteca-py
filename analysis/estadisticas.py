import pandas as pd

def top_libros_mas_prestados(prestamos, libros, top_n=5):
    # Crear DataFrame de préstamos
    data = [{'libro_id': p.libro_id} for p in prestamos]
    df = pd.DataFrame(data)
    if df.empty:
        return []
    # Contar préstamos por libro_id
    conteo = df['libro_id'].value_counts().head(top_n)
    # Convertir a lista con títulos
    resultado = []
    for libro_id, cantidad in conteo.items():
        titulo = None
        for libro in libros:
            if libro.id == libro_id:
                titulo = libro.titulo
                break
        resultado.append({'titulo': titulo, 'cantidad': cantidad})
    return resultado

def top_alumnos_mas_prestaron(prestamos, alumnos, top_n=10):
    # Crear DataFrame de préstamos
    data = [{'alumno_dni': p.alumno_dni} for p in prestamos]
    df = pd.DataFrame(data)
    if df.empty:
        return []
    # Contar préstamos por alumno_dni
    conteo = df['alumno_dni'].value_counts().head(top_n)
    # Convertir a lista con nombres
    resultado = []
    for dni, cantidad in conteo.items():
        nombre = None
        for alumno in alumnos:
            if alumno.dni == dni:
                nombre = alumno.nombre
                break
        resultado.append({'nombre': nombre, 'cantidad': cantidad})
    return resultado
