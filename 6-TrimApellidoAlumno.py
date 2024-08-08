import pandas as pd

# Este programa carga un archivo Excel con calificaciones de alumnos,
# y quita los espacios a la izquierda y a la derecha en la columna "ApellidoAlumno".

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Quitar los espacios a la izquierda y a la derecha en la columna "ApellidoAlumno"
if 'ApellidoAlumno' in df.columns:
    df['ApellidoAlumno'] = df['ApellidoAlumno'].str.strip()

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_trim_apellido.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')