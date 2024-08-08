import pandas as pd
import numpy as np

# Este programa carga un archivo Excel con calificaciones de alumnos,
# agrega una columna llamada "Mat_Fisica" con valores aleatorios entre 0 y 100
# con un decimal, ordena la tabla por el campo "Nombre", guarda el archivo modificado,
# muestra el número de registros y campos de la tabla, y muestra qué campos son numéricos.

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Generar valores aleatorios entre 0 y 100 con un decimal para la columna "Mat_Fisica"
df['Mat_Fisica'] = np.round(np.random.uniform(0, 100, size=len(df)), 1)

# Ordenar la tabla por el campo "Nombre"
df_ordenado = df.sort_values(by='Nombre')

# Guardar el archivo Excel modificado
df_ordenado.to_excel('calificaciones_alumnos_tipo_numerico.xlsx', index=False)

# Obtener el número de registros y campos de la tabla
num_registros = df_ordenado.shape[0]
num_campos = df_ordenado.shape[1]

# Mostrar el número de registros y campos
print(f'El número de registros en la tabla es: {num_registros}')
print(f'El número de campos en la tabla es: {num_campos}')

# Identificar los campos numéricos
campos_numericos = df_ordenado.select_dtypes(include=[np.number]).columns.tolist()

# Mostrar los campos numéricos
print(f'Los campos numéricos en la tabla son: {campos_numericos}')

# Mostrar un mensaje indicando que el archivo se ha guardado exitosamente
print('El archivo modificado ha sido guardado como "calificaciones_alumnos_tipo_numerico.xlsx"')