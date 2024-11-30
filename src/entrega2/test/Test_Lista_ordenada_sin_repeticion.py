'''
Created on 9 nov 2024

@author: rober
'''


from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repiticion


lista = Lista_ordenada_sin_repiticion.of(lambda x: -x)

print("TEST DE LA LISTA ORDENADA SIN REPETICION")
print("#"*48," \n")
print("Se añade en este orden: 23, 47, 47, 1, 2, -3, 4, 5 \n")
lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)
print(f"Resultado de la lista ordenada sin repetición: {lista} \n")

print("#"*48," \n")
print(f"El elemento eliminado al utilizar remove(): {lista.remove()} \n")

print("#"*48," \n")
lista.add(47)
print(f"Elementos eliminados utilizando remove_all: {lista.remove_all()} \n")
  
print("#"*48," \n")
print("Comprobando si se añaden los números en la posición correcta... \n")

    
lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)
lista.add(0)
print(f"Lista después de añadirle el 0: {lista} \n") 

    
lista.add(10)
print(f"Lista después de añadirle el 10: {lista} \n") 

   
lista.add(7)
print(f"Lista después de añadirle el 7: {lista} \n")  


 