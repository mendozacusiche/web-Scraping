import funciones # importa todo el archivo
from funciones import sumar, limpiar_Pantalla # importa el metodo a usar 
from funciones import * # importa todos los modulos 
from funciones import sumar as sum # renombrarar nombre de metodo
resultado = funciones.sumar(30, 20)

resultado = sumar(50,40)

print(resultado)


print(__name__)

limpiar_Pantalla()