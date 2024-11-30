'''
Created on 9 nov 2024

@author: rober
'''
from __future__ import annotations
from typing import Callable, List, TypeVar, Generic
from abc import abstractmethod
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from _operator import index
from mypy.typeshed.stdlib.ntpath import join

E = TypeVar("E")


class Pila(Agregado_lineal, Generic[E]):
    
    @classmethod
    def of(cls) -> Pila[E]:
        return cls()
    
    def add(self, e:E) -> None:
        self._elements.insert(0, e)
        
    def __repr__(self)->str:
        Pila = ",".join(repr(el) for el in self._elements)
        return f"Pila({Pila})"
        