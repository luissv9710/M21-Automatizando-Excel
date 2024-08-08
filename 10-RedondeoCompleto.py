import pandas as pd

# Este programa carga un archivo Excel con calificaciones de alumnos,
# y redondea a cero decimales las columnas "Mat_CalculoIntegral", "Mat_ProgramacionOOP",
# "Mat_EstructuraDatos" y "Promedio".

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Redondear a cero decimales las columnas especificadas
columnas_a_redondear = ['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos', 'Promedio']

for columna in columnas_a_redondear:
    if columna in df.columns:
        df[columna] = df[columna].round(0)

# Guardar el archivo Excel modificado
archivo_modificado = 'calificaciones_alumnos_redondeocompleto.xlsx'
df.to_excel(archivo_modificado, index=False)

print(f'El archivo modificado ha sido guardado como "{archivo_modificado}"')