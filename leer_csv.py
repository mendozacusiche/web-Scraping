# importamos el módulo
import csv 
from datetime import datetime

# Abrimos un archivo en modo lectura

with open("brcusdt.csv", "r", encoding="utf-8") as f:
    # Creamos el objeto que se encargá de leer el archivo CSV
    filas = csv.reader(f)

    # Interamos sobre cada lista de listas
    for fila in filas:
        fecha = datetime.fromtimestamp(int(fila[0])/1000)
        open = float(fila[1])
        high = float(fila[2])
        low = float(fila[3])
        close = float(fila[4])
        volumen = float(fila[5])
        print(fecha, open, high, low, close, volumen)