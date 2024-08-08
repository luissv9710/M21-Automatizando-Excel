import pandas as pd

# Este programa carga un archivo Excel con calificaciones de alumnos,
# y sustituye el fragmento de cadena "Luis" por "Louis" y "Alberto" por "Albert"
# en las columnas "NombreAlumno" y "Nombre".

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Función para realizar sustituciones en una cadena
def sustituir_fragmentos(texto):
    if isinstance(texto, str):
        texto = texto.replace('Luis', 'Louis')
        texto = texto.replace('Alberto', 'Albert')
    return texto

# Aplicar las sustituciones a las columnas especificadas
columnas_a_sustituir = ['NombreAlumno', 'Nombre']

for columna in columnas_a_sustituir:
    if columna in df.columns:
        df[columna] = df[columna].apply(sustituir_fragmentos)

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_sustituircadena.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')