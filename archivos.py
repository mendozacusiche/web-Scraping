# Abrir el archivo (mode lectura o escritura)
# Leer o guardar en el archivo
# Cerrar el archivo

lista = ["Pepito", "Jose", "Gustavo", "Diego", "Meli"]
archivo = open("archivo_texto.txt","a",encoding="utf-8")
archivo.write("Suscribete a mi canal\n")
archivo.write("y dale al like\n")
archivo.write(str(lista))
archivo.close()

archivo = open("archivo_texto.txt", "r",encoding="utf-8")
contenido = archivo.read()
archivo.close()
print(contenido)

# interar sobre archivos 
archivo = open("archivo_texto.text", "r", encoding="utf-8")
for linea in archivo:
    print(linea.replace("\n",""))
    #print(linea,end="")
archivo.close()