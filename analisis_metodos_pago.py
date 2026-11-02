from pyspark.sql import SparkSession
from pyspark.sql.functions import count, col

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("Analisis_Metodos_Pago") \
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

# Contar registros por método de pago
metodos_pago = df.groupBy("payment_method").agg(
    count("transaction_id").alias("cantidad_transacciones")
)

# Ordenar de mayor a menor
metodos_pago = metodos_pago.orderBy(
    col("cantidad_transacciones").desc()
)

# Mostrar resultados
print("METODOS DE PAGO MAS UTILIZADOS")
metodos_pago.show(truncate=False)

# Guardar resultados
metodos_pago.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("/home/bigdata/proyecto_bigdata/resultados/metodos_pago")

spark.stop()
