# Lista de precios real
precios = [234.43, 350.35, 100, 23.45, 1.75, 29.99, 199.95]
nuevaLista = []
# bucle for 

for i in precios:
    if i > 100:
        nuevaLista.append(i)
else:
    print("hola")

print("Fin del bucle")

for i in nuevaLista:
    print(i)

# diccionario de precios
precios = {"nuevo":300.25, "usado":125.33, "alquiler":30, "stock":103}

# ejemplo de bucle "fo" con diccionarios 

for key in precios:
    print(precios[key])

for i in range(10):
    print(f"SUSCRIBETE{i}")

