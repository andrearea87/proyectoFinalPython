import pandas as pd
import os

#Funcion para escribir los datos en u archivo de texto
def guardar_datos_en_csv(datos, archivo):
      df=pd.DataFrame(datos)
      df.to_csv(archivo,index=False, encoding="utf-8")
      return df
  
#Funcion para guardar datos en csv
def cargar_datos_csv(archivo):
    datos=pd.read_csv(archivo)
    return datos

#Guardar archivo en texto plano
def guardar_texto_plano(datos, nombre_archivo):
    with open(nombre_archivo,"a") as archivo:
        archivo.write(datos)