'''
Created on 9 nov 2024

@author: rober
'''

from __future__ import annotations
from typing import Callable, List, TypeVar, Generic
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from _operator import index


E = TypeVar("E")

class Cola(Agregado_lineal[E], Generic[E]):
    
    @classmethod
    def of(cls) -> Cola[E]:
        return cls()
    
    def add(self,e:E) -> None:
        self._elements.append(e)
        
    def __repr__(self)->str:
        elements_str= ",".join(repr(el) for el in self._elements)
        return f"Cola({elements_str})"
    
    
        