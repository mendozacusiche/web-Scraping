import re # Importamos la libreria de reguex

texto = "La lluva en Sevilla es una maravilla y la cma de España es la caña"

# operador .
x  = re.search(r'c..a',texto)
# todos los medode de la class 're.Match'
dir(x)
# Retorna una considencia
x.group()

re.findall(r'c..a', texto)

# conjuntos 
# [mñ]

re.findall(r'ca[mñ]a',texto)

# ^not niega todo lo siguiente
re.findall(r'ca[^mñ]a', texto)

# retorna una lista de caracteres de a una letra
# rangos y cuantificadores
re.findall(r'[a-z]', texto)

# pregunta si conside una o mas entra a-z 
re.findall(r'[a-z]+', texto)

# \d+ digitos entre 0..9
# \D+ retorna todo lo que no sea numero
re.findall(r'\d+', texto)

# divide texto en palabra
re.findall(r'\w+', texto)

# retorna todo lo que no se texto
re.findall(r'\W+', texto)

# retorna espacios en blanco tabulador salto de linea
re.findall(r'\s+', texto)
# patron  '+' tiene que considir una o mas veces
re.findall(r'+', texto)
# considir 0 o mas veces *
# concide 0 ó 1 '?'
# numero exacto de repeticiones delpatron
re.findall(r'colou{3}r', texto)
