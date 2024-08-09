import time

# Ejemolos con libreria Time 
inicio = time.time()
input("¿Cómo te llamas? ")
fin = time.time()
print(f'Has tardado {int(round(fin-inicio))} segundos en contestar')