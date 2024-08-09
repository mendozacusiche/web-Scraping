import pickle
from clases import Soldado
with open("tropas.pkl", "rb") as archivo:
    objetos = pickle.load(archivo)

for obj in objetos:
    obj.mostrar_info()