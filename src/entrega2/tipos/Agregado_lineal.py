'''
Created on 9 nov 2024

@author: rober
'''

from __future__ import annotations
from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod


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
            
        
    
    