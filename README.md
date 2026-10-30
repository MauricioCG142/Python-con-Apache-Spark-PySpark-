# Python-con-Apache-Spark-PySpark-
Proyecto académico de análisis del comportamiento de compra y la retención de clientes en el sector minorista mediante Apache Spark (PySpark), utilizando procesamiento por lotes para explorar, limpiar y analizar grandes volúmenes de datos.

# Análisis del comportamiento de compra y la retención de clientes mediante Apache Spark

## 1. Descripción del proyecto

Este proyecto tiene como propósito analizar el comportamiento de compra y la retención de clientes en el sector minorista mediante herramientas de procesamiento distribuido de datos.

Para su desarrollo se utiliza Apache Spark, a través de PySpark, con el fin de realizar el procesamiento por lotes (*Batch Processing*) de un conjunto de datos que contiene información sobre clientes, transacciones, productos, promociones y hábitos de compra.

El análisis busca identificar patrones de consumo, examinar el comportamiento de las ventas, reconocer las categorías de productos con mayor actividad y explorar características relacionadas con el abandono de clientes.

## 2. Problema abordado

Las empresas del sector minorista generan grandes cantidades de información a partir de sus operaciones comerciales. Analizar estos datos permite comprender los hábitos de compra, identificar tendencias y obtener información útil para apoyar la toma de decisiones.

Por esta razón, se propone utilizar Apache Spark para procesar y analizar un conjunto de datos de ventas y comportamiento de clientes, con el propósito de identificar patrones comerciales y explorar las características asociadas a la retención y el abandono de clientes.

## 3. Conjunto de datos

Se utiliza el conjunto de datos **Retail Sales and Customer Behavior Analysis**, específicamente el archivo `retail_data.csv`.

Características generales:

- **Formato:** CSV.
- **Tamaño aproximado:** 542,64 MB.
- **Registros estimados:** alrededor de un millón, según la descripción de la fuente.
- **Columnas estimadas:** más de 100, según la descripción de la fuente.
- **Tipo de información:** datos simulados de ventas, clientes, productos y comportamiento de compra.

Entre las variables de interés se encuentran:

- `customer_id`: identificador del cliente.
- `transaction_id`: identificador de la transacción.
- `transaction_date`: fecha de la transacción.
- `product_category`: categoría del producto.
- `quantity`: cantidad de productos adquiridos.
- `unit_price`: precio unitario.
- `total_sales`: valor total de las ventas.
- `purchase_frequency`: frecuencia de compra.
- `days_since_last_purchase`: días desde la última compra.
- `churned`: indicador de abandono del cliente.

**Nota:** El archivo de datos no se incluye directamente en este repositorio debido a su tamaño. Debe descargarse desde la fuente original y ubicarse en la carpeta `data/`.

## 4. Tecnologías utilizadas

- **Python:** lenguaje de programación utilizado para desarrollar el procesamiento.
- **Apache Spark:** motor de procesamiento distribuido de grandes volúmenes de datos.
- **PySpark:** interfaz de Python para trabajar con Apache Spark.
- **Pandas:** apoyo para organizar resultados cuando sea necesario.
- **Matplotlib:** generación de gráficos y visualizaciones.
- **GitLab:** alojamiento y control de versiones del código fuente.

## 5. Procesamiento de datos

El procesamiento por lotes contempla las siguientes etapas:

1. **Carga de datos:** lectura del archivo CSV mediante PySpark.
2. **Exploración inicial:** identificación de las dimensiones, columnas y tipos de datos.
3. **Limpieza:** revisión de valores nulos, registros duplicados y posibles inconsistencias.
4. **Transformación:** selección y preparación de variables relevantes para el análisis.
5. **Análisis exploratorio:** evaluación de las ventas, categorías de productos, frecuencia de compra y comportamiento de los clientes.
6. **Visualización:** elaboración de gráficos que faciliten la interpretación de los resultados.

## 6. Estructura del repositorio

```text
analisis-retail-spark/
│
├── data/
│   └── README.md
│
├── resultados/
│
├── src/
│   └── procesamiento_batch.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 7. Requisitos para la ejecución

Para ejecutar el proyecto se requiere:

- Python 3.
- Java compatible con la versión de Apache Spark instalada.
- Apache Spark y PySpark.
- Las bibliotecas indicadas en el archivo `requirements.txt`.

## 8. Instalación y ejecución

**Paso 1. Clonar el repositorio**

```bash
git clone URL_DEL_REPOSITORIO
```

**Paso 2. Ingresar a la carpeta del proyecto**

```bash
cd analisis-retail-spark
```

**Paso 3. Crear un entorno virtual**

```bash
python3 -m venv venv
```

**Paso 4. Activar el entorno virtual**

En Ubuntu o Linux:

```bash
source venv/bin/activate
```

**Paso 5. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**Paso 6. Ubicar el conjunto de datos**

Descargar el archivo `retail_data.csv` y guardarlo en la carpeta `data/`.

La ruta esperada es:

```text
data/retail_data.csv
```

**Paso 7. Ejecutar el procesamiento**

```bash
python3 src/procesamiento_batch.py
```

## 9. Resultados esperados

Al ejecutar el programa se espera obtener información relacionada con:

- Características generales del conjunto de datos.
- Cantidad de registros y variables.
- Revisión de valores nulos y duplicados.
- Comportamiento de las ventas por categoría de producto.
- Frecuencia de compra de los clientes.
- Distribución de clientes según el indicador de abandono.
- Gráficos que faciliten la interpretación de los resultados.

Los resultados definitivos dependerán de la ejecución del código y de la calidad de los datos disponibles.

## 10. Autoría

Proyecto académico desarrollado como parte de la actividad de procesamiento de datos con Apache Spark.

**Tecnología principal:** Apache Spark con PySpark.
**Mauricio Castro Gonzalez**
**Grupo:142**

**Repositorio:** GitHub.

