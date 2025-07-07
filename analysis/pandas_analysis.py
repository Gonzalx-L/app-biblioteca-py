import pandas as pd

def top_libros_prestados(lista_prestamos, lista_libros, top_n=5):
    df_prestamos = pd.DataFrame(lista_prestamos)
    df_libros = pd.DataFrame(lista_libros)
    if df_prestamos.empty or df_libros.empty:
        return [], []
    conteo = df_prestamos['id_libro'].value_counts().head(top_n)
    nombres = []
    cantidad = []
    for id_libro, cant in conteo.items():
        titulo = df_libros.loc[df_libros['id_libro'] == id_libro, 'titulo'].values[0]
        nombres.append(titulo)
        cantidad.append(int(cant))
    return nombres, cantidad

def top_alumnos_prestamos(lista_prestamos, lista_alumnos, top_n=5):
    df_prestamos = pd.DataFrame(lista_prestamos)
    df_alumnos = pd.DataFrame(lista_alumnos)
    if df_prestamos.empty or df_alumnos.empty:
        return [], []
    conteo = df_prestamos['dni_alumno'].value_counts().head(top_n)
    dnis = []
    cantidad = []
    for dni, cant in conteo.items():
        dnis.append(str(dni))
        cantidad.append(int(cant))
    return dnis, cantidad
