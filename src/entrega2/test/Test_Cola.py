'''
Created on 9 nov 2024

@author: rober
'''

from entrega2.tipos.Cola import Cola

cola = Cola.of()
cola.add_all([23,47,1,2,-3,4,5])

print("TEST DE COLA")
print("#"*48," \n")
print(f"Resultado de la cola: {cola} \n")

print("#"*48," \n")
print(f"Elemntos eliminados utilizando remove_all: {cola.remove_all} \n")
