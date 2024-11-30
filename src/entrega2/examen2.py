'''
Created on 21 nov 2024

@author: rober
'''
from typing import Callable, List, TypeVar, Generic, Optional
from abc import ABC, abstractmethod
from entrega2.tipos.Agregado_lineal import Agregado_lineal

'''Clase creada para el ejercicio 1'''
 
E = TypeVar("E")

class ColaConLimite(Agregado_lineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad  

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena, no se puede agregar el elemento.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return self.size >= self.capacidad

    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite[E]":
        return cls(capacidad)

    
    

'''    
Clase que se modifica para crear Agregado_Lineal2

E = TypeVar("E")

class Agregado_lineal(ABC, Generic[E]):
    
    def __init__(self):
        self._elements: list[E]=[]  
    
    @property
    def size(self):
        return len(self._elements)
    
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    @property
    def elements(self) -> List:
        return list(self._elements)
    
    @abstractmethod
    def add(self,e:E) -> None:
        pass
    
    def add_all(self,ls:list[E]) -> None:
        for elements in ls:
            self.add(elements)
            
    def remove(self) -> E:
        assert len(self._elements), "El agregado está vacío"
        return self._elements.pop(0)
    
    def remove_all(self) -> list[E]:
        listaremove=[]
        while not self.is_empty:
            listaremove.append(self.remove())
            
        return listaremove
            
'''


#Clase modificada a partir de la anterior
E = TypeVar("E")

class Agregado_lineal2(ABC, Generic[E]):
    
    def __init__(self):
        self._elements: list[E] = []  
    
    @property
    def size(self) -> int:
        return len(self._elements)
    
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    @property
    def elements(self) -> List[E]:
        return list(self._elements)
    
    @abstractmethod
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: list[E]) -> None:
        for element in ls:
            self.add(element)
            
    def remove(self) -> E:
        assert len(self._elements), "El agregado está vacío"
        return self._elements.pop(0)
    
    def remove_all(self) -> list[E]:
        list_removed = []
        while not self.is_empty:
            list_removed.append(self.remove())
        return list_removed
    
    def contains(self, e: E) -> bool:
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        for element in self._elements:
            if func(element):
                return element
        return None
    
    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [element for element in self._elements if func(element)]
                
'''Clase que hereda de Agregado_lineal2 para poder comprabar las nuevas funciones recien creadas'''           

E = TypeVar("E")

class ColaConLimite2(Agregado_lineal2[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad  

    def add(self, e: E) -> None:
        if self.is_full():
            raise OverflowError("La cola está llena, no se puede agregar el elemento.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return self.size >= self.capacidad

    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite[E]":
        return cls(capacidad)
                
                
#Parte de pruebas de la clase ColaConLimite ejemplo del examen              
cola=ColaConLimite.of(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

try:
    cola.add("Tarea 4") #Debe de lanzar overflow
except OverflowError as e:
    print(e)   #Debe imprimir: "La cola esta llena"
print(cola.remove())

#Parte de pruebas de la clase ColaConLimite para cubrir todad la casuistica
cola = ColaConLimite2.of(5)

# Agregar elementos hasta llenar la cola
cola.add(1)
cola.add(2)
cola.add(3)
cola.add(4)
cola.add(5)
print("Cola después de agregar 5 elementos:", cola.elements)  

# Intentar agregar un elemento cuando la cola está llena
try:
    cola.add(6)  # Debería lanzar un OverflowError
except OverflowError as e:
    print(f"Error esperado al intentar agregar un sexto elemento: {e}")

# Verificar si cumple la condicion usando filter
print(f"Elementos menores a 5: {cola.filter(lambda x: x < 5)}")  

# Verificar si el numero existe usando contains
print(f"¿El número 3 está en la cola?: {cola.contains(3)}")  
print(f"¿El número 6 está en la cola?: {cola.contains(6)}")  

