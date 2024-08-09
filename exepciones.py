# inicializamos las variables
a = 0
b = 0 
# bucle infinito while

while True:
    
    a = input("Ingrese el primer número")
    b = input("Inggrese el segundo número")

    try:
        a = float(a)
        b = float(b)
        division = a / b
    except ValueError:
        print("ERROR: Debes de introducir números")
        print()
    except ZeroDivisionError:
        print("ERROR: No se puede divider por zero")
    except:
        print("ERROR DESCONOCIDO")
        print()
        exit()
    else:
        print(f"{a} / {b} = {division}")
        break
    finally:
        print("Esto siempre se ejecuta")
        exit()