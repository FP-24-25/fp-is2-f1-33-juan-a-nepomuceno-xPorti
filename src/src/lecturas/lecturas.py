'''
Created on 15 oct 2024

@author: rober
'''

from typing import Optional
import csv

def contador_palabras(fichero,sep,cad) -> float:
    with open(fichero,encoding="utf-8") as f:
        lector = f.read()
        palabras = (lector.lower()).split(sep)
        contador = palabras.count(cad)
        
    return contador
    
def creador_lista(fichero, cad) -> list[str]:
    ls:list=[]
    cad=cad.lower()
    with open(fichero,encoding="utf-8") as f:
        for linea in f:
            if cad in linea.lower():
                ls.append(linea.strip())
        
    return ls

def palabras_unicas(fichero) -> list[str]:
    with open(fichero,encoding="utf-8") as f:
        lector = f.read()
        palabras = lector.split()
        plabras_unicas=set(palabras)
        
    return list(plabras_unicas)


def longitud_promedio_lineas(file_path:str,sep:str=",") -> Optional[float]:
    n=0
    terminos=0
    with open(file_path,encoding="utf-8") as f:
        lectorCSV=csv.reader(f,delimiter=sep)
        for lineas in lectorCSV:
            terminos += len(lineas) 
            n+=1
        
    if n == 0:  
        return None
    
    promedio = terminos/n
        
    return promedio
                    
