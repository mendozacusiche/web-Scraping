# variables 

a = 1
b = 2

# ejemplo de la sentencia "if"
if a < b:
    print(f"{a} es mayor que {b}")
elif a > b: 
    print(f"{a} es menor que {b}")
else:
    print(f"{a} es igual que {b}")

# constantes en python se declaran todo en mayuscula 
# precio minimo para procesesar un producto
PRECIO_MINIMO = 500

# lista con las tiendad soportadas
tiendas = ["Amazon", "AliExpress","Bangood"]
# ejemplo de productos 
producto = {"nombre": "iPhone","tienda":"Amazon","precio":800,"stock":0}

if producto["tienda"] in tiendas:
    print(f'El producto{producto["nombre"]} si está soportado')
else:
    print(f'El producto {producto["nombre"]} No supera el precio minimo')

# comprobamos si el precio del producto supera el minimo establecido

if producto["precio"] >= PRECIO_MINIMO:
    print(f'el producto{producto["nombre"]} supera el precio minimo establecido')
else:
    print(f'El producto{producto["nombre"]} No super el precio minimo')

# comprobamos si el producto tiene stock

if producto["stock"] > 0:
    print(f'El procuto{producto["nombre"]} tiene stock({producto["stock"]})')
else:
    print(f'El producto {producto["nombre"]} No tiene stock 😭')
