# Python - Ejercicios de Práctica

Este repositorio contiene una serie de ejercicios de Python que cubren desde conceptos básicos hasta temas más avanzados como manejo de fechas, funciones, pandas y conexiones a bases de datos SQL.

## 📋 Descripción de los Ejercicios

### Ejercicios Básicos (1-12)

**practica1.py** - Manipulación de listas
- Crear una lista con meses del año (enero a junio, excepto abril)
- Añadir elementos con `append()`
- Insertar elementos en posiciones específicas con `insert()`
- Eliminar elementos de la lista

**practica2.py** - Condicionales y tipos de datos
- Comparar un número con 20 usando `if/else`
- Trabajar con números enteros y decimales
- Conversión de tipos de datos con `int()` y `float()`

**practica3.py** - Bucles For básicos
- Recorrer una lista de días de la semana con un bucle `for`
- Mostrar cada elemento de la lista con un mensaje personalizado

**practica4.py** - Iteración sobre listas
- Recorrer una lista de números con bucle `for`
- Imprimir cada número de la lista

**practica5.py** - Función range()
- Usar `range()` para generar secuencias de números
- Recorrer números del 6 al 23

**practica6.py** - Range con pasos negativos
- Generar secuencias descendentes con `range()`
- Recorrer del 54 al 12, de dos en dos

**practica7.py** - Bucles con contadores
- Enumerar los meses del año con su posición ordinal
- Usar un contador incremental dentro de un bucle `for`

**practica8.py** - Listas paralelas
- Combinar dos listas para mostrar información relacionada
- Usar números ordinales en texto (primer, segundo, tercero...)

**practica9.py** - Condicionales múltiples
- Clasificar números por rangos o tramos (0-30, 31-60, etc.)
- Usar `elif` para múltiples condiciones
- Manejar valores fuera de rango

**practica10.py** - Manipulación de strings
- Recorrer las letras de una palabra
- Filtrar caracteres específicos
- Convertir a mayúsculas con `.upper()`

**practica11.py** - Break en bucles
- Sumar números de una lista hasta alcanzar un límite
- Usar `break` para detener un bucle
- Acumuladores en bucles

**practica12.py** - Métodos de strings
- Dividir una cadena en palabras con `.split()`
- Acceder a elementos específicos por índice

### Ejercicios de Funciones (13-16)

**practica13.py** - Funciones básicas
- Crear una función personalizada que realiza operaciones matemáticas
- Recibir parámetros mediante `input()`
- Imprimir resultados desde la función

**practica14.py** - Funciones que retornan valores
- Calcular el área de un triángulo
- Usar `return` para devolver resultados
- Redondear números con `round()`

**practica15.py** - Funciones con validación
- Convertir números de mes a nombres de meses
- Validar que el número esté en un rango válido (1-12)
- Manejar errores de entrada

**practica16.py** - Comparación de valores
- Comparar dos números y determinar cuál es mayor
- Manejar tres posibles resultados (mayor, menor, igual)

### Ejercicios de Bucles While (17)

**practica17.py** - Bucle While
- Implementar un bucle `while` con condición
- Incrementar una variable de forma controlada
- Recorrer desde el 10 hasta el 50, de 2 en 2

### Ejercicios de Fechas (18-22)

**practica18.py** - Diferencia entre fechas
- Usar el módulo `datetime` para trabajar con fechas
- Calcular la diferencia de días entre dos fechas
- Validar que una fecha sea anterior a hoy
- Usar `date.today()` y operaciones con fechas

**practica19.py** - Formato de fechas
- Crear fechas a partir de día, mes y año
- Formatear fechas con `strftime()`
- Mostrar fechas en formato mm/dd/aa

**practica20.py** - Semana del año
- Convertir strings a fechas con `.split()`
- Obtener el número de semana del año
- Trabajar con formatos de fecha dd-mm-aaaa

**practica21.py** - Medir tiempo transcurrido
- Usar `datetime.now()` para obtener la hora actual
- Calcular diferencias de tiempo entre ejecuciones
- Diseñado para trabajar en celdas de Jupyter

**practica22.py** - Operaciones complejas con fechas
- Trabajar con múltiples listas simultáneamente
- Parsear fechas con formato personalizado usando `strptime()`
- Incrementar fechas con `timedelta()` (días, horas, minutos)
- Combinar información de diferentes listas por índice

### Ejercicios de Pandas (23)

**practica23.py** - Series de Pandas
- Crear series de pandas desde listas
- Filtrar datos con condiciones
- Ordenar y reindexar series
- Aplicar funciones personalizadas con `.apply()`
- Calcular estadísticas: promedio (`.mean()`), desviación típica (`.std()`), varianza (`.var()`)
- Calcular suma acumulada con `.cumsum()`

### Ejercicios Avanzados - Bases de Datos (34)

**practica34.py** - Conexión a SQL Server y análisis de datos
- Conectar a SQL Server usando `pyodbc`
- Ejecutar consultas SQL desde Python
- Cargar datos en DataFrames con `pd.read_sql()`
- Combinar DataFrames con `pd.merge()`
- Realizar cálculos y transformaciones de datos
- Agrupar datos con `groupby()`
- Exportar resultados a Excel con `.to_excel()`
- Crear gráficos circulares con `matplotlib`
- Visualizar distribución de importes por ciudad

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** - Análisis y manipulación de datos
- **PyODBC** - Conexión a bases de datos SQL Server
- **Matplotlib** - Visualización de datos
- **datetime** - Manejo de fechas y tiempos

## 📂 Estructura del Repositorio

```
├── practica1.py - practica23.py  → Ejercicios básicos y avanzados
├── practica34.py                  → Proyecto con SQL y visualización
├── clasesCD.ipynb                 → Notebook de clases
├── ejercicios1.ipynb              → Notebook con ejercicios
├── BBDD/                          → Archivos de bases de datos
├── DataFrames/                    → Archivos CSV para análisis
├── Generados/                     → Archivos de salida generados
└── README.md                      → Este archivo
```

## 🚀 Cómo usar estos ejercicios

1. Cada archivo `.py` es independiente y puede ejecutarse por separado
2. Algunos ejercicios requieren entrada del usuario mediante `input()`
3. Los ejercicios están ordenados de menor a mayor dificultad
4. El ejercicio 34 requiere una base de datos SQL Server configurada

## 📚 Conceptos Cubiertos

- Variables y tipos de datos
- Estructuras de control (if/else, for, while)
- Listas y manipulación de colecciones
- Funciones y parámetros
- Manejo de strings
- Fechas y tiempos
- Pandas y análisis de datos
- Conexiones a bases de datos
- Visualización con matplotlib

---

*Repositorio de ejercicios para aprendizaje de Python*
