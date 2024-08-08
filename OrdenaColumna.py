import pandas as pd
import numpy as np

# Este programa carga un archivo Excel con calificaciones de alumnos,
# agrega una columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100
# con un decimal, ordena la tabla por el campo "Nombre" y guarda el archivo modificado.

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Generar valores aleatorios entre 0 y 100 con un decimal para la columna "Mat_Fisica"
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, size=len(df)), 1)

# Ordenar la tabla por el campo "Nombre"
df_ordenado = df.sort_values(by='Nombre')

# Guardar el archivo Excel modificado
df_ordenado.to_excel('calificaciones_alumnos_ordenado.xlsx', index=False)

# Mostrar un mensaje indicando que el archivo se ha guardado exitosamente
print('El archivo modificado ha sido guardado como "calificaciones_alumnos_ordenado.xlsx"')