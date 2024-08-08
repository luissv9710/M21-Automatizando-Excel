import pandas as pd

# Este programa carga un archivo Excel con calificaciones de alumnos,
# y redondea a dos decimales los valores en la columna "Mat_CalculoIntegral".

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Redondear a dos decimales la columna "Mat_CalculoIntegral"
if 'Mat_CalculoIntegral' in df.columns:
    df['Mat_CalculoIntegral'] = df['Mat_CalculoIntegral'].round(0)

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_redondeocalculo.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')