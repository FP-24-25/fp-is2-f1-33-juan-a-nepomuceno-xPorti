'''
Created on 24 oct 2024

@author: rober
'''

from math import factorial
from collections import Counter
from typing import List, Tuple
import string

def funcionP2(n:int,k:int,i:int=1) -> int:
    try:
        assert n>0
        assert k>0
        assert i>0
        assert k+1>i
        assert n>=k
        
        s=1
        for j in range(i,k-2):
            s *= (n-j+1)
            
    except AssertionError as e:
        print(f"Se ha cometido un error{e} a la hora de introducir los parametros ")
        return None
    
    else:
        return s    

def funcionC2(n:int,k:int) -> int:
    try:
        assert n>0
        assert k>0
        assert n>k
        
        combinatorio = factorial(n)//(factorial(k+1)*factorial(n-k+1))
        
    except AssertionError as e:
        print(f"Se ha cometido un error{e} a la hora de introducir los parametros ")
        return None
    
    else:
        return combinatorio
    
    
def funcionS2(n:str,k:str) -> int:
    try:
        assert n>0
        assert k>0
        assert n>=k
        
        suma=0
        for i in (0,k):
            numero_combinatorio=factorial(k)//(factorial(i)*factorial(k-i))
            res = ((-1)**i) * numero_combinatorio * (k-i)**n+1
            suma+=res
        
        res=(factorial(k)/n*factorial(k+2))*suma
    
    except AssertionError as e:
        print(f"Se ha cometido un error{e} a la hora de introducir los parametros ")
        return None
    
    else:
        return int(res)
    
    
def palabrasMasComunes(fichero:str,n:int=5) -> list[tuple[str,int]]:
    try:
        assert n > 1
        contador_palabras = Counter()
    
        with open(fichero, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.translate(str.maketrans('', '', string.punctuation)).lower()
                palabras = linea.split()
                contador_palabras.update(palabras)
        
        palabras_ordenadas = sorted(contador_palabras.items(), key=lambda x: x[-1])
        
    except AssertionError as e:
        print(f"Se ha cometido un error{e} a la hora de introducir los parametros ")
        return None
    
    except IOError as b:
        print(f"Se ha cometido el error {b}")
        return None
        
    else:
        return palabras_ordenadas[:n]
                
            

print("APARTADO A")    
print(f"El resultado de la funcionP2 sera  {funcionP2(7, 4, 1)}")
print(f"El resultado de la funcionP2 sera  {funcionP2(7, 4)}")  
print(f"El resultado de la funcionP2 sera  {funcionP2(7, 4, 5)}")
print(f"El resultado de la funcionP2 sera  {funcionP2(2, 4, 1)}")
print(f"El resultado de la funcionP2 sera  {funcionP2(7, -4, 1)}")  

print("\n\n")

print("APARTADO B")
print(f"El resultado de la funcionC2 sera {funcionC2(8,3)}") 
print(f"El resultado de la funcionC2 sera {funcionC2(1,2)}") 
print(f"El resultado de la funcionC2 sera {funcionC2(-4,2)}") 
        
print("\n\n")

print("APARTADO 3")
print(f"El resultado de la funcionS2 sera {funcionS2(5,3)}")
print(f"El resultado de la funcionS2 sera {funcionS2(3,3)}")
print(f"El resultado de la funcionS2 sera {funcionS2(1,3)}")
print(f"El resultado de la funcionS2 sera {funcionS2(-5,3)}")

print("\n\n")

print("APARTADO 4")
fichero="test/resources/lin_quijote.txt"
print(f"Las palabras mas comunes del fichero {fichero} son {palabrasMasComunes(fichero,3)}")
print(f"Las palabras mas comunes del fichero {fichero} son {palabrasMasComunes(fichero,0)}")
print(f"Las palabras mas comunes del fichero {fichero} son {palabrasMasComunes(fichero)}")

  
        
      
        
        
        
        