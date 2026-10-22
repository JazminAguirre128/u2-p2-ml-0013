import numpy as np 
# Meredith Aguirre NC = 0013 Fecha 22/10/2026
# Ejemplos de numpy Numerical Python
print("-------- Espaciado linealmente en array -------- 0013")
arre = np.linspace(start = 0, stop = 1, num = 5)
print(arre)
print("-------- Matrix identidad en array -------- 0013")
matriz = np.eye(3)
print(matriz)
print("-------- Genera numeros al azar (aleatorios) en 2D en array -------- 0013")
numale = np.random.random((3, 4)) # Genera 12 numeros aleatorios 
print(numale)
print("Genera 9 numeros aleatorios entre cero y uno")
numale = np.random.random((3, 3)) # Genera 12 numeros aleatorios 
print(numale)
# Como generar 9 números aleatorios comprendidos entre 1 y 20 
# Con numpy en un arreglo de 3 x 3
print("Genera 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size = 9).reshape(3, 3)
print(arre)
print("Meredith Aguirre NC = 0013")