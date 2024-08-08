import pandas as pd

# Este programa carga un archivo Excel con calificaciones de alumnos,
# y redondea a cero decimales los valores en la columna "Mat_EstructuraDatos".

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Redondear a cero decimales la columna "Mat_EstructuraDatos"
if 'Mat_EstructuraDatos' in df.columns:
    df['Mat_EstructuraDatos'] = df['Mat_EstructuraDatos'].round(0)

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_redondeoestructura.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')