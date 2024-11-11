'''
Created on 15 oct 2024

@author: rober
'''


from src.lecturas.lecturas import *
from typing import Optional

print("#####################################################")
print("TEST DE LA FUNCIÓN 6")
sep=" "
cad="quijote"
path = "resources\\lin_quijote.txt"
print(f'El número de veces que aparece la palabra {cad} en el fichero {path} es: {contador_palabras(path,sep,cad,)}\n\n')


print("#####################################################")
print("TEST DE LA FUNCIÓN 7")
cad="quijote"
path="resources/lin_quijote.txt"
print(f'Las líneas en las que aparece la palabra {cad} son: {creador_lista(path,cad)}\n\n')


print("#####################################################")
print("TEST DE LA FUNCIÓN 8")
path="resources/archivo_palabras.txt"
print(f'Las palabras únicas en el fichero {path} son: {palabras_unicas(path)}\n\n')


print("#####################################################")
print("TEST DE LA FUNCIÓN 9")
path="resources/palabras_random.csv"
print(f'La longitud promedio de las líneas del fichero {path} es: {longitud_promedio_lineas(path)}\n\n')

print("TEST DE LA FUNCIÓN 9")
path="resources/vacio.csv"
print(f'La longitud promedio de las líneas del fichero {path} es: {longitud_promedio_lineas(path)}\n\n')

