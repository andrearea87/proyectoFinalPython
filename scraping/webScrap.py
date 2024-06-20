import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from utilitarios import log

#Decorador para medir tiempo de ejecucion
def medir_tiempo(func):   
    def wrapper(*args, **kwargs):
        inicio=time.time()
        resultado=func(*args, **kwargs)
        fin=time.time()
        tiempo = round(fin-inicio,4)
        now = datetime.now()
        mensaje=str(now)+" - Tiempo de ejecucion de "+func.__name__+":" +str(tiempo)+ " segundos"
        print(f"Tiempo de ejecucion de {func.__name__}: {fin-inicio:.4f} segundos")
        log.escribir_datos_en_archivo(mensaje, "log_procesamiento.txt")
        return resultado
    return wrapper

@medir_tiempo
def obtener_datos_productos_2(url):
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    productos=[]    
    #Adaptar los selectores a la estructura de sitio a scrapear
    items=soup.select(".card-wrapper")    
    for item in items:
        name_element =item.select_one(".full-unstyled-link")        
        price_element = item.select_one(".money") 
        #controlar que ambos elementos existan antes de acceder a su texto
        if name_element and price_element:
            name=name_element.get_text(strip=True)
            price=price_element.get_text(strip=True) 
            productos.append({"Producto": name, "Precio":price}) 
    return productos

@medir_tiempo
def obtener_datos_todas_paginas_2(base_url):
    productos=[]
    page=1
    while True:
        url = f"{base_url}?page={page}"
        nuevos_productos=obtener_datos_productos_2(url)
        if not nuevos_productos:
            break
        productos.extend(nuevos_productos)
        page+=1
        time.sleep(2)
    return productos

@medir_tiempo
def obtener_datos_productos_1(url):
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    productos=[]    
    #Adaptar los selectores a la estructura de sitio a scrapear
    items=soup.select(".product-card")    
    for item in items:
        name_element =item.select_one(".product-title")        
        price_element = item.select_one(".money")     
              
        #controlar que ambos elementos existan antes de acceder a su texto
        if name_element and price_element:
            name=name_element.get_text(strip=True)
            price=price_element.get_text(strip=True) 
            productos.append({"Producto": name, "Precio":price}) 
    return productos

@medir_tiempo
def obtener_datos_todas_paginas_1(base_url):
    productos=[]
    page=1
    while True:
        url = f"{base_url}?page={page}"       
        nuevos_productos=obtener_datos_productos_1(url)
        if not nuevos_productos:
            break
        productos.extend(nuevos_productos)
        page+=1
        time.sleep(2)
    return productos 
