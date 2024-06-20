1. Se realiza el analisis de dos sitios web que venden ropa para mujer:
 - https://www.simpleretro.com/collections/view-all
 - https://www.unique-vintage.com/collections/dresses

2. Se obtienen datos de cada unas de las páginas de los sitios

3. En la ruta "log/log_procesamiento.txt" se crea archivo de log con los tiempos de ejecucion de las funciones criticas

4. Se limpia los datos obtenidos y se los guarda en archivos en la ruta "data/productos_web_1.csv" y "data/productos_web_2.csv"

5. Se lee los archivos anteriores, se calcula IVA y subtotal, y se edita los archivos agregando esas columnas

6. Se genera un reporte de estadisticas basicas por cada sitio web, con los siguientes datos:
 - Total de productos encontrados
 - Precio promedio, maximo y minimo
 - Los 5 productos mas caros
 - Los 5 productos mas baratos

7. Se crea archivo del reporte anterior en la ruta "reporte/reporteBasico.txt"

8. En la ruta "notebook/exploration.ipynb" se realizan graficos estadisticos con las frecuencias de los precios/productos de cada sitio web

8. El programa esta dividido en los siguientes modulos/paquetes:
 - scraping/webScrap.py: funciones para hacer scraping
 - analisis/analizarDatos.py: funciones para limpiar datos y calcular IVA/subtotal
 - reporte/reporteDatos.py: funciones para generar el reporte de estadisticas basicas
 - utilitarios/manejoArchivo.py: funciones para leer y guardar archivos
 - utilitarios/log.py: funciones para registrar datos en archivo log



