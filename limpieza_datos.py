from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, when

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Calidad_Datos_Retail") \
    .master("local[*]") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

# Leer conjunto de datos
ruta = "/home/bigdata/proyecto_bigdata/datos/retail_data.csv"

df = spark.read.csv(
    ruta,
    header=True,
    inferSchema=True
)

# Cantidad de registros y columnas
print("TOTAL DE REGISTROS:", df.count())
print("TOTAL DE COLUMNAS:", len(df.columns))

# Mostrar tipos de datos
print("\nTIPOS DE DATOS:")
df.printSchema()

# Calcular valores nulos por columna
print("\nVALORES NULOS POR COLUMNA:")

nulos = df.select([
    sum(when(col(c).isNull(), 1).otherwise(0)).alias(c)
    for c in df.columns
])

nulos.show(truncate=False, vertical=True)

# Identificar registros duplicados
duplicados = df.count() - df.dropDuplicates().count()

print("\nREGISTROS DUPLICADOS:", duplicados)

# Cerrar Spark
spark.stop()
