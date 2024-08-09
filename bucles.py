# menú de opciones 
print("OPCIONES:")
print("[1] Suscribirme")
print("[2] Darle a like")
print("[3] Dejar un comentario")
print()
# inicializamos las variables
opcion = 0
intentos = 0

#bucle hasta que se introduzca un opcion correcta
while opcion  < 1 or int(opcion) > 3:
    opcion = input("Seleccionar una opción: ")
    
    try:
        opcion = int(opcion)
    except ValueError:
        opcion = 0

    intentos +=1
    if intentos == 5:
        print(f"Has superado la cantidad de intentos : {intentos}")
        break
else:    
    # break
    # continue siguiente siglo del bucle
    # mostrar la opción introducida
    print(f"Has escogido la opcion{opcion} ")
