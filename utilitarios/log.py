def escribir_datos_en_archivo(datos, archivo):
    path_log="log/"+archivo
    with open(path_log, "a", encoding="utf-8") as f:
        f.write(datos + "\n")