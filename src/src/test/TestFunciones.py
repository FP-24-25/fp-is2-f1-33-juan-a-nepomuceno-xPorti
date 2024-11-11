'''
Created on 10 oct 2024

@author: rober

'''
from src.funciones.funciones import *       

print("#####################################################")
print("TEST DE LA FUNCIÓN 1")
n=4
k=2
print(f'El producto de {n} y {k} es: {producto(n,k)}\n\n')


print("#####################################################")
print("TEST DE LA FUNCIÓN 2")
a=3
r=5
k=2
print(f'El producto de la secuencia geométrica con a1 = {a}, r = {r} y k = {n} es: {secuencia(a,r,k)}\n\n')


print("#####################################################")
print("TEST DE LA FUNCIÓN 3")
n=4
k=2
print(f'El número combinatorio de {n} y {k} es: {combinatorio(n,k)}\n\n')

 
print("#####################################################")
print("TEST DE LA FUNCIÓN 4")
n=4
k=2
   
print(f'El número S(n,k) siendo n = {n} y k = {k} es: {sumatorio(n,k)}\n\n')


print("#####################################################")
print("TEST DE LA FUNCIÓN 5")
a=3
epsilon=0.001
f=lambda x:2*x**2
fder=lambda x:4*x
print(f"Resultado de la función 5 con a = {a} y e = {epsilon}, f(x) = 2x^2 y f'(x) = 4x : {metodo_newton(f,fder,a,epsilon)}")
        
        
        
        

    
    
    
    
#def factorial_auxiliar():
    
        
    
    