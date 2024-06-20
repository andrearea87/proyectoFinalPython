import pandas as pd
import time
from datetime import datetime
from utilitarios import log
from utilitarios import manejoArchivo

#Decorador para medir tiempo de ejecucion
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio=time.time()
        resultado=func(*args, **kwargs)
        fin=time.time()
        tiempo = round(fin-inicio,4)
        now = datetime.now()
        mensaje=str(now) + " - Tiempo de ejecucion de "+func.__name__+":" +str(tiempo)+ " segundos"
        print(f"Tiempo de ejecucion de {func.__name__}: {fin-inicio:.4f} segundos")
        log.escribir_datos_en_archivo(mensaje, "log_procesamiento.txt")
        return resultado
    return wrapper

@medir_tiempo
def procesar_datos_1(productos):
    datos_procesados = []
    for producto in productos:
        nombre=producto.get('Producto').replace("【Final Sale】", "").replace("【Flash Sale】", "").replace("【SALE】", "").replace("(Add-on Item)","")       
        #Convertir el precio a numero flotante
        precio = float(producto.get('Precio').replace("$", ""))      
        datos_procesados.append({"Producto": nombre, "Precio":precio})        
    return datos_procesados

@medir_tiempo
def procesar_datos_2(productos):
    datos_procesados = []
    for producto in productos:
        nombre=producto.get('Producto')       
        #Convertir el precio a numero flotante
        precio = float(producto.get('Precio').replace("$", ""))       
        datos_procesados.append({"Producto": nombre, "Precio":precio}) 
    return datos_procesados

def calcular_impuesto(archivo):
    #Lee los datos
    df=manejoArchivo.cargar_datos_csv(archivo)    
    #Calcular impuesto (12%) y subtotal 
    df["Subtotal"] = round(df["Precio"] - ((df["Precio"]*12)/112),2)
    df["Impuesto 12%"] = round(((df["Precio"]*12)/112),2)
    #guardar las nuevas columnas en el archivo excel
    manejoArchivo.guardar_datos_en_csv(df, archivo)


