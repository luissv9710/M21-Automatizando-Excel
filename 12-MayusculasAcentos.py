import pandas as pd
import unicodedata

# Este programa carga un archivo Excel con calificaciones de alumnos,
# convierte a letras mayúsculas y elimina los acentos de los textos en
# las columnas "NombreAlumno", "ApellidoAlumno" y "Nombre".

# Función para eliminar acentos de una cadena
def quitar_acentos(texto):
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    return ''.join(c for c in texto_normalizado if not unicodedata.combining(c))

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Convertir a letras mayúsculas y quitar acentos en las columnas especificadas
columnas_a_procesar = ['NombreAlumno', 'ApellidoAlumno', 'Nombre']

for columna in columnas_a_procesar:
    if columna in df.columns:
        df[columna] = df[columna].str.upper()  # Convertir a mayúsculas
        df[columna] = df[columna].apply(quitar_acentos)  # Eliminar acentos

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_mayusculas_acentos.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')