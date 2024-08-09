# Funciones python
clear = "\33[2J\33[H"
def limpiar_Pantalla():
    print(clear)

def sumar(num1, num2):
    print(num1 + num2)

def sumar2(n1, n2):
    return n1 + n2 

# Variables globales y locales 
# valores por defecto
# primero van los parametros obligatorios y despues los 
# parametros por defecto
def multiplicar(n1=5, n2=4):
    #  global n3 = 3
    
    n3 = 3
    print("n3 en el la funcion = ",n3)
    return n1 * n2 

if __name__ == "__Main__":

    resultado = multiplicar(n2=20)
    n3 = 10
    resultaodo =multiplicar(3, 4)
    print("n3en el programprincipal ,",n3)
    resultado = sumar2(2, 3)
    print("Hola")
    limpiar_Pantalla()
    print("Adios")