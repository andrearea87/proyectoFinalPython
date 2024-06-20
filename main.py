from scraping import webScrap
from analisis import analizarDatos
from reporte import reporteDatos
from utilitarios import manejoArchivo


url1="https://www.simpleretro.com/collections/view-all"
url2="https://www.unique-vintage.com/collections/dresses"

def iniciarProcesamiento(archivo1, archivo2):    
    print("Iniciando procesamiento de sitios web...\n")
    #Procesar y analizar sitio 1
    procesar_sitio(1, url1, archivo1)
    #Procesar y analizar sitio 2
    procesar_sitio(2, url2, archivo2)
    #Generar Reporte 
    print("Generando Reporte Final") 
    reporteDatos.generarReporte(archivo1,url1, archivo2, url2)    
    print("\n...Procesamiento finalizado")
    
def procesar_sitio(sitio, url, archivo):
    print("\n"+str(sitio)+". Procesando sitio web: "+url)
    print(str(sitio)+".1. Scraping sitio web "+url)
    datos_procesados = []  
    #Hacer scraping de la Web
    if sitio==1:
        productos_web_1=webScrap.obtener_datos_todas_paginas_1(url)
        #Procesar los datos
        print(str(sitio)+".2. Procesando datos sitio web " + url)
        datos_procesados=analizarDatos.procesar_datos_1(productos_web_1) 
    elif sitio ==2: 
        productos_web_2=webScrap.obtener_datos_todas_paginas_2(url)
        #Procesar los datos
        print(str(sitio)+".2. Procesando datos sitio web " + url)
        datos_procesados=analizarDatos.procesar_datos_2(productos_web_2)      

    print(str(sitio)+".3. Guardando datos sitio web " + url)
    df= manejoArchivo.guardar_datos_en_csv(datos_procesados,archivo)
    #Calcular impuesto
    print(str(sitio)+".4. Calculando Subtotal e Impuesto " + url)
    analizarDatos.calcular_impuesto(archivo)      
         
    
if __name__ == "__main__":
    datapath_1="data/productos_web_1.csv"
    datapath_2="data/productos_web_2.csv"      
    iniciarProcesamiento(datapath_1, datapath_2)