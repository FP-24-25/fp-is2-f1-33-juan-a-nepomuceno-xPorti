'''
Created on 9 nov 2024

@author: rober
'''

from __future__ import annotations
from typing import Callable, List, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from _operator import index




E = TypeVar("E")
P = TypeVar("P")

class Cola_de_Prioridad(Generic[E, P]):
    
    def __init__(self):
        self._elements:List[E]=[]
        self._priorities:List[P]=[]

    def size(self) -> int:
        return len(self._elements)
    
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        return list(self._elements)
    
    
    def add(self, e: E, priority: P) -> None:
        index = self._index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)
        
    def add_all(self, ls:List[tuple[E,P]]) -> None:
        
        for e, priority in ls:
            self.add(e, priority)
            
    def remove(self) -> E:
        assert len(self._elements) > 0, "El agregado esta vacio"
        element = self._elements.pop(0)
        self._priorities.pop(0)
        return element
    
    def remove_all(self) -> List[E]:
        listaremove=[]
        while not self.is_empty:
            listaremove.append(self.remove())
            
        return listaremove
   
    def _index_order(self,priority:P) -> int:
        for index, existing_priority in enumerate(self._priorities):
            if priority < existing_priority:
                return index
        return len(self._elements)
    
    def decrease_priority(self, e:E, new_priority:P):
        if e in self._elements:
            index=self._elements.index()
            current_priority=self._priorities[index]
            if new_priority < current_priority:
                self._element.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)
                
    def __repr__(self) -> str:
        ColaPrioridad = ",".join(f"({repr(el)}, {repr(pri)})" for el, pri in zip(self._elements, self._priorities))
        return f"ColaPrioridad[{ColaPrioridad}]"
            
            
        
        
    