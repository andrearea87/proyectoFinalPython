import pandas as pd
from datetime import datetime
from utilitarios import manejoArchivo

def estadisticas_precios(df, url):
    now = datetime.now()
    estadisticas = "\n\n******* ESTADISTICAS BASICAS DE SITIO WEB: " + url + " - Fecha: " + str(now)+" ******* \n"
    estadisticas+="\n1. TOTAL DE PRODUCTOS ENCONTRADOS: "+str(len(df))+" productos\n"
    estadisticas+="\n2. PRECIO PROMEDIO, MAXIMO Y MINIMO\n"
    estadisticas+= "\nPrecio promedio: $" + str(round(df["Precio"].mean(),2))
    estadisticas+= "\nPrecio maximo: $" + str(round(df["Precio"].max(),2))
    estadisticas+= "\nPrecio minimo: $"+ str(round(df["Precio"].min(),2))
    estadisticas+="\n\n3. LOS 5 PRODUCTOS MAS COSTOSOS\n"
    estadisticas+= str(df.nlargest(5, "Precio"))
    estadisticas+="\n\n4. LOS 5 PRODUCTOS MAS BARATOS\n"
    estadisticas+= str(df.nsmallest(5, "Precio"))
    print(estadisticas)
    return estadisticas    

def generarReporte(archivo_datos_1, url1, archivo_datos_2, url2):   
    estadistica1= estadisticas_precios(manejoArchivo.cargar_datos_csv(archivo_datos_1), url1)    
    estadistica2= estadisticas_precios(manejoArchivo.cargar_datos_csv(archivo_datos_2), url2) 
    manejoArchivo.guardar_texto_plano(estadistica1+estadistica2, "reporte/reporteBasico.txt")   