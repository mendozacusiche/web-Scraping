# importamos los módulos
import csv 
import json
from urllib.request import urlopen

# Realizamos la petición HTTP

req = urlopen("https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1M")

# Convertimos los datos JSON a una estructura de datos de Python

datos = json.loads(req.read())

# Abrimos un archivo en modo escritura
with open("brcusdt.csv", "w", encoding="utf-8") as f:
    # Creamos el objeto que se encarga de guardar el archivo csv
    writer = csv.writer(f, lineterminator="\n")
    # Iteramos sobre cada lista de listas

    for fila in datos:
        print(fila)
        writer.writerow(fila)

# Abrimos un archivo en modo lectura
with open("brcusdt.csv", "r", encoding="utf-8") as f:
    # Creamos el objeto que se encargará de leer el archivo csv
    fila = csv.reader(f)
    # Iteramos sobre cas lista de lista
    for fila in fila:
        print(fila)