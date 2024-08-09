import pickle
# todo en python es un objeto
# ente o es esto o comportamiento
# clase es una especie de plantilla

class Soldado:
    # atributos de clase
    vuela = False
    velocidad = 3 

    # costructor 
    def __init__(self, nivel, ):
        self.nivel = nivel
        self.vida = nivel * 1000
        self.fuerza = nivel * 100

    # Metodo que muestra el estado del objeto
    def mostrar_info(self):
        print(f'nivel.........:{self.nivel}')
        print(f'vida..........:{self.vida}')
        print(f'fuerza........:{self.fuerza}')
        print(f'velocidad.....:{self.velocidad}')
        print(f'vuelta........:{self.vuela}')
        print()


    # Metodo que havilta el objeto la capacidad de volar
    def coger_alas(self):
        self.vuela = True
    
    # Metodo que resta daño a la vida del objeto
    def recibe_golpe(self, danio):
        self.vida = danio

    def sube_nivel(self, niveles):
        self.nivel += niveles
        self.vida = self.nivel * 1000
        self.fuerza = self.nivel * 100
        self.velocidad += niveles


if __name__ == "__main__":
    # Instancia de un soldado
    print("Creaamos un objeto")
    tropa = Soldado(5)
    tropa.mostrar_info()

    # Llamamos al método coger_alas
    tropa.coger_alas()
    tropa.mostrar_info()

    # Llamamos al método recibe_golpe
    print("recibimos un golpe")
    tropa.recibe_golpe(340)
    tropa.mostrar_info()

    print("Subimos 3 niveles")
    tropa.sube_nivel(3)
    tropa.mostrar_info()

    tropa2  = Soldado(10)

    tropa.recibe_golpe(340)
    tropa.mostrar_info()

    print("Subimos 3 niveles")
    tropa.sube_nivel(3)
    tropa.mostrar_info

    objectos = [tropa, tropa2]

    # Forma clasica de abrir archivos
    # archivo = open("tropas.pkl", "wb")
    # pickle.dump(objectos, archivo)
    # archivo.close()

    #with open("tropas.pkl", "wb") as archivo:
    #    pickle.dump(objectos, archivo)
    #
    #print("Fin del programa")

