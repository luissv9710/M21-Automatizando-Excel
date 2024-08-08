import pandas as pd

# Este programa carga un archivo Excel con calificaciones de alumnos,
# y convierte a letras mayúsculas los valores en las columnas "NombreAlumno",
# "ApellidoAlumno" y "Nombre".

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Convertir a letras mayúsculas las columnas especificadas
columnas_a_mayusculas = ['NombreAlumno', 'ApellidoAlumno', 'Nombre']

for columna in columnas_a_mayusculas:
    if columna in df.columns:
        df[columna] = df[columna].str.upper()

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_mayusculas.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')