import pandas as pd
import matplotlib.pyplot as plt

# Este programa carga un archivo Excel con calificaciones de alumnos,
# extrae las calificaciones de tres materias y grafica las calificaciones
# de cada alumno sin encimar las etiquetas en el eje X.

# Cargar el archivo Excel
archivo_excel = 'calificaciones_alumnos.xlsx'
df = pd.read_excel(archivo_excel)

# Extraer los nombres de los alumnos y las calificaciones
nombres = df['Nombre']
calificaciones = df[['Mat_CalculoIntegral', 'Mat_ProgramacionOOP', 'Mat_EstructuraDatos']]

# Crear una lista de materias
materias = ['Cálculo Integral', 'Programación OOP', 'Estructura de Datos']

# Configurar el tamaño de la figura para que las etiquetas no se encimen
plt.figure(figsize=(10, 6))

# Graficar las calificaciones de cada alumno
for i, nombre in enumerate(nombres):
    plt.plot(materias, calificaciones.iloc[i], marker='o', label=nombre)

# Configurar etiquetas y título del gráfico
plt.xlabel('Materias')
plt.ylabel('Calificaciones')
plt.title('Calificaciones de Alumnos por Materia')

# Rotar las etiquetas del eje X para evitar que se encimen
plt.xticks(rotation=45)

# Mostrar leyenda con los nombres de los alumnos
plt.legend(loc='best', bbox_to_anchor=(1, 1), title='Alumnos')

# Ajustar los márgenes para que las etiquetas de la leyenda no se recorten
plt.tight_layout()

# Mostrar el gráfico
plt.show()