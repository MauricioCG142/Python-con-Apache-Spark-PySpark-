from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, count, round, col

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_Ventas_Categorias") \
    .master("local[*]") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

# Leer el conjunto de datos original
ruta = "/home/bigdata/proyecto_bigdata/datos/retail_data.csv"

df = spark.read.csv(
    ruta,
    header=True,
    inferSchema=True
)

# Agrupar ventas por categoría
ventas_categoria = df.groupBy("product_category").agg(
    round(sum("total_sales"), 2).alias("ventas_totales"),
    count("transaction_id").alias("cantidad_registros")
)

# Ordenar de mayor a menor
ventas_categoria = ventas_categoria.orderBy(
    col("ventas_totales").desc()
)

# Mostrar resultados
print("VENTAS POR CATEGORIA DE PRODUCTO")
ventas_categoria.show(truncate=False)

# Guardar resultados en CSV
ventas_categoria.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/home/bigdata/proyecto_bigdata/resultados/ventas_categorias")

spark.stop()
