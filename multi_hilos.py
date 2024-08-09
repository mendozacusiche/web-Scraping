import threading
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
    id_hilo = threading.current_thread().ident
    nombre_hilo = threading.current_thread().name
    for i in range(101):
        cant_hilos = threading.active_count()
        hora = datetime.now().strftime("%H:%M:%S.%f")
        print(f'{color}#{i}: {hora} {id_hilo} {nombre_hilo} {cant_hilos} {gris}')
        time.sleep(0.01)

colores = (verde, amarillo, azul, magenta, gris, blanco, rojo)

# Main 
if __name__ == '__main__':
    # Gurardamos la hora de inicio
    id_main = threading.main_thread().ident
    nombre_main = threading.main_thread().name
    print("ID main: ",id_main)
    print("Nombre.:",nombre_main)
    input("Pulsar ENTER para comenzar")

    inicio = datetime.now()
    
    #for col in colores:
    #    mostrar_hora(col)
    h1 = threading.Thread(name="hilo1", target=mostrar_hora, args=(verde,))
    h2 = threading.Thread(name="hilo2", target=mostrar_hora, args=(amarillo,))
    h3 = threading.Thread(name="hilo3", target=mostrar_hora, args=(azul,))
    h4 = threading.Thread(name="hilo4", target=mostrar_hora, args=(magenta,))
    h5 = threading.Thread(name="hilo5", target=mostrar_hora, args=(gris,))
    h6 = threading.Thread(name="hilo6", target=mostrar_hora, args=(blanco,))
    h7 = threading.Thread(name="hilo7", target=mostrar_hora, args=(rojo,))

    # iniciamos los hilos
    h1.start()
    h2.start()
    h3.start()
    h4.start()
    h5.start()
    h6.start()
    h7.start()
    # Obligamos a que los hilos finalicen su ejecución para continuar
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    h5.join()
    h6.join()
    h7.join()

    

    # Mostramos los segundos que ha tardado
    print()
    print("Hilos..:", threading.activeCount())
    print(f'Finalizado en {(datetime.now() - inicio).total_seconds()} segundos. ')