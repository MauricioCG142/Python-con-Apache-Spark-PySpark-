import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import csv
import os

# Directorio de resultados
base = "/home/bigdata/proyecto_bigdata/resultados"

# Crear función para leer los archivos CSV de Spark
def leer_csv(carpeta):
    ruta = os.path.join(base, carpeta)

    archivo = [
        f for f in os.listdir(ruta)
        if f.endswith(".csv")
    ][0]

    with open(os.path.join(ruta, archivo), newline="") as f:
        return list(csv.DictReader(f))


# 1. Gráfico de ventas por categoría
datos = leer_csv("ventas_categorias")

categorias = [fila["product_category"] for fila in datos]
ventas = [float(fila["ventas_totales"]) for fila in datos]

plt.figure(figsize=(9, 5))
plt.bar(categorias, ventas)
plt.title("Ventas totales por categoría de producto")
plt.xlabel("Categoría")
plt.ylabel("Ventas totales")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig(os.path.join(base, "grafico_ventas_categorias.png"))
plt.close()


# 2. Gráfico de métodos de pago
datos = leer_csv("metodos_pago")

metodos = [fila["payment_method"] for fila in datos]
cantidades = [
    int(fila["cantidad_transacciones"]) for fila in datos
]

plt.figure(figsize=(9, 5))
plt.bar(metodos, cantidades)
plt.title("Métodos de pago más utilizados")
plt.xlabel("Método de pago")
plt.ylabel("Cantidad de registros")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(base, "grafico_metodos_pago.png"))
plt.close()


# 3. Gráfico de ventas mensuales
datos = leer_csv("ventas_mensuales")

meses = [int(fila["month_of_year"]) for fila in datos]
ventas_mensuales = [
    float(fila["ventas_totales"]) for fila in datos
]

nombres_meses = [
    "Enero", "Febrero", "Marzo", "Abril",
    "Mayo", "Junio", "Julio", "Agosto",
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

plt.figure(figsize=(11, 5))
plt.bar(meses, ventas_mensuales)
plt.title("Ventas totales por mes")
plt.xlabel("Mes")
plt.ylabel("Ventas totales")
plt.xticks(meses, nombres_meses, rotation=30)
plt.tight_layout()
plt.savefig(os.path.join(base, "grafico_ventas_mensuales.png"))
plt.close()

print("Los tres gráficos fueron generados correctamente.")
print("Ubicación:", base)
