from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, round, col

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_Ventas_Mensuales") \
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

# Agrupar ventas por mes
ventas_mensuales = df.groupBy("month_of_year").agg(
    round(sum("total_sales"), 2).alias("ventas_totales")
)

# Ordenar los meses
ventas_mensuales = ventas_mensuales.orderBy("month_of_year")

# Mostrar resultados
print("VENTAS TOTALES POR MES")
ventas_mensuales.show(truncate=False)

# Guardar resultados
ventas_mensuales.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/home/bigdata/proyecto_bigdata/resultados/ventas_mensuales")

spark.stop()
