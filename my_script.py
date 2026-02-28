# importar la libreria de numpy
import numpy as np          # pip install numpy

# ver la version de numpy
print("la version de numpy es: ", np.__version__)

# Listas nativas de python
vector = [10, 20, 30, 40, 50]
print(vector)

# acceder a un elemento mediante su índice
print(vector[0])
print(vector[-1])      # ultimo elemento
print(vector[2])
print(vector[4])
print(vector[-2])      # penultimo elemento

# ====================
# NUMPY
# ====================
print("=== TRABAJANDO CON NUMPY ===")
#creamos un vector con numpy
vector_numpy = np.array([1, 8, 6, 4, 15])
print(vector_numpy)

#creamos un vector con numpy con valores consecutivos
vector_numpy_consecutivo = np.arange(0, 10)
print(vector_numpy_consecutivo)

#creamos un vector de 0 a 9 avanzando de 2 en 2
vector_numpy_consecutivo_2 = np.arange(0, 10, 2)
print(vector_numpy_consecutivo_2)
#creamos un vector de 5 numeros aleatorios
vector_numpy_aleatorio = np.random.rand(5)
print(vector_numpy_aleatorio)

#creamos un vector de 5 numeros aleatorios con numeros enteros
vector_numpy_aleatorio_enteros = np.random.randint(0, 100, 5)
print(vector_numpy_aleatorio_enteros)

# ========================
# PROPIEDADES DE NUMPY
# ========================
print("== PROPIEDADES DE NUMPY ==")

#tipo de datos de los elementos del array
print(vector_numpy_aleatorio.dtype)

#numero total de elementos del array
print(vector_numpy_aleatorio.size)

#numero de dimensiones del array
print(vector_numpy_aleatorio.ndim)

# ============================
# OPERACIONES VECTORIZADAS
# ============================
print("===> OPERACIONES VECTORIZADAS ===")

# Array de Numpy
v = np.array([10, 20, 30, 40])

# Lista de python
lista_nativa = [10, 20, 30, 40]

# multiplicacion de lista python
lista_multiplicacion = [ x * 2 for x in lista_nativa]
print(lista_multiplicacion)

# multiplicacion por escalar
print("multiplicacion por escalar: ", v * 5)
# suma por escalar
print("suma por escalar: ", v + 5)

#Promedio
print("promedio: ", np.mean(v))
#Suma total de elementos
print("suma total de elementos: ", np.sum(v))
#Valor maximo
print("valor maximo: ", np.max(v))
#Valor minimo
print("valor minimo: ", np.min(v))

#===============================
# PANDAS
#===============================
import pandas as pd

print("="*40)
print("========= TRABAJANDO CON PANDAS =========")
print("="*40)

# Datos en forma de diccionario
data = {
    "Nombre": ["Ana", "Karina", "Camila", "Juan"],
    "Edad": [30, 25, 5, 20],
    "Ciudad": ["Bogota", "Medellin", "Cali", "Medellin"]
}

# Mostrar el diccionario crudo
print("Diccionario original:")
print(data)
print("-"*40)

# Creamos un DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame
print("DataFrame con Pandas:")
print(df)

print("--- ACCESO A DATOS EN PANDAS ---")

# Accedemos a una sola columna
print(df["Nombre"])

# Accedemos a varias columnas
print(df[["Edad", "Ciudad"]])

# Accedemos a una fila por índice
print(df.loc[3])

# OPERACIONES BÁSICAS EN PANDAS
print("--- OPERACIONES BÁSICAS EN PANDAS ---")

# AGREGAR UNA NUEVA COLUMNA
df["Salario"] = [2000, 5000, 0, 2200]
print(df)

# Cálculos de estadísticas
promedio_edad = df["Edad"].mean()
salario_maximo = df["Salario"].max()
salario_minimo = df["Salario"].min()
salario_total = df["Salario"].sum()

print("Promedio de edad: ", promedio_edad)
print("Salario máximo: ", salario_maximo)
print("Salario mínimo: ", salario_minimo)
print("Salario total: ", salario_total)

# FILTRADO DE DATOS EN PANDAS
#============================
print("=== FILTRADO DE DATOS EN PANDAS ===")

# Filtramos a personas con edad mayor a 29
mayores_a_20 = df[df["Edad"] > 20]
print(mayores_a_20)

# Filtramos a personas que viven en Medellín
personas_medellin = df[df["Ciudad"] == "Medellín"]
print(personas_medellin)

# ============================
# IMPORTAR / EXPORTAR
# ============================

print("\n")

print(df)

# Exportamos el DataFrame a un archivo CSV
df.to_csv("personas.csv", index=False)

# ==== IMPORTAR / EXPORTAR ====

print("\n")
print("IMPORTAR/EXPORTAR")
print(df)

# Exportamos el DataFrame a un archivo CSV
# df.to_csv("personas.csv", index=False)

# Importar el CSV para un nuevo DataFrame
nuevo_df2 = pd.read_csv("personas.csv")

print("\n")
print(nuevo_df2)

# DATAFRAME VACÍO
df_vacio = pd.DataFrame()
print(df_vacio)

# ===========================================
# CONVERSIÓN A NUMPY
# ===========================================
# Convertir un DataFrame a un array de NumPy
array_numpy = nuevo_df2.to_numpy()
print(array_numpy)
