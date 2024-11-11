'''
Created on 9 nov 2024

@author: rober
'''


from typing import List
from entrega2.tipos.Lista_ordenada import Lista_ordenada 



print("TEST DE LISTA ORDENADA:")
print("#" * 48, "\n")

    
lista = Lista_ordenada.of(lambda x: x)
print("Creación de una lista con criterio de orden lambda x: x \n")

    
lista.add(3)
lista.add(1)
lista.add(2)
print("Se añade en este orden: 3, 1, 2 \n")

   
print("Resultado de la lista:", lista, "\n")  

print("#" * 48," \n")

print(f"El elemento eliminado al utilizar remove(): {lista.remove()} \n")
lista.add(1)

    #removed_element = lista.remove()
    #print(f"El elemento eliminado al utilizar remove(): {removed_element}")  

print("#" * 48," \n")

   
print(f"Elementos eliminados utilizando remove_all: {lista.remove_all()} \n")  

print("#" * 48," \n")

    
print("Comprobando si se añaden los números en la posición correcta... \n")

    
lista.add(3)
lista.add(1)
lista.add(2)
lista.add(0)
print(f"Lista después de añadirle el 0: {lista} \n") 

    
lista.add(10)
print(f"Lista después de añadirle el 10: {lista} \n") 

   
lista.add(7)
print(f"Lista después de añadirle el 7: {lista} \n")  



