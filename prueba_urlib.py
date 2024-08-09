import urllib.request

# Devuelve el código html de una url
def get_html(url):
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    return html 

# Main 
if __name__ == '__main__':
    # Variable con la url a la que queremos acceder
    url = "https://es.wikipedia.org/wiki/Friki"
    # vbrimos un archivo en modo escritura 
    f = open("pagina.html", "w", encoding="utf-8")
    # Guardamos el contenido HTML de la página
    f.write(get_html(url))
    # Cerramos el archivo
    f.close()
    # Informamos que el proceso ha finalizado
    print("Fin del programa")