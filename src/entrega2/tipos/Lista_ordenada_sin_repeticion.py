'''
Created on 9 nov 2024

@author: rober
'''

from __future__ import annotations
from typing import Callable, List, TypeVar, Generic
from _elementtree import Element
from abc import abstractmethod
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from _operator import index



E = TypeVar("E")
R = TypeVar("R")


class Lista_ordenada_sin_repiticion(Agregado_lineal[E], Generic[E,R]):
    def __init__(self, order: Callable[[E],R]):
        super().__init__()
        self._order: Callable[[E],R] = order
    
    @classmethod    
    def of(cls,order: Callable[[E], R]) -> "Lista_ordenada_sin_repeticion[E, R]":
        return cls(order)
    
    
    def __index_order(self, e: E) -> int:
        e_order=self._order(e)
        
        for index, elementos_existentes in enumerate(self._elements):
            if e_order < self._order(elementos_existentes):
                return index
        return len(self._elements)
    
    def add(self,e:E) -> None:
        if e in self._elements:
             return
         
        index= self.__index_order(e)
        self._elements.insert(index,e)
        
    def __repr__(self)->str:
        elements_str= ",".join(repr(el) for el in self.elements)
        return f"ListaOrdenadaSinRepeticion({elements_str})"
        
        
        