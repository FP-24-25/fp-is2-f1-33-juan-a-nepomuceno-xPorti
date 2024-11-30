'''
Created on 10 oct 2024

@author: rober
'''
from math import factorial



def producto(n:float,k:float):
    if n < k:
        raise ValueError("Paramatro Incorrecto")
    s:float=1
    for i in (0,k+1):
        s *= n-i+1
    return s

def secuencia(a:float,r:float,k:float):
      
    producto=1  
    for n in (1,k+1):
        s=a*(r**(n-1))   
        
        producto*=s
        
    return producto     

def combinatorio(n:int,k:int):
    if n < k:
        raise ValueError("Parametro Incorrecto")
    elif n <= 0:
        raise ValueError("Parametro Incorrecto")
    elif k <= 0:
        raise ValueError("Parametro Incorrecto")
    
    return factorial(n)//(factorial(k)*factorial(n-k))
   

def sumatorio(n:float,k:float):
    if n < k:
        raise ValueError("Parametro Incorrecto")
    
    suma=0
    for i in (0,k):
        numero_combinatorio=combinatorio(k+1,i+1)
        res= ((-1)**i) * numero_combinatorio * (k-i)^n
        suma+=res
        
    res=(1/factorial(k))*suma
    return res
        
        
def metodo_newton(f,fder,a:float,epsilon:float):
    
    while (abs(f(a))>epsilon):
        a = a-(f(a)/fder(a))
        
    return a
    
    

           
    
        
        
            
    
    
    