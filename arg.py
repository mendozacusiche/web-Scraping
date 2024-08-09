import sys

# Retorna la suma de 2 números 
def sumar(n1, n2):
    return n1 + n2 


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("ERROR: Parámetros incorrectos")
        print("modo de uso:")
        print(f'{sys.executable} {sys.argv[0]} número1 y número2')
        print("ejemplo:")
        print(f'{sys.executable} {sys.argv[0]} 4, 8')
        sys.exit(1)
    # Si hay 3 parámetros
    else:
        # guardamos en n1 el primer número comprobando que sea un número 

        try:
            n1 = int(sys.argv[1])
        except ValueError:
            print("ERROR: El primer paŕametro no es un número")
            sys.exit(1)
        
        #guardamos en n2 el segundo número comprobando que sea un numero entero

        try:
            n2 = int(sys.argv[2])
        except ValueError:
            print("ERROR: El segundo parámetro no es un número")
            sys.exit(1)
        
        # Mostramos el resultado
        print(f'La suma de {n1} y {n2} es {sumar(n1, n2)}')
    sys.exit(0) 


