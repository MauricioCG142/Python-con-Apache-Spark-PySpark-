from pyspark.sql import SparkSession

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_Retail_Batch") \
    .master("local[*]") \
    .getOrCreate()

# Ruta del conjunto de datos
ruta = "/home/bigdata/proyecto_bigdata/datos/retail_data.csv"

# Leer archivo CSV
df = spark.read.csv(ruta, header=True, inferSchema=True)

# Mostrar información general
print("Total de registros:", df.count())
print("Total de columnas:", len(df.columns))

# Mostrar nombres de las columnas
print("Columnas del conjunto de datos:")
print(df.columns)

# Mostrar primeros registros
df.show(5, truncate=False)

# Cerrar sesión de Spark
spark.stop()
