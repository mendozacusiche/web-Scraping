# Importamos los módulos necesarios
import random
import platform
import os 

# Limpia la pantalla 
def limpiar_pantalla():
    so = platform.system    # sistema operativo
    if so == "Windows":     # si el sistema es Windows
        os.system("cls")    
    elif os == "Linux":
        os.system("clear")

# Main
if __name__ == '__main__':
    limpiar_pantalla()
    frase = input("Jugador 1: Escribe una frase: ")
    lista_frase = frase.split()
    # Desordenamos las palabra de la frase
    random.shuffle(lista_frase)
    # Convertimos la lista en un string
    frase_desordenada = " ".join(lista_frase)
    # Limpiamos la pantalla paa que el jugador 2 no pueda ve la palabra original
    limpiar_pantalla()
    
    intentos = 0
    while True:
        # Mostramos la frase con las palabras desordenadas
        print(frase_desordenada.upper())
        # El jugador 2 introduce la frase

        intentos += 1   # Incrementamos en 1 intento
        frase2 = input("Jugador 2: Adivena la frase: ")

        # Comprobamos si  es la misma grase que la ordenada
        if  frase.lower() == frase2.lower():
            print(f'¡En hora buena! Has acertado en {intentos} intentos')
            break # Salimos del bucle
        else:   # si no es la misma frase
            print(f'¡Has fallado! Intentos :{intentos}')
        print()