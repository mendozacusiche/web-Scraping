import datetime 

# Solicitamos una fecha en formato DD-MM-AAAA
fecha = input("Introduce tu fecha de nacimiento (dia-mes-año): ")

# Convertimos la fecha strng en formato datetime
fecha_dt = datetime.datetime.strptime(fecha, "%d-%m-%Y")

# Tupla con los nombres de los dias de la semana
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Obtenemos el índice del dia de la semana de la fecha
indice = datetime.date.weekday(fecha_dt)

# Mostramos el dia de la semana que corresponde a la fecha indicada
print(f'Has nacido un {dias[indice]}')

# https://es.wikipedia.org/wiki/Friki