#
# Este script define una funcion secuencial que se encarga de procesar los elementos de un vector de longitud 144. Cada posición del vector se inicializa con el valor 33 y se calcula su fibonnacci, el resultado siendo guardado en la misma posicion i del vector 
#
# Autores: 
# Gabriela Guzmán - guzman.gabriela@correounivalle.edu.co
# Laura Stefania Salazar - laura.blanco@correounivalle.edu.co
# Juliana Melissa Bolaños - juliana.araujo@correounivalle.edu.co
#
# Fecha: 2024-10-17
#

from fibonacci import fibo
from time import time

def fiboWorkerSecuencial():
    ti = time()
    vector = []
    for n in range(144):
        vector.append(33)
        numero = vector[n]
        vector[n] = fibo(vector[n])
        print(f"El fibonacci del numero {numero} ubicado en la posicion {n+1} es {vector[n]}")
    print(f"El proceso tomo {time() - ti}")

fiboWorkerSecuencial()
