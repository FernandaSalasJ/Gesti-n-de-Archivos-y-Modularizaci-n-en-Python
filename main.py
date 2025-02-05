# Proyecto: Clase 5
# Estudiante: Fernanda Salas
# Fecha de Inicio: 04/02/2025
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

# from analisis_datos.estadisticas import media,calcular_mediana #Importar modulos

from analisis_datos import *

lista_compras = generar_lista_de_compras()
print(lista_compras)
precios = [precio for _, precio in lista_compras]
print('Media: ', media(precios))
print('Mediana: ', calcular_mediana(precios)) 

#se desea vincular el modulo para traer lo que dice en estadistica.py

#from analisis_datos.estadisticas import media,calcular_mediana 
#importar modulos

from analisis_datos import media, calcular_mediana

lista_parametro = [5, 3, 1, 2, 4] #quiero calcular la media y mediana
print('Media: ', media(lista_parametro))
print('Mediana: ', calcular_mediana(lista_parametro))
#despues de guardar, F5 o Run Debugging y luego F11 se fue al init y siempre F11

