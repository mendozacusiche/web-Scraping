from datetime import datetime
import time

# Colores 
verde = "\33[1;32m"     # Color verde claro
amarillo = "\33[1;33m"  # Color amarillo claro
azul = "\33[1;36m"      # Color azul claro
magenta = "\33[2;35m"   # Color magenta claro
gris = "\33[0;37m"      # Color gris
blanco = "\33[1;37m"    # Color blanco
rojo = "\33[1;31m"      # color rojo claro

# Imprime la hora del color indicado 100 veces
def mostrar_hora(color):
    for i in range(101):
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f'{color}#{i}: {hora}{gris}')
        time.sleep(0.01)

colores = (verde, amarillo, azul, magenta, gris, blanco, rojo)

# Main 
if __name__ == '__main__':
    # Gurardamos la hora de inicio
    inicio = datetime.now()
    
    for col in colores:
        mostrar_hora(col)
    
    # Mostramos los segundos que ha tardado
    print()
    print(f'Finalizado en {(datetime.now() - inicio).total_seconds()} segundos. ')